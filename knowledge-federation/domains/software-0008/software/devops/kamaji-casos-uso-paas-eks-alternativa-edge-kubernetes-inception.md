---
id: software.devops.tranche15.001480
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/clastix/kamaji/master/README.md", "https://kamaji.clastix.io/reference/api/", "https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kamaji: casos de uso em Platform Engineering, Control Plane as a Service e Kubernetes at the Edge

## Em uma frase
O modelo de *Kubernetes Inception* (usar um cluster Kubernetes para hospedar dezenas de planos de controle Kubernetes) posiciona o Kamaji como motor central para construir plataformas PaaS internas, provedores de Kubernetes gerenciado (KaaS) e frotas de Edge Computing.

## Por que importa
Em cenários de Edge Computing ou lojas físicas com hardware restrito, rodar o control plane pesado localmente em cada loja consome memória preciosa; com o Kamaji, o control plane fica centralizado no datacenter e apenas os worker nodes leves rodam na ponta.

## Como funciona
Os usuários finais de cada tenant recebem permissões completas de `cluster-admin` dentro do seu próprio `TenantControlPlane` (podendo instalar CRDs, webhooks e operadores livremente), enquanto permanecem estritamente isolados no nível de infraestrutura dentro do management cluster.

## Exemplo
```bash
kubectl --kubeconfig=tenant.kubeconfig auth can-i '*' '*'
kubectl --kubeconfig=tenant.kubeconfig get nodes
```

## Limites e trade-offs
Para proteger o cluster de gerenciamento contra vizinhos barulhentos (*noisy neighbors*), defina sempre `requests` e `limits` de CPU e memória nos componentes `apiServer`, `controllerManager` e `scheduler` da especificação do `TenantControlPlane`.

## Como verificar
Confirme com `kubectl top pods -n tenants` no cluster de gerenciamento que os Pods de cada control plane respeitam os limites de recursos declarados.

## Conexões
- [[kamaji-upgrades-blue-green-10s-scale-to-zero-otimizacao]] — Veja também: Kamaji: upgrades Blue/Green de versão Kubernetes em 10 segundos e escalonamento elástico de Control Planes.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
