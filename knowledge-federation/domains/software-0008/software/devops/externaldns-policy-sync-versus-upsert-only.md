---
id: software.devops.tranche03.000216
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

# Políticas de ciclo de vida de registros: --policy=sync versus --policy=upsert-only

## Em uma frase
No final da subseção Setup Steps, o README alerta que a remoção automática de registros DNS quando Services são excluídos exige configurar --policy=sync, enquanto com --policy=upsert-only os registros são apenas criados ou atualizados e nunca são deletados pelo ExternalDNS.

## Por que importa
Em ambientes onde a exclusão acidental de um manifesto Kubernetes nunca deve remover imediatamente o registro DNS em produção, --policy=upsert-only funciona como trava de segurança; já em ambientes dinâmicos de preview ou produção totalmente automatizada, --policy=sync evita o acúmulo de registros órfãos apontando para IPs desativados (dangling DNS).

## Como funciona
Escolha explicitamente entre --policy=upsert-only (quando preferir limpeza manual controlada de registros antigos) e --policy=sync (quando desejar reconciliação completa incluindo deleção ao remover o Service/Ingress).

## Exemplo
Uma plataforma de ambientes efêmeros por pull request usa --policy=sync para limpar automaticamente os subdomínios DNS assim que o namespace de teste é destruído.

## Limites e trade-offs
Manter registros DNS órfãos apontando para IPs públicos liberados na nuvem sob --policy=upsert-only cria risco de subdomain takeover se o IP for realocado a terceiros; audite periodicamente a zona DNS.

## Como verificar
Conferi a lista final de experimentos em Setup Steps no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-internal-hostname-and-publish-internal-services]] — Veja também: Registros DNS apontando para ClusterIP com internal-hostname e --publish-internal-services.
- [[externaldns-txt-prefix-cname-conflict-prevention]] — Veja também: Uso obrigatório de --txt-prefix com registros CNAME e risco de perda de propriedade.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
