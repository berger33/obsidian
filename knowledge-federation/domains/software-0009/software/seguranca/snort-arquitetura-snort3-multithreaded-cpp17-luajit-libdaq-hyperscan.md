---
id: software.seguranca.tranche14.001341
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

# Arquitetura do **Cisco Snort 3 (`snort3/snort3` — Snort++)**: Motor NIDS/NIPS **Multithreaded em C++17**, Configuração **LuaJIT (`snort.lua`)** e **Hyperscan**

## Em uma frase
Qual foi o salto arquitetural que transformou o clássico Snort 2.9 (que era *single-threaded*, obrigando administradores a rodar 16 processos separados do Snort em um servidor de 16 núcleos consumindo 16x a memória RAM!) no moderno **Cisco Snort 3 (`Snort++`)**?

## Por que importa
Reescrito do zero em **C++17 modular**, o **Snort 3** introduziu uma arquitetura **Nativamente Multithreaded com Configuração Compartilhada**: um único processo `snort` carrega na memória uma única vez as tabelas de regras, os autômatos de busca de padrões (**Intel Hyperscan**) e o mapa de rede (`Host Attribute Table`), enquanto lança **`N` Packet Processing Threads (`--max-packet-threads` / `-z`)** com afinidade de CPU gerenciada via `hwloc` para inspecionar dezenas de Gigabits por segundo em paralelo!

## Como funciona
Além disso, o antigo `snort.conf` ad-hoc foi substituído por uma configuração 100% programável em **LuaJIT (`snort.lua` e `snort_defaults.lua`)**, acompanhada por mais de **200 plugins modulares**, detecção automática de serviços independente de porta (**`wizard` + `binder`**) e abstração de captura via **`libdaq` (Data Acquisition Library)**!

## Exemplo
```bash
# Validar a sintaxe do arquivo snort.lua + regras IPS e executar o Snort 3 com 8 threads de processamento de pacotes sobre um diretorio de PCAPs
snort -V
snort -c /etc/snort/snort.lua -R /etc/snort/rules/snort3-community.rules -T
snort -c /etc/snort/snort.lua --pcap-dir ./pcaps/ --pcap-filter '*.pcap' -A alert_fast --max-packet-threads 8
```

## Limites e trade-offs
Sempre execute **`snort -c /etc/snort/snort.lua -T`** (*Test Mode*) no seu pipeline de CI/CD antes de aplicar qualquer atualização de regras ou configuração em sensores de produção: ele compila toda a árvore Lua e todas as regras IPS e falha imediatamente se houver qualquer erro sintático ou referência ausente!

## Como verificar
Use **`snort --help-module <nome_modulo>`** e **`snort --help-config`** diretamente no terminal para consultar a documentação autogerada de qualquer um dos mais de 200 módulos do Snort 3.

## Conexões
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Veja também: Configuração de **`snort.lua`** e Detecção de Protocolos Independente de Porta (**Portless Inspection**): Como o **`wizard`** e o **`binder`** Derrotam Evasões de Porta!.
- [[snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data]] — Referência cruzada direta com snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
