---
id: software.devops.tranche15.001474
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
fontes: ["https://kamaji.clastix.io/reference/api/", "https://raw.githubusercontent.com/clastix/kamaji/master/README.md", "https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kamaji: gerenciamento automático e auto-healing dos addons `coreDNS`, `kubeProxy` e `konnectivity`

## Em uma frase
Por meio do bloco `spec.addons`, o Kamaji configura e reconcilia automaticamente os componentes essenciais do cluster tenant (`coreDNS`, `kubeProxy` e `konnectivity`), recriando-os de forma idempotente caso sejam removidos por erro humano.

## Por que importa
Em clusters onde os desenvolvedores recebem permissão de administrador sobre o plano de controle do tenant, um `kubectl delete deployment coredns -n kube-system` acidental derrubaria a resolução de nomes do cluster se não houvesse reconciliação externa.

## Como funciona
O controlador do Kamaji monitora continuamente o cluster tenant a partir do cluster de gerenciamento: em `addons.coreDNS` (com `dnsServiceIPs`, `imageRepository` e `imageTag`), `addons.kubeProxy` e `addons.konnectivity`, qualquer desvio ou exclusão é revertido automaticamente.

## Exemplo
```yaml
spec:
  addons:
    coreDNS: {}
    kubeProxy: {}
    konnectivity: {}
```

## Limites e trade-offs
Nos addons `coreDNS` e `kubeProxy`, o repositório (`imageRepository`) e a tag (`imageTag`) são configuráveis para espelhos internos, mas o nome da imagem base permanece fixado em `coredns` e `kube-proxy`.

## Como verificar
No cluster tenant, verifique que os Pods de `coredns`, `kube-proxy` e `konnectivity-agent` estão rodando em `kube-system`.

## Conexões
- [[kamaji-datastore-multitenancy-etcd-kine-postgresql-mysql-nats]] — Veja também: Kamaji: desacoplamento e multi-tenancy do `Datastore` com etcd ou Kine (PostgreSQL, MySQL e NATS).
- [[kamaji-konnectivity-redes-mistas-nat-hibrido-cloud-onprem]] — Veja também: Kamaji: comunicação segura entre Control Plane e Worker Nodes em redes distintas via Konnectivity.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://kamaji.clastix.io/reference/api/) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
