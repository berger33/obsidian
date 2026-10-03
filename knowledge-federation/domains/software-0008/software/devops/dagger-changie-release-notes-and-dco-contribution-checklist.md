---
id: software.devops.tranche06.000570
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

# Governança de releases com Changie, geração de código (dagger generate) e DCO no Dagger

## Em uma frase
A seção *4. Prepare your pull request* de `CONTRIBUTING.md` documenta o checklist obrigatório de engenharia e governança do projeto Dagger antes de submeter qualquer mudança: (1) gerar documentação da API, bindings de clientes e demais arquivos gerados com **`dagger generate`** e incluí-los no commit; (2) executar todos os linters com **`dagger check *:lint`**; (3) se a mudança for visível ao usuário (*user-facing*), instalar e executar a ferramenta **[Changie](https://changie.dev/guide/installation/)** (**`changie new`**) para gerar o fragmento estruturado de nota de release e adicioná-lo ao commit; e (4) assinar todos os commits sob a licença **Apache-2.0** com o **Developer Certificate of Origin (DCO)** via **`git commit -s`** (onde a linha `Signed-off-by` deve corresponder ao nome real do autor).

## Por que importa
Manter um único arquivo `CHANGELOG.md` editado manualmente em centenas de pull requests simultâneos gera conflitos constantes de merge no Git; o uso do **Changie** (`changie new`) cria pequenos arquivos estruturados independentes por PR que são consolidados automaticamente no momento da release.

## Como funciona
Ao contribuir para o repositório `dagger/dagger` (ou ao adotar o mesmo padrão nos seus próprios repositórios de plataforma), execute `dagger generate`, `dagger check *:lint`, `changie new` e `git commit -s` antes de abrir o pull request.

## Exemplo
Um engenheiro adiciona uma nova opção ao CLI do Dagger, roda `dagger generate`, valida o código com `dagger check *:lint`, registra a nota de versão com `changie new` e faz `git commit -s`, passando em todos os gates automatizados do PR na primeira tentativa.

## Limites e trade-offs
Se houver conflitos com a branch `main` durante a revisão do PR, o `CONTRIBUTING.md` orienta realizar `git rebase` da sua branch sobre a `main` mais recente em vez de commits de merge desordenados.

## Como verificar
Verifique com `git status` e `git log -1` que nenhum arquivo gerado por `dagger generate` ficou fora do commit, que o fragmento do Changie foi incluído e que o rodapé `Signed-off-by:` está presente.

## Conexões
- [[dagger-reusable-module-ecosystem-and-cross-language-sharing]] — Veja também: Ecossistema de módulos reutilizáveis do Dagger e composição entre diferentes linguagens.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
