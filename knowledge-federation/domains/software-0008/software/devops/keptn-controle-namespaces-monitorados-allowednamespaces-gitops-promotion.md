---
id: software.devops.tranche20.001990
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md", "https://keptn.sh/stable/docs/core-concepts/", "https://github.com/keptn/lifecycle-toolkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keptn Governança de Namespaces e Promoção GitOps: configuração de `allowedNamespaces` e estágios de `promotion`

## Em uma frase
Por padrão, a orquestração de ciclo de vida do Keptn monitora os namespaces do cluster exceto namespaces reservados de sistema (como `kube-system` e `keptn-system`), podendo ser restrita via Helm (`allowedNamespaces`) ou ativada seletivamente, além de suportar tarefas de **promoção (`promotionTasks`)** ao final de um release bem-sucedido.

## Por que importa
Em clusters compartilhados, a equipe de plataforma pode querer ativar a interceptação de webhooks do Keptn apenas nos namespaces `staging` e `prod`, e acionar automaticamente a promoção da versão para o próximo estágio no Git apenas depois que todas as avaliações pós-deploy de `staging` passaram.

## Como funciona
Quando todas as `postDeploymentTasks` e `postDeploymentEvaluations` de um `KeptnAppVersion` terminam com sucesso, o Keptn executa as tarefas do estágio de **promotion** (ex.: um `KeptnTask` que abre um Pull Request no repositório GitOps ou dispara um webhook do Argo CD/GitLab para promover a tag para produção).

## Exemplo
```yaml
# Trecho de KeptnAppContext configurando tarefa de promoção após aprovação dos SLOs pós-deploy:
apiVersion: lifecycle.keptn.sh/v1beta1
kind: KeptnAppContext
metadata:
  name: ecommerce
  namespace: staging
spec:
  postDeploymentEvaluations:
    - staging-slo-evaluation
  promotionTasks:
    - trigger-gitops-prod-pr
```

## Limites e trade-offs
Nunca instale workloads de negócio no namespace `keptn-system`, pois ele é excluído da instrumentação dos webhooks de ciclo de vida do próprio Keptn.

## Como verificar
Verifique os seletores de namespace configurados no webhook com `kubectl get mutatingwebhookconfigurations -o yaml | grep -A 15 namespaceSelector`.

## Conexões
- [[keptn-certificate-operator-webhooks-tls-integracao-cert-manager]] — Veja também: Keptn Certificate Manager vs `cert-manager`: gerenciamento de certificados TLS para os webhooks e APIs do Keptn.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://keptn.sh/stable/docs/core-concepts/) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
