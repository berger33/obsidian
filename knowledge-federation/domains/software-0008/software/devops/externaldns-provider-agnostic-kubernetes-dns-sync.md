---
id: software.devops.tranche03.000211
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

# Sincronização declarativa e agnóstica de recursos Kubernetes com provedores DNS

## Em uma frase
O README oficial no repositório kubernetes-sigs/external-dns define o ExternalDNS como o controlador que sincroniza Services e Ingresses expostos no Kubernetes com provedores DNS: inspirado no Kubernetes DNS (KubeDNS), ele consulta a API do Kubernetes para determinar a lista desejada de registros DNS, mas, diferentemente do KubeDNS, não é um servidor DNS em si — ele apenas configura provedores DNS externos (como AWS Route 53 ou Google Cloud DNS) de maneira agnóstica ao provedor.

## Por que importa
Sem o ExternalDNS, sempre que um Service do tipo LoadBalancer ou um Ingress recebe um novo endereço IP externo no cluster, alguém precisa atualizar manualmente a zona DNS no provedor de nuvem ou executar scripts externos fora do ciclo declarativo do Kubernetes.

## Como funciona
Implante o ExternalDNS como controlador no cluster para que a criação ou alteração de Services e Ingresses atualize automaticamente os registros A, AAAA ou CNAME no provedor DNS configurado.

## Exemplo
Ao expor uma nova API via Ingress no Kubernetes, o ExternalDNS lê o hostname desejado na API do cluster e cria o registro correspondente no AWS Route 53 ou Google Cloud DNS.

## Limites e trade-offs
Como o ExternalDNS apenas configura provedores DNS externos e não responde consultas DNS diretamente, a resolução final continua dependendo da disponibilidade e propagação do provedor DNS escolhido.

## Como verificar
Conferi a abertura e a seção What It Does no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-domain-filter-and-txt-owner-id-safety]] — Veja também: Isolamento seguro de zonas não vazias com --domain-filter e --txt-owner-id.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
