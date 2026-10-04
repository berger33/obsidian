---
id: software.seguranca.tranche10.000914
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
fontes: ["https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md", "https://www.cloudquery.io/docs/cli/getting-started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CloudQuery em Escala Enterprise: Descoberta Automática de Contas via **AWS Organizations (`org`)**, **GCP Folders** e **Azure Subscriptions**

## Em uma frase
Em uma organização onde novas contas AWS ou projetos GCP são provisionados toda semana via Terraform/Control Tower, manter uma lista estática de IDs de contas no arquivo de configuração da ferramenta de segurança cria pontos cegos (*blind spots*) imediatos.

## Por que importa
O plugin AWS do CloudQuery resolve isso nativamente através do bloco **`org:`** dentro de `spec:`: você informa a role de leitura da conta de gerenciamento/delegada da **AWS Organizations** e o nome da IAM Role padronizada presente nas contas-membro (ex.: `member_role_name: "CloudQuerySecurityAuditRole"`), podendo filtrar por **Unidades Organizacionais (`organization_units: ["ou-..."]`)** ou pular contas de sandbox (`skip_organizational_units`)!

## Como funciona
No **GCP**, o plugin `cloudquery/gcp` descobre automaticamente todos os projetos ativos abaixo de `folder_ids` usando `folder_recursion_depth`; e no **Azure**, o plugin `cloudquery/azure` descobre todas as `subscriptions` acessíveis pela Service Principal!

## Exemplo
```yaml
# aws-org.yml — Descoberta automatica de todas as contas de uma AWS Organization assumindo IAM Role somente-leitura
kind: source
spec:
  name: aws_organization_prod
  path: cloudquery/aws
  registry: cloudquery
  version: "v27.0.0"
  tables: ["aws_s3_buckets", "aws_iam_*", "aws_ec2_*", "aws_rds_*"]
  destinations: ["postgresql"]
  spec:
    regions: ["*"]
    org:
      admin_account:
        local_profile: "org-management-readonly"
      member_role_name: "CloudQuerySecurityAuditRole"
      member_role_session_name: "cloudquery-cspm-sync"
```

## Limites e trade-offs
Para máxima segurança na AWS Organizations, configure uma **Conta Membro Delegada de Segurança (*Delegated Administrator*)** para listar as contas da organização (`organizations:ListAccounts`) em vez de usar credenciais da conta Management raiz (`root management account`).

## Como verificar
Confirme após o sync com `SELECT DISTINCT account_id FROM aws_s3_buckets;` que todas as contas ativas da organização foram inventariadas.

## Conexões
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Veja também: CloudQuery: Modos de Escrita no Destino (**`overwrite-delete-stale`**, **`overwrite`** e **`append`**) e Migração Automática de Schema (`migrate_mode`).
- [[cloudquery-politicas-seguranca-sql-cspm-aws-gcp-azure-k8s]] — Veja também: CloudQuery **CSPM Policies em SQL**: Execução de Views de Conformidade (**CIS, NIST, PCI DSS**) e Detecção de Exposição Pública sobre o Banco Sincronizado.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas]] — Referência cruzada direta com cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas.
- [[steampipe-agregadores-multi-conta-connections-spc-aws-organizations]] — Referência cruzada direta com steampipe-agregadores-multi-conta-connections-spc-aws-organizations.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
