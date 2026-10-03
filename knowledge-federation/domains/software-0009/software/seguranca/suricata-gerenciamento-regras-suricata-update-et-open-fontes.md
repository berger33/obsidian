---
id: software.seguranca.tranche02.000193
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

# Suricata Gerenciamento de Regras (`suricata-update`): atualização automatizada do *Emerging Threats Open (ET Open)* e tuning via `enable.conf`/`disable.conf`/`modify.conf`

## Em uma frase
A ferramenta oficial **`suricata-update`** (incluída nas instalações modernas do Suricata) automatiza o download, mesclagem, ajuste local e validação de conjuntos de regras públicas e comerciais — usando por padrão o ruleset gratuito **Proofpoint Emerging Threats Open (`et/open`)** — e compilando o arquivo unificado `/var/lib/suricata/rules/suricata.rules`.

## Por que importa
Editar manualmente um arquivo baixado de 40.000 regras para comentar um falso positivo faz com que sua alteração seja perdida no dia seguinte quando o cron atualizar as regras.

## Como funciona
Com o `suricata-update`, você declara suas customizações em quatro arquivos permanentes em `/etc/suricata/`: **`enable.conf`** (habilita regras desativadas por padrão), **`disable.conf`** (desativa por SID, regex ou grupo), **`drop.conf`** (converte regras `alert` em `drop` para modo IPS) e **`modify.conf`** (altera campos de regras via regex), e recarrega o motor a quente sem derrubar pacotes com **`suricatasc -c reload-rules`**!

## Exemplo
```bash
# Atualizando as fontes de regras, aplicando disable.conf/drop.conf, testando com suricata -T e recarregando a quente:
suricata-update
suricatasc -c reload-rules
```

## Limites e trade-offs
Configure sempre o comando `suricata-update` para rodar o teste de validação (`suricata -T`) automaticamente antes de substituir o arquivo `suricata.rules` em produção.

## Como verificar
Execute `suricata-update list-sources` para ver os feeds de inteligência disponíveis (como `et/open`, `sslbl/ssl-fp-blacklist`, `oisf/trafficid`).

## Conexões
- [[suricata-eve-json-log-unificado-alert-flow-dns-http-tls-fileinfo]] — Veja também: Suricata `EVE JSON` (`eve.json`): telemetria unificada de alertas, fluxos (`flow`), `dns`, `http`, `tls`, `ssh`, `smb` e `fileinfo`.
- [[suricata-anatomia-regras-assinaturas-sticky-buffers-http-dns-tls]] — Veja também: Suricata Linguagem de Regras e *Sticky Buffers*: escrita de assinaturas de camada 7 (`http.uri`, `http.user_agent`, `dns.query`, `tls.sni`).

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
