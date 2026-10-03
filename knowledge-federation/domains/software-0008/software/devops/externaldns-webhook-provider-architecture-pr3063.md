---
id: software.devops.tranche03.000219
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md", "https://github.com/kubernetes-sigs/external-dns"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura de provedores via Webhook (PR 3063) e fim de novos provedores in-tree

## Em uma frase
A seção New providers do README estabelece uma diretriz arquitetural importante: nenhum novo provedor será adicionado ao código principal (in-tree) do ExternalDNS; em vez disso, o projeto introduziu um sistema de webhooks (discutido no PR #3063) para adicionar novos provedores como processos externos, alertando expressamente que os mantenedores do ExternalDNS não revisaram esses provedores externos e não assumem responsabilidade por seu uso.

## Por que importa
Congelar a entrada de novos provedores in-tree evita que o binário central acumule dezenas de SDKs de nuvens específicas e ciclos de release acoplados, permitindo que qualquer provedor DNS mantenha seu próprio adaptador webhook desacoplado.

## Como funciona
Para provedores DNS modernos mantidos fora da árvore principal, implante o contêiner do provedor webhook correspondente como sidecar do ExternalDNS após auditar o código, a licença e a manutenção do repositório externo.

## Exemplo
Uma organização utiliza um provedor DNS regional que não está in-tree acoplando o adaptador webhook ao pod do ExternalDNS após revisão interna de segurança do código do webhook.

## Limites e trade-offs
Como os mantenedores do ExternalDNS declaram expressamente não revisar os repositórios de webhooks de terceiros, aplique análise de vulnerabilidades e revisão de código antes de dar credenciais da sua zona DNS a um webhook externo.

## Como verificar
Conferi a seção New providers no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-external-ips-bare-metal-nat-metallb]] — Veja também: Precedência da lista externalIPs em clusters bare-metal atrás de NAT ou com MetalLB.
- [[externaldns-verification-with-dig-and-faq-namespaces]] — Veja também: Verificação prática de resolução com dig +short e escopo de namespaces no FAQ.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/external-dns) — Repositório oficial do ExternalDNS em kubernetes-sigs com código-fonte, docs/faq.md e docs/contributing/dev-guide.md.; consultado em 2026-10-03.
