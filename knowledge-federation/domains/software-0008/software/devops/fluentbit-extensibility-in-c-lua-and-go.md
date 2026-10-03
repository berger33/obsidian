---
id: software.devops.tranche02.000177
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md", "https://docs.fluentbit.io/manual/pipeline/inputs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Extensibilidade poliglota: plugins em C, filtros em Lua e outputs em Go

## Em uma frase
Na seção `Key Features`, sob o item **Extensibility**, o README especifica as três linguagens suportadas para estender o Fluent Bit: escrever plugins em **C**, filtros customizados em **Lua** e plugins de output em **Go** (`Write plugins in C, filters in Lua, and outputs in Go`).

## Por que importa
Nem toda regra de negócio ou sistema legado possui um plugin nativo pronto: poder escrever um filtro rápido de transformação em script Lua sem recompilar o agente, um conector de saída em Go aproveitando SDKs modernos ou um plugin nativo em C para performance máxima resolve integrações específicas com agilidade.

## Como funciona
Escolha filtros em **Lua** para lógicas customizadas de enriquecimento e mascaramento de dados em tempo de execução, **Go** para integrar novos destinos que já possuam SDK oficial em Go e **C** para extensões nativas no núcleo do agente.

## Exemplo
Uma equipe escreve um pequeno filtro em Lua para mascarar números de documentos sensíveis nos logs antes que o plugin de Output os envie ao armazenamento externo.

## Limites e trade-offs
Scripts Lua executam para cada registro que passa pelo filtro; mantenha o código Lua enxuto e sem chamadas bloqueantes externas para não degradar a vazão do agente.

## Como verificar
Conferi o item Extensibility (C, Lua e Go) na seção Key Features do README oficial de `fluent/fluent-bit`.

## Conexões
- [[fluentbit-tls-async-io-and-prometheus-self-monitoring]] — Veja também: Rede segura com TLS/SSL, I/O assíncrono e exposição de métricas internas para Prometheus.
- [[fluentbit-cmake-build-requirements-and-cli-quickstart]] — Veja também: Requisitos de compilação (CMake, Flex, Bison, YAML e OpenSSL) e quickstart via CLI.

## Fontes
- [Fluent Bit — GitHub README](https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md) — Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.; consultado em 2026-10-03.
- [Fluent Bit Official Documentation — Pipeline Inputs, Filters & Outputs](https://docs.fluentbit.io/manual/pipeline/inputs) — Documentação oficial dos plugins de Input, Filter e Output e guias de instalação do Fluent Bit.; consultado em 2026-10-03.
