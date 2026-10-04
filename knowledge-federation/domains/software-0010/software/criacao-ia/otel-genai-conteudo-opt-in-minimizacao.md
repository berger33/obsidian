---
id: software.criacao_ia.tranche03.000288
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/5ca9052bc796ef1e497200b1d558fd87a201f335/docs/gen-ai/gen-ai-events.md", "https://opentelemetry.io/docs/security/handling-sensitive-data/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI: minimizar conteúdo de prompt e resposta na telemetria

## Em uma frase
A captura de mensagens, instruções e detalhes de operações GenAI é opt-in porque pode exportar conteúdo confidencial, não apenas metadados de observabilidade.

## Por que importa
Prompts podem conter dados pessoais, credenciais copiadas, informação de negócio ou conteúdo de ferramentas. Eventos e spans duráveis ampliam o número de sistemas que recebem esse material, e habilitar captura em todas as requisições pode criar risco de privacidade, custo e retenção sem benefício proporcional.

## Como funciona
As convenções marcam `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions` e o evento `gen_ai.client.inference.operation.details` como opt-in; instrumentações podem oferecer filtragem ou truncamento. Habilite somente campos necessários, prefira dados sintéticos em ambientes de teste e aplique minimização, acesso restrito e retenção aos exporters e Collector. Mensagens em eventos devem preservar estrutura conforme o schema definido pela convenção.

## Exemplo
Uma equipe coleta operation.name, provider, model e usage em produção, mas mantém conteúdo desativado. Em um ambiente isolado de depuração, ativa mensagens truncadas por tempo limitado, remove campos sensíveis no Collector e expira traces e eventos após a investigação.

## Limites e trade-offs
Truncar não garante remoção de PII, e redaction posterior não desfaz a cópia inicial para exporter, buffer ou storage. A aplicação continua responsável por revisar conteúdo emitido por bibliotecas de instrumentação e cumprir consentimento e políticas legais aplicáveis.

## Como verificar
Inspecione payloads antes e depois do Collector, teste prompt com identificadores-canário e confirme que nada aparece quando opt-in está desligado. Verifique permissões, logs auxiliares, retenção e configuração de captura em SDKs de cada linguagem.

## Conexões
- [[otel-genai-streaming-latencias-por-chunk]] — OpenTelemetry GenAI streaming: distinguir time to first chunk de cadência.
- [[otel-genai-evaluation-result-correlacao]] — OpenTelemetry GenAI evaluation.result: correlacionar resultado ao output avaliado.

## Fontes
- [OpenTelemetry GenAI — Events, revisão 5ca9052](https://github.com/open-telemetry/semantic-conventions-genai/blob/5ca9052bc796ef1e497200b1d558fd87a201f335/docs/gen-ai/gen-ai-events.md) — define o evento opt-in de detalhes e atributos estruturados de mensagens Consulta: 2026-10-04.
- [OpenTelemetry — Handling sensitive data](https://opentelemetry.io/docs/security/handling-sensitive-data/) — atribui ao implementador minimização, revisão e proteção de dados sensíveis coletados Consulta: 2026-10-04.
