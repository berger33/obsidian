---
id: software.criacao_ia.tranche04.000398
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
fontes: ["https://huggingface.co/docs/transformers/main_classes/text_generation", "https://huggingface.co/docs/transformers/kv_cache"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: cache_implementation escolhe o destino da KV — dynamic, static, offload ou quantizada

## Em uma frase
A config de geração aceita cache_implementation: 'dynamic' (default, cresce com realloc), 'static' (pré-alocada, barata em CUDA graphs), 'offloaded'/'offloaded_static' (KV para CPU em camadas) e 'quantized' (KV comprimida), com max_cache_len dimensionando o static.

## Por que importa
KV cache é o gargalo de memória de decodificação longa, e os modos são trade-offs diferentes, não tiers de 'performance': static elimina o realloc (e é o que casa com compile/CUDA graphs — com o preço de pré-alocar), offload troca VRAM por bandwidth, quantized troca precisão por capacidade. Errar a escolha é pagar a conta errada no lugar errado — o 'OOM em 8k de contexto' que resolve com duas linhas de config.

## Como funciona
Da página de geração (e da seção kv_cache): 'cache_implementation' com os quatro valores e o subtipo offloaded_static; para static/offloaded_static defina max_cache_len — pré-dimensionar evita recompilação (a doc nota o efeito em torch.compile). A rota quantizada tem seus próprios parâmetros (a página de kv_cache cobre os quantizadores por camada). Decisão por perfil: decode curto variável → dynamic; decode de comprimento limitado + compile/graphs → static; contexto que não cabe → offloaded (se o bandwidth aguenta) ou quantized (se a qualidade aguenta).

## Exemplo
Um servidor de roleplay com saídas de até 2k por usuário em 4090 16 GB: static + max_cache_len alinhado ao teto, com o espaço de VRAM reservado sendo a base da conta de -np; o modo dynamic estourava realloc com o batch variável.

## Limites e trade-offs
static pré-aloca por batch — em lotes variáveis o desperdício paga a previsibilidade; e o valor errado de max_cache_len ou cresce demais (OOM na reserva) ou corta (erro/truncamento). offloaded mede bandwidth PCIe no decode — em tokens/s o ganho pode ser negativo com geração curta. quantized afeta qualidade de retrieved-context (o mesmo aviso da KV quantizada do outro runtime se aplica — avalie no seu task). A lista de modos é da API do Transformers, não de vLLM/TGI: port não herda.

## Como verificar
O teste é mem+throughput nas duas pontas: pico de memória do processo e tokens/s por batch size por modo, no comprimento real do produto (não num toy de 128 tokens). Um assert de 'sem recompilação' no run de static+compile (o log do torch.compile mostra o recapture) valida o max_cache_len. Para quantized, o suite de qualidade da nota de KV (extrativa de documento longo) antes do rollout.

## Conexões
- [[hf-repeticao-ngram-e-bias]] — Transformers: o arsenal anti-repetição — n-gramas, penalidades e viés de tokens.
- [[hf-assisted-decoding-especifico]] — Transformers: decodificação assistida — draft por modelo, n-gram, medusa ou ensemble.

## Fontes
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — a configuração de cache (implementation, max_cache_len, offloading) na API de geração Consulta: 2026-10-04.
- [Transformers — KV cache](https://huggingface.co/docs/transformers/kv_cache) — a explicação dos formatos de cache e dos quantizadores por camada Consulta: 2026-10-04.
