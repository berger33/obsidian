---
id: software.devops.tranche17.001612
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

# Clusternet: *Shadow APIs* via Aggregated APIServer (`shadow/v1alpha1`) para captura transparente de recursos

## Em uma frase
O `clusternet-hub` expõe o grupo de API `shadow/v1alpha1` como um *Aggregated APIServer*, espelhando todos os tipos de recursos do Kubernetes (e CRDs) para que objetos criados pelos usuários sejam automaticamente encapsulados em objetos `Manifest` multi-cluster em vez de serem instanciados localmente no cluster pai.

## Por que importa
No cluster hospedeiro (pai), criar um `apps/v1 Deployment` normal faria o `kube-controller-manager` local criar Pods no próprio cluster pai. Com as *Shadow APIs*, o usuário usa a mesma estrutura exata do recurso (ou o plugin `kubectl clusternet`) e o Clusternet o armazena apenas como um template de distribuição (`Manifest`).

## Como funciona
Quando uma requisição é enviada para `/apis/shadow/v1alpha1/...` (ou interceptada pelo wrapper `client-go` / `kubectl clusternet apply`), o `clusternet-hub` converte e persiste o objeto em um recurso `Manifest` (`apps.clusternet.io/v1alpha1`), mantendo-o inerte no cluster pai até que uma `Subscription` o selecione e distribua para os clusters filhos.

## Exemplo
```bash
kubectl krew install clusternet
kubectl clusternet apply -f my-deployment.yaml
kubectl get manifests -n default
```

## Limites e trade-offs
Se o `clusternet-hub` estiver indisponível, chamadas direcionadas ao grupo `shadow/v1alpha1` falharão na camada de agregação da API do cluster pai; monitore continuamente a saúde do `APIService`.

## Como verificar
Após executar `kubectl clusternet apply -f my-deployment.yaml`, rode `kubectl get manifests` para confirmar que o template foi gravado sem criar Pods locais no cluster pai (`kubectl get pods`).

## Conexões
- [[clusternet-arquitetura-hub-agent-scheduler-controller-cncf]] — Veja também: Clusternet: arquitetura CNCF Sandbox (`clusternet-hub`, `clusternet-agent`, `clusternet-scheduler` e `clusternet-controller-manager`).
- [[clusternet-sockets-websocket-tunnel-acesso-clusters-filhos-rbac]] — Veja também: Clusternet: túnel reverso WebSocket e visitação direta de clusters filhos com regras RBAC dinâmicas.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://clusternet.io/docs/introduction/) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
