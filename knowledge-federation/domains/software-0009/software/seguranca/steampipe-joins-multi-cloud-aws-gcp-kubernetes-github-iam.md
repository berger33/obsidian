---
id: software.seguranca.tranche10.000902
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

# Steampipe: **JOINs Relacionais Cross-Cloud e Cross-SaaS** (`aws` + `kubernetes` + `github` + `okta`) para Investigação de Incidentes e IAM

## Em uma frase
O poder mais extraordinário do modelo SQL do Steampipe frente a CLIs isoladas (`aws cli`, `gcloud`, `kubectl`, `gh`) é a capacidade de executar um **`JOIN` SQL único que cruza dados de dois ou mais provedores diferentes na mesma query**!

## Por que importa
Imagine um cenário real de **Resposta a Incidentes (DFIR)** ou auditoria de **IAM**: você quer descobrir se alguma chave de acesso IAM ativa na **AWS (`aws_iam_access_key`)** pertence a um ex-funcionário cujo usuário já foi desativado no **Okta (`okta_user`)** ou removido da organização no **GitHub (`github_my_organization_member`)**, ou cruzar um `LoadBalancer` do **Kubernetes (`kubernetes_service`)** com o `Security Group` correspondente na **AWS (`aws_vpc_security_group`)**!

## Como funciona
Como cada plugin é mapeado como um schema dentro do mesmo banco PostgreSQL do Steampipe, basta instalar os plugins necessários e fazer o `JOIN` diretamente entre as tabelas!

## Exemplo
```sql
-- Cruzar chaves de acesso IAM ativas na AWS ( > 90 dias ) com os detalhes de MFA do usuario IAM correspondente
SELECT
  u.name AS user_name,
  u.mfa_enabled,
  k.access_key_id,
  k.create_date,
   AGE(NOW(), k.create_date) AS key_age
FROM
  aws_iam_user AS u
  JOIN aws_iam_access_key AS k ON u.name = k.user_name
WHERE
  k.status = 'Active'
  AND k.create_date < NOW() - INTERVAL '90 days';
```

## Limites e trade-offs
Aproveite todas as funções nativas de **JSONB do PostgreSQL (`jsonb_array_elements`, `->`, `->>`, `@>`)** nas queries do Steampipe: como documentos complexos de IAM Policies, Security Group Rules e Pod Specs são expostos como colunas `jsonb`, você pode desaninhar regras de firewall e políticas IAM diretamente no SQL!

## Como verificar
Execute `steampipe query "SELECT ..."` passando `--output json` ou `--output csv` para exportar o resultado do JOIN para relatórios de auditoria.

## Conexões
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Veja também: **Turbot Steampipe (`turbot/steampipe`)**: Arquitetura **Zero-ETL** baseada em **PostgreSQL Foreign Data Wrappers (FDW)** para Consulta de APIs Cloud via SQL.
- [[steampipe-agregadores-multi-conta-connections-spc-aws-organizations]] — Veja também: Steampipe: Conexões Multi-Conta e **Agregadores (`type = "aggregator"`)** em `~/.steampipe/config/*.spc` para Varrer **AWS Organizations / GCP Folders**.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
