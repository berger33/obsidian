---
id: software.devops.tranche03.000220
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

# Verificação prática de resolução com dig +short e escopo de namespaces no FAQ

## Em uma frase
No guia Running Locally e na seção What It Does, o README mostra como validar na prática se o registro DNS foi criado e aponta para o IP do balanceador executando dig +short nginx.example.org., além de lembrar que o exemplo local assume o namespace default e remeter ao documento docs/faq.md (e ao guia de contribuição docs/contributing/dev-guide.md) para detalhes sobre filtragem de namespaces e compilação a partir do fonte.

## Por que importa
Confiar apenas na ausência de erros no log do controlador sem testar a resolução DNS real com dig e sem verificar quais namespaces o ExternalDNS está observando pode mascarar problemas de delegação de zona ou RBAC.

## Como funciona
Após implantar ou alterar anotações no ExternalDNS, valide a propagação com dig +short <hostname> e consulte docs/faq.md para configurar corretamente o escopo de namespaces monitorados no cluster.

## Exemplo
O engenheiro executa dig +short nginx.example.org. no terminal de verificação pós-deploy e confirma que o IP retornado coincide com o EXTERNAL-IP do Service no Kubernetes.

## Limites e trade-offs
Respostas em cache de resolvedores DNS locais podem atrasar a visualização de mudanças recentes; consulte diretamente o nameserver autoritativo com dig @<ns> +short durante o diagnóstico.

## Como verificar
Conferi as seções What It Does e Setup Steps no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-webhook-provider-architecture-pr3063]] — Veja também: Arquitetura de provedores via Webhook (PR 3063) e fim de novos provedores in-tree.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/external-dns) — Repositório oficial do ExternalDNS em kubernetes-sigs com código-fonte, docs/faq.md e docs/contributing/dev-guide.md.; consultado em 2026-10-03.
