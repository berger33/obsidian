---
id: software.devops.tranche06.000568
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

# Exploração interativa do grafo de contêineres e módulos com o REPL (dagger shell)

## Em uma frase
O README oficial destaca entre os recursos centrais do pilar **Programmable** a presença de um **REPL interativo (interactive REPL / `dagger shell`)**. Em vez de editar código, salvar e rodar um script repetidas vezes para descobrir quais funções um módulo oferece ou qual o conteúdo de um diretório dentro de um contêiner intermediário, o desenvolvedor pode abrir o shell interativo do Dagger, encadear chamadas à System API ou a módulos da comunidade com autocompletar, inspecionar arquivos gerados e até abrir um terminal interativo dentro de qualquer contêiner intermediário do pipeline para depuração imediata.

## Por que importa
Quando uma etapa de compilação falha dentro de um contêiner em um pipeline tradicional, reproduzir exatamente o estado daquele contêiner no instante da falha é trabalhoso. Com o shell interativo e depuração de contêineres do Dagger, você inspeciona o sistema de arquivos exato da etapa em segundos.

## Como funciona
Use o modo interativo do Dagger (`dagger shell`) para prototipar novos pipelines, explorar módulos externos antes de importá-los no código do seu SDK e inspecionar artefatos intermediários durante a depuração de falhas de build.

## Exemplo
Para testar como um módulo comunitário de lint funciona sobre seu repositório sem escrever código ainda, o engenheiro abre o shell interativo do Dagger, encadeia a chamada passando o diretório atual `.` e inspeciona o resultado diretamente no terminal.

## Limites e trade-offs
Uma vez validado o fluxo interativamente no REPL, codifique a sequência no módulo versionado do seu repositório (em Go, Python, TypeScript, etc.) para que fique coberta por revisão de código e controle de versão.

## Como verificar
Inicie uma sessão no CLI do Dagger para inspecionar as funções disponíveis de um módulo (`dagger functions`) e valide a assinatura de entrada e saída de cada função.

## Conexões
- [[dagger-dagger-in-dagger-playground-and-self-hosted-ci]] — Veja também: Desenvolvimento Dogfooding ("Dagger-in-Dagger") com dagger shell playground e dagger check.
- [[dagger-reusable-module-ecosystem-and-cross-language-sharing]] — Veja também: Ecossistema de módulos reutilizáveis do Dagger e composição entre diferentes linguagens.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
