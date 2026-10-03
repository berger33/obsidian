---
id: software.devops.tranche15.001476
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

# Kamaji: ciclo de vida automatizado de certificados X.509 (`kubeadm`), rotação e auto-healing de estado

## Em uma frase
O Kamaji utiliza internamente bibliotecas do `kubeadm` para gerar, armazenar em Secrets do cluster de gerenciamento e rotacionar automaticamente todos os certificados X.509 e kubeconfigs de cada `TenantControlPlane`.

## Por que importa
A expiração de certificados internos da PKI do Kubernetes (`apiserver`, `front-proxy-client`, `etcd/datastore client`) é uma das causas mais críticas de indisponibilidade total de clusters gerenciados manualmente.

## Como funciona
Como os objetos `TenantControlPlane` e seus Secrets residem no management cluster sob reconciliação contínua do Operator, o Kamaji renova certificados antes do vencimento e, caso alguém apague acidentalmente o Deployment ou Secret gerado do control plane no management cluster, recria os recursos de forma idempotente.

## Exemplo
```bash
kubectl get secrets -n tenants -l kamaji.clastix.io/name=tenant-prod-cp
```

## Limites e trade-offs
Os certificados e chaves privadas da CA de cada cluster tenant ficam armazenados como Secrets no namespace do `TenantControlPlane` dentro do management cluster; restrinja o acesso RBAC a esses Secrets no cluster de gerenciamento.

## Como verificar
Extraia o kubeconfig administrativo do tenant a partir do Secret `<tcp-name>-admin-kubeconfig` e verifique a validade do certificado emitido.

## Conexões
- [[kamaji-konnectivity-redes-mistas-nat-hibrido-cloud-onprem]] — Veja também: Kamaji: comunicação segura entre Control Plane e Worker Nodes em redes distintas via Konnectivity.
- [[kamaji-cluster-api-control-plane-provider-infraestrutura-suportada]] — Veja também: Kamaji: provedor de Control Plane para Cluster API (CAPI) e matriz de provedores de infraestrutura.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
