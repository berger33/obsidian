---
id: software.devops.tranche11.001044
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://goldilocks.docs.fairwinds.com/advanced/", "https://goldilocks.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Configuração avançada de VPA no Goldilocks: vpa-update-mode e vpa-resource-policy por namespace ou workload

## Em uma frase
Embora o Goldilocks crie VPAs com `updateMode: "Off"` por padrão (apenas recomendação), usuários avançados podem sobrescrever o modo de atualização (`goldilocks.fairwinds.com/vpa-update-mode`) em nível de namespace ou de workload individual e definir políticas de recursos por container (`goldilocks.fairwinds.com/vpa-resource-policy`) com `minAllowed`, `maxAllowed` e `controlledValues`.

## Por que importa
Em alguns ambientes não críticos ou workloads elásticos onde o VPA Updater e o Admission Webhook estão deliberadamente instalados, a equipe pode querer que o Goldilocks configure `updateMode: "Auto"` ou `"Initial"` para um workload específico, impondo tetos (`maxAllowed`), pisos (`minAllowed`) e desabilitando o auto-scaling em containers sidecar como `istio-proxy`.

## Como funciona
Conforme documentado nas seções *VPA Update Mode*, *VPA Resource Policy* e *Workload Specifications* (`goldilocks.docs.fairwinds.com/advanced/`): (1) a label `goldilocks.fairwinds.com/vpa-update-mode="auto"` (ou `"off"`, `"initial"`, `"recreate"`) no namespace altera o modo dos VPAs daquele namespace; (2) a anotação **`goldilocks.fairwinds.com/vpa-update-mode=<mode>`** em um workload específico controla o `updateMode` daquele workload individualmente, independentemente da label do namespace; e (3) a anotação **`goldilocks.fairwinds.com/vpa-resource-policy`** recebe um objeto JSON definindo `containerPolicies` — onde cada item pode fixar `containerName`, `minAllowed` (`cpu`, `memory`), `maxAllowed`, `mode: "Off"` e `controlledValues` (`RequestsAndLimits` por padrão, ou `RequestsOnly`).

## Exemplo
```yaml
# Definir vpa-resource-policy via anotação JSON no Namespace para limitar CPU/memória e ignorar o sidecar istio-proxy
apiVersion: v1
kind: Namespace
metadata:
  name: pagamentos
  labels:
    goldilocks.fairwinds.com/enabled: "true"
  annotations:
    goldilocks.fairwinds.com/vpa-resource-policy: >
      {
        "containerPolicies": [
          {
            "containerName": "nginx",
            "minAllowed": { "cpu": "250m", "memory": "100Mi" },
            "maxAllowed": { "cpu": "2000m", "memory": "2048Mi" },
            "controlledValues": "RequestsOnly"
          },
          {
            "containerName": "istio-proxy",
            "mode": "Off"
          }
        ]
      }
```

## Limites e trade-offs
A documentação oficial adverte explicitamente que alterar `vpa-update-mode` para diferente de `"off"` é para uso avançado e **não é recomendado nem o padrão**, pois o auto-scaling vertical ativo requer o VPA Updater e o Admission Webhook e pode causar evicção/recriação de pods e conflito caso o mesmo workload utilize um HorizontalPodAutoscaler (HPA) baseado em CPU ou memória.

## Como verificar
Inspecione o objeto VPA gerado pelo controlador (`kubectl -n pagamentos get vpa -o yaml`) para confirmar que `spec.updatePolicy.updateMode` e `spec.resourcePolicy.containerPolicies` refletem exatamente as anotações configuradas.

## Conexões
- [[goldilocks-controlador-flags-labels-namespaces-metricas]] — Veja também: Controlador do Goldilocks: precedência de labels sobre flags de CLI, --on-by-default, --ignore-controller-kind e métricas Prometheus.
- [[goldilocks-cli-dashboard-summary-exclusao-containers-sidecars]] — Veja também: Comandos da CLI do Goldilocks (dashboard, summary, create-vpas, delete-vpas) e exclusão de containers sidecar (--exclude-containers).
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
