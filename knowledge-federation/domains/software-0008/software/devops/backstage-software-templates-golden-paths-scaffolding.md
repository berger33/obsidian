---
id: software.devops.tranche05.000423
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

# Criação padronizada de novos projetos e Golden Paths com Backstage Software Templates

## Em uma frase
O segundo pilar nativo documentado no README oficial é o **Backstage Software Templates** (`backstage.io/docs/features/software-templates/`, o motor de *Scaffolder* do Backstage), que permite **criar rapidamente novos projetos e padronizar o ferramental com as melhores práticas da organização**. Por meio de formulários guiados no portal, o desenvolvedor preenche parâmetros (nome do serviço, equipe, banco de dados, linguagem) e o template executa ações automatizadas: renderiza o esqueleto do código, cria o repositório no Git, configura o pipeline de CI/CD, adiciona o `catalog-info.yaml` e registra o novo serviço automaticamente no Software Catalog.

## Por que importa
Quando um desenvolvedor cria um novo microsserviço copiando e colando um repositório antigo qualquer, ele também copia configurações obsoletas de Dockerfile, versões vulneráveis de bibliotecas e pipelines fora do padrão. Os Software Templates materializam **Golden Paths** (caminhos dourados) com segurança, observabilidade e governança já embutidas desde o primeiro commit.

## Como funciona
Construa Software Templates para os tipos de projetos mais frequentes da organização (por exemplo, serviço Go/Java/Node.js, biblioteca compartilhada, pipeline de dados ou módulo Terraform/Terragrunt), já incluindo lint, geração de SBOM (Syft), scan (Grype/Trivy) e manifesto Kubernetes/Helm.

## Exemplo
Um time de produto precisa lançar um novo microsserviço em Go; pelo Backstage Software Templates, o engenheiro preenche 4 campos e em menos de um minuto recebe o repositório Git criado com pipeline GitHub Actions, instrumentação OpenTelemetry, Dockerfile rootless e registro automático no catálogo.

## Limites e trade-offs
Note que o Software Template atua no momento da criação inicial (*scaffolding* / Day 1); para evitar que os repositórios gerados fiquem defasados nos meses seguintes (Day 2), combine os templates com módulos de CI reutilizáveis, imagens base gerenciadas e automação de atualização de dependências.

## Como verificar
Execute um Software Template em ambiente de homologação no modo dry-run ou criando um repositório de teste e confirme a execução limpa de todas as etapas de scaffolding e registro no catálogo.

## Conexões
- [[backstage-software-catalog-metadata-and-ownership]] — Veja também: Gerenciamento de microsserviços, bibliotecas, pipelines e modelos de ML no Backstage Software Catalog.
- [[backstage-techdocs-docs-like-code-architecture]] — Veja também: Documentação técnica "docs like code" integrada ao catálogo com Backstage TechDocs.

## Fontes
- [Backstage GitHub — README.md (Software Catalog, Software Templates, TechDocs, Plugins & Security)](https://raw.githubusercontent.com/backstage/backstage/master/README.md) — README oficial do Backstage (projeto CNCF Incubating criado pelo Spotify sob Apache-2.0) detalhando os três pilares nativos Software Catalog, Software Templates e TechDocs ("docs like code"), ecossistema de plugins, Storybook/Design System e reporte de vulnerabilidades via HackerOne/SECURITY.md.; consultado em 2026-10-03.
- [Backstage Documentation — Getting Started & Architecture Overview](https://backstage.io/docs/getting-started) — Documentação oficial de início rápido e visão geral de arquitetura do Backstage em backstage.io/docs.; consultado em 2026-10-03.
- [Backstage — Official GitHub Repository](https://github.com/backstage/backstage) — Repositório principal Apache-2.0 do Backstage na CNCF.; consultado em 2026-10-03.
