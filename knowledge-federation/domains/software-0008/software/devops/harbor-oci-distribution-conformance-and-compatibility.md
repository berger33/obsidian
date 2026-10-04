---
id: software.devops.tranche02.000149
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

# Testes de conformidade OCI Distribution e matriz de compatibilidade de adaptadores

## Em uma frase
As seções `OCI Distribution Conformance Tests` e `Compatibility` do README fornecem o link para o relatório público de testes de conformidade OCI Distribution do Harbor (`storage.googleapis.com/harbor-conformance-test/report.html`) e para a lista de compatibilidade de componentes (`goharbor.io/docs/edge/install-config/harbor-compatibility-list/`), que detalha `Replication adapters`, `OIDC adapters` e `Scanner adapters`.

## Por que importa
A conformidade com a especificação OCI Distribution garante que clientes padrão do ecossistema — como `containerd`, `helm`, `cosign`, `skaffold` e controladores GitOps — interajam com o Harbor sem extensões proprietárias incompatíveis.

## Como funciona
Consulte o relatório de conformidade OCI e a matriz de compatibilidade de adaptadores de replicação, OIDC e scanner ao integrar o Harbor com outros registros de nuvem ou ferramentas de segurança.

## Exemplo
Antes de configurar replicação bidirecional entre o Harbor on-premises e um registro de nuvem pública, o arquiteto confere a seção `Replication adapters` na lista de compatibilidade oficial.

## Limites e trade-offs
Ao atualizar o Harbor, verifique se o adaptador externo de scanner de vulnerabilidades utilizado pela equipe permanece suportado na nova versão.

## Como verificar
Conferi as seções OCI Distribution Conformance Tests e Compatibility no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-cosign-release-signature-verification]] — Veja também: Verificação criptográfica de instaladores do Harbor com Cosign a partir da v2.15.0.
- [[harbor-architecture-overview-and-community-calls]] — Veja também: Visão arquitetural na wiki oficial e reuniões comunitárias quinzenais em dois fusos.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
