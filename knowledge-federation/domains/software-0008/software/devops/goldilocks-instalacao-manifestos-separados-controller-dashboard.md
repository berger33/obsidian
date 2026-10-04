---
id: software.devops.tranche11.001048
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
fontes: ["https://goldilocks.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/advanced/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Instalação do Goldilocks via manifestos Kubernetes separados (controller e dashboard) e RBAC

## Em uma frase
Além da instalação preferencial via Helm (`fairwinds-stable/goldilocks`), o Goldilocks disponibiliza coleções separadas de manifestos YAML em `hack/manifests/controller` e `hack/manifests/dashboard` para implantar o controlador e o servidor web de forma independente no cluster.

## Por que importa
Ambientes que não utilizam Helm diretamente ou que preferem compor overlays Kustomize a partir de manifestos puros podem controlar separadamente o ciclo de vida, as réplicas, as NetworkPolicies e as contas de serviço (`ServiceAccount` / `ClusterRole`) do controlador e do dashboard.

## Como funciona
Conforme o *Method 2 - Manifests* na documentação oficial de instalação (`goldilocks.docs.fairwinds.com/installation/`), o repositório `FairwindsOps/goldilocks` organiza em `hack/manifests/controller` os recursos necessários para o loop de reconciliação (Deployment do `goldilocks controller`, `ServiceAccount` e permissões RBAC para observar namespaces, workloads e criar/atualizar/deletar objetos `VerticalPodAutoscaler`), e em `hack/manifests/dashboard` o Deployment e o Service `ClusterIP` (`goldilocks-dashboard`) que lê os objetos VPA em modo somente-leitura para renderizar a interface web na porta `8080`.

## Exemplo
```bash
# Instalar os componentes controller e dashboard do Goldilocks a partir dos manifestos YAML oficiais
git clone https://github.com/FairwindsOps/goldilocks.git
cd goldilocks
kubectl create namespace goldilocks
kubectl -n goldilocks apply -f hack/manifests/controller
kubectl -n goldilocks apply -f hack/manifests/dashboard
```

## Limites e trade-offs
Como o serviço `goldilocks-dashboard` expõe informações sobre todos os namespaces, workloads e configurações de recursos do cluster sem autenticação embutida por padrão, a instalação padrão cria apenas um Service do tipo `ClusterIP` (acessível via `kubectl port-forward`); caso deseje expô-lo via Ingress, proteja-o obrigatoriamente com um proxy autenticador como o **OAuth2 Proxy**.

## Como verificar
Verifique os pods e serviços criados com `kubectl -n goldilocks get deploy,pods,svc` e confirme que ambos os Deployments (`goldilocks-controller` e `goldilocks-dashboard`) estão `Available`.

## Conexões
- [[goldilocks-interpretacao-qos-guaranteed-burstable-dashboard]] — Veja também: Interpretação das recomendações do Goldilocks Dashboard: classes de QoS Guaranteed versus Burstable no Kubernetes.
- [[goldilocks-exclusao-containers-por-workload-anotacoes-granulares]] — Veja também: Exclusão granular de containers e desativação por workload individual no Goldilocks.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.
- [[oauth2proxy-integracao-ingress-nginx-ext-authz-headers]] — Referência cruzada direta com oauth2proxy-integracao-ingress-nginx-ext-authz-headers.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/installation/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
