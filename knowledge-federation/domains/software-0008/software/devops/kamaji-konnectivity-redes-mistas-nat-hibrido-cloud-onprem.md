---
id: software.devops.tranche15.001475
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

# Kamaji: comunicação segura entre Control Plane e Worker Nodes em redes distintas via Konnectivity

## Em uma frase
O addon `konnectivity` do Kamaji estabelece túneis reversos seguros entre os worker nodes e o `kube-apiserver` hospedado, permitindo operar clusters híbridos onde os worker nodes ficam atrás de NAT ou em redes privadas não roteáveis pelo control plane.

## Por que importa
Em topologias híbridas (Control Plane na nuvem e worker nodes on-premises/edge) sem IPs públicos nos nós, o `kube-apiserver` não conseguiria abrir conexões TCP diretas para o Kubelet a fim de atender `kubectl logs`, `kubectl exec` ou `kubectl port-forward`.

## Como funciona
Quando `addons.konnectivity` está habilitado, o Kamaji injeta o `konnectivity-server` junto ao Pod do `kube-apiserver` no management cluster e implanta o `konnectivity-agent` nos worker nodes do tenant. Os agentes iniciam conexões de saída para o control plane, e todo o tráfego API-para-nó flui por esse túnel autenticado.

## Exemplo
```bash
kubectl --kubeconfig=tenant.kubeconfig get pods -n kube-system -l k8s-app=konnectivity-agent
kubectl --kubeconfig=tenant.kubeconfig logs -n kube-system -l k8s-app=konnectivity-agent --tail=20
```

## Limites e trade-offs
Sempre que os worker nodes residirem em uma VPC, datacenter ou rede edge diferente da rede do cluster de gerenciamento, o addon `konnectivity` é obrigatório para que comandos interativos do Kubelet funcionem.

## Como verificar
Teste `kubectl --kubeconfig=tenant.kubeconfig exec` e `kubectl logs` contra um Pod rodando em um worker node remoto.

## Conexões
- [[kamaji-addons-gerenciados-coredns-kubeproxy-konnectivity]] — Veja também: Kamaji: gerenciamento automático e auto-healing dos addons `coreDNS`, `kubeProxy` e `konnectivity`.
- [[kamaji-gestao-automatica-certificados-kubeadm-rotacao-autohealing]] — Veja também: Kamaji: ciclo de vida automatizado de certificados X.509 (`kubeadm`), rotação e auto-healing de estado.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
