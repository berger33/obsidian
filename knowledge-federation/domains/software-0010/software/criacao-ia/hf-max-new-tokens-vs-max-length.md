---
id: software.criacao_ia.tranche04.000392
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

# Transformers: max_new_tokens é o budget relativo; max_length é o absoluto que te morderá

## Em uma frase
Geração é limitada por max_length (índice absoluto na sequência) ou max_new_tokens (quantos tokens novos); a doc recomenda o relativo — e sem config o greedy para em ~20 tokens novos.

## Por que importa
O par de knobs é a causa do 'por que a resposta cortou em 20?' em todo primeiro uso: sem generation config, o limite default de novos tokens é curto (a página registra o teto de 20 para o caso sem config). E max_length absoluto significa que prompt longo + max_length fixo = resposta encurtada silenciosamente — o bug de produção clássico de pipelines com entradas variáveis.

## Como funciona
Sempre defina explicitamente o budget: 'max_new_tokens=N' na chamada ou no config. A página de estratégias usa o default curto como o caso de atenção do greedy: 'if no generation config... will generate at most 20 tokens', com a instrução preferir max_new_tokens. Para orçamento total, calcule 'min(max_new_tokens, context_len - input_len)' você mesmo — o modelo tem janela própria, e excedê-la é erro/clip conforme o modelo.

## Exemplo
Um RAG que injeta 3k de contexto e 'max_length 4096': as respostas sumiram em prompts de 3,8k (sobravam 296 tokens de saída); a migração para 'max_new_tokens 512' por request conserta o que a métrica de truncamento denuncia.

## Limites e trade-offs
Alguns modelos/tarefas têm limites próprios de posição e o clip é do modelo, não do config. 'max_new_tokens' com streaming precisa de stop conditions além dele (eos próprio, ou stopping criteria — a página cobre os callbacks) ou você paga o budget inteiro por request. E o teto de 20 sem config é comportamento documentado do greedy default, não um piso garantido entre versões — configure explicitamente.

## Como verificar
Um fixture sem config que gera 'hello world?' e conta tokens: a asserção do teto atual (20) na sua versão documenta a regra. Dois prompts (curto/longo) com max_length fixo vs. max_new_tokens fixo: o diff de comprimento de resposta é a lição visual. Logger de 'input_len + output_len vs budget' num canary por release.

## Conexões
- [[hf-generation-config-nen-hereda-modelo]] — Transformers: os None da GenerationConfig são herança, não desatenção.
- [[hf-beams-e-amostragem-tabela]] — Transformers: num_beams × do_sample é uma tabela de 4 modos, não dois knobs independentes.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — o teto de 20 tokens do caso sem config e a recomendação de max_new_tokens Consulta: 2026-10-04.
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — a definição dos dois campos na config de geração Consulta: 2026-10-04.
