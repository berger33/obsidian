---
id: software.devops.tranche01.000006
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md", "https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os seis níveis de estabilidade de componentes por sinal: Development a Unmaintained

## Em uma frase
O documento oficial docs/component-stability.md explica que os componentes do Collector encontram-se em diferentes estágios de maturidade — Development, Alpha, Beta, Stable, Deprecated e Unmaintained — e que a estabilidade de um componente capaz de lidar com múltiplos sinais pode depender do sinal em questão, devendo cada componente listar no próprio README seu nível atual para cada sinal de telemetria (traces, metrics, logs).

## Por que importa
Um mesmo exporter ou processor pode já ser Stable para traces e ainda estar em Alpha ou Beta para logs; verificar a matriz por sinal no README do componente evita colocar em produção crítica um caminho de código que ainda não tem garantias de estabilidade de configuração.

## Como funciona
Antes de habilitar um receiver, processor, exporter, connector ou extension em produção, abra o README específico daquele componente e confira o nível de estabilidade declarado especificamente para o sinal que você vai trafegar.

## Exemplo
Um componente em estágio Development ainda não tem todas as peças prontas, pode mudar de configuração com frequência e traz a recomendação explícita de não ser usado em produção, enquanto Alpha é voltado a cargas não críticas limitadas.

## Limites e trade-offs
A classificação de estabilidade é granular por componente e por sinal; o fato de o core do Collector ser estável não implica que todos os componentes de contrib tenham atingido Stable.

## Como verificar
Conferi as seções Stability levels, Development e Alpha em docs/component-stability.md.

## Conexões
- [[otelcol-cosign-image-signature-verification]] — Veja também: Verificação criptográfica de assinaturas das imagens oficiais com Sigstore Cosign.
- [[otelcol-beta-and-stable-configuration-deprecation-rules]] — Veja também: Garantias de configuração em Beta e Stable: depreciação com WARN e prazo N+2 ou 6 meses.

## Fontes
- [OpenTelemetry Collector — Stability Levels and versioning](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md) — Documento oficial docs/component-stability.md com os seis níveis de estabilidade por sinal, regras de depreciação em Beta/Stable (N+2 ou 6 meses) e requisitos de testes em Stable.; consultado em 2026-10-03.
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
