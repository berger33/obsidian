---
id: software.criacao_ia.tranche04.000396
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
fontes: ["https://huggingface.co/docs/transformers/generation_strategies", "https://huggingface.co/docs/transformers/main_classes/text_generation"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: os filtros alternativos do sampling — min_p, top_h, typical_p — e suas faixas

## Em uma frase
Fora do top-k/top-p, a config de amostragem expõe min_p (corte relativo ao máximo: escalonado com o resto), top_h (entropia mínima), typical_p (local typicality) e o corte epsilon (epsilon sampling) — com faixas recomendadas documentadas.

## Por que importa
Cada um ataca um regime diferente da cauda: min_p corta tokens 'baixos em relação ao melhor' (robusto a entropia variável do contexto), top_h mantém o mínimo de massa de entropia (a métrica informativa de 'quanta incerteza sobreviver'), typical_p mantém o que tem surprisal perto da entropia local. Usar sem a orientação da doc (min_p 0,01–0,2; top_h 0,3–0,6; epsilon 3e-4–9e-4) é tuning no escuro.

## Como funciona
Da página de sampling: min_p é multiplicado pela probabilidade do melhor token (com as demais normalizações, daí a relação com top_p recomendada); a doc sugere 0,01–0,2. top_h define o piso de entropia a manter (0,3–0,6 sugerido). typical_p (a distribuição de surprisal perto da entropia local, com a faixa clássica de 0,9) e epsilon sampling (corte em função da probabilidade do melhor token; valores 3e-4–9e-4 sugeridos) são os outros dois. A combinação com renormalize_logits continua a nota padrão. São knobs de qualidade-estilo, não de velocidade.

## Exemplo
Um chat criativo 'menos robótico' que rejeitava top-p: o preset que ficou foi top_k 100 + min_p 0.08 — a cauda média cortada (artefato), a cauda de contexto permitida (o token raro certo que top-p puro mata). O A/B de qualidade foi por faixas da doc, não por gosto.

## Limites e trade-offs
A faixa recomendada é um ponto de partida documentado, não um contrato: a sensibilidade do seu modelo a cada corte é empiria (e a doc mesma lista como recomendação de calibração). Filtros relativos (min_p, epsilon) respondem diferente a temperatura alta vs. baixa — a ordem do pipeline de samplers importa (nota llama.cpp irmã tem a ordem do outro runtime; aqui, a doc descreve os campos, a sequência é da implementação). E nenhum filtro de cauda substitui no_repeat_ngram (próxima nota) para repetição estrutural.

## Como verificar
Um harness de 'varrer uma faixa por filtro e medir distinct-n + n-gram repetition + ROUGE contra referência' — as faixas da doc viram eixo do gráfico, e o joelho é o seu preset. Teste unitário: o filtro isolado muda exatamente o que deve (o corte de cauda não deve alterar o top-1 do modo greedy). Snapshot de distribuição num prompt canary por release de transformers.

## Conexões
- [[hf-temperature-topk-topp-defaults]] — Transformers: os defaults de sampling (1.0/50/1.0) não são config — são a ausência dela.
- [[hf-repeticao-ngram-e-bias]] — Transformers: o arsenal anti-repetição — n-gramas, penalidades e viés de tokens.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a seção de sampling com min_p/top_h/typical_p/epsilon e as faixas sugeridas Consulta: 2026-10-04.
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — os campos correspondentes na classe de config Consulta: 2026-10-04.
