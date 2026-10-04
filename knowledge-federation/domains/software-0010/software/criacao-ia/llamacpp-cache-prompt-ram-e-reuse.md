---
id: software.criacao_ia.tranche04.000384
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

# llama.cpp server: cache de prompt tem três camadas — o mesmo estado, três knobs

## Em uma frase
A cache de KV do prompt vive em --cache-prompt (on por default), o cache entre sessões ociosas em --cache-ram (8192 MiB default), e o reaproveitamento parcial de prefixo divergente em --cache-reuse N — knobs que se somam e se engolem entre si.

## Por que importa
Latência de prompt processing é a métrica que o usuário sente como 'o app pensa'; e as três chaves atacam o mesmo problema em camadas diferentes — cache-prompt elimina requantizar o turno anterior da mesma sessão, cache-ram guarda prefixos de sessões ociosas na RAM, e cache-reuse aceita divergência no início da conversa (shiftando o KV para o sufixo). Errar a combinação é pagar os três custos de novo.

## Como funciona
Padrões do README: --cache-prompt on significa avaliar só o sufixo não-visto do prompt (a reutilização é de prefixo exato, e o log informa quando não casou). --cache-ram com valor em MiB define o teto do cache ocioso (0/-1 desliga) e --cache-idle-slots depende dele. --cache-reuse N habilita o caminho de shift de KV para o maior sufixo compatível quando o prefixo divergiu (com o custo de recomputar a janela de alinhamento). Comece pelo padrão, mude uma chave por vez e meça TTFT.

## Exemplo
Um chat de suporte com 12-turnos: cache-prompt padrão serve (mesma sessão, prefixo crescente); o cache-ram sobe para 16384 para sessões de janela que abrem e fecham; cache-reuse fica desligado até alguém medir o ganho — e o ganho não veio no perfil deles.

## Limites e trade-offs
Cache de prefixo tem semântica de string exata: um byte antes do system prompt muda tudo e o cache perde — 'por que não cacheou?' é quase sempre timestamp/random no início. --cache-ram é budget, não afeta o cache-prompt da sessão viva. E cache-reuse tem o preço do KV-shift (reprocessar N tokens de alinhamento): com prompts curtos o saldo pode ser negativo — a doc posiciona como caso de prefixo longo divergente.

## Como verificar
No log do server, a linha de cache de prompt informa tokens avaliados vs. total por request — ler isso é a verificação do hit. Dois requests idênticos: o segundo deve ter TTFT visivelmente menor (mesmo slot). Desligue --cache-ram (0) e ligue --cache-idle-slots: a segunda exige a primeira, e a recusa de startup é o teste da dependência documentada.

## Conexões
- [[llamacpp-slots-paralelos-np-cb]] — llama.cpp server: -np multiplica o contexto e -cb faz o cache caber em cada slot.
- [[llamacpp-endpoints-completion-vs-openai]] — llama.cpp server: /completion é API própria, /v1/completions é a de OpenAI.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — as três chaves de cache com defaults (8192 MiB, on/off, dependência idle-slots) e a nota de sufixo Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o contexto de custo por token que o cache paga para não repetir Consulta: 2026-10-04.
