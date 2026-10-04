---
id: software.seguranca.tranche10.000905
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

# Powerpipe HCL: Autoria de **Controles e Benchmarks Customizados (*Policy-as-Code*)** com SQL (`status`, `reason`, `resource` e Dimensões)

## Em uma frase
Toda organização possui regras internas de segurança e governança que vão além dos benchmarks públicos do CIS (por exemplo: *"Todo bucket S3 ou instância EC2 de produção deve ter a tag `DataClassification` e `OwnerEmail`"* ou *"Nenhum Security Group pode permitir a porta 22 para fora da CIDR da VPN corporativa `10.250.0.0/16`"*).

## Por que importa
No Powerpipe, criar seus próprios controles *Policy-as-Code* versionados em Git é simples: você escreve blocos **`query`**, **`control`** e **`benchmark`** em arquivos **`.pp` (Powerpipe HCL)**!

## Como funciona
A convenção obrigatória de toda `query` de controle no Powerpipe é retornar pelo menos três colunas no `SELECT`: **`resource`** (o identificador/ARN único do ativo), **`status`** (`'ok'`, `'alarm'`, `'info'` ou `'skip'`) e **`reason`** (a explicação legível para o relatório de auditoria), além de dimensões opcionais como `region` e `account_id`!

## Exemplo
```hcl
# controles_internos.pp — Controle customizado em Powerpipe HCL exigindo criptografia KMS em volumes EBS
control "ebs_volume_encrypted_with_cmk" {
  title       = "Volumes EBS de producao devem usar criptografia habilitada"
  severity    = "high"
  sql         = <<-EOQ
    SELECT
      arn AS resource,
      CASE
        WHEN encrypted THEN 'ok'
        ELSE 'alarm'
      END AS status,
      CASE
        WHEN encrypted THEN volume_id || ' esta criptografado (' || COALESCE(kms_key_id, 'default key') || ').'
        ELSE volume_id || ' NAO esta criptografado!'
      END AS reason,
      region,
      account_id
    FROM
      aws_ebs_volume;
  EOQ
}
```

## Limites e trade-offs
Para executar imediatamente seu controle customizado sem precisar instalá-lo em um repositório remoto, basta rodar **`powerpipe control run ebs_volume_encrypted_with_cmk`** no diretório onde está o arquivo `.pp`!

## Como verificar
Use variáveis parametrizadas (`variable "approved_regions" { type = list(string) ... }`) no arquivo `.pp` ou `.spvars` para reutilizar o mesmo controle em diferentes unidades de negócio.

## Conexões
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Veja também: **Powerpipe (`turbot/powerpipe`)**: Execução de +5.000 Controles de Conformidade (**CIS Benchmarks, NIST 800-53, PCI DSS, SOC 2, HIPAA**) sobre o Steampipe.
- [[steampipe-auditoria-shift-left-iac-plugins-terraform-kubernetes-docker]] — Veja também: Steampipe **Shift-Left IaC**: Auditoria SQL de Arquivos Locais **Terraform (`.tf`, `.tfstate`)**, Manifestos **Kubernetes YAML** e **`Dockerfile`**.
- [[kics-desenvolvimento-queries-customizadas-rego-cxpolicy-metadata]] — Referência cruzada direta com kics-desenvolvimento-queries-customizadas-rego-cxpolicy-metadata.
- [[cloudquery-politicas-seguranca-sql-cspm-aws-gcp-azure-k8s]] — Referência cruzada direta com cloudquery-politicas-seguranca-sql-cspm-aws-gcp-azure-k8s.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
