---
id: software.devops.tranche01.000002
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
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os cinco objetivos de projeto: Usable, Performant, Observable, Extensible e Unified

## Em uma frase
Logo após a definição inicial, o README oficial enumera os cinco objetivos que guiam o OpenTelemetry Collector: Usable (configuração padrão razoável, suporte a protocolos populares, roda e coleta out of the box), Performant (altamente estável e performático sob cargas e configurações variadas), Observable (um exemplar de serviço observável), Extensible (customizável sem tocar no código core) e Unified (base de código única, implantável como agente ou collector com suporte a traces, métricas e logs).

## Por que importa
Explicitar que a mesma base de código deve servir tanto como agente local quanto como collector gateway para os três sinais (traces, metrics e logs) e ser extensível sem alterar o núcleo evita a fragmentação entre coletores separados por sinal.

## Como funciona
Avalie a topologia de implantação escolhendo se o mesmo binário do Collector rodará como agente próximo à carga de trabalho ou como serviço agregador, monitorando a telemetria interna do próprio Collector (como orientado no objetivo Observable e no link de Monitoring do topo).

## Exemplo
Graças ao objetivo Extensible, equipes podem montar distribuições customizadas com seus próprios componentes sem precisar modificar o repositório core.

## Limites e trade-offs
Embora a base de código seja unificada para traces, métricas e logs, o nível de estabilidade de cada componente individual pode variar conforme o sinal, como detalhado em docs/component-stability.md.

## Como verificar
Conferi a lista Objectives na abertura do README oficial do OpenTelemetry Collector.

## Conexões
- [[otelcol-what-it-is]] — Veja também: OpenTelemetry Collector: implementação agnóstica a fornecedor para receber, processar e exportar telemetria.
- [[otelcol-otlp-protocol-version-stability]] — Veja também: Suporte nativo ao protocolo OTLP v1.10.0 e definição de estabilidade do protocolo.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [OpenTelemetry Collector — Stability Levels and versioning](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md) — Documento oficial docs/component-stability.md com os seis níveis de estabilidade por sinal, regras de depreciação em Beta/Stable (N+2 ou 6 meses) e requisitos de testes em Stable.; consultado em 2026-10-03.
