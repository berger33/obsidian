---
id: software.seguranca.tranche08.000797
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **ZGrab 2.0 (`zgrab2 multiple -c config.ini`)**: Orquestração de Múltiplos Protocolos L7, Formato CSV (`IP, DOMAIN, TAG, PORT`) e **`--trigger`**

## Em uma frase
Muitas vezes, uma auditoria de superfície de ataque precisa coletar **múltiplos protocolos no mesmo host** (por exemplo: fazer handshake HTTP na porta `80`, HTTP + TLS + fingerprinting **JARM** na porta `443` e coletar o algoritmo de HostKey **SSH** na porta `22`), ou precisa conectar no endereço `IP` enviando um `DOMAIN` específico no cabeçalho HTTP `Host` e na extensão TLS **SNI**!

## Por que importa
Conforme documentado no `README.md` oficial do **ZGrab 2.0**, ambos os requisitos são atendidos nativamente: **(1)** o formato de entrada CSV do ZGrab 2.0 aceita até quatro colunas **`IP, DOMAIN, TAG, PORT`** (quando `IP` e `DOMAIN` são informados juntos, o ZGrab2 conecta no `IP` mas envia `DOMAIN` no TLS SNI e no HTTP `Host`!); e **(2)** o módulo **`zgrab2 multiple -c multiple.ini`** executa múltiplos módulos e portas em uma única passagem usando gatilhos **`trigger="<TAG>"`**!

## Como funciona
Isso permite alimentar o `zgrab2 multiple` diretamente com a saída do **OWASP Amass (`IP, FQDN`)** para inspecionar milhares de Virtual Hosts com SNI correto!

## Exemplo
```ini
# /cases/easm/multiple_audit.ini — Configuracao ZGrab 2.0 para auditar HTTP (80), HTTPS (443) e SSH (22) simultaneamente
[Application Options]
output-file="/cases/easm/multi_protocol_results.jsonl"
senders=200

[http]
name="http80"
port=80
endpoint="/"
max-redirects=1

[http]
name="https443"
port=443
use-https=true
endpoint="/"

[ssh]
name="ssh22"
port=22
```

## Limites e trade-offs
Para executar o arquivo `.ini` acima contra uma lista CSV contendo `10.20.1.10, portal.internal.corp`, basta rodar: **`zgrab2 multiple -c /cases/easm/multiple_audit.ini --input-file=/cases/easm/targets.csv`**!

## Como verificar
Verifique no arquivo `multi_protocol_results.jsonl` que cada linha JSON contém as chaves `.data.http80`, `.data.https443` e `.data.ssh22` agrupadas para aquele ativo.

## Conexões
- [[zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes]] — Veja também: Arquitetura **ZMap (L4) + ZGrab 2.0 (L7)**: Pipeline de Sondagem em Escala de Camada de Transporte para Transcrição Completa de Handshakes de Aplicação.
- [[zmap-auditoria-protocolos-industriais-ot-ics-scada-zgrab2-modbus-siemens-dnp3]] — Veja também: ZGrab 2.0 em Auditoria de Redes **OT / ICS / SCADA** e Bancos de Dados: Módulos `modbus`, `siemens` (S7), `dnp3`, `bacnet`, `fox` e `mongodb`/`redis`.
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — Referência cruzada direta com amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
