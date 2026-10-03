---
id: software.devops.tranche06.000567
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

# Desenvolvimento Dogfooding ("Dagger-in-Dagger") com dagger shell playground e dagger check

## Em uma frase
O guia oficial `CONTRIBUTING.md` revela como a própria equipe do Dagger desenvolve e testa o Dagger usando o próprio Dagger (*"To develop Dagger, we use - surprise! - Dagger"*): ao executar **`dagger shell playground`**, o ambiente (1) compila o Dagger Engine com os SDKs core embutidos; (2) inicia o engine de desenvolvimento como um serviço Dagger (**dagger-in-dagger**); (3) compila o Dagger CLI; (4) sobe um contêiner efêmero com o CLI instalado e o engine disponível como sidecar; e (5) abre um terminal interativo pronto para uso. Além disso, todos os linters e testes de integração do repositório são executados via **`dagger check *:lint`**, **`dagger check test-split:*`** e **`dagger check *sdk:*test*`**.

## Por que importa
O fato de um projeto complexo com motor de execução em contêineres e 8 SDKs de linguagens diferentes compilar, fazer lint, testar todos os SDKs e subir seu próprio servidor de documentação (`dagger api call docs server up`) inteiramente através de comandos `dagger check` e `dagger api call` comprova na prática a maturidade do modelo de CI programável.

## Como funciona
Adote a convenção de comandos padronizados de verificação nos seus próprios módulos Dagger (permitindo rodar linters e testes com `dagger check` ou chamadas diretas de função) para que qualquer desenvolvedor ou pipeline de CI execute toda a validação do projeto de forma uniforme.

## Exemplo
Um contribuidor que está adicionando um recurso ao motor do Dagger executa `dagger shell playground` para testar interativamente o novo CLI contra o engine em contêiner e, antes de abrir o PR, roda `dagger check *:lint` e `dagger api call engine-dev test --pkg="./core/integration" --run="^TestModule/TestNamespacing$"`.

## Limites e trade-offs
Como o `dagger shell playground` executa contêineres dentro de contêineres (*dagger-in-dagger*) e compila os SDKs core, reserve espaço em disco e memória adequados para o cache do BuildKit/Dagger Engine na máquina de desenvolvimento.

## Como verificar
Execute os comandos de verificação e lint de um módulo Dagger e confirme que todos os checks passam em contêineres isolados.

## Conexões
- [[dagger-composable-workflows-services-and-network-tunnels]] — Veja também: Orquestração de serviços efêmeros (bancos de dados, APIs) e túneis de rede em funções em sandbox no Dagger.
- [[dagger-interactive-repl-and-dagger-shell-exploration]] — Veja também: Exploração interativa do grafo de contêineres e módulos com o REPL (dagger shell).

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
