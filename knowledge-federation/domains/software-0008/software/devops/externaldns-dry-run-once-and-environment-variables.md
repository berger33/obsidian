---
id: software.devops.tranche03.000213
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

# Validação prévia com --dry-run e --once e configuração por variáveis EXTERNAL_DNS_*

## Em uma frase
Na seção Running ExternalDNS e no guia Running Locally, o README orienta executar o ExternalDNS em modo de simulação (--dry-run) e em um único ciclo de sincronização (--once) para inspecionar quais alterações seriam submetidas à API do provedor DNS antes de ativar o loop contínuo, destacando também que todas as flags de linha de comando podem ser substituídas por variáveis de ambiente (por exemplo, --dry-run pode ser substituído por EXTERNAL_DNS_DRY_RUN=1).

## Por que importa
Testar uma nova configuração de filtro ou provedor diretamente em modo de escrita contínua contra uma zona DNS de produção pode criar ou remover dezenas de registros indevidamente; rodar antes com --once --dry-run mostra exatamente o plano de mudanças sem tocar no provedor.

## Como funciona
Antes de promover mudanças de flags no Deployment do ExternalDNS, execute um ciclo com --dry-run (ou EXTERNAL_DNS_DRY_RUN=1) e verifique os registros que seriam criados, atualizados ou removidos nos logs.

## Exemplo
Um engenheiro valida localmente a configuração com external-dns --txt-owner-id my-cluster-id --provider google --google-project example-project --source service --once --dry-run antes de implantar o controlador no cluster.

## Limites e trade-offs
Lembre-se de desativar o modo --dry-run e remover --once quando passar para o Deployment definitivo do loop de controle no cluster.

## Como verificar
Conferi a seção Running ExternalDNS e o bloco Running Locally no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-domain-filter-and-txt-owner-id-safety]] — Veja também: Isolamento seguro de zonas não vazias com --domain-filter e --txt-owner-id.
- [[externaldns-hostname-and-ttl-service-annotations]] — Veja também: Anotações external-dns.kubernetes.io/hostname e external-dns.kubernetes.io/ttl em Services.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
