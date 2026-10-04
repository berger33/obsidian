---
id: software.seguranca.tranche10.000906
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

# Steampipe **Shift-Left IaC**: Auditoria SQL de Arquivos Locais **Terraform (`.tf`, `.tfstate`)**, Manifestos **Kubernetes YAML** e **`Dockerfile`**

## Em uma frase
O Steampipe não consulta apenas APIs de nuvem ao vivo: através dos plugins oficiais **`terraform`**, **`kubernetes`** e **`docker`**, ele também analisa **arquivos estáticos de Infraestrutura como Código (IaC) diretamente no disco ou repositório Git**!

## Por que importa
Por exemplo, o plugin **`terraform`** expõe tabelas como `terraform_resource`, `terraform_module`, `terraform_variable`, `terraform_output` e `terraform_state_resource`: permitindo escrever queries SQL que auditam tanto o código HCL (`.tf`) quanto o arquivo de estado (`.tfstate`), ou **fazer um `JOIN` entre o que está declarado no `.tfstate` do Terraform e o que realmente existe ao vivo na conta AWS (`aws_*`) para detectar *Cloud Drift* e recursos órfãos ("Shadow IT")**!

## Como funciona
Da mesma forma, o plugin `kubernetes` pode ser configurado em `kubernetes.spc` com `source_type = ["helm", "manifest", "deployed"]` para cruzar manifestos YAML locais com os objetos reais rodando no cluster!

## Exemplo
```sql
-- Detectar Cloud Drift / Shadow IT: listar instancias EC2 rodando na AWS que NAO constam no Terraform State!
SELECT
  live.instance_id,
  live.instance_type,
  live.region,
  live.tags ->> 'Name' AS name
FROM
  aws_ec2_instance AS live
  LEFT JOIN terraform_state_resource AS tf
    ON tf.type = 'aws_instance'
    AND (tf.attributes_std ->> 'id') = live.instance_id
WHERE
  tf.name IS NULL;
```

## Limites e trade-offs
Reflita sobre o poder dessa query de `LEFT JOIN` entre `aws_ec2_instance` e `terraform_state_resource`: em 10 linhas de SQL você descobre instantaneamente qualquer servidor EC2, bucket S3 ou usuário IAM que foi criado manualmente no console web ("ClickOps") ou por um invasor fora da governança do Terraform!

## Como verificar
Combine essa detecção de drift com o `kics scan` para cobrir tanto a pré-implantação quanto a reconciliação em produção.

## Conexões
- [[steampipe-autoria-controles-customizados-powerpipe-hcl-policy-as-code]] — Veja também: Powerpipe HCL: Autoria de **Controles e Benchmarks Customizados (*Policy-as-Code*)** com SQL (`status`, `reason`, `resource` e Dimensões).
- [[steampipe-auditoria-postura-github-supply-chain-branch-protection-actions]] — Veja também: Steampipe Plugin **`github`**: Auditoria SQL de **Supply Chain, Repositórios Públicos, Branch Protection, Segredos e GitHub Actions**.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.
- [[kics-analise-terraform-variaveis-tfvars-modulos-plan-json]] — Referência cruzada direta com kics-analise-terraform-variaveis-tfvars-modulos-plan-json.
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — Referência cruzada direta com cloudquery-deteccao-drift-historico-temporal-snapshots-sql.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
