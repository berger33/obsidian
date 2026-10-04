---
id: software.criacao_ia.tranche04.000385
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

# llama.cpp server: /completion é API própria, /v1/completions é a de OpenAI

## Em uma frase
O server expõe os dois sabores de endpoint — o nativo (/completion, /embeddings etc.) e o compatível OpenAI (/v1/...) — com campos e semantics diferentes; e o /health responde 503 'Loading model' enquanto o modelo entra.

## Por que importa
Clientes copiados de exemplos OpenAI apontando para /completions (sem o /v1) recebem a API nativa com campos que parecem familiares e não são; orquestradores de k8s que não tratam o 503 de load fazem restart-loop de um pod perfeitamente saudável. A doc enumera os dois conjuntos explicitamente e marca a escolha: para compatibilidade, use os da família /v1.

## Como funciona
Nativo: /completion aceita prompt bruto + sampling no mesmo corpo (e é o que os exemplos históricos do server usam). OpenAI-compat: /v1/chat/completions, /v1/completions, /v1/embeddings etc. com os shapes esperados — o caminho para Plugs que só falam OpenAI. /health retorna 200 com 'ok' quando pronto e 503 'Loading model' durante o load (a doc documenta o estado), e /props (se --props on) permite ajustar properties por POST. Streaming: os dois sabores têm variantes SSE — confira a flag de stream por endpoint na doc, não por memória.

## Exemplo
Um LangChain genérico recebe base URL .../v1 e model qualquer: os dois primeiros timeouts 'inexplicáveis' eram /completions nativo recebendo bodies OpenAI-shaped — o fix foi o /v1 na configuração, zero código.

## Limites e trade-offs
A compatibilidade OpenAI é subset declarada, não OpenAI inteira: fields exóticos do SDK podem ser ignorados silenciosamente (a doc lista o que mapeia). /health 503 durante load é um estado, não um bug — o readiness probe tem que aceitá-lo. E a API nativa é volúvel entre releases (a doc da ferramenta é a fonte de verdade da sua build), enquanto a /v1 tende a ser a mais estável — mais uma razão para preferi-la em produção.

## Como verificar
Um teste de fumaça por endpoint com curl contra o build seu: os dois shapes, status esperados, e o diff de campos que o SDK usa. Readiness: probe com 503→200 (o padrão k8s) contra um load de modelo grande. Uma request de chat com field desconhecido na /v1: confirme o comportamento (ignore vs. 400) e registre na decisão de SDK.

## Conexões
- [[llamacpp-cache-prompt-ram-e-reuse]] — llama.cpp server: cache de prompt tem três camadas — o mesmo estado, três knobs.
- [[llamacpp-servidor-sem-auth-na-rede]] — llama.cpp server: não é um servidor de produção exposto — e as três chaves que aproximam.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — a listagem de endpoints com os exemplos por sabor (nativo e OpenAI) e o estado de /health Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — documenta como a saída estruturada chega nos dois sabores (grammar vs response_format) Consulta: 2026-10-04.
