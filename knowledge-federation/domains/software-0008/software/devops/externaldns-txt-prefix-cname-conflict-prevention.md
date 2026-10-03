---
id: software.devops.tranche03.000217
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

# Uso obrigatório de --txt-prefix com registros CNAME e risco de perda de propriedade

## Em uma frase
A seção Note do README adverte que, ao utilizar o registro de propriedade TXT (txt registry) e tentar criar um registro CNAME, a flag --txt-prefix deve ser definida para evitar conflitos de protocolo DNS, e alerta que alterar o valor de --txt-prefix posteriormente resultará em perda de propriedade (lost ownership) sobre os registros criados anteriormente.

## Por que importa
Pelo padrão do protocolo DNS (RFCs de CNAME), um nome que possui um registro CNAME não pode coexistir com outros tipos de registro (como um TXT de mesmo nome) no mesmo nó da zona; definir --txt-prefix grava o TXT em um nome prefixado separado, resolvendo o conflito.

## Como funciona
Defina --txt-prefix desde a implantação inicial do ExternalDNS sempre que sua arquitetura criar registros CNAME (como ao apontar para hostnames de balanceadores AWS ELB/ALB) e nunca altere esse prefixo sem um plano de migração da zona.

## Exemplo
Ao configurar o ExternalDNS para criar CNAMEs de Ingresses na AWS, a equipe define um --txt-prefix fixo no manifesto do controlador para que os registros TXT de propriedade não colidam com os CNAMEs.

## Limites e trade-offs
Se --txt-prefix for alterado em produção, o ExternalDNS deixará de reconhecer os registros antigos como seus e não conseguirá atualizá-los até que os registros TXT sejam migrados.

## Como verificar
Conferi o primeiro parágrafo da seção Note no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-policy-sync-versus-upsert-only]] — Veja também: Políticas de ciclo de vida de registros: --policy=sync versus --policy=upsert-only.
- [[externaldns-external-ips-bare-metal-nat-metallb]] — Veja também: Precedência da lista externalIPs em clusters bare-metal atrás de NAT ou com MetalLB.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
