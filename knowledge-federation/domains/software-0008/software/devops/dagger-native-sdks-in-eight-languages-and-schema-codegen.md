---
id: software.devops.tranche06.000563
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

# SDKs nativos gerados a partir do schema para 8 linguagens (Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust)

## Em uma frase
O README oficial destaca que o Dagger disponibiliza **SDKs nativos para 8 linguagens de programação**: **Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust**. Cada SDK é gerado automaticamente a partir do schema da API do Dagger (`dagger generate`), garantindo código idiomático na linguagem escolhida com total segurança de tipos (*type safety*), preenchimento automático (*autocompletion*) na IDE e interoperabilidade total entre módulos escritos em linguagens diferentes.

## Por que importa
Forçar uma equipe de engenharia que trabalha 100% em Python, TypeScript ou Rust a escrever sua automação de CI/CD em Groovy (Jenkins) ou Bash desestimula a manutenção e os testes do pipeline. Com os 8 SDKs nativos do Dagger, a equipe escreve o pipeline de entrega na mesma linguagem e IDE da própria aplicação.

## Como funciona
Escolha o SDK do Dagger correspondente à linguagem principal da sua equipe (por exemplo, Python para equipes de IA/dados, TypeScript para equipes web/Node.js, Go ou Rust para equipes de infraestrutura) mantendo a capacidade de consumir módulos da comunidade escritos em qualquer uma das 8 linguagens.

## Exemplo
Uma equipe de backend Java escreve seu pipeline de build e testes de integração usando o SDK Java do Dagger com validação de tipos em tempo de compilação na IDE, enquanto reutiliza um módulo comunitário de publicação OCI escrito em Go.

## Limites e trade-offs
Conforme documenta o `CONTRIBUTING.md`, ao desenvolver alterações na API ou bindings de SDKs do próprio Dagger, execute sempre **`dagger generate`** para atualizar a documentação da API, os client bindings e os arquivos gerados antes de criar o commit.

## Como verificar
Inicialize um módulo de teste no SDK da sua linguagem preferida e verifique que a IDE reconhece os tipos gerados da API do Dagger sem erros de compilação.

## Conexões
- [[dagger-system-api-and-typed-content-addressed-artifacts]] — Veja também: A System API multi-linguagem do Dagger e artefatos tipados endereçados por conteúdo.
- [[dagger-incremental-execution-and-content-addressed-caching]] — Veja também: Execução incremental por padrão e cache endereçado por conteúdo no Dagger.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
