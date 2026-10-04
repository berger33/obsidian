---
id: software.devops.tranche05.000422
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

# Gerenciamento de microsserviços, bibliotecas, pipelines e modelos de ML no Backstage Software Catalog

## Em uma frase
O primeiro pilar nativo destacado no README oficial é o **Backstage Software Catalog** (`backstage.io/docs/features/software-catalog/`), projetado para gerenciar todo o patrimônio de software da organização — incluindo **microsserviços, bibliotecas, pipelines de dados, websites e modelos de Machine Learning (ML)** — além de recursos de infraestrutura, APIs, sistemas, domínios e equipes proprietárias. O catálogo funciona ingerindo arquivos de metadados declarativos (tipicamente `catalog-info.yaml`) versionados nos próprios repositórios Git junto ao código-fonte.

## Por que importa
Planilhas manuais de inventário de sistemas ficam desatualizadas na mesma semana em que são criadas. Quando o arquivo descritor da entidade vive no mesmo repositório Git do serviço e é atualizado via pull request pelos próprios desenvolvedores, o catálogo reflete continuamente a topologia real de propriedade (`owner`), ciclo de vida (`lifecycle`) e dependências.

## Como funciona
Padronize a inclusão de um manifesto `catalog-info.yaml` na raiz de todos os repositórios de microsserviços, bibliotecas, pipelines de dados e modelos de ML, configurando provedores de descoberta automática da organização (GitHub, GitLab, Bitbucket) no Software Catalog.

## Exemplo
Quando um alerta de incidente dispara na madrugada para um microsserviço desconhecido, o engenheiro de plantão pesquisa o nome do componente no Backstage Software Catalog e identifica imediatamente a equipe proprietária (`spec.owner`), o canal de suporte, as APIs consumidas e os links operacionais.

## Limites e trade-offs
Evite cadastrar entidades manualmente de forma avulsa sem vínculo com o repositório de código ou sem validar a existência do grupo proprietário (`Group`/`User`) sincronizado do provedor de identidade corporativo, pois componentes "órfãos" destroem a confiabilidade do catálogo.

## Como verificar
Registre um componente de teste no Software Catalog e verifique que a entidade aparece sem erros de processamento, com proprietário (`owner`), tipo (`type`) e estágio de ciclo de vida (`lifecycle`) devidamente resolvidos.

## Conexões
- [[backstage-internal-developer-portal-framework-overview]] — Veja também: Backstage como framework open-source para construção de Internal Developer Portals (IDP).
- [[backstage-software-templates-golden-paths-scaffolding]] — Veja também: Criação padronizada de novos projetos e Golden Paths com Backstage Software Templates.

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
