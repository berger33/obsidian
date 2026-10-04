---
id: software.seguranca.tranche02.000198
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
fontes: ["https://docs.suricata.io/en/latest/what-is-suricata.html", "https://raw.githubusercontent.com/OISF/suricata/main/README.md", "https://github.com/OISF/suricata"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Suricata Performance Multi-Gigabit (`runmode: workers`, `AF_PACKET`, `eBPF` Bypass e `Hyperscan`): eliminação de perda de pacotes (`kernel_drops`)

## Em uma frase
Para processar links de **10 Gbps a 100+ Gbps** sem perda de pacotes (`capture.kernel_drops`), a arquitetura recomendada do Suricata utiliza **`runmode: workers`** (onde cada thread worker executa todo o pipeline — recepção, decodificação, stream TCP, detecção L7 e saída — para um subconjunto de fluxos na mesma CPU com *CPU affinity* fixada), combinado com **`mpm-algo: hs` (Intel Hyperscan / Vectorscan)** e **bypass de fluxos via `eBPF`/`XDP`**.

## Por que importa
Em links de alto tráfego, 80% dos bytes pertencem a poucos fluxos longos (*elephant flows*, como backups cifrados, streams de vídeo ou replicação de banco) que já tiveram seu handshake inspecionado; continuar passando cada pacote de 10 GB pela CPU do IDS satura a máquina.

## Como funciona
Habilitando `stream.bypass: yes` e o filtro **eBPF / XDP** na placa de rede, assim que o Suricata conclui a inspeção inicial de um fluxo criptografado ou aciona uma regra com a palavra-chave `bypass;`, ele instrui o kernel/NIC a ignorar os pacotes restantes daquela sessão diretamente no driver!

## Exemplo
```bash
# Monitorando em tempo real a taxa de pacotes e verificando se capture.kernel_drops permanece em 0:
suricatasc -c "iface-stat eth0"
jq 'select(.event_type=="stats") | .stats.capture' /var/log/suricata/eve.json | tail -n 5
```

## Limites e trade-offs
Sempre defina as variáveis de rede **`HOME_NET`** e **`EXTERNAL_NET: "!$HOME_NET"`** com os blocos CIDR reais da sua organização no `suricata.yaml`; deixar `EXTERNAL_NET: "any"` degrada a performance e multiplica falsos positivos.

## Como verificar
Verifique nos eventos `"event_type": "stats"` do `eve.json` que `capture.kernel_drops` é igual a `0` ou inferior a `0,01%`.

## Conexões
- [[suricata-file-extraction-file-store-sha256-deteccao-malware-rede]] — Veja também: Suricata File Extraction e Hashing (`file-store` v2 e `fileinfo`): cálculo de SHA-256 em tempo real e captura forense de arquivos trafegados.
- [[suricata-analise-offline-pcap-replay-regressao-ci-unix-socket]] — Veja também: Suricata Análise Forense de `PCAP` (`-r`) e Automação via Unix Socket (`suricatasc`): processamento em lote de capturas de tráfego.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
