---
id: software.devops.tranche02.000150
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
fontes: ["https://raw.githubusercontent.com/goharbor/harbor/main/README.md", "https://github.com/goharbor/harbor"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Visão arquitetural na wiki oficial e reuniões comunitárias quinzenais em dois fusos

## Em uma frase
O topo do README e as seções `Architecture` e `Community` apontam para o documento `Architecture Overview of Harbor` na wiki oficial (`github.com/goharbor/harbor/wiki/Architecture-Overview-of-Harbor`) e informam que o projeto realiza chamadas comunitárias quinzenais (`bi-weekly community calls`) em dois fusos horários diferentes, com agenda e gravações mantidas em `goharbor/community/blob/master/MEETING_SCHEDULE.md`.

## Por que importa
Compreender como os componentes internos do Harbor (portal, core, registry, jobservice, banco de dados e cache) se articulam ajuda a dimensionar armazenamento, banco de dados e réplicas para ambientes de alto tráfego de pulls.

## Como funciona
Estude o documento `Architecture Overview of Harbor` antes de projetar uma instalação de alta disponibilidade e acompanhe o calendário de reuniões em `goharbor/community` para discutir demandas com os mantenedores.

## Exemplo
Um engenheiro de confiabilidade revisa a arquitetura oficial do Harbor para separar o armazenamento de objetos das imagens do banco de dados de metadados.

## Limites e trade-offs
Dimensionar apenas os pods de front-end do Harbor sem escalar o backend de armazenamento de objetos e o banco de dados causará gargalos durante picos simultâneos de pull no cluster.

## Como verificar
Conferi o quadro Community Meeting e a seção Architecture no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-oci-distribution-conformance-and-compatibility]] — Veja também: Testes de conformidade OCI Distribution e matriz de compatibilidade de adaptadores.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor — Repositório Oficial no GitHub](https://github.com/goharbor/harbor) — Repositório oficial do Harbor com código-fonte, api/v2.0/swagger.yaml, docs/signature-verification.md e releases.; consultado em 2026-10-03.
