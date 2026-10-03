---
id: software.seguranca.tranche01.000090
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos Topologias de Deploy e Storage Drivers: `sidecar` vs `service` no Kubernetes e sincronização via `git`, `blob` ou `disk`

## Em uma frase
Conforme destacado no README oficial, o Cerbos PDP pode ser implantado no Kubernetes (via Helm chart oficial) como **sidecar container** dentro de cada Pod da aplicação (comunicando-se via `localhost:3593` ou Unix Domain Socket com latência sub-milissegundo) ou como **serviço compartilhado** (`Deployment` + HPA), utilizando os drivers de armazenamento **`disk`**, **`git`**, **`blob`** (S3/GCS/MinIO), **`bundle`** ou **bancos SQL** (`postgres`, `mysql`, `sqlite3`).

## Por que importa
Em serviços de altíssima vazão que fazem múltiplas checagens de autorização por requisição, rodar o Cerbos como sidecar elimina 100% dos saltos de rede e garante que uma falha em outro Pod nunca afete a autorização local.

## Como funciona
Com o driver `git` ou `blob`, cada instância do Cerbos PDP faz polling periódico (`updatePollInterval`) no repositório Git ou bucket S3, compila as políticas alteradas a quente em memória e passa a servir a nova versão com zero downtime.

## Exemplo
```yaml
# Exemplo de storage driver git no .cerbos.yaml para atualização contínua GitOps sem restart:
storage:
  driver: "git"
  git:
    protocol: https
    url: https://github.com/org/authz-policies.git
    branch: main
    subDir: policies
    checkoutDir: /tmp/cerbos-policies
    updatePollInterval: 60s
```

## Limites e trade-offs
Ao rodar o container do Cerbos em Kubernetes com `readOnlyRootFilesystem: true`, monte um volume `emptyDir` no diretório configurado em `checkoutDir` / `workDir`.

## Como verificar
Consulte as métricas Prometheus expostas pelo Cerbos (`/metrics`) para monitorar a latência de avaliação e o status de sincronização do storage driver.

## Conexões
- [[cerbos-audit-logs-decision-logs-outputs-mascaramento-campos-sensiveis]] — Veja também: Cerbos Decision Audit Logs e Policy Outputs: trilha de auditoria de decisões e retorno de obrigações/máscaras para a aplicação.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
