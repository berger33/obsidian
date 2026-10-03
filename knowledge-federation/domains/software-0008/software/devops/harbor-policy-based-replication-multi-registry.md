---
id: software.devops.tranche02.000143
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
fontes: ["https://raw.githubusercontent.com/goharbor/harbor/main/README.md", "https://goharbor.io/docs/latest/install-config/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Replicação baseada em políticas com filtros, retentativa automática e adaptadores

## Em uma frase
Na seção `Features`, o README explica que o recurso **Policy based replication** permite replicar (sincronizar) imagens e charts entre múltiplas instâncias de registro com base em políticas que utilizam filtros (`repository`, `tag` e `label`), realizando retentativas automáticas caso ocorram erros, o que auxilia no balanceamento de carga, alta disponibilidade e implantações multi-datacenter em cenários híbridos e multi-cloud.

## Por que importa
Distribuir imagens automaticamente de um registro central para registros regionais próximos aos clusters Kubernetes reduz a latência de pull durante escalonamentos horizontais e protege a operação contra indisponibilidade de links WAN.

## Como funciona
Configure políticas de replicação no Harbor filtrando apenas os repositórios e tags aprovados para produção e monitore o status das tarefas de sincronização entre datacenters ou nuvens.

## Exemplo
Uma imagem assinada publicada no Harbor central é replicada automaticamente para três instâncias regionais do Harbor que atendem clusters Kubernetes locais.

## Limites e trade-offs
Filtros de replicação excessivamente amplos (sem filtro de tag ou repositório) podem replicar imagens temporárias de branches de desenvolvimento e esgotar o armazenamento dos registros de borda.

## Como verificar
Conferi as seções Features e Compatibility no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-rbac-projects-ldap-and-oidc-identity]] — Veja também: Controle de acesso baseado em papéis (RBAC) por projeto e autenticação LDAP/AD e OIDC.
- [[harbor-vulnerability-scanning-and-deployment-policies]] — Veja também: Scan regular de vulnerabilidades e políticas para impedir o deploy de imagens vulneráveis.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
