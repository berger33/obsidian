---
id: software.seguranca.tranche14.001348
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

# Saídas Estruturadas de Eventos no Snort 3: Configurando **`alert_json`** para Ingestão Direta em **SIEM (Wazuh, OpenSearch, ELK, Splunk)** e Captura de Pacotes

## Em uma frase
Enquanto versões antigas do Snort dependiam do formato binário `unified2` e de processos intermediários complexos como `Barnyard2` apenas para converter alertas em texto/banco de dados, como o **Snort 3** exporta alertas e telemetria de alta velocidade diretamente para pipelines modernos de **SIEM e Data Lake (OpenSearch, Wazuh, Elasticsearch, Vector, FluentBit)**?

## Por que importa
Através do plugin nativo de saída **`alert_json`** configurado na seção `7. configure outputs` do `snort.lua`!

## Como funciona
No bloco **`alert_json = { ... }`**, você define **`file = true`** (que grava no arquivo `alert_json.txt` com rotação automática por tamanho em MB via `limit = 100`) e escolhe exatamente quais **campos (`fields`)** deseja incluir em cada linha JSON (`JSON Lines`): timestamp com precisão de microssegundos, `pkt_num`, `proto`, `pkt_gen`, `src_addr`, `src_port`, `dst_addr`, `dst_port`, `service` (identificado pelo `wizard`!), `rule` (`gid:sid:rev`), `msg`, `class`, `priority`, `action` (`allow`/`drop`/`block`), `http_uri`, `http_host` e até o payload em **`b64_data`**!

## Exemplo
```lua
-- Configurar no snort.lua a saida estruturada alert_json com rotacao de 100 MB e campos enriquecidos de Camada 7 + payload em Base64
alert_json =
{
    file = true,
    limit = 100,
    fields = 'timestamp pkt_num proto pkt_gen src_addr src_port dst_addr dst_port service rule action priority class msg b64_data',
}
```

## Limites e trade-offs
Incluir o campo **`b64_data`** na lista `fields` do `alert_json` é uma mão na roda enorme para o analista de SOC Nivel 2/3: quando um alerta dispara no Wazuh ou OpenSearch, o próprio evento JSON já traz em Base64 o pacote exato que disparou a regra — permitindo inspecionar o payload completo do ataque na tela do SIEM sem precisar buscar o PCAP externo!

## Como verificar
Para análises forenses que exigem o pacote bruto em formato `.pcap` padrão do Wireshark apenas quando um alerta ocorre, você pode habilitar simultaneamente `log_pcap = { limit = 500 }`.

## Conexões
- [[snort-reputacao-ip-suppress-event-filter-rate-filter-anti-dos]] — Veja também: Controle de Ruído, **IP Reputation (`reputation`)**, **`suppress`**, **`event_filter`** e **`rate_filter`** no Snort 3: Prevenindo Alert Fatigue e Floods.
- [[snort-profiling-performance-profiler-latency-tuning-regras-lentas]] — Veja também: Engenharia de Performance e Detecção de Gargalos no Snort 3: **`profiler` (CPU/Memória por Regra e Módulo)**, **`latency`** e **`perf_monitor`**.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
