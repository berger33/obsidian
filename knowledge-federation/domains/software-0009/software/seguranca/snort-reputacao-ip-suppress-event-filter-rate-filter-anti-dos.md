---
id: software.seguranca.tranche14.001347
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/snort3/snort3/master/README.md", "https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Controle de Ruído, **IP Reputation (`reputation`)**, **`suppress`**, **`event_filter`** e **`rate_filter`** no Snort 3: Prevenindo Alert Fatigue e Floods

## Em uma frase
O que acontece se um scanner de vulnerabilidades autorizado interno rodar um scan contra sua sub-rede ou se um ataque de força bruta disparar a mesma regra 50.000 vezes em 1 minuto? Sem filtros de eventos e reputação de IP, o SIEM é inundado por milhares de alertas repetidos (**Alert Fatigue**)!

## Por que importa
Na seção `2` e na seção `6. configure filters` do `snort.lua`, o Snort 3 oferece quatro mecanismos nativos de controle de tráfego e eventos: **(1) `reputation` (*IP Reputation Inspector*)** — bloqueia (`blacklist`) ou aprova (`whitelist`) pacotes imediatamente na entrada antes mesmo de gastar CPU avaliando regras IPS, consultando listas de milhões de IPs de Threat Intelligence!; **(2) `suppress`** — suprime alertas de um `gid`/`sid` específico globalmente ou apenas para determinados IPs de origem/destino (`track = 'by_src', ip = '10.10.50.5'`); **(3) `event_filter`** — controla a frequência de geração de logs de uma regra (`type = 'limit'`, `type = 'threshold'` ou `type = 'both'` por janela de `seconds`); e **(4) `rate_filter`**!

## Como funciona
O **`rate_filter`** é ainda mais poderoso que o `event_filter`: quando uma conexão excede `count` eventos em `seconds`, o `rate_filter` pode **mudar dinamicamente a ação da regra (`new_action = 'drop'` ou `'block'`) durante um `timeout`** — transformando uma regra de alerta de login falho em um bloqueio automático temporário contra força bruta!

## Exemplo
```lua
-- Configurar no snort.lua supressao cirurgica para o scanner interno, limitacao de logs (event_filter) e bloqueio dinamico por taxa (rate_filter)
suppress =
{
    { gid = 1, sid = 2100498, track = 'by_src', ip = '10.10.99.10/32' },
}

event_filter =
{
    { gid = 1, sid = 1000001, type = 'both', track = 'by_src', count = 5, seconds = 60 },
}

rate_filter =
{
    { gid = 1, sid = 1000050, track = 'by_src', count = 20, seconds = 30, new_action = 'block', timeout = 600 },
}
```

## Limites e trade-offs
Qual é a diferença entre os três tipos de **`event_filter`** no Snort 3? **`limit`** alerta apenas nas primeiras `count` vezes dentro da janela de `seconds` (e silencia o resto da janela); **`threshold`** só alerta a cada `count` ocorrências; e **`both`** (o mais recomendado para o SOC!) alerta **apenas uma única vez** no instante em que a meta de `count` ocorrências dentro de `seconds` é atingida!

## Como verificar
Para testar rapidamente uma supressão sem editar o arquivo `snort.lua`, passe **`--lua "suppress = { { gid = 1, sid = 2123 } }"`** diretamente na linha de comando.

## Conexões
- [[snort-modos-operacao-libdaq-afpacket-nfq-inline-ips-drop-reject]] — Veja também: Operação Inline (**IPS Ativo: `drop`, `sdrop`, `reject`**) vs. Passivo (**IDS / TAP**) no Snort 3 com **`libdaq` (`afpacket`, `nfq`, `pcap`, `dpdk`)**.
- [[snort-saidas-logs-alert-json-unified2-integracao-siem-opensearch]] — Veja também: Saídas Estruturadas de Eventos no Snort 3: Configurando **`alert_json`** para Ingestão Direta em **SIEM (Wazuh, OpenSearch, ELK, Splunk)** e Captura de Pacotes.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Referência cruzada direta com snort-configuracao-snort-lua-home-net-wizard-binder-portless.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
