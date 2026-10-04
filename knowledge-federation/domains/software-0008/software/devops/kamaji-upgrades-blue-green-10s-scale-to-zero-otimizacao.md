---
id: software.devops.tranche15.001479
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

# Kamaji: upgrades Blue/Green de versão Kubernetes em 10 segundos e escalonamento elástico de Control Planes

## Em uma frase
Como o plano de controle roda como um Deployment de Pods stateless sobre um `Datastore` externo, o Kamaji realiza upgrades de versão do Kubernetes em cerca de 10 segundos usando estratégia Blue/Green e permite escalar réplicas a zero quando o cluster está ocioso.

## Por que importa
Atualizar o control plane em VMs tradicionais com `kubeadm upgrade` nó a nó leva dezenas de minutos e mantém versões mistas de `kube-apiserver` respondendo simultaneamente durante a janela.

## Como funciona
Quando o campo `spec.version` do `TenantControlPlane` é atualizado (ou quando `spec.replicas` é alterado para `0` em ambientes efêmeros de CI/dev), o Kamaji substitui os Pods do plano de controle rapidamente sem tocar nos discos de dados do `Datastore`.

## Exemplo
```bash
kubectl patch kamajicontrolplane tenant-prod-cp -n tenants \
  --type merge -p '{"spec":{"version":"v1.31.1"}}'
kubectl rollout status deployment/tenant-prod-cp -n tenants
```

## Limites e trade-offs
Ao escalar `replicas: 0` para economizar recursos em clusters de desenvolvimento noturnos, lembre-se de que os Kubelets dos worker nodes perderão conexão com a API até que `replicas` volte para `>= 1`.

## Como verificar
Acompanhe `kubectl rollout status` do Deployment do `TenantControlPlane` durante uma atualização de versão e meça o tempo de convergência.

## Conexões
- [[kamaji-datastore-overrides-separacao-eventos-etcd-escalabilidade]] — Veja também: Kamaji: separação de recursos de alto volume com `dataStoreOverrides` no `TenantControlPlane`.
- [[kamaji-casos-uso-paas-eks-alternativa-edge-kubernetes-inception]] — Veja também: Kamaji: casos de uso em Platform Engineering, Control Plane as a Service e Kubernetes at the Edge.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
