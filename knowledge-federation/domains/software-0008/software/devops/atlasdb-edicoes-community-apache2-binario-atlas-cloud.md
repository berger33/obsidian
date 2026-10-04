---
id: software.devops.tranche08.000770
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/getting-started", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: arquitetura de edições do Atlas (código base Apache-2.0, binário oficial e recursos avançados)

## Em uma frase
O repositório `ariga/atlas` publica o código-fonte do núcleo do motor de esquemas sob licença Apache-2.0 (`cmd/atlas-community`), enquanto o binário oficial distribuído pela Ariga (`atlasgo.sh`, Homebrew, Docker `arigaio/atlas`) inclui recursos gratuitos adicionais e integrações opcionais com o Atlas Cloud/Pro.

## Por que importa
Engenheiros de plataforma que compilam ferramentas a partir do código-fonte ou auditam dependências precisam entender a diferença entre compilar o binário comunitário do repositório Git (`cmd/atlas-community`) e instalar a distribuição oficial binária do Atlas. O README do repositório `ariga/atlas` explica como ambas as distribuições funcionam.

## Como funciona
O repositório aberto no GitHub (`github.com/ariga/atlas`) contém a biblioteca Go de inspeção, diff, parser HCL/SQL e o ponto de entrada comunitário sob licença **Apache-2.0**. Os binários oficiais distribuídos em `https://atlasgo.sh`, Homebrew (`ariga/tap/atlas`), Docker (`arigaio/atlas`) e npm (`@ariga/atlas`) fornecem a CLI completa pronta para uso (incluindo analisadores de lint, suporte ampliado a dialetos e objetos avançados como views, functions, triggers e RLS, além de integração com `atlas login` para recursos de equipe e registro de esquemas).

## Exemplo
```bash
# Executar o Atlas via container Docker oficial arigaio/atlas inspecionando um banco na rede do host
docker run --rm arigaio/atlas:latest \
  schema inspect -u "postgres://postgres:pass@host.docker.internal:5432/appdb?sslmode=disable"
```

## Limites e trade-offs
Alguns objetos de banco de dados avançados (como `views`, `materialized views`, `functions`, `procedures`, `triggers`, `sequences` e `Security-as-Code` / `schema test`) e conectores corporativos (como Snowflake, Redshift e Spanner) requerem o binário oficial com conta autenticada (`atlas login`) ou licença Atlas Pro, não estando presentes se você compilar apenas o binário mínimo `cmd/atlas-community` sem os módulos estendidos.

## Como verificar
Execute `atlas version` para verificar a edição do binário instalado (`community` vs build oficial da Ariga) e consulte a matriz de funcionalidades em `atlasgo.io`.

## Conexões
- [[atlasdb-integracao-cloud-native-terraform-kubernetes-operator-cicd]] — Veja também: Ariga Atlas: integrações cloud-native com Terraform Provider, Kubernetes Operator e GitHub Actions/GitLab CI.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd]] — Referência cruzada direta com atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd.
- [[flyway-edicoes-community-apache2-teams-enterprise-redgate]] — Referência cruzada direta com flyway-edicoes-community-apache2-teams-enterprise-redgate.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
