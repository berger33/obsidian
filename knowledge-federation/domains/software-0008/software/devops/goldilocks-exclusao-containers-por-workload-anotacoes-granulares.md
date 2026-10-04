---
id: software.devops.tranche11.001049
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

# Exclusão granular de containers e desativação por workload individual no Goldilocks

## Em uma frase
O Goldilocks permite excluir containers específicos de um workload individual ou desabilitar a geração de VPA para um Deployment específico dentro de um namespace habilitado, combinando anotações/labels em nível de workload com as flags globais do dashboard.

## Por que importa
Quando um namespace inteiro está habilitado com `goldilocks.fairwinds.com/enabled=true` (ou `--on-by-default`), pode existir um workload específico naquele namespace que já possui um VPA customizado gerenciado manualmente pela equipe, ou um container init/sidecar específico cujas métricas distorcem o sumário daquele Deployment.

## Como funciona
Conforme a documentação *Advanced Usage* (`goldilocks.docs.fairwinds.com/advanced/`), o Goldilocks respeita a hierarquia de configuração onde labels e anotações mais específicas sobrescrevem o comportamento geral do namespace ou das flags de CLI: (1) pode-se controlar o comportamento ou excluir workloads individuais dentro de um namespace monitorado; e (2) na seção *Container Exclusions*, além da flag global `--exclude-containers` nos comandos `dashboard` e `summary`, containers podem ser excluídos para workloads individuais via anotação no próprio recurso, evitando que containers auxiliares poluam as recomendações de CPU e memória da aplicação principal.

## Exemplo
```bash
# Executar o servidor do dashboard do Goldilocks excluindo globalmente containers sidecar de malha e observabilidade
goldilocks dashboard \
  --exclude-containers="istio-proxy,linkerd-proxy,datadog-agent,fluent-bit"
```

## Limites e trade-offs
Se um workload já possuir um objeto `VerticalPodAutoscaler` criado manualmente por fora do Goldilocks (sem as labels de propriedade do Goldilocks), o `goldilocks summary` e o `goldilocks dashboard` consultarão apenas os objetos VPA que possuem as labels gerenciadas pela ferramenta.

## Como verificar
Verifique as labels aplicadas nos objetos VPA gerados pelo controlador com `kubectl get vpa -A --show-labels` para identificar os recursos gerenciados pelo Goldilocks.

## Conexões
- [[goldilocks-instalacao-manifestos-separados-controller-dashboard]] — Veja também: Instalação do Goldilocks via manifestos Kubernetes separados (controller e dashboard) e RBAC.
- [[goldilocks-integracao-ecossistema-fairwinds-polaris-pluto-finops]] — Veja também: Integração do Goldilocks com Polaris e Pluto em fluxos contínuos de governança e FinOps no Kubernetes.
- [[goldilocks-cli-dashboard-summary-exclusao-containers-sidecars]] — Referência cruzada direta com goldilocks-cli-dashboard-summary-exclusao-containers-sidecars.
- [[goldilocks-controlador-flags-labels-namespaces-metricas]] — Referência cruzada direta com goldilocks-controlador-flags-labels-namespaces-metricas.
- [[goldilocks-modos-atualizacao-vpa-update-mode-resource-policy]] — Referência cruzada direta com goldilocks-modos-atualizacao-vpa-update-mode-resource-policy.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
