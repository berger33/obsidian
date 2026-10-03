---
id: software.devops.tranche03.000215
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md", "https://kubernetes-sigs.github.io/external-dns/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Registros DNS apontando para ClusterIP com internal-hostname e --publish-internal-services

## Em uma frase
Ainda na subseção Setup Steps, o README explica que a anotação external-dns.kubernetes.io/internal-hostname=nginx.internal.example.org. pode ser usada para criar registros DNS tendo o endereço ClusterIP do Service como alvo, ressaltando que, se o Service não for do tipo LoadBalancer, é necessário passar a flag --publish-internal-services ao ExternalDNS.

## Por que importa
Em redes corporativas conectadas por VPN, Direct Connect ou CNI roteável onde clientes internos precisam resolver nomes em uma zona DNS privada apontando para IPs internos do cluster, separar internal-hostname do hostname público evita expor endpoints internos em zonas públicas.

## Como funciona
Utilize a anotação external-dns.kubernetes.io/internal-hostname em conjunto com uma instância do ExternalDNS configurada para a zona DNS interna e habilite --publish-internal-services quando expuser Services do tipo ClusterIP.

## Exemplo
Um serviço interno recebe a anotação external-dns.kubernetes.io/internal-hostname=nginx.internal.example.org. para que sistemas legados na VPC corporativa resolvam seu endereço interno.

## Limites e trade-offs
O endereço ClusterIP só é roteável dentro da malha do cluster ou em topologias de rede integradas; verifique se os clientes que consultam a zona DNS privada conseguem alcançar a faixa de IPs publicada.

## Como verificar
Conferi a instrução sobre internal-hostname e a flag --publish-internal-services na subseção Setup Steps do README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-hostname-and-ttl-service-annotations]] — Veja também: Anotações external-dns.kubernetes.io/hostname e external-dns.kubernetes.io/ttl em Services.
- [[externaldns-policy-sync-versus-upsert-only]] — Veja também: Políticas de ciclo de vida de registros: --policy=sync versus --policy=upsert-only.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
