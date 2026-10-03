---
id: software.devops.tranche01.000003
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
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte nativo ao protocolo OTLP v1.10.0 e definição de estabilidade do protocolo

## Em uma frase
Na seção Supported OTLP version, o README oficial registra que a base de código atual é construída sobre a versão v1.10.0 do protocolo OTLP (OpenTelemetry Protocol), classificada como Stable segundo a definição oficial de estabilidade no repositório open-telemetry/opentelemetry-proto.

## Por que importa
Saber exatamente contra qual versão da especificação OTLP (v1.10.0 Stable) o Collector é compilado garante interoperabilidade previsível entre SDKs de diferentes linguagens e coletores intermediários na malha de telemetria.

## Como funciona
Padronize o envio de telemetria das aplicações para o Collector usando OTLP e consulte a definição de estabilidade em open-telemetry/opentelemetry-proto ao atualizar SDKs ou coletores em etapas diferentes.

## Exemplo
Quando um serviço instrumentado envia spans, métricas ou logs em OTLP estável, o Collector decodifica a carga de acordo com o contrato v1.10.0 sem precisar de tradutores legados.

## Limites e trade-offs
A estabilidade do protocolo OTLP na camada de transporte é distinta do nível de estabilidade de um receiver, processor ou exporter específico dentro do Collector.

## Como verificar
Conferi a seção Supported OTLP version no README oficial do OpenTelemetry Collector.

## Conexões
- [[otelcol-five-core-objectives]] — Veja também: Os cinco objetivos de projeto: Usable, Performant, Observable, Extensible e Unified.
- [[otelcol-go-minor-version-compatibility-policy]] — Veja também: Política de suporte a versões menores do Go (N e N-1, remoção de N-2) quando usado como biblioteca.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
