---
id: software.devops.tranche05.000429
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/backstage/backstage/master/README.md", "https://backstage.io/docs/getting-started", "https://github.com/backstage/backstage"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Processo de RFCs, governança CNCF em backstage/community e encontros mensais

## Em uma frase
As seções *Community* e *Governance* do README oficial detalham como a evolução técnica do Backstage é conduzida na CNCF: propostas arquiteturais seguem o processo público de **RFCs** (`github.com/backstage/backstage/labels/rfc`), a governança formal reside em `GOVERNANCE.md` dentro do repositório `github.com/backstage/community` (que também organiza as **Backstage Community Sessions** mensais), a lista de empresas usuárias é mantida em `ADOPTERS.md` e o roadmap público de entregas fica em `backstage.io/docs/overview/roadmap`.

## Por que importa
Equipes de plataforma que dependem estrategicamente do Backstage precisam acompanhar o roadmap oficial e as RFCs abertas para alinhar suas customizações internas à direção futura do projeto (como evoluções do sistema de backend e plugins) sem criar forks incompatíveis.

## Como funciona
Consulte regularmente o roadmap oficial (`backstage.io/docs/overview/roadmap`) e as issues marcadas com a label `rfc` antes de desenvolver mudanças estruturais profundas na sua instalação do Backstage.

## Exemplo
Antes de escrever um mecanismo próprio de autorização e carregamento dinâmico de plugins, a equipe de plataforma revisa as RFCs e decisões arquiteturais do Backstage e adota a implementação oficial recém-entregue no roadmap do projeto.

## Limites e trade-offs
Ao planejar contribuições upstream ou aguardar revisões de mantenedores, observe avisos sazonais comunicados no README (como períodos de férias de verão em que o tempo de resposta pode ser mais lento) e participe das discussões no Discord oficial e nas Community Sessions.

## Como verificar
Verifique as notas de versão em `github.com/backstage/backstage/releases` e o documento `GOVERNANCE.md` em `backstage/community` ao planejar atualizações periódicas da plataforma.

## Conexões
- [[backstage-api-entities-and-system-domain-modeling]] — Veja também: Modelagem de APIs (OpenAPI, AsyncAPI, gRPC, GraphQL), Sistemas e Domínios no Backstage.
- [[backstage-security-release-process-and-hackerone-reporting]] — Veja também: Processo de releases de segurança (SECURITY.md) e reporte privado de vulnerabilidades no Backstage.

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
