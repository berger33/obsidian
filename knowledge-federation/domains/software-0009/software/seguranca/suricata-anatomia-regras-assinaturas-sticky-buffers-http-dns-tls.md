---
id: software.seguranca.tranche02.000194
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

# Suricata Linguagem de Regras e *Sticky Buffers*: escrita de assinaturas de camada 7 (`http.uri`, `http.user_agent`, `dns.query`, `tls.sni`)

## Em uma frase
As regras do Suricata são compostas por três partes — **Action** (`alert`, `pass`, `drop`, `reject`), **Header** (`protocol`, `src_ip`, `src_port`, `direction` `->`/`<>`, `dst_ip`, `dst_port`) e **Options** entre parênteses — utilizando **Sticky Buffers** modernos de camada de aplicação (`http.uri`, `http.method`, `http.header`, `http.request_body`, `dns.query`, `tls.sni`, `tls.cert_subject`) em vez de inspecionar apenas pacotes TCP brutos.

## Por que importa
Escrever uma regra antiga `alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (content:"/admin";)` falha se a aplicação HTTP rodar na porta `8080` e desperdiça CPU varrendo todo o payload TCP em vez de olhar apenas para o buffer normalizado da URI HTTP.

## Como funciona
Ao declarar `alert http ...` e usar o *sticky buffer* **`http.uri; content:"/admin/config.php"; startswith;`** acompanhado de **`fast_pattern`** (que alimenta o motor *Multi-Pattern Matcher — MPM* Hyperscan/Aho-Corasick), o Suricata identifica o protocolo HTTP em qualquer porta (DPID — *Dynamic Protocol Identification*), decodifica encodings de URL e avalia o buffer exato em nanosegundos!

## Exemplo
```text
alert http $EXTERNAL_NET any -> $HOME_NET any (
    msg:"CORP SEC - Tentativa de acesso a endpoint de debug exposto";
    flow:established,to_server;
    http.method; content:"GET";
    http.uri; content:"/_debug/vars"; startswith; fast_pattern;
    classtype:web-application-attack;
    sid:9000001; rev:1;
)
```

## Limites e trade-offs
Reserve sempre a faixa de identificadores **`sid: 1000000–1999999`** (ou acima de `9000000`) para as regras internas criadas pela sua equipe, evitando colisão com os SIDs oficiais do Emerging Threats.

## Como verificar
Valide a sintaxe e a performance da sua regra customizada com `suricata -T -S ./local.rules` e `--engine-analysis`.

## Conexões
- [[suricata-gerenciamento-regras-suricata-update-et-open-fontes]] — Veja também: Suricata Gerenciamento de Regras (`suricata-update`): atualização automatizada do *Emerging Threats Open (ET Open)* e tuning via `enable.conf`/`disable.conf`/`modify.conf`.
- [[suricata-inspecao-tls-fingerprinting-ja3-ja4-sni-certificados-c2]] — Veja também: Suricata Inspeção de Tráfego Criptografado TLS: fingerprinting de clientes/servidores (`JA3`, `JA3S`, `JA4`), `tls.sni` e certificados X.509.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
