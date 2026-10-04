---
id: software.criacao_ia.tranche04.000399
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://huggingface.co/docs/transformers/generation_strategies", "https://huggingface.co/blog/universal_assisted_generation"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: decodificação assistida — draft por modelo, n-gram, medusa ou ensemble

## Em uma frase
O generate() aceita decodificação assistida: um draft model, prompt-lookup por n-gramas, ou métodos específicos (medusa, eagle) via helpers especializados — com schedules e confiança controlando quantos tokens rascunho o target aceita por passo.

## Por que importa
Decodificação autoregressiva paga o passo por token; assistida propõe k tokens de uma vez e o modelo-alvo verifica. O ganho não é grátis: aceitar a proposta errada é rerunir — os knobs existem para calibrar essa aposta. E cada método tem requisitos de modelo (medusa/eagle têm cabeçalhos próprios), o que faz da escolha uma decisão de stack, não um toggle.

## Como funciona
O bloco documentado: 'assistant_model' (draft; num_assistant_tokens por passo de rascunho, num_assistant_tokens_schedule heurístico|heuristic_transient|constant para ajustar k conforme os acertos, assistant_confidence_threshold para cortar por confiança) e 'prompt_lookup_num_tokens' (+ max_matching_ngram_size, default 2) para o modo sem draft-model (repetir n-gramas do prompt como proposta). Os specialised helpers (generate_medusa/generate_eagle) vêm dos exemplos/rotas específicas que o post de universal assisted generation descreve, incluindo ensemble com weight em (0,1) — o post é a visão de conjunto dos métodos e seus trade-offs.

## Exemplo
Um servidor de extração (respostas que copiam muito do contexto) liga prompt_lookup_num_tokens 3 sem draft model algum: a sobreposição de n-gramas do documento vira o rascunho e o ganho aparece exatamente onde o texto é copycat — o caso que o próprio modo foi desenhado para servir.

## Limites e trade-offs
Assistência é sensível a regime: em saída criativa sem overlap, o draft perde e você paga o custo dele (a heurística de schedule tenta mitigar; o transient congela k após o aquecimento). Draft model tem seu próprio footprint de VRAM — o 'grátis' só existe no prompt-lookup. Medusa/EAGLE exigem pesos treinados para o alvo (um 7B específico, não qualquer), o que os ancora a uma decisão de distribuição de modelo. E assistida + beam search não é combinada pela doc como suporte trivial — os modos de busca e verificação colidem.

## Como verificar
O teste honesto é end-to-end tokens/s no workload real, não no exemplo da doc: assistido vs. vanilla na mesma GPU, mesmo batch. Um harness de 'taxa de aceitação de draft' (o log do caminho assistido expõe métricas por versão) separa 'o modo está errado' de 'o knob está errado'. Para specialised helpers, um smoke test de carregamento dos pesos extras no seu alvo antes de investir no rollout.

## Conexões
- [[hf-cache-implementation-quatro-modos]] — Transformers: cache_implementation escolhe o destino da KV — dynamic, static, offload ou quantizada.
- [[hf-retornos-e-custom-generate]] — Transformers: past_key_values no retorno e generate custom por repositório.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a seção de assisted generation com assistant model, schedules e prompt-lookup Consulta: 2026-10-04.
- [HF blog — Universal assisted generation](https://huggingface.co/blog/universal_assisted_generation) — o post oficial que enquadra draft/n-gram/medusa/eagle e ensemble Consulta: 2026-10-04.
