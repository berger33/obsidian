---
id: software.criacao_ia.tranche04.000395
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

# Transformers: os defaults de sampling (1.0/50/1.0) não são config — são a ausência dela

## Em uma frase
Sem tocar na GenerationConfig, o sampling roda com temperature 1.0, top_k 50 e top_p 1.0 — a biblioteca amostra da distribuição quase-crua do modelo, e o que você chama de 'nossa temperatura' pode nunca ter sido definida.

## Por que importa
Os três parâmetros interagem e a doc de sampling os lista com esses defaults explícitos. 'Top-k=50' default é um corte que o time não decidiu (um modelo com cauda pesada perde tokens legítimos; um com cauda limpa não sente). E port de outros runtimes com 'top_k=-1' ou 'do_sample=False' muda o que esses três campos significam — carregar defaults sem ler é o bug de paridade.

## Como funciona
O trio documentado: temperature reescala os logits antes da softmax (1.0 = nenhum efeito, abaixo afia, acima achata); top_k mantém os k mais prováveis; top_p (nucleus) mantém o prefixo cumulativo até p. A ordem de interação e as renormalizações vivem na config de sampling, e a página recomenda 'renormalize_logits=True' para compatibilidade correta de filtros compostos. Regra de port: liste explicitamente os três no seu config, mesmo quando iguais ao default — o default da biblioteca não é o default do seu produto.

## Exemplo
Um port que 'piorou após migrar para HF' tinha top_k do runtime anterior em 40; o 50 silencioso aceitava o token 51º que degradava o factual. A config explícita dos três + o snapshot do config resolvido na CI fechou a divergência.

## Limites e trade-offs
temperature 0 é o modo greedy (do_sample=False), não 'um número pequeno' — a família de amostragem é um switch de modo, não uma rampa contínua com ela desligada. top_p e top_k juntos dependem da ordem interna (e da renormalização) — resultados podem divergir de pipelines que filtram na ordem oposta. E o renormalize_logits recomendado na página é compatibilidade de semantics, não garantia de igualdade com outros runtimes.

## Como verificar
Snapshot de config resolvido (to_dict) num teste de paridade por release — o assert pega mudanças de default. Um golden-set com seed por modo: a distribuição de tokens amostrados não deve mudar sem PR que assuma isso. O diff de top-1 entre temperature 1.0 e 0 é a calibração rápida do 'quão afiado o modelo já está sozinho'.

## Conexões
- [[hf-early-stopping-never]] — Transformers: early_stopping do beam tem três estados — e 'never' existe por um motivo.
- [[hf-min-p-top-h-typical-p-filtros]] — Transformers: os filtros alternativos do sampling — min_p, top_h, typical_p — e suas faixas.

## Fontes
- [Transformers — Generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — a seção de sampling com defaults e a nota de renormalize_logits Consulta: 2026-10-04.
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — os campos e defaults na classe de config Consulta: 2026-10-04.
