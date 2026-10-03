---
id: software.seguranca.tranche10.000901
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

# **Turbot Steampipe (`turbot/steampipe`)**: Arquitetura **Zero-ETL** baseada em **PostgreSQL Foreign Data Wrappers (FDW)** para Consulta de APIs Cloud via SQL

## Em uma frase
**Steampipe** (`turbot/steampipe`, licença AGPLv3, criado pela Turbot HQ) é um motor **Zero-ETL** escrito em Go que expõe APIs de provedores de nuvem, plataformas SaaS, clusters Kubernetes e arquivos de configuração como **tabelas relacionais consultáveis em tempo real usando SQL padrão (PostgreSQL)**!

## Por que importa
Como funciona por baixo do capô? O binário `steampipe` gerencia uma instância embutida do **PostgreSQL** combinada com um **Foreign Data Wrapper (FDW) em Go** que se comunica via gRPC com os plugins instalados (`steampipe plugin install aws gcp azure kubernetes github`): quando você executa um `SELECT`, o planejador do Postgres empurra os predicados da cláusula `WHERE` (*Key Columns / Quals*) diretamente para o plugin Go, que faz apenas as chamadas de API REST/gRPC necessárias em paralelo e preenche as linhas virtuais em memória!

## Como funciona
Além da CLI com Postgres embutido, os plugins do Steampipe também são distribuídos como **Extensões Nativas para PostgreSQL existente**, **Extensões SQLite** e binários standalone de exportação.

## Exemplo
```sql
-- Consultar em tempo real buckets S3 da AWS que nao possuem bloqueio completo de acesso publico ativado
SELECT
  name,
  region,
  account_id,
  block_public_acls,
  block_public_policy,
  ignore_public_acls,
  restrict_public_buckets
FROM
  aws_s3_bucket
WHERE
  NOT (block_public_acls AND block_public_policy AND ignore_public_acls AND restrict_public_buckets);
```

## Limites e trade-offs
Entenda a importância de passar colunas indexadas de filtro (*Key Columns*, como `WHERE region = 'sa-east-1'` ou `WHERE arn = '...'`): quando a coluna está na cláusula `WHERE`, o FDW chama o método `Get` pontual da API da nuvem em milissegundos em vez de listar (`List`) milhares de recursos em todas as regiões!

## Como verificar
Use o meta-comando `.inspect <plugin>` ou `.inspect <tabela>` dentro do shell interativo `steampipe query` para ver todas as tabelas e colunas disponíveis.

## Conexões
- [[steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam]] — Veja também: Steampipe: **JOINs Relacionais Cross-Cloud e Cross-SaaS** (`aws` + `kubernetes` + `github` + `okta`) para Investigação de Incidentes e IAM.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Referência cruzada direta com steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
