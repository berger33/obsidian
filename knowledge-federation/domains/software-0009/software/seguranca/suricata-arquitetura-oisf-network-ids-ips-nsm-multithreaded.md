---
id: software.seguranca.tranche02.000191
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

# OISF Suricata: arquitetura multi-thread de alta performance para `IDS`, `IPS` e `Network Security Monitoring (NSM)`

## Em uma frase
Conforme documentado na página oficial *What is Suricata* (`docs.suricata.io/en/latest/what-is-suricata.html`) e no README do repositório, o **Suricata** (`OISF/suricata`, mantido pela fundação sem fins lucrativos **Open Information Security Foundation — OISF** sob licença GPL-2.0) é um motor de alta performance para **Detecção de Intrusão de Rede (IDS)**, **Prevenção de Intrusão (IPS)** e **Monitoramento de Segurança de Rede (NSM)**.

## Por que importa
Motores IDS legados single-threaded da década de 1990 saturam um único núcleo de CPU em links de poucos gigabits e limitam-se a casar assinaturas de bytes sem extrair telemetria rica de protocolos de camada de aplicação.

## Como funciona
O Suricata combina um pipeline nativamente **multi-threaded** e escalável para múltiplos núcleos/filas RSS de placas de rede (suportando `AF_PACKET`, `AF_XDP`, `DPDK`, `PF_RING`, `Netmap` e `NFQUEUE`) com parsers profundos de camada 7 (HTTP/1/2/3, TLS/JA3/JA4, DNS, SMB, Kerberos, SSH, RDP, Modbus, DNP3 — muitos escritos em **Rust** por segurança de memória), operando simultaneamente como IDS/IPS de assinaturas e gravador NSM de transações de rede!

## Exemplo
```bash
# Validando a configuração suricata.yaml e as regras carregadas em modo de teste (-T):
suricata -T -c /etc/suricata/suricata.yaml -v
```

## Limites e trade-offs
Conforme enfatiza o README oficial do Suricata, por processar tráfego de rede não confiável diretamente da linha, o projeto passa por fuzzing contínuo no OSS-Fuzz com AddressSanitizer/LeakSanitizer e parsers críticos em Rust.

## Como verificar
Execute `suricata --build-info` para inspecionar os recursos compilados (Rust, AF_PACKET, Hyperscan, JA3/JA4, eBPF).

## Conexões
- [[suricata-eve-json-log-unificado-alert-flow-dns-http-tls-fileinfo]] — Veja também: Suricata `EVE JSON` (`eve.json`): telemetria unificada de alertas, fluxos (`flow`), `dns`, `http`, `tls`, `ssh`, `smb` e `fileinfo`.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://docs.suricata.io/en/latest/what-is-suricata.html) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
