---
id: software.seguranca.tranche10.000909
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/turbot/steampipe/main/README.md", "https://raw.githubusercontent.com/turbot/powerpipe/main/README.md", "https://steampipe.io/docs/reference/cli/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Steampipe & Powerpipe em **CI/CD**: Snapshots Históricos (**`.pps`**, `--snapshot`), Exportação (`json`, `html`, `md`, `csv`, `asff`) e Exit Codes

## Em uma frase
Como integrar o Steampipe e o Powerpipe em pipelines agendados do GitHub Actions / GitLab CI para gerar evidências auditáveis para auditores externos (ISO 27001 / SOC 2) e falhar o pipeline se surgirem novos alarmes críticos?

## Por que importa
No Powerpipe, passar a flag **`--snapshot`** (ou `--snapshot-location`) ao executar um benchmark ou dashboard salva um **Snapshot Completo (`.pps`)** contendo todas as entradas, queries, resultados e metadados daquele instante no tempo — permitindo comparar a evolução da conformidade entre duas datas!

## Como funciona
Além disso, a flag **`--output` (`-o`)** do `powerpipe benchmark run` exporta relatórios prontos em **`html`**, **`json`**, **`md`** (Markdown), **`csv`** e **`asff`** (*AWS Security Finding Format*, para ingestão direta no **AWS Security Hub**!), e os códigos de saída documentados (`0` quando todos os controles passam sem alarmes/erros, ou diferente de zero quando há alarmes) permitem bloquear o job de CI/CD automaticamente!

## Exemplo
```bash
# Executar um benchmark no CI/CD gerando simultaneamente um Snapshot (.pps) e um relatorio em formato AWS Security Hub (ASFF)
powerpipe benchmark run aws_compliance.benchmark.foundational_security \
  --snapshot \
  --export /cases/cspm/aws_foundational.html \
  --output asff > /cases/cspm/aws_security_hub_findings.json
```

## Limites e trade-offs
Use a flag **`--filter`** ou **`--tag`** no `powerpipe benchmark run` (ex.: `--tag "cis_level=1"`) quando quiser que o pipeline bloqueante de CI/CD avalie apenas os controles de Nível 1 de alta severidade, deixando os controles informativos de Nível 2 para o relatório semanal.

## Como verificar
Verifique os códigos de saída oficiais da CLI do Steampipe (`0` sucesso, `11–14` erros de plugin, `41` falha na query) em scripts de automação.

## Conexões
- [[steampipe-modo-servico-steampipe-service-cache-ttl-clientes-externos]] — Veja também: Steampipe **`steampipe service`**: Operação como Daemon PostgreSQL (`:9193`), Controle de **Cache TTL (`--cache-ttl`)** e Conexão via `psql` / Grafana / Metabase.
- [[steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm]] — Veja também: Decisão Arquitetural de CSPM: Quando Usar **Steampipe (Zero-ETL Live SQL)** vs **CloudQuery (ELT Data Warehouse)** vs **Prowler**.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Referência cruzada direta com steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
