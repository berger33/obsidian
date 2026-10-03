---
id: software.devops.tranche06.000562
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

# A System API multi-linguagem do Dagger e artefatos tipados endereçados por conteúdo

## Em uma frase
A seção *Features* do README oficial descreve a arquitetura central do motor do Dagger: a **System API** — uma API cross-language para orquestrar **contêineres, sistemas de arquivos (diretórios e arquivos), segredos, repositórios Git, túneis de rede e serviços**, onde cada operação é fortemente tipada e componível — combinada com **artefatos tipados (Typed artifacts)**. No Dagger, é possível definir tipos de objetos customizados com estado e funções encapsuladas; esses tipos são **endereçados por conteúdo (content-addressed)** e podem ser passados através de fronteiras de linguagem de SDK e fronteiras de módulos sem necessidade de serialização manual.

## Por que importa
Em scripts tradicionais de CI, passar o resultado de uma ferramenta em Python para outra ferramenta em Go exige gravar arquivos soltos em diretórios temporários no host e torcer para que variáveis de ambiente ou permissões não quebrem. No Dagger, uma função retorna um objeto tipado `Directory`, `File`, `Container` ou `Service` endereçado por hash criptográfico, que outra função escrita em outra linguagem consome diretamente com segurança de tipos.

## Como funciona
Modele seus pipelines recebendo e retornando tipos nativos da System API (`Directory`, `Container`, `Secret`, `Service`) em vez de depender de caminhos globais no sistema de arquivos da máquina host.

## Exemplo
Um módulo de segurança escrito em Go recebe um objeto `Container` produzido por um módulo de build escrito em Python, executa o scanner de vulnerabilidades sobre o contêiner e retorna o relatório sem que os dois módulos precisem combinar caminhos em disco no runner.

## Limites e trade-offs
Nunca passe credenciais sensíveis (tokens de registro, chaves de nuvem ou senhas de banco) como strings simples de variáveis de ambiente nos argumentos das funções; utilize sempre o tipo **`Secret`** nativo da System API do Dagger, que nunca é gravado em texto claro nas camadas de cache nem exposto nos logs/traces.

## Como verificar
Inspecione a assinatura tipada das funções do seu módulo Dagger e verifique que diretórios, contêineres e segredos utilizam os tipos nativos da System API.

## Conexões
- [[dagger-programmable-local-first-repeatable-observable-delivery]] — Veja também: Os quatro pilares do Dagger: entrega de software programável, local-first, repetível e observável.
- [[dagger-native-sdks-in-eight-languages-and-schema-codegen]] — Veja também: SDKs nativos gerados a partir do schema para 8 linguagens (Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust).

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
