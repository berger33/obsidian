---
id: software.devops.tranche05.000425
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

# Arquitetura extensível de plugins open-source e internos no Backstage

## Em uma frase
Além do catálogo, templates e TechDocs, o README oficial destaca o crescente **ecossistema de plugins open-source** (`github.com/backstage/backstage/tree/master/plugins` e diretório comunitário) que expande a customização e as funcionalidades do Backstage. A arquitetura do Backstage é construída como um núcleo enxuto cercado por plugins de frontend e backend que integram ferramentas de Kubernetes, Argo CD, GitHub Actions, Tekton, PagerDuty, Grafana, SonarQube, custos de nuvem e APIs proprietárias da própria empresa.

## Por que importa
Nenhuma empresa usa exatamente a mesma pilha de ferramentas de infraestrutura; a arquitetura baseada em plugins permite que o portal exiba na página de cada microsserviço o status real dos seus pods Kubernetes, o histórico de sincronização no Argo CD e os últimos workflows de CI sem acoplar essas integrações ao core do Backstage.

## Como funciona
Instale apenas os plugins que resolvem dores reais das equipes de engenharia, associando a exibição de cada aba ou card no catálogo a anotações específicas no `catalog-info.yaml` do componente, e desenvolva plugins internos leves quando precisar integrar sistemas legados corporativos.

## Exemplo
Ao adicionar a anotação do Kubernetes e do Argo CD no `catalog-info.yaml` de um serviço, a página daquele serviço no Backstage passa a exibir automaticamente a saúde dos Deployments/Pods em produção e o estado `Synced`/`Healthy` da aplicação GitOps.

## Limites e trade-offs
Evite instalar dezenas de plugins simultaneamente sem curadoria de UX e sem monitorar a compatibilidade de versão durante upgrades do Backstage, pois plugins abandonados ou mal configurados poluem a interface e atrasam atualizações da plataforma.

## Como verificar
Instale ou habilite um plugin na instância de desenvolvimento do Backstage e confirme que o card correspondente renderiza os dados da entidade anotada sem erros no console ou no backend.

## Conexões
- [[backstage-techdocs-docs-like-code-architecture]] — Veja também: Documentação técnica "docs like code" integrada ao catálogo com Backstage TechDocs.
- [[backstage-architecture-overview-and-adr-decisions]] — Veja também: Arquitetura do Backstage (Frontend, Backend, Proxy e Banco de Dados) e Architecture Decision Records (ADRs).

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
