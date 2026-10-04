---
id: software.seguranca.tranche11.001013
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Scout Suite no **Microsoft Azure (`scout azure`)**: Modos de Autenticação (`--cli`, `--msi`, `--service-principal`) e Varredura Multi-Subscription

## Em uma frase
Em ambientes **Microsoft Azure e Microsoft Entra ID (antigo Azure AD)**, a complexidade de autenticação e a divisão de recursos por dezenas de **Subscriptions** dificultam auditorias manuais pelo Azure Portal.

## Por que importa
O provedor **`scout azure`** (visível em `ScoutSuite/__main__.py`) oferece seis estratégias nativas de autenticação: **(1) `--cli`** (reutiliza a sessão já autenticada no `az login` local); **(2) `--user-account`** ou **`--user-account-browser`** (fluxo interativo com suporte a MFA no navegador); **(3) `--service-principal`** (com `--tenant-id`, `--client-id` e `--client-secret`, ou `--file-auth`); e **(4) `--msi` (*Managed Service Identity*)** (para rodar diretamente dentro de uma VM ou container Azure sem nenhuma credencial estática!)!

## Como funciona
E para cobrir todo o locatário corporativo de uma só vez, basta passar **`--all-subscriptions`** (ou `--subscription-ids <sub1> <sub2>`), auditando simultaneamente Microsoft Entra ID, Azure RBAC, Storage Accounts, Key Vaults, Network Security Groups (NSGs), Azure SQL, CosmosDB, App Services, Virtual Machines e Security Center (Defender for Cloud)!

## Exemplo
```bash
# Auditar todas as Subscriptions acessiveis de um Tenant Azure usando a sessao autenticada do Azure CLI (--cli --all-subscriptions)
scout azure \
  --cli \
  --tenant-id 00000000-0000-0000-0000-000000000000 \
  --all-subscriptions \
  --report-dir /cases/cloud-audit/scout-azure \
  --no-browser
```

## Limites e trade-offs
Atenção a um detalhe importante de permissões no Azure: atribuir a role **`Reader`** na raiz do Management Group (ou nas Subscriptions) permite ao Scout Suite ler todos os recursos de infraestrutura (VMs, NSGs, Storage, SQL), mas para que ele consiga auditar também usuários, grupos e aplicações do **Microsoft Entra ID**, a identidade auditora precisa ter a role **`Directory Readers`** no Entra ID!

## Como verificar
Verifique no relatório HTML gerado a seção `Azure Active Directory` e `RBAC` para identificar atribuições excessivas de `Owner` ou `Contributor`.

## Conexões
- [[scoutsuite-auditoria-aws-iam-s3-ec2-rds-cloudtrail-vpc]] — Veja também: Scout Suite na **AWS (`scout aws`)**: Escopo de Serviços (`--services`), Regiões (`--regions`), Controle de Taxa (`--max-rate`) e Mínimo Privilégio IAM.
- [[scoutsuite-auditoria-gcp-projects-folders-organizations-service-account]] — Veja também: Scout Suite no **Google Cloud Platform (`scout gcp`)**: Auditoria em Escala por **Organization (`--organization-id`), Folder (`--folder-id`) e `--all-projects`**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.
- [[cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure]] — Referência cruzada direta com cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
