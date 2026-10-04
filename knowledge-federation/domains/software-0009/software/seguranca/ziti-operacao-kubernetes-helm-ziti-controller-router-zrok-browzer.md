---
id: software.seguranca.tranche04.000310
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/openziti/ziti/release-next/README.md", "https://netfoundry.io/docs/openziti/intro/", "https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenZiti: Implantação em Kubernetes via Helm, `ziti-host` para ClusterIPs, `zrok` e BrowZer

## Em uma frase
O ecossistema OpenZiti para Kubernetes inclui charts Helm para Controller, Router e `ziti-edge-tunnel` (modo `ziti-host`), além de extensões especializadas como `zrok` (compartilhamento Zero Trust) e OpenZiti BrowZer (acesso web clientless via WebAssembly).

## Por que importa
Permite expor APIs `ClusterIP` e o próprio `kube-apiserver` de clusters Kubernetes privados sem `LoadBalancer` público nem Ingress exposto na internet.

## Como funciona
Um pod `ziti-host` rodando dentro do cluster Kubernetes possui uma identidade com permissão `Bind` e encaminha conexões da malha para serviços DNS internos (`*.svc.cluster.local`). Já o **OpenZiti BrowZer** carrega um SDK OpenZiti compilado em WebAssembly diretamente no navegador após login OIDC, permitindo acessar aplicações web *dark* sem instalar agente no desktop.

## Exemplo
```bash
# Instalar o pod ziti-host no cluster Kubernetes privado usando o chart oficial OpenZiti
helm repo add openziti https://docs.openziti.io/helm-charts/
helm repo update

helm upgrade --install ziti-host openziti/ziti-host \
  --namespace ziti-system --create-namespace \
  --set-file zitiIdentity=/etc/ziti/k8s-cluster-binder.json
```

## Limites e trade-offs
Se o pod `ziti-host` tiver acesso irrestrito de saída no cluster, qualquer serviço mapeado erroneamente por um administrador no Controller poderá ser alcançado; restrinja o pod com `NetworkPolicy` de *egress* no Kubernetes.

## Como verificar
Verifique `kubectl -n ziti-system logs deploy/ziti-host` e confirme o registro de *terminators* saudáveis para os `ClusterIPs` internos configurados no OpenZiti.

## Conexões
- [[ziti-smart-routing-fabric-mesh-terminators-load-balancing-ha]] — Veja também: OpenZiti: Smart Routing na Fabric Mesh, Terminators, Custos Dinâmicos e Alta Disponibilidade.
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.
- [[ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns]] — Referência cruzada direta com ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.
