---
id: software.devops.tranche01.000090
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://github.com/jaegertracing/jaeger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Governança aberta (`GOVERNANCE.md`, `MAINTAINERS.md`), reuniões de status e canais `#jaeger` e `jaeger-tracing`

## Em uma frase
As seções Get Involved, Contributing, Maintainers, Project Status Meetings, Roadmap e Get in Touch do README oficial documentam como interagir com o projeto: as regras para se tornar mantenedor estão em `GOVERNANCE.md`, a lista oficial fica em `MAINTAINERS.md` (usando a menção `@jaegertracing/jaeger-maintainers` em issues/PRs), ideias de contribuição (muitas sem exigir código) estão em `jaegertracing.io/get-involved/`, o roadmap fica em `jaegertracing.io/docs/roadmap/` e o contato ocorre pela sala `#jaeger` no Slack da CNCF, pelo grupo de e-mail `jaeger-tracing`, pelo GitHub Issues/Discussions e pelas reuniões regulares por vídeo (`jaegertracing.io/get-in-touch/`).

## Por que importa
Saber que existe um handle de equipe padronizado (`@jaegertracing/jaeger-maintainers`) para acionar mantenedores em PRs e que contribuições não se limitam a código (incluindo documentação em `jaegertracing/documentation` e casos de uso em `ADOPTERS.md`) reduz a barreira de entrada para usuários corporativos participarem da evolução da ferramenta.

## Como funciona
Use o canal `#jaeger` no Slack da CNCF ou o GitHub Discussions para dúvidas operacionais, participe das Project Status Meetings abertas a usuários finais e marque `@jaegertracing/jaeger-maintainers` quando precisar de revisão dos mantenedores em issues ou pull requests relevantes.

## Exemplo
O README também agradece nominalmente à CNCF, à Uber pela doação inicial e aos patrocinadores de software e infraestrutura (1Password, Codecov.io, Dosu, GitHub, Google Analytics, Netlify e Oracle Cloud Infrastructure).

## Limites e trade-offs
Antes de compilar o projeto a partir do código-fonte ou submeter alterações, leia as instruções de build e estilo em `./CONTRIBUTING.md`.

## Como verificar
Conferi as seções Get Involved até Sponsors no chunk 1 do README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-security-audits-and-mechanisms]] — Veja também: Auditorias de segurança independentes (`jaegertracing/security-audits`) e resumo de mecanismos de segurança.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
