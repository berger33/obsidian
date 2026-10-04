---
id: software.criacao_ia.tranche04.000383
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

# llama.cpp server: -np multiplica o contexto e -cb faz o cache caber em cada slot

## Em uma frase
Serving paralelo é -np slots (com divisão de contexto por slot) e, com cache compartilhado entre requests, -cb (continuous batching) é o ajuste do orçamento de prompt por passo.

## Por que importa
Um servidor local mono-request desperdiça GPU ociosa entre tokens; -np resolve throughput por concorrência, mas cada slot carrega seu próprio KV — o erro é manter o -c de single-user e descobrir que 4 slots × 32k não cabem. E sem continuous batching, prompts longos dominam cada step de decode; com -cb ligado (default on na doc), o processamento é dividido entre slots no mesmo batch.

## Como funciona
O README documenta -np (com -1 = auto-dimensionado pelo contexto disponível no modo de cache) e as opções de slot; --slots on expõe o endpoint/visualização dos slots (GET /slots) para verificar o estado por sessão. A prática de plan: definir contexto-alvo por usuário, multiplicar por -np, caber no VRAM de KV (com a nota de -c acima do trained pedindo técnicas extras), e medir p99 de decode com a carga real de concorrência, não com um curl solitário.

## Exemplo
Um API interna com 8 usuários de chat: -np 8, -c ajustado para 8k/slot, --slots on para o painel de 'quem está gerando'; a capacidade vira gráfico em vez de achismo.

## Limites e trade-offs
Slots não são isolados no modelo: KV por slot é memória por slot, e a cota de -c dividida muda o teto de conversa, não só o desempenho. --props (propriedades por request) e --slots não vêm ligados por default (a doc: slots off, props off) — quem conta com eles no observability ativa cedo. E concorrência acima do VRAM é swap/OOM, não 'fila educada': o admission control é do proxy.

## Como verificar
GET /slots com --slots on durante carga: confirme N ativos e a janela por slot — o estado documentado vira mensurável. Compare throughput total em -np 1 vs. 4 vs. 8 com o mesmo -c total: a curva satura onde o seu VRAM diz. Teste o refusal: N+1 clientes simultâneos além da cota — o comportamento esperado é recusa/latência, não crash.

## Conexões
- [[llamacpp-flash-attention-quantizacao-kv]] — llama.cpp server: Flash Attention abre a porta da quantização de KV.
- [[llamacpp-cache-prompt-ram-e-reuse]] — llama.cpp server: cache de prompt tem três camadas — o mesmo estado, três knobs.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — as flags de paralelismo (-np, -cb, --slots, --props) e defaults documentados Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o texto vizinho sobre o que mais compete pelo orçamento do passo Consulta: 2026-10-04.
