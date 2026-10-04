---
id: software.seguranca.tranche02.000199
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/OISF/suricata/main/README.md", "https://docs.suricata.io/en/latest/what-is-suricata.html", "https://github.com/OISF/suricata"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Suricata Análise Forense de `PCAP` (`-r`) e Automação via Unix Socket (`suricatasc`): processamento em lote de capturas de tráfego

## Em uma frase
Conforme mencionado no README oficial (*traffic replay based IDS and IPS tests*, *large pcap collection processing*, *unix socket testing*), o Suricata pode processar arquivos **`.pcap` / `.pcapng`** offline na velocidade máxima do disco (`suricata -r captura.pcap -l ./out`) ou manter um pool de workers pronto via **Unix Socket (`suricatasc -c "pcap-file ..."`)** para analisar centenas de arquivos PCAP sem o tempo de inicialização de carregar 40.000 regras a cada arquivo!

## Por que importa
Em laboratórios de análise de malware (Cuckoo/CAPE), pipelines de teste de regras em CI ou investigações forenses com milhares de PCAPs, iniciar um novo processo Suricata do zero para cada PCAP de 50 KB gastaria 5 segundos compilando regras e 1 milissegundo lendo o PCAP.

## Como funciona
Iniciando o Suricata em **`--unix-socket`** mode, os compiladores de regras (Hyperscan) ficam carregados em memória e você enfileira novos arquivos PCAP via `suricatasc -c "pcap-file /captures/sample1.pcap /logs/sample1"` com processamento instantâneo!

## Exemplo
```bash
# Analisando um arquivo PCAP forense offline com regras específicas e desativando validação de checksum de offload:
suricata -r ./incidente-2026.pcap -l ./resultado-forense -S ./regras-investigacao.rules -k none
```

## Limites e trade-offs
Ao analisar arquivos `.pcap` capturados na própria máquina de origem (onde a placa de rede usa *TCP Checksum Offloading* e os pacotes capturados têm checksum inválido antes de irem para o hardware), passe sempre a flag **`-k none`** para que o Suricata não descarte os pacotes por erro de checksum!

## Como verificar
Execute o comando acima sobre um PCAP de teste e inspecione `./resultado-forense/eve.json` e `fast.log`.

## Conexões
- [[suricata-tuning-performance-runmodes-workers-af-packet-ebpf-hyperscan]] — Veja também: Suricata Performance Multi-Gigabit (`runmode: workers`, `AF_PACKET`, `eBPF` Bypass e `Hyperscan`): eliminação de perda de pacotes (`kernel_drops`).
- [[suricata-datasets-thresholding-suppress-rate-filter-correlacao-ioc]] — Veja também: Suricata `Datasets`, `Thresholds`, `Suppress` e `Flowbits`: correlação de estado entre pacotes, listas dinâmicas e controle de ruído.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://docs.suricata.io/en/latest/what-is-suricata.html) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
