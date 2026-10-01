---
id: software.devops.observabilidade-sinais.000001
tipo: conceito
dominio: software
subdominio: devops
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://opentelemetry.io/docs/concepts/signals/", "https://opentelemetry.io/docs/specs/otel/overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
aliases: [Sinais de observabilidade, Telemetria distribuída]
---

# Sinais de observabilidade em sistemas distribuídos

## Em uma frase
Métricas, traces e logs mostram aspectos diferentes do comportamento de um sistema; IDs de correlação e contexto propagado ajudam a relacionar essas evidências durante uma investigação.

## Por que importa
Uma métrica pode revelar que a latência aumentou, mas não apontar qual dependência atrasou uma requisição. Um trace pode localizar o trecho lento, enquanto logs associados ao trace explicam o evento ou a falha observada. Nenhum sinal, isoladamente, descreve tudo. Uma instrumentação consistente diminui o tempo entre detectar um sintoma e formular uma hipótese testável.

## Como funciona
Em OpenTelemetry, uma métrica é uma medida agregável ao longo do tempo, um trace representa o caminho de uma operação e seus spans, e um log registra um evento. O contexto pode propagar identificadores entre processos, permitindo correlacionar spans e, quando configurado, logs. A biblioteca de instrumentação exporta telemetria para um coletor ou backend; OpenTelemetry padroniza a geração e o transporte, mas não é, por si só, o armazenamento nem a interface de consulta.

## Exemplo
Para uma requisição de checkout, uma métrica mostra aumento no percentil 95 de duração; o trace evidencia que a chamada ao serviço de estoque concentra o atraso; o log daquele span registra um timeout na dependência. A investigação passa de “o checkout está lento” para uma dependência e um tipo de falha reproduzíveis.

## Limites e trade-offs
Instrumentar tudo sem política de amostragem e retenção aumenta custo. Labels de alta cardinalidade, como IDs de usuário em métricas, podem explodir séries temporais. Telemetria também pode carregar dados pessoais ou segredos. Limite atributos, aplique redação e controle acesso conforme o risco.

## Como verificar
Inicie uma operação de teste e confirme que o trace atravessa os serviços esperados, que spans mantêm relação pai-filho e que erros podem ser correlacionados a logs sem expor payloads sensíveis. Compare o volume e a cardinalidade das métricas com limites operacionais e valide amostragem sob pico.

## Conexões
- [[timeouts-retries-backoff-jitter]] — retries precisam ser observáveis para não ocultar degradação.
- [[sli-slo-orcamento-de-erro]] — sinais operacionais podem alimentar indicadores de nível de serviço.
- [[gates-de-qualidade-no-merge]] — instrumentação também requer configuração e revisão confiáveis.

## Fontes
- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/) — definições de traces, metrics, logs e baggage; acesso em 2026-10-01.
- [OpenTelemetry Specification — Overview](https://opentelemetry.io/docs/specs/otel/overview/) — modelo conceitual, spans e propagação de contexto; acesso em 2026-10-01.
