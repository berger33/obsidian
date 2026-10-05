---
id: software.criacao_ia.tranche05.000408
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
fontes: ["https://docs.ollama.com/api/create", "https://docs.ollama.com/api/introduction"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: criar um modelo derivado com parâmetros e instruções explícitas

## Em uma frase
`POST /api/create` cria um nome de modelo a partir de um modelo existente e aceita configuração como template, system, parâmetros e mensagens.

## Por que importa
Empacotar uma configuração reutilizável pode facilitar distribuição dentro de um ambiente, mas torna necessário registrar de quais valores e modelos a derivação depende.

## Como funciona
Informe o nome de destino em `model` e, quando aplicável, `from`, `system`, `template`, `parameters`, `messages` ou arquivos digestados. A resposta pode transmitir atualizações de status, pois `stream` também é verdadeiro por padrão.

## Exemplo
Uma equipe cria `assistant-review` a partir de um modelo aprovado, incorpora instruções revisadas e parâmetros versionados, acompanha os estados do create e verifica o nome resultante com `/api/tags`.

## Limites e trade-offs
A criação e a remoção de modelos requerem um servidor Ollama local segundo a introdução da API; o endpoint não substitui revisão de licença nem análise de proveniência dos pesos.

## Como verificar
Teste em uma instalação descartável, confirme o destino no inventário e use `/api/show` para conferir os metadados relevantes; não trate uma mensagem intermediária como confirmação definitiva.

## Conexões
- [[ollama-api-tags-vs-show-model-metadata]] — Ollama API: usar tags para inventário e show para metadados de um modelo.
- [[ollama-api-copy-modelo-com-nome-separado]] — Ollama API: copiar um modelo para um nome isolado antes de alterar a configuração.

## Fontes
- [Ollama API — Create a model](https://docs.ollama.com/api/create) — Lista campos aceitos para criação e resposta com atualizações de status. Consulta: 2026-10-04.
- [Ollama API — Introduction](https://docs.ollama.com/api/introduction) — Ressalva que criação e remoção de modelos exigem servidor local. Consulta: 2026-10-04.
