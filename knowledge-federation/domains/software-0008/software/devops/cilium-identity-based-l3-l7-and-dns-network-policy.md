---
id: software.devops.tranche02.000125
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://docs.cilium.io/en/stable/overview/component-overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Políticas de rede L3–L7 e DNS baseadas em identidade de segurança

## Em uma frase
A subseção `Network Policy` do `README.rst` explica que firewalls tradicionais de contêineres filtram por IPs de origem e portas de destino — exigindo manipular firewalls em todos os servidores sempre que um contêiner inicia no cluster —, enquanto o Cilium atribui uma **identidade de segurança** a grupos de contêineres que compartilham políticas idênticas, associando essa identidade aos pacotes emitidos e validando-a no nó receptor, além de suportar políticas L3/L4, políticas baseadas em DNS (FQDNs ou wildcards como `api.example.com` e `*.trusted.com`), políticas L7 (método HTTP, URL path como `GET /public/.*`, cabeçalhos como `X-Token: [0-9]+` e chamadas gRPC) e políticas por CIDR.

## Por que importa
Desacoplar a segurança do endereço IP efêmero do pod permite escalar políticas em clusters dinâmicos e controlar egressos para APIs externas por nome DNS e caminho HTTP.

## Como funciona
Defina políticas do Cilium combinando seletores de labels (identidade), regras de egress por FQDN DNS e restrições L7 de método/caminho HTTP ou gRPC conforme o princípio do menor privilégio.

## Exemplo
Um pod de pagamento recebe permissão de saída apenas para `api.example.com` via política DNS e aceita internamente apenas `GET` em `/public/.*` ou chamadas com o cabeçalho `X-Token`.

## Limites e trade-offs
Políticas DNS dependem de que as consultas DNS dos pods passem pela inspeção DNS do Cilium; conexões diretas por IP hardcoded não serão autorizadas pela regra de FQDN.

## Como verificar
Conferi a subseção Network Policy em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-cluster-mesh-multicluster-service-discovery]] — Veja também: Cluster Mesh: descoberta global de serviços e identidade unificada entre clusters.
- [[cilium-service-mesh-encryption-and-gateway-api]] — Veja também: Service Mesh sem sidecars tradicionais: criptografia IPsec/WireGuard/ztunnel e Gateway API.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
