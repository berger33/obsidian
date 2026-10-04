---
id: software.criacao_ia.tranche04.000394
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

# Transformers: early_stopping do beam tem três estados — e 'never' existe por um motivo

## Em uma frase
Em beam search, early_stopping controla quando a busca termina: 'never' (só termina no fim do max length), True (padrão comportamental: para quando há hipóteses suficientes 'terminadas'), ou False (corta quando a melhor corrente não pode ser batida pelo heurística de fim).

## Por que importa
Cortesia com o custo de beams: early_stopping=True pode economizar metade dos passos com qualidade idêntica em geração curta; mas em texto onde a hipótese boa 'melhora no fim' (resumo que fecha a frase, título que resolve a referência), a parada antecipada perde a melhor saída — é o cenário que o modo 'never' existe para cobrir, e o tri-estado documentado na página de estratégias é a alavanca.

## Como funciona
A página lista 'early_stopping' na tabela de beam search com o efeito de 'never'/True/False: com never, todas as hipóteses vão ao limite de comprimento; com True, terminou quando o número de sequências terminadas excede os beams; False é o corte clássico por bound. Combine com length_penalty (que só tem efeito em beam search — mesma fonte): um penalty maior favorece hipóteses longas, e early_stopping frouxo + penalty agressivo é a dupla de trade-off tempo/qualidade da busca.

## Exemplo
Um motor de 'headline A/B' com beams 8: a versão com early_stopping default cortava títulos bons pela metade da frase; 'never' + length_penalty 1.0 recuperou a qualidade com ~2× tempo de decode — a medição dos dois lados da flag é o case.

## Limites e trade-offs
O tri-estado é API específica de geração HF (outros runtimes têm binário); não generalize a config entre stacks. 'never' em modelos com EOS fraco (que ignora o token de fim) paga o teto de max_new_tokens por hipótese — budget sempre. E early stopping é busca, não amostragem: em modo beam-sample (nota anterior) a terminação antecipada interage com a estocasticidade da expansão — teste o combo.

## Como verificar
Um par de métricas por release: taxa de hipóteses finalizadas vs. passos médios decodificados, com/sem 'never' — o delta é a decisão. Um teste determinístico com corpus de títulos e assert de igualdade de top-1 entre runs fixa o estado. Se você trocou beams por amostragem, a página e o teste confirmam que early_stopping é no-op fora de beam.

## Conexões
- [[hf-beams-e-amostragem-tabela]] — Transformers: num_beams × do_sample é uma tabela de 4 modos, não dois knobs independentes.
- [[hf-temperature-topk-topp-defaults]] — Transformers: os defaults de sampling (1.0/50/1.0) não são config — são a ausência dela.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a seção de beam search com early_stopping e length_penalty e suas semânticas Consulta: 2026-10-04.
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — a definição e defaults dos campos na config Consulta: 2026-10-04.
