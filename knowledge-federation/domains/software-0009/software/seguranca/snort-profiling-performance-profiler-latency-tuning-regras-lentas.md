---
id: software.seguranca.tranche14.001349
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

# Engenharia de Performance e Detecção de Gargalos no Snort 3: **`profiler` (CPU/Memória por Regra e Módulo)**, **`latency`** e **`perf_monitor`**

## Em uma frase
Imagine que o seu sensor **Snort 3** está monitorando um link de 10 Gbps e você nota alguns pacotes descartados (`dropped packets`) nos horários de pico. Como descobrir com precisão matemática **quais das 35.000 regras carregadas (ou qual inspetor de protocolo)** estão consumindo 80% do tempo de CPU das threads de pacotes?

## Por que importa
Habilitando na seção `4. configure performance` do `snort.lua` os três módulos nativos de telemetria e proteção de latência do Snort 3: **(1) `profiler`** — mede em ciclos de CPU / microssegundos o custo exato de **cada regra individual (`rule`)** e de **cada inspetor/módulo (`module`)**, além do consumo de memória RAM (`memory`), e imprime ao final (ou periodicamente) o ranking das regras mais caras (`count`, `checks`, `matches`, `avg/check`, `total_time`)!; **(2) `perf_monitor`** — grava métricas contínuas de PPS, Mbps, CPU e sessões TCP/UDP em CSV/JSON; e **(3) `latency`**!

## Como funciona
O módulo **`latency`** é uma proteção vital para sensores **IPS Inline**: você define um orçamento máximo de microssegundos por regra (`max_time = 500` na sub-tabela `rule`) e por pacote (`max_time = 1500` na sub-tabela `packet`) — se uma regra com regex pesada exceder o limite de microssegundos em um pacote malformado (**ReDoS de rede**), o Snort 3 suspende temporariamente aquela regra lenta e **impede que o link de rede sofra latência ou queda**!

## Exemplo
```lua
-- Habilitar no snort.lua o profiler das 20 regras mais caras em CPU e a protecao de tempo maximo de avaliacao (latency)
profiler =
{
    modules = { show = true, count = 15, sort = 'total_time' },
    rules   = { show = true, count = 20, sort = 'total_time' },
}

latency =
{
    packet = { max_time = 1500 },
    rule   = { max_time = 500, suspend = true, max_suspend_time = 30000 },
}
```

## Limites e trade-offs
Ao analisar a tabela **`rule profile`** gerada pelo `profiler`, procure por regras que têm milhares de `checks` (avaliações completas da árvore da regra) mas `0` `matches`: isso quase sempre indica que a regra escolheu um `fast_pattern` curto demais ou muito comum (como `content:"GET";`) — adicionar um `fast_pattern` mais específico reduz o tempo de CPU daquela regra em mais de 95%!

## Como verificar
Compilar o Snort 3 com a biblioteca **Intel Hyperscan (`search_engine = { search_method = 'hyperscan' }`)** acelera tanto o *Multi-Pattern Matcher* quanto a avaliação de expressões regulares PCRE2 compatíveis.

## Conexões
- [[snort-saidas-logs-alert-json-unified2-integracao-siem-opensearch]] — Veja também: Saídas Estruturadas de Eventos no Snort 3: Configurando **`alert_json`** para Ingestão Direta em **SIEM (Wazuh, OpenSearch, ELK, Splunk)** e Captura de Pacotes.
- [[snort-gerenciamento-regras-pulledpork3-talos-policies-connectivity-security]] — Veja também: Gerenciamento de Regras **Cisco Talos** e Políticas Baseadas em Metadados (**`connectivity`, `balanced`, `security`, `max-detect`**) no Snort 3 com **PulledPork 3**.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.
- [[snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data]] — Referência cruzada direta com snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data.
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Referência cruzada direta com modsecurity-processadores-body-json-xml-limites-anti-dos-pcre.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
