---
id: software.criacao_ia.tranche04.000397
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
fontes: ["https://huggingface.co/docs/transformers/generation_strategies", "https://huggingface.co/docs/transformers/internal/generation_utils"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: o arsenal anti-repetição — n-gramas, penalidades e viés de tokens

## Em uma frase
A config expõe quatro alavancas para repetição e controle de vocabulário: no_repeat_ngram_size (proíbe n-gramas repetidos), encoder_no_repeat_ngram_size (idem contra o input), repetition_penalty (desvaloriza o que já apareceu) e as listas de supressão/forçamento (suppress_tokens, bad_words_ids, forced_bos_token_id, sequence_bias).

## Por que importa
'Repetir' é a falha número 1 de geração longa, e cada alavanca corrige um mecanismo diferente: loop exato de frase (ngram ban), parafrasear o input (encoder ngram), estilo 'eco' difuso (penalty) e tokens estruturais na resposta (as listas). Tratar as quatro como 'o anti-repeat' e setar tudo junto é o outro modo de quebrar a geração — o no_repeat_ngram_size alto demais bloqueia até conectivos comuns e a frase morre no terceiro 'the'.

## Como funciona
Os campos documentados: no_repeat_ngram_size=4 proíbe repetir 4-gramas (valores típicos 2–8; a página explica o efeito de 'não pode produzir nenhum n-grama repetido'); encoder_no_repeat_ngram_size impede copiar do input (resumo que não vira transcrição); repetition_penalty >1.0 desvaloriza presença anterior (1.0 = nenhum efeito, documentado), com a variante por-frequência (penalty é por vocabulário — a referência cobre os campos de sub/inf/presence); suppress_tokens proíbe tokens inteiros (o default cobre unk etc.), bad_words_ids veda sequências, sequence_bias soma logit a tokens forçados/evitados com pesos.

## Exemplo
O pipeline de resumo executivo: no_repeat_ngram_size=3 + encoder_no_repeat_ngram_size=4 eliminaram o loop e a transcrição do parágrafo 1; no A/B, repetition_penalty 1.2 foi o que piorou — as listas de controle estrutural ficaram, o 'gatilho de gosto' saiu.

## Limites e trade-offs
No-repeat n-gram é uma máscara absoluta: em geração longa e vocabulário pequeno, pode não haver continuação válida e o comportamento vira degenerado (a doc avisa do trade-off); tamanho baixo (2) proíbe até 'de a' repetido — 3–4 é o piso sensato. bad_words_ids com tokens que aparecem em contexto normal é censura acidental — a lista deve ser de subtokens, não de 'palavras'. E nenhum deles ensina o modelo: são pós-processamento de logits, sintoma, não causa.

## Como verificar
O suite de repetição: N amostras × distinct-2/distinct-3 e taxa de n-gram repetido, por combo de flags — o delta documenta cada alavanca separadamente (o erro comum é medir o bundle). Um teste adversarial com o prompt 'repita X' confirma que o ngram ban ganha do pedido. Sequence bias: asserção de que os tokens forçados aparecem em 100% com peso alto.

## Conexões
- [[hf-min-p-top-h-typical-p-filtros]] — Transformers: os filtros alternativos do sampling — min_p, top_h, typical_p — e suas faixas.
- [[hf-cache-implementation-quatro-modos]] — Transformers: cache_implementation escolhe o destino da KV — dynamic, static, offload ou quantizada.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a seção de controle de repetição com os quatro grupos de campos Consulta: 2026-10-04.
- [Transformers — generation utils (referência interna)](https://huggingface.co/docs/transformers/internal/generation_utils) — a implementação dos logit processors/weights referenciada pelo mecanismo Consulta: 2026-10-04.
