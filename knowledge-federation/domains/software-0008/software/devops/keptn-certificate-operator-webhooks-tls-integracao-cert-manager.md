---
id: software.devops.tranche20.001989
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

# Keptn Certificate Manager vs `cert-manager`: gerenciamento de certificados TLS para os webhooks e APIs do Keptn

## Em uma frase
O Keptn inclui por padrão o componente **Keptn Certificate Manager** (`certificate-operator`, status `stable`), que provisiona e rotaciona automaticamente os certificados TLS necessários para a comunicação segura entre o `kube-apiserver` e os webhooks/serviços de métricas do Keptn, permitindo alternativamente delegar essa função ao **`cert-manager`** existente no cluster.

## Por que importa
Os Mutating/Validating Webhooks de ciclo de vida do Keptn e o servidor da Custom Metrics API exigem certificados TLS válidos com `caBundle` injetado nos recursos `MutatingWebhookConfiguration`, `ValidatingWebhookConfiguration`, `APIService` e `CustomResourceDefinition` (conversion webhooks).

## Como funciona
Na instalação padrão via Helm (`helm upgrade --install keptn keptn/keptn`), o `certificate-operator` embutido do Keptn gerencia todo esse ciclo sem exigir dependências externas. Caso sua política de plataforma exija centralizar todos os certificados no `cert-manager`, basta desabilitar o `certificate-operator` embutido nas opções do chart Helm e configurar os `Issuer`/`Certificate` correspondentes do `cert-manager`.

## Exemplo
```bash
# Inspecionando o pod do certificate-operator e o Secret TLS gerado em keptn-system:
kubectl get pods -n keptn-system -l control-plane=certificate-operator
kubectl get secret -n keptn-system keptn-certs
```

## Limites e trade-offs
Se os certificados do webhook expirarem ou o `certificate-operator` for removido sem substituição pelo `cert-manager`, a criação de Pods nos namespaces monitorados pelo webhook do Keptn falhará no admission controller.

## Como verificar
Verifique a validade do certificado atual no Secret `keptn-certs` em `keptn-system` e a presença do `caBundle` em `kubectl get mutatingwebhookconfigurations`.

## Conexões
- [[keptn-autoscaling-hpa-custom-metrics-api-adapter-escalonamento]] — Veja também: Keptn com HorizontalPodAutoscaler (`HPA`): escalonamento de Pods no Kubernetes baseado em `KeptnMetric` via Custom Metrics API.
- [[keptn-controle-namespaces-monitorados-allowednamespaces-gitops-promotion]] — Veja também: Keptn Governança de Namespaces e Promoção GitOps: configuração de `allowedNamespaces` e estágios de `promotion`.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://keptn.sh/stable/docs/core-concepts/) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
