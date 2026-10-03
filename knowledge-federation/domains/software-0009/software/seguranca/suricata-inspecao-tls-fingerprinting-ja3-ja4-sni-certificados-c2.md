---
id: software.seguranca.tranche02.000195
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

# Suricata Inspeção de Tráfego Criptografado TLS: fingerprinting de clientes/servidores (`JA3`, `JA3S`, `JA4`), `tls.sni` e certificados X.509

## Em uma frase
Mesmo sem descriptografar sessões TLS 1.2 / TLS 1.3 (*sem MITM*), o parser TLS/QUIC do Suricata extrai metadados ricos do handshake (`ClientHello` e `ServerHello`): **`tls.sni`** (*Server Name Indication*), versão TLS, cifras, certificados X.509 (`subject`, `issuerdn`, `serial`, `fingerprint` SHA-1/SHA-256, validade) e os hashes de fingerprint comportamental **`JA3`**, **`JA3S`** e **`JA4`**!

## Por que importa
Como mais de 90% do tráfego de malware e Command-and-Control (C2, como Cobalt Strike, Sliver, Metasploit) usa HTTPS/TLS, inspecionar apenas payloads em texto claro deixaria o IDS cego; porém, o cliente TLS de um malware em Go/Python/C tem uma combinação única de extensões TLS e curvas elípticas no `ClientHello`.

## Como funciona
Os fingerprints **`JA3`** e **`JA4`** resumem a estrutura exata do `ClientHello` TLS (independentemente do IP ou domínio de destino), permitindo detectar clientes de C2 ou ferramentas de ataque diretamente em regras do Suricata (`ja3.hash`, `ja4.hash`) e nos logs `eve.json`!

## Exemplo
```text
alert tls $HOME_NET any -> $EXTERNAL_NET any (
    msg:"CORP SEC - Cliente TLS suspeito identificado via JA4 hash";
    flow:established,to_server;
    ja4.hash; content:"t13d1516h2_8daaf6152771_e5627efa2ab1";
    classtype:trojan-activity;
    sid:9000002; rev:1;
)
```

## Limites e trade-offs
No `suricata.yaml`, certifique-se de que `ja3-fingerprints: yes` e `ja4-fingerprints: yes` estão habilitados dentro de `app-layer.protocols.tls`.

## Como verificar
Analise um arquivo `.pcap` contendo tráfego HTTPS (`suricata -r capture.pcap -l ./logs`) e inspecione os objetos `.tls` no `eve.json`.

## Conexões
- [[suricata-anatomia-regras-assinaturas-sticky-buffers-http-dns-tls]] — Veja também: Suricata Linguagem de Regras e *Sticky Buffers*: escrita de assinaturas de camada 7 (`http.uri`, `http.user_agent`, `dns.query`, `tls.sni`).
- [[suricata-modo-ips-inline-af-packet-nfqueue-acao-drop-reject]] — Veja também: Suricata em Modo IPS Inline (`AF_PACKET` Layer 2 Bridge e `NFQUEUE`): bloqueio ativo de ataques com ações `drop` e `reject`.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
