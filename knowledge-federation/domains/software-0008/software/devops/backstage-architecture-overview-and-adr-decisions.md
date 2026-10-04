---
id: software.devops.tranche05.000426
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

# Arquitetura do Backstage (Frontend, Backend, Proxy e Banco de Dados) e Architecture Decision Records (ADRs)

## Em uma frase
A seção *Documentation* do README oficial aponta diretamente para a visão geral de arquitetura (`backstage.io/docs/overview/architecture-overview`) e para o registro histórico de **Architecture Decision Records — ADRs** (`backstage.io/docs/architecture-decisions/`). A arquitetura padrão do Backstage consiste em uma aplicação frontend Single-Page Application (React/TypeScript), um backend Node.js modular onde rodam os plugins de backend (como o processador do catálogo, o scaffolder e o proxy reverso seguro para APIs externas) e um banco de dados relacional (como PostgreSQL em produção) para armazenar o estado indexado das entidades.

## Por que importa
Compreender como o frontend conversa com os plugins de backend e como o backend armazena e atualiza assincronamente o grafo de entidades no banco de dados é essencial para dimensionar réplicas, configurar segredos de integração e evitar exposição de tokens de terceiros no navegador do usuário.

## Como funciona
Em produção, implante o Backstage com banco de dados **PostgreSQL** gerenciado (nunca o banco SQLite em memória usado apenas para desenvolvimento local), proteja tokens de integração de APIs externas no backend/proxy do Backstage e consulte os ADRs oficiais ao projetar extensões customizadas.

## Exemplo
Para integrar um painel interno que exige token de API privilegiado, a equipe de plataforma configura a rota autenticada no backend/proxy do Backstage em vez de fazer chamadas diretas a partir do navegador React do desenvolvedor.

## Limites e trade-offs
Nunca exponha credenciais administrativas de provedores de nuvem, GitHub Apps ou clusters Kubernetes na configuração de frontend enviada ao navegador; mantenha todos os segredos estritamente na camada de backend do Backstage.

## Como verificar
Verifique nos logs de inicialização do backend do Backstage a conexão bem-sucedida com o banco PostgreSQL e o ciclo de sincronização das entidades do catálogo.

## Conexões
- [[backstage-open-source-plugin-ecosystem-and-extensibility]] — Veja também: Arquitetura extensível de plugins open-source e internos no Backstage.
- [[backstage-design-system-and-storybook-ui-components]] — Veja também: Padronização visual de plugins com Backstage Design System e Storybook.

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
