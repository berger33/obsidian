---
id: software.devops.tranche08.000769
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/getting-started", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: integrações cloud-native com Terraform Provider, Kubernetes Operator e GitHub Actions/GitLab CI

## Em uma frase
O Atlas integra-se a stacks cloud-native por meio do **Atlas Terraform Provider** (gerenciando o esquema dentro do plano do Terraform), do **Atlas Kubernetes Operator** (CRDs `AtlasSchema` e `AtlasMigration`) e de integrações nativas com GitHub Actions, GitLab CI, CircleCI e Bitbucket.

## Por que importa
Quando uma equipe provisiona um banco RDS/CloudSQL via Terraform ou implanta microsserviços no Kubernetes via GitOps (Argo CD / Flux), executar migrações de banco fora do fluxo de IaC/GitOps cria uma desconexão entre o provisionamento da infraestrutura e a evolução do esquema. A seção `Cloud-Native Integrations` do README oficial do Atlas conecta essas camadas.

## Como funciona
(1) **Terraform Provider**: permite declarar recursos `atlas_schema` ou `atlas_migration` no mesmo código Terraform que provisiona o RDS/CloudSQL, fazendo com que `terraform plan` mostre o diff SQL do banco e `terraform apply` aplique o esquema; (2) **Kubernetes Operator**: permite gerenciar esquemas e migrações nativamente no Kubernetes como Custom Resources (`AtlasSchema` para fluxo declarativo e `AtlasMigration` para fluxo versionado), reconciliados continuamente junto aos manifestos da aplicação; e (3) **CI/CD Integrations**: actions e componentes prontos para GitHub Actions, GitLab CI, CircleCI e Bitbucket Pipelines que executam `migrate lint` nos Pull Requests (postando relatórios comentados no PR) e `migrate apply` no merge.

## Exemplo
```yaml
# Exemplo de Custom Resource AtlasMigration gerenciado pelo Atlas Kubernetes Operator via GitOps
apiVersion: db.atlasgo.io/v1alpha1
kind: AtlasMigration
metadata:
  name: app-db-migration
spec:
  urlFrom:
    secretKeyRef:
      name: db-credentials
      key: url
  dir:
    configMapRef:
      name: app-migrations-dir
```

## Limites e trade-offs
Ao gerenciar migrações via **Atlas Kubernetes Operator** ou **Terraform Provider**, o controlador automatizado nunca deve aplicar mudanças destrutivas silenciosamente (`DROP TABLE`/`DROP COLUMN`) sem validação prévia; por isso, o operador e o provider integram verificações de segurança que bloqueiam a aplicação automática de planos destrutivos a menos que explicitamente autorizados pela política configurada.

## Como verificar
Em um cluster Kubernetes com o Atlas Operator instalado, execute `kubectl get atlasmigrations,atlasschemas` e verifique nas condições do status (`Ready=True`) a versão aplicada do esquema.

## Conexões
- [[atlasdb-seguranca-como-codigo-rbac-roles-permissions-rls]] — Veja também: Ariga Atlas: Security-as-Code para bancos de dados (roles, users, permissions e Row-Level Security em HCL).
- [[atlasdb-edicoes-community-apache2-binario-atlas-cloud]] — Veja também: Ariga Atlas: arquitetura de edições do Atlas (código base Apache-2.0, binário oficial e recursos avançados).
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-fluxo-versionado-migrate-diff-lint-apply]] — Referência cruzada direta com atlasdb-fluxo-versionado-migrate-diff-lint-apply.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
