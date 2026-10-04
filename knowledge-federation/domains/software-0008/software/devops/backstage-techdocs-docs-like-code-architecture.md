---
id: software.devops.tranche05.000424
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

# Documentação técnica "docs like code" integrada ao catálogo com Backstage TechDocs

## Em uma frase
O terceiro pilar nativo incluído no Backstage é o **Backstage TechDocs** (`backstage.io/docs/features/techdocs/`), que torna simples criar, manter, encontrar e consumir documentação técnica usando uma abordagem **"docs like code"**. Os engenheiros escrevem a documentação em arquivos Markdown dentro do próprio repositório Git do serviço (tipicamente na pasta `docs/` com um arquivo `mkdocs.yml`), e o TechDocs compila e exibe essas páginas diretamente na aba *Docs* da entidade correspondente no Backstage Software Catalog.

## Por que importa
Wikis corporativas externas separadas do código-fonte rapidamente viram cemitérios de páginas desatualizadas e difíceis de encontrar. Com o TechDocs, atualizar a documentação de arquitetura ou o runbook operacional faz parte do mesmo pull request que altera o código do serviço, e a documentação fica a um clique de distância na página do componente no catálogo.

## Como funciona
Inclua a estrutura básica do TechDocs (`mkdocs.yml` e `docs/index.md`) em todos os Software Templates da empresa e configure o TechDocs para compilar e publicar os artefatos estáticos das documentações em um bucket de armazenamento de objetos (S3, GCS ou Azure) durante o pipeline de CI/CD.

## Exemplo
Durante uma revisão de código que adiciona um novo endpoint gRPC e uma variável de ambiente obrigatória, o revisor exige no mesmo PR a atualização de `docs/runbook.md`; após o merge, o pipeline publica a atualização e o novo procedimento aparece imediatamente no Backstage TechDocs.

## Limites e trade-offs
Para ambientes de produção no Backstage, siga a arquitetura recomendada pela documentação oficial do TechDocs (gerar os sites estáticos nos runners de CI/CD e armazená-los em object storage externo) em vez de deixar o backend do Backstage rodar containers MkDocs sob demanda a cada visualização de usuário.

## Como verificar
Acesse a aba *Docs* de um componente registrado no Backstage e confirme a renderização correta do Markdown e a indexação do conteúdo na busca global do portal.

## Conexões
- [[backstage-software-templates-golden-paths-scaffolding]] — Veja também: Criação padronizada de novos projetos e Golden Paths com Backstage Software Templates.
- [[backstage-open-source-plugin-ecosystem-and-extensibility]] — Veja também: Arquitetura extensível de plugins open-source e internos no Backstage.

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
