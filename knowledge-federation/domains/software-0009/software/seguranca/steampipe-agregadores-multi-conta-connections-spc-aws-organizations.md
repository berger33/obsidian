---
id: software.seguranca.tranche10.000903
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

# Steampipe: Conexões Multi-Conta e **Agregadores (`type = "aggregator"`)** em `~/.steampipe/config/*.spc` para Varrer **AWS Organizations / GCP Folders**

## Em uma frase
Em organizações enterprise que operam dezenas ou centenas de contas AWS (ou projetos GCP / assinaturas Azure), auditar uma conta por vez é inviável.

## Por que importa
No Steampipe, cada conexão de plugin é declarada em arquivos HCL **`~/.steampipe/config/<plugin>.spc`**: você pode definir conexões individuais para cada conta (`connection "aws_prod"`, `connection "aws_staging"`, `connection "aws_secops"`) e criar uma **Conexão Agregadora (`type = "aggregator"`)** que une todas elas sob um único schema SQL (ex.: `aws_all`) usando wildcards (`connections = ["aws_*"]`)!

## Como funciona
Quando você executa `SELECT account_id, instance_id FROM aws_all.aws_ec2_instance`, o Steampipe dispara as consultas **concorrentemente em todas as contas AWS agregadas** e retorna uma tabela unificada de toda a organização!

## Exemplo
```hcl
# ~/.steampipe/config/aws.spc — Configuracao de multiplas contas AWS e um agregador unificado aws_all
connection "aws_prod" {
  plugin  = "aws"
  profile = "prod-security-audit"
  regions = ["sa-east-1", "us-east-1"]
}

connection "aws_staging" {
  plugin  = "aws"
  profile = "staging-security-audit"
  regions = ["sa-east-1"]
}

connection "aws_all" {
  plugin      = "aws"
  type        = "aggregator"
  connections = ["aws_*"]
}
```

## Limites e trade-offs
Observe o atributo `regions = ["sa-east-1", "us-east-1"]` (ou `regions = ["*"]`): liste apenas as regiões onde sua organização opera (ou use SCPs para bloquear as demais) para evitar chamadas de API desnecessárias em 30 regiões globais a cada query.

## Como verificar
Defina o `search_path` no workspace do Steampipe para priorizar o schema agregador `aws_all` nas auditorias corporativas.

## Conexões
- [[steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam]] — Veja também: Steampipe: **JOINs Relacionais Cross-Cloud e Cross-SaaS** (`aws` + `kubernetes` + `github` + `okta`) para Investigação de Incidentes e IAM.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Veja também: **Powerpipe (`turbot/powerpipe`)**: Execução de +5.000 Controles de Conformidade (**CIS Benchmarks, NIST 800-53, PCI DSS, SOC 2, HIPAA**) sobre o Steampipe.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
