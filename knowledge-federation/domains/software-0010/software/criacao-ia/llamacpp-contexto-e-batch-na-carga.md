---
id: software.criacao_ia.tranche04.000381
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
fontes: ["https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md", "https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# llama.cpp server: tamanho de contexto e batch de prompt são duas alavancas separadas

## Em uma frase
O contexto do servidor (-c, default 0 = o valor do modelo) dimensiona a janela viva por slot; o batch (-b 2048 default, com -ub 512 de microbatch) dimensiona o processamento de prompt — configurar um não configura o outro.

## Por que importa
O erro de capacity planning em llama.cpp é ler -c como 'performance': contexto grande paga KV em RAM por slot sempre, enquanto o throughput de prompt depende de -b/-ub e do hardware. Times que sobem -c para 'aceitar arquivos maiores' veem latência piorar e culpam o modelo, quando o dial do throughput era o batch.

## Como funciona
Para prompts longos, o caminho é -b/-ub (o processamento é particionado em microbatches de -ub; -b grande ajuda quando a placa aguenta o VRAM do gráfico) — a doc do server registra os defaults 2048/512 e as interações com Flash Attention (nota separada). O -c define quanto contexto total existe por slot; com múltiplos slots (-np), ele se divide — e o custo real é KV por token. A decisão correta: medir o prompt típico do produto, dar folga (a cache de sistema + histórico), e não 'o máximo do modelo'.

## Exemplo
Um chat de documentos com prompts de ~6k tokens e resposta de 1k: -c 8192 por slot com -np 4 (contexto por slot conforme o modo de divisão), -b 4096/-ub 1024 num 4090 — o TTFT cai pelo batch, o VRAM de KV não explode por capricho.

## Limites e trade-offs
Valores de -c acima do trained do modelo dependem de YaRN/context-shift, não de mágica — a doc separa as flags de extensão. -b acima do que o VRAM do gráfico aguenta degrada (ou OOM). E o contexto do servidor é um orçamento por slot: N slots paralelos dividem a janela total configurada conforme o modo, então 'contexto de trabalho por usuário' é a conta que importa, não o -c bruto.

## Como verificar
Rode com --slots ligado e leia o estado por slot (janela usada) durante o load real — a verificação é a medição, não a flag. Compare TTFT de um prompt fixo em -b 512/2048/8192 na sua GPU: a curva é a decisão de -b. Force um prompt maior que -c e observe o comportamento de recusa/shift documentado na build.

## Conexões
- [[llamacpp-flash-attention-quantizacao-kv]] — llama.cpp server: Flash Attention abre a porta da quantização de KV.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — a tabela de opções com os defaults de -c, -b e -ub e as interações documentadas Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o vizinho de config que também come tokens do mesmo orçamento de contexto Consulta: 2026-10-04.
