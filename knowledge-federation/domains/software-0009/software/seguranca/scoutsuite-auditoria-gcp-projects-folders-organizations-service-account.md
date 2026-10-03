---
id: software.seguranca.tranche11.001014
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

# Scout Suite no **Google Cloud Platform (`scout gcp`)**: Auditoria em Escala por **Organization (`--organization-id`), Folder (`--folder-id`) e `--all-projects`**

## Em uma frase
No **Google Cloud Platform (GCP)**, cada ambiente ou microsserviço costuma ser isolado em seu próprio **GCP Project**, fazendo com que uma empresa de médio porte tenha facilmente 100 a 500 projetos organizados sob **Folders** e uma **Organization** raiz.

## Por que importa
Em vez de obrigar o auditor a rodar um comando para cada projeto, o provedor **`scout gcp`** (conforme definido em `ScoutSuite/__main__.py`) aceita quatro escopos hierárquicos: **`--project-id <id>`** (um projeto específico), **`--folder-id <id>`** (todos os projetos dentro de uma pasta GCP), **`--organization-id <id>`** (toda a organização GCP) ou **`--all-projects`** (todos os projetos visíveis pela credencial)!

## Como funciona
Para autenticação, você pode usar **`--user-account`** (`gcloud auth application-default login`) ou **`--service-account <caminho_json>`**, auditando Cloud IAM (incluindo chaves de Service Accounts criadas pelo usuário e vínculos com `primitive roles` `roles/owner` e `roles/editor`), Cloud Storage (GCS), Compute Engine (GCE e regras de Firewall VPC), Cloud SQL, KMS, Stackdriver Logging/Monitoring e GKE!

## Exemplo
```bash
# Auditar todos os projetos de uma Organizacao Google Cloud Platform usando Application Default Credentials (--user-account)
scout gcp \
  --user-account \
  --organization-id 123456789012 \
  --report-dir /cases/cloud-audit/scout-gcp \
  --max-workers 10 \
  --no-browser
```

## Limites e trade-offs
Quais papéis IAM (`Roles`) conceder à conta de auditoria na raiz da Organização GCP para que o `scout gcp` tenha visibilidade completa com privilégio mínimo? Atribua **`roles/viewer`** (*Viewer*), **`roles/iam.securityReviewer`** (*Security Reviewer*) e **`roles/cloudasset.viewer`**!

## Como verificar
Revise prioritariamente no relatório de GCP todas as Service Accounts que possuem chaves JSON gerenciadas pelo usuário (`userManaged` keys) ou que usam a Service Account padrão do Compute Engine com escopo `cloud-platform`.

## Conexões
- [[scoutsuite-auditoria-azure-rbac-entra-storage-network-keyvault]] — Veja também: Scout Suite no **Microsoft Azure (`scout azure`)**: Modos de Autenticação (`--cli`, `--msi`, `--service-principal`) e Varredura Multi-Subscription.
- [[scoutsuite-customizacao-rulesets-regras-json-conditions-parametrizadas]] — Veja também: Anatomia do Motor de Regras do Scout Suite (**`Ruleset` & `ProcessingEngine`**): Como Escrever **Regras e Rulesets JSON Customizados (`--ruleset`)**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
