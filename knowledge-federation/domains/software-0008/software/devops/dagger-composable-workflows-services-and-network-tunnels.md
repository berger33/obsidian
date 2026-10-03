---
id: software.devops.tranche06.000566
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

# Orquestração de serviços efêmeros (bancos de dados, APIs) e túneis de rede em funções em sandbox no Dagger

## Em uma frase
A descrição da **System API** e do pilar **Repeatable** no README oficial destaca que o Dagger não orquestra apenas comandos isolados de build, mas também **serviços em contêiner (`Service`) e túneis de rede**, com dependências de host explícitas e estritamente tipadas e artefatos intermediários construídos *just-in-time*. Dentro de um workflow Dagger, uma função pode instanciar um banco de dados PostgreSQL, um broker Kafka ou um servidor HTTP da própria aplicação como um `Service` efêmero, vinculá-lo (`withServiceBinding`) ao contêiner executor de testes de integração e encerrar tudo automaticamente assim que os testes terminam.

## Por que importa
Subir bancos de dados e serviços dependentes para testes de integração usando `docker-compose` por fora do script de teste frequentemente sofre com conflitos de portas no host (`port 5432 already in use`), condições de corrida antes do banco ficar pronto e contêineres órfãos esquecidos após falhas. Os serviços gerenciados pelo Dagger iniciam sob demanda em rede isolada com aguardo automático de prontidão e ciclo de vida atrelado ao teste.

## Como funciona
Em seus módulos Dagger de testes de integração e E2E, declare os bancos de dados e microsserviços auxiliares como objetos `Service` vinculados ao contêiner de teste via `withServiceBinding`, sem expor portas fixas na máquina host.

## Exemplo
Para rodar a suíte de testes de integração de uma API, a função Dagger inicia um contêiner `postgres:16` como `Service`, vincula-o com o alias `db` ao contêiner da suíte de testes, aguarda a porta 5432 aceitar conexões, executa os testes e destrói o serviço automaticamente ao final.

## Limites e trade-offs
Quando precisar inspecionar ou acessar interativamente do seu navegador local um serviço que está rodando dentro do sandbox do Dagger, utilize os recursos explícitos de exposição de serviço/túnel de rede do CLI do Dagger.

## Como verificar
Execute uma função Dagger que vincula um contêiner de serviço (`Service`) a um contêiner cliente e confirme nos spans da TUI a inicialização just-in-time e o encerramento limpo do serviço.

## Conexões
- [[dagger-built-in-opentelemetry-tracing-tui-and-observability]] — Veja também: Observabilidade nativa no Dagger: emissão automática de traces OpenTelemetry, TUI ao vivo e visualização web.
- [[dagger-dagger-in-dagger-playground-and-self-hosted-ci]] — Veja também: Desenvolvimento Dogfooding ("Dagger-in-Dagger") com dagger shell playground e dagger check.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
