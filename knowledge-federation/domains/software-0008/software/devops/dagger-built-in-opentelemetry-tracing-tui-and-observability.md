---
id: software.devops.tranche06.000565
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

# Observabilidade nativa no Dagger: emissão automática de traces OpenTelemetry, TUI ao vivo e visualização web

## Em uma frase
O pilar **Observable** e a seção *Built-in tracing* do README oficial destacam um diferencial único do Dagger frente a executores tradicionais de CI: **toda operação executada no Dagger emite automaticamente um trace completo OpenTelemetry**, enriquecido por logs granulares e métricas de cada etapa e contêiner. O CLI do Dagger já inclui uma **interface rica de terminal ao vivo (live TUI)** que renderiza a árvore hierárquica de spans e tempos em tempo real no terminal, além de permitir visualizar o trace em uma interface web (Dagger Cloud) ou exportar os spans para **Jaeger, Honeycomb, Grafana Tempo ou qualquer backend compatível com OTLP**.

## Por que importa
Nos sistemas de CI tradicionais, quando um pipeline complexo com etapas paralelas falha, o desenvolvedor precisa procurar o erro em um "muro de texto" (*wall of text logs*) com milhares de linhas misturadas. Com os traces OpenTelemetry nativos do Dagger, você expande exatamente o span que falhou ou que demorou mais tempo e lê apenas os logs daquela operação isolada.

## Como funciona
Utilize a TUI interativa do Dagger no terminal durante o desenvolvimento local para identificar gargalos de tempo nos spans de build/teste e configure variáveis de exportação OpenTelemetry (`OTEL_EXPORTER_OTLP_ENDPOINT`) nos runners de CI para arquivar os traces dos pipelines no seu backend OTel (como o Grafana Tempo).

## Exemplo
Um pipeline de integração começa a levar 4 minutos a mais que o normal; ao inspecionar o trace OpenTelemetry emitido automaticamente pelo Dagger, o engenheiro identifica em segundos qual span específico de download de pacote sofreu degradação de latência.

## Limites e trade-offs
Ao executar o Dagger em ambientes de CI sem terminal interativo TTY, os spans e logs continuam sendo emitidos de forma estruturada e exportados para o coletor OpenTelemetry configurado.

## Como verificar
Execute um comando Dagger no terminal observando a árvore de spans ao vivo na TUI e verifique a duração registrada em cada operação.

## Conexões
- [[dagger-incremental-execution-and-content-addressed-caching]] — Veja também: Execução incremental por padrão e cache endereçado por conteúdo no Dagger.
- [[dagger-composable-workflows-services-and-network-tunnels]] — Veja também: Orquestração de serviços efêmeros (bancos de dados, APIs) e túneis de rede em funções em sandbox no Dagger.

## Fontes
- [Dagger GitHub — README.md (Programmable, Local-First, Repeatable & Observable CI/CD, System API, 8 SDKs & Built-in OTel Tracing)](https://raw.githubusercontent.com/dagger/dagger/main/README.md) — README oficial do Dagger detalhando automação de entrega de software programável (engine, System API, SDKs para 8 linguagens: Go, Python, TypeScript, PHP, Java, .NET, Elixir e Rust, REPL interativo e módulos), local-first, repetível (funções em contêineres isolados, artefatos tipados endereçados por conteúdo e cache incremental) e observável (traces OpenTelemetry nativos na TUI e web).; consultado em 2026-10-03.
- [Dagger GitHub — CONTRIBUTING.md (Dagger-in-Dagger Playground, dagger check, dagger generate, Changie & DCO)](https://raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md) — Guia oficial de engenharia e contribuição do Dagger detalhando como o próprio Dagger usa Dagger para build/test/lint (dagger shell playground, dagger check *:lint, dagger check *sdk:*test*, dagger generate), notas de release com Changie e conformidade Apache-2.0 + DCO Signed-off-by.; consultado em 2026-10-03.
- [Dagger — Official GitHub Repository](https://github.com/dagger/dagger) — Repositório oficial Apache-2.0 do Dagger.; consultado em 2026-10-03.
