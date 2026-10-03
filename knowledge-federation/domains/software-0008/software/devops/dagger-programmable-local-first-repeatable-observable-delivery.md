---
id: software.devops.tranche06.000561
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/dagger/dagger/main/README.md", "https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md", "https://github.com/dagger/dagger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os quatro pilares do Dagger: entrega de software programável, local-first, repetível e observável

## Em uma frase
O Dagger (`dagger.io` / `docs.dagger.io`), licenciado sob Apache-2.0, é uma plataforma para automatizar a entrega de software (construir, testar e publicar qualquer base de código com confiabilidade e escala) que roda localmente, no servidor de CI ou diretamente na nuvem. Conforme define o README oficial, o Dagger substitui scripts shell frágeis e dezenas de arquivos YAML proprietários de CI por quatro pilares fundamentais: **Programável** (motor completo de execução, System API, SDKs em 8 linguagens, REPL interativo e ecossistema de módulos reutilizáveis), **Local-first** (qualquer tarefa automatizada roda de forma idêntica no laptop, em um sandbox de IA, no servidor de CI ou na nuvem, exigindo apenas um runtime de contêiner como o Docker), **Repetível** (ferramentas rodam em contêineres orquestrados por funções em sandbox com dependências explícitas e cache incremental por padrão) e **Observável** (toda operação emite um trace completo OpenTelemetry).

## Por que importa
O maior gargalo do CI/CD tradicional é o ciclo "commit -> push -> esperar 15 minutos na fila do CI -> descobrir um erro de sintaxe no YAML ou diferença de pacote na máquina do runner". Com o modelo *local-first* e repetível do Dagger, o pipeline roda exatamente dentro dos mesmos contêineres no laptop do desenvolvedor antes mesmo do `git push`.

## Como funciona
Instale o CLI do Dagger (`brew install dagger/tap/dagger` ou script oficial em `dagger.io/install`) e encapsule as etapas de build, lint, teste e empacotamento do projeto em funções Dagger chamadas tanto localmente quanto pelo runner de CI.

## Exemplo
Um desenvolvedor executa a função de validação do Dagger localmente em seu laptop antes de abrir um PR; como todas as ferramentas e dependências rodam dentro de contêineres isolados pelo motor do Dagger, o resultado local é 100% idêntico ao que roda no GitHub Actions ou GitLab CI.

## Limites e trade-offs
Em vez de manter centenas de linhas de YAML específicas do provedor de CI, reduza o YAML do CI a um gatilho mínimo que apenas inicia o runtime de contêiner e invoca a função correspondente do módulo Dagger do repositório.

## Como verificar
Execute `dagger version` e rode uma função de build/teste local com o CLI do Dagger confirmando a execução determinística em contêiner.

## Conexões
- [[dagger-system-api-and-typed-content-addressed-artifacts]] — Veja também: A System API multi-linguagem do Dagger e artefatos tipados endereçados por conteúdo.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
