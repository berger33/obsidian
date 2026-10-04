---
id: software.criacao_ia.tranche03.000281
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-token-metrics.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI: interpretar gen_ai.provider.name pela perspectiva da instrumentation

## Em uma frase
`gen_ai.provider.name` identifica o provider reconhecido pela instrumentation, não necessariamente o fabricante do modelo que está por trás de um proxy.

## Por que importa
Agregações multi-provider dependem de um discriminador coerente entre traces, métricas e eventos. Se uma aplicação envia requests por uma camada compatível com API OpenAI, mas a instrumentation reconhece um serviço Bedrock, atribuir nomes por formato HTTP em vez de provider pode misturar convenções incompatíveis.

## Como funciona
A semconv recomenda escolher o valor com o melhor conhecimento disponível para a instrumentation; ele pode divergir do provider upstream real quando existe proxy ou hosting transparente. Trate o valor como discriminador da família de convenções específicas do provider e mantenha-o consistente com atributos específicos como `aws.bedrock.*`; não misture automaticamente atributos de providers distintos.

## Exemplo
Para uma integração instrumentada diretamente como AWS Bedrock, registre `gen_ai.provider.name=aws.bedrock` junto dos atributos Bedrock correspondentes. Se a aplicação só observa um proxy OpenAI-compatible e não sabe o backend, não invente o upstream: use o provider conhecido pela biblioteca e documente a fronteira de observação.

## Limites e trade-offs
Esse atributo não prova a localização física do modelo nem identifica sozinho a rota real do tráfego. Valores customizados podem ser necessários e devem ser acordados entre instrumentações antes de dashboards dependerem deles.

## Como verificar
Inspecione spans, métricas e eventos de cada provider; valide o mesmo discriminador nos sinais relacionados e procure combinações cruzadas indevidas como `aws.bedrock.*` sob `openai`.

## Conexões
- [[otel-genai-operation-name-taxonomia]] — OpenTelemetry GenAI: padronizar gen_ai.operation.name sem apagar a operação real.

## Fontes
- [OpenTelemetry GenAI — Model spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md) — define provider.name como discriminador e admite diferença em relação ao upstream por proxy Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Inference token metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-token-metrics.md) — reaplica provider.name nas métricas e descreve consistência entre atributos e sinais Consulta: 2026-10-04.
