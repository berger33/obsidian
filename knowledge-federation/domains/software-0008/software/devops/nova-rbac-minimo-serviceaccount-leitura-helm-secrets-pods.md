---
id: software.devops.tranche12.001147
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://nova.docs.fairwinds.com/usage/", "https://nova.docs.fairwinds.com/quickstart/", "https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Configuração de RBAC de Mínimo Privilégio para Execução In-Cluster

## Em uma frase
Para rodar o Nova dentro de um cluster Kubernetes como Job ou CronJob, o `ServiceAccount` associado precisa de permissões de leitura (`get`, `list`) sobre os Secrets/ConfigMaps de armazenamento do Helm v3 e sobre os Pods (quando `--containers` é utilizado).

## Por que importa
Conceder `cluster-admin` a um CronJob de auditoria ou, no extremo oposto, conceder apenas leitura de `Pods` sem acesso aos `Secrets` do tipo `helm.sh/release.v1` faz com que o Nova ou tenha privilégios excessivos ou retorne uma lista vazia de charts Helm.

## Como funciona
O Helm v3 armazena os metadados de cada release em objetos `Secret` (driver padrão) com o label `owner=helm` no namespace onde a release foi instalada. Portanto, a `ClusterRole` do Nova requer `get` e `list` em `secrets`, `configmaps` e `pods` (e `namespaces`) para inspecionar as releases e imagens em todo o cluster sem permissão de escrita (`create`, `update`, `delete`).

## Exemplo
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: nova-audit-reader
rules:
  - apiGroups: [""]
    resources: ["namespaces", "pods", "secrets", "configmaps"]
    verbs: ["get", "list"]
```

## Limites e trade-offs
Como a leitura de `secrets` no Kubernetes API não permite filtrar por `type: helm.sh/release.v1` diretamente nas regras da `ClusterRole`, o ServiceAccount do Nova deve ser restrito exclusivamente ao Pod de auditoria e nunca compartilhado com workloads de aplicação.

## Como verificar
Verifique as permissões do ServiceAccount com `kubectl auth can-i list secrets --all-namespaces --as=system:serviceaccount:platform-audit:nova-reader` antes de agendar o CronJob.

## Conexões
- [[nova-migracao-registry-imagens-assinadas-imutaveis-pkg-dev]] — Veja também: Fairwinds Nova: Migração de Registry (us-docker.pkg.dev) e Imagens Assinadas e Imutáveis.
- [[nova-combinado-pluto-polaris-goldilocks-governanca-upgrades]] — Veja também: Fairwinds Nova: Uso Combinado com Pluto, Polaris e Goldilocks no Planejamento de Upgrades de Cluster.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://nova.docs.fairwinds.com/usage/) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/quickstart/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
