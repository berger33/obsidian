---
id: software.devops.tranche17.001613
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://clusternet.io/docs/introduction/", "https://raw.githubusercontent.com/clusternet/clusternet/main/README.md", "https://github.com/clusternet/clusternet"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clusternet: túnel reverso WebSocket e visitação direta de clusters filhos com regras RBAC dinâmicas

## Em uma frase
O `clusternet-agent` estabelece um canal de comunicação full-duplex sobre WebSocket até o `clusternet-hub`, permitindo que operadores e ferramentas acessem a API de qualquer cluster filho (mesmo atrás de firewall/NAT) usando um endpoint proxy no cluster pai com impersonação RBAC dinâmica.

## Por que importa
Expor a porta `6443` de centenas de clusters de borda na internet pública representa um risco grave de segurança, e distribuir centenas de arquivos `kubeconfig` estáticos para engenheiros impede a revogação centralizada de acessos.

## Como funciona
Quando o `clusternet-agent` se registra, o `clusternet-controller-manager` cria um objeto `ManagedCluster` e registra o socket de proxy no `clusternet-hub`. Um usuário autenticado no cluster pai pode acessar o cluster filho apontando o `kubectl` para o sub-recurso de proxy do cluster pai (`/apis/proxies.clusternet.io/v1alpha1/sockets/<cluster-id>/proxy/...`), onde o Clusternet aplica regras de RBAC dinâmicas antes de encaminhar a chamada pelo túnel.

## Exemplo
```bash
kubectl get managedclusters -A -o wide
kubectl --kubeconfig parent.kubeconfig \
  --server="https://parent-apiserver:6443/apis/proxies.clusternet.io/v1alpha1/sockets/cls-child-01/proxy/direct" \
  get nodes
```

## Limites e trade-offs
Para que o redirecionamento e upgrade de conexões (`kubectl exec`, `logs`, `port-forward`) funcionem através do `clusternet-hub` em versões modernas do Kubernetes (`>= 1.26`), a flag `--aggregator-reject-forwarding-redirect=false` deve estar configurada no `kube-apiserver` do cluster pai.

## Como verificar
Execute `kubectl get nodes` através da URL de socket proxy de um cluster filho e confirme que os nós retornados são os do cluster filho remoto.

## Conexões
- [[clusternet-shadow-apis-aggregated-apiserver-manifest-encapsulation]] — Veja também: Clusternet: *Shadow APIs* via Aggregated APIServer (`shadow/v1alpha1`) para captura transparente de recursos.
- [[clusternet-subscription-scheduling-replication-dividing-static-dynamic]] — Veja também: Clusternet: agendamento multi-cluster via CRD `Subscription` (`Replication`, `Static` e `Dynamic` Dividing).

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://clusternet.io/docs/introduction/) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
