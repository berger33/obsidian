---
id: software.criacao_ia.tranche05.000410
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://docs.ollama.com/api/delete", "https://docs.ollama.com/api/introduction"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: proteger a remoção de modelos com confirmação do nome exato

## Em uma frase
`DELETE /api/delete` remove o modelo nomeado no corpo da requisição, por isso uma interface administrativa deve exigir um alvo explícito e confirmar o efeito.

## Por que importa
Uma remoção disparada por seleção desatualizada ou nome resolvido parcialmente pode interromper ferramentas locais que ainda dependem daquele modelo.

## Como funciona
Envie `model` com o nome exato e use o método HTTP DELETE documentado. Restrinja a ação a operadores autorizados, mostre o alvo antes de confirmar e atualize o inventário depois da resposta.

## Exemplo
O painel abre uma confirmação com `local-code-review`, envia a remoção somente após ação deliberada do operador e verifica que o nome deixou de aparecer em `/api/tags`.

## Limites e trade-offs
A referência informa sucesso da operação, mas não descreve uma lixeira ou recuperação. A introdução da API também informa que criar e remover modelos requer servidor local; trate o comando como potencialmente destrutivo.

## Como verificar
Em um ambiente descartável, valide autorização, método e nome serializado, confirme que cancelamento não envia requisição e confira o resultado por nova listagem.

## Conexões
- [[ollama-api-copy-modelo-com-nome-separado]] — Ollama API: copiar um modelo para um nome isolado antes de alterar a configuração.

## Fontes
- [Ollama API — Delete a model](https://docs.ollama.com/api/delete) — Define método DELETE, corpo com nome do modelo e resposta de sucesso. Consulta: 2026-10-04.
- [Ollama API — Introduction](https://docs.ollama.com/api/introduction) — Esclarece que a operação de remoção requer servidor local. Consulta: 2026-10-04.
