---
id: software.criacao_ia.tranche03.000290
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/README.md", "https://opentelemetry.io/docs/specs/otel/document-status/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI semconv: interpretar o status Development antes de fixar integração

## Em uma frase
O repositório atual declara as convenções GenAI consultadas como `Development`, por isso nomes e comportamentos não devem ser tratados como contratos estáveis sem revisão de versão.

## Por que importa
Instrumentações e exporters podem implementar subconjuntos diferentes enquanto o esquema evolui; misturar um dashboard novo com SDK antigo pode produzir campos ausentes ou semânticas divergentes. A página antiga de GenAI no site principal também informa que o conteúdo foi movido e não é mantido naquele repositório.

## Como funciona
Use `open-telemetry/semantic-conventions-genai` como fonte ativa, anote o commit ou release que orienta a integração e teste o sinal realmente emitido por cada SDK. Antes de atualizar, compare nomes de atributos, requirement levels e schemas de eventos; status é declarado por documento individual, não por toda a especificação nem por cada implementação.

## Exemplo
Uma atualização do dashboard adota `gen_ai.client.inference.usage.*` a partir de uma revisão registrada. O pipeline valida cardinalidade e payload de uma chamada real em staging; só depois migra queries e retenção, preservando alias temporário se SDKs em produção ainda emitem nomes anteriores.

## Limites e trade-offs
Fixar um commit melhora reprodutibilidade, mas não garante que SDKs implementem aquela revisão ou todos os recursos. Maturidade `Development` na orientação OpenTelemetry significa que peças e opções podem mudar; não inferir estabilidade só porque o código do signal parece definitivo.

## Como verificar
Inclua revisão esperada em documentação e fixtures de telemetry, compare SDKs e exportadores e revise mudanças upstream antes de atualizar. Confirme o status no arquivo específico e a disponibilidade na compliance matrix para a linguagem usada.

## Conexões
- [[otel-genai-evaluation-result-correlacao]] — OpenTelemetry GenAI evaluation.result: correlacionar resultado ao output avaliado.

## Fontes
- [OpenTelemetry GenAI — índice de semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/README.md) — identifica o repositório atual, sinais cobertos e status Development Consulta: 2026-10-04.
- [OpenTelemetry — Definitions of Document Statuses](https://opentelemetry.io/docs/specs/otel/document-status/) — explica que o status se aplica ao documento individual, não à especificação inteira Consulta: 2026-10-04.
