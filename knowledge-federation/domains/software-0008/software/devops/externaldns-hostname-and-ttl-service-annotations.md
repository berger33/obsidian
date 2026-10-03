---
id: software.devops.tranche03.000214
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

# Anotações external-dns.kubernetes.io/hostname e external-dns.kubernetes.io/ttl em Services

## Em uma frase
Na subseção Setup Steps do README, o fluxo prático demonstra como anotar um Service do Kubernetes com o nome DNS externo desejado usando external-dns.kubernetes.io/hostname=nginx.example.org. e, opcionalmente, customizar o tempo de vida (TTL) do registro DNS resultante por meio da anotação external-dns.kubernetes.io/ttl=10, remetendo ao documento docs/advanced/ttl.md para detalhes avançados de TTL.

## Por que importa
Controlar tanto o FQDN quanto o TTL diretamente nas anotações do Service permite que equipes reduzam o TTL (por exemplo, para 10 ou 60 segundos) antes de uma migração de tráfego ou failover entre clusters sem precisar acessar o console do provedor DNS.

## Como funciona
Adicione a anotação external-dns.kubernetes.io/hostname com o domínio qualificado e ajuste external-dns.kubernetes.io/ttl nos manifestos dos Services expostos conforme a necessidade de velocidade de propagação DNS.

## Exemplo
Antes de recriar um balanceador de carga em uma janela de mudança, a equipe reduz o TTL via anotação external-dns.kubernetes.io/ttl=10 para acelerar a convergência dos clientes para o novo IP.

## Limites e trade-offs
Alguns provedores DNS impõem um valor mínimo de TTL ou usam TTL fixo para registros do tipo Alias; consulte docs/advanced/ttl.md para o comportamento específico do seu provedor.

## Como verificar
Conferi a subseção Setup Steps no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-dry-run-once-and-environment-variables]] — Veja também: Validação prévia com --dry-run e --once e configuração por variáveis EXTERNAL_DNS_*.
- [[externaldns-internal-hostname-and-publish-internal-services]] — Veja também: Registros DNS apontando para ClusterIP com internal-hostname e --publish-internal-services.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
