---
id: software.devops.tranche03.000212
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

# Isolamento seguro de zonas não vazias com --domain-filter e --txt-owner-id

## Em uma frase
A seção Running ExternalDNS do README explica que o controlador mantém zonas selecionadas (por meio da flag --domain-filter) sincronizadas com recursos do cluster e que, por padrão, tem consciência apenas dos registros que ele próprio gerencia — podendo administrar com segurança zonas hospedadas não vazias —, recomendando fortemente definir --txt-owner-id com um valor único que não mude durante todo o ciclo de vida do cluster.

## Por que importa
Em zonas DNS corporativas compartilhadas entre múltiplos clusters Kubernetes e registros criados manualmente, o registro TXT paralelo contendo o valor de --txt-owner-id é o que impede um cluster de sobrescrever ou apagar registros pertencentes a outro cluster ou a sistemas legados.

## Como funciona
Defina sempre --domain-filter para restringir as zonas autorizadas e atribua um --txt-owner-id exclusivo e imutável para cada cluster Kubernetes que opera sobre a mesma zona DNS.

## Exemplo
Dois clusters (staging e prod) compartilham o domínio example.org; como cada instância do ExternalDNS possui seu próprio --txt-owner-id gravado nos registros TXT de propriedade, um cluster nunca remove os registros do outro.

## Limites e trade-offs
Alterar o valor de --txt-owner-id em um cluster já em produção fará o ExternalDNS perder o vínculo de propriedade sobre os registros criados anteriormente.

## Como verificar
Conferi a seção Running ExternalDNS e a subseção Setup Steps no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-provider-agnostic-kubernetes-dns-sync]] — Veja também: Sincronização declarativa e agnóstica de recursos Kubernetes com provedores DNS.
- [[externaldns-dry-run-once-and-environment-variables]] — Veja também: Validação prévia com --dry-run e --once e configuração por variáveis EXTERNAL_DNS_*.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
