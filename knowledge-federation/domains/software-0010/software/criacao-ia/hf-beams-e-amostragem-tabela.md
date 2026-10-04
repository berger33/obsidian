---
id: software.criacao_ia.tranche04.000393
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

# Transformers: num_beams × do_sample é uma tabela de 4 modos, não dois knobs independentes

## Em uma frase
A doc das estratégias define os modos de geração como combinação: greedy (beams=1, sem sample), beam search (beams>1, determinístico), sample (beams=1, do_sample=True) e beam-sample (beams>1 + sample) — a tabela é o contrato.

## Por que importa
Pedir 'beam search' a um pipeline que setou do_sample=True não te dá beam search — te dá a variante estocástica da árvore, com comportamento radicalmente diferente em qualidade/repetição. E a crença de que 'sampling é a temperatura do beam' é o modo beam-sample da tabela, um híbrido que poucos times escolhem conscientemente. A classificação documentada elimina o debate.

## Como funciona
A página traz a matriz por estratégia (greedy, beam search e amostragem; com o efeito de num_beams>1 em cada) e os parâmetros por família: beam controla num_beams, early_stopping, length_penalty (nota: length penalty só vale em beam — documento na mesma página); sampling controla temperature/top-k/top-p. Para decisão: classificação/extrativa tende a greedy ou beam baixo; geração longa criativa tende a sample; beam+sample é o que a tabela chama de beam-sample e precisa de motivo explícito.

## Exemplo
Um gerador de títulos que 'melhorava com beams' mas tinha do_sample=True do preset herdado: os títulos variavam entre runs por causa do modo beam-sample silencioso — o fix foi o par explícito (num_beams=4, do_sample=False) em vez de qualquer temperatura.

## Limites e trade-offs
Beam search com modelos decodificador-esquerda-causal de grande escala tem performance de qualidade muito diferente da era seq2seq; a doc descreve o mecanismo, a adequação ao seu modelo é empiria (e o guidance do próprio texto de geração favorece sampling para criativo longo). num_beams alto multiplica o batch interno (custo linear em beams, com a ressalva de que a cache de KV é ampliada — nota separada de cache). E beam-sample não é 'melhor dos dois': é um terceiro comportamento.

## Como verificar
Um teste de sensibilidade: a mesma seed em (1,0), (4,0), (1,1), (4,1) com temperatura fixa — as quatro famílias devem responder diferente onde esperado (determinismo só nos do_sample=False). Registre a matriz como documentação viva do preset. No canary de produção, a métrica 'distinct-n' por modo separa 'estou gerando variedade' de 'estou gerando aleatoriedade'.

## Conexões
- [[hf-max-new-tokens-vs-max-length]] — Transformers: max_new_tokens é o budget relativo; max_length é o absoluto que te morderá.
- [[hf-early-stopping-never]] — Transformers: early_stopping do beam tem três estados — e 'never' existe por um motivo.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a tabela de estratégias e os parâmetros por família (beams, sample, híbrido) Consulta: 2026-10-04.
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — os campos num_beams/do_sample na classe e seus defaults Consulta: 2026-10-04.
