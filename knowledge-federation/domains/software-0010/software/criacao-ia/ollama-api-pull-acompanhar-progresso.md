---
id: software.criacao_ia.tranche05.000406
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
fontes: ["https://docs.ollama.com/api/pull", "https://docs.ollama.com/api/tags"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: acompanhar o progresso do pull sem fixar mensagens de status

## Em uma frase
`POST /api/pull` pode transmitir atualizações de progresso, então um cliente de instalação precisa separar estados intermediários do resultado final.

## Por que importa
Downloads podem levar tempo e a interface deve manter o usuário informado sem marcar um modelo como disponível antes da conclusão reportada pelo servidor.

## Como funciona
A referência de pull documenta `stream` como verdadeiro por padrão e descreve respostas de status de progresso; para uma resposta única, envie `stream: false`. Trate o campo de status como mensagem atual, sem assumir uma enumeração imutável de textos.

## Exemplo
Um painel mostra cada atualização recebida para o modelo escolhido, desabilita o botão enquanto a operação está ativa e confirma a disponibilidade com uma consulta subsequente ao catálogo.

## Limites e trade-offs
As mensagens de progresso são dependentes da operação e não devem funcionar como identificadores persistentes nem como prova de que um nome específico de modelo foi carregado corretamente.

## Como verificar
Em um servidor de teste, observe pull com stream ligado e desligado, assegure que o cliente não confunde uma atualização com sucesso final e confirme o modelo no catálogo após completar.

## Conexões
- [[ollama-api-embeddings-lote-e-truncamento]] — Ollama API: gerar embeddings em lote e escolher a política de truncamento.
- [[ollama-api-tags-vs-show-model-metadata]] — Ollama API: usar tags para inventário e show para metadados de um modelo.

## Fontes
- [Ollama API — Pull a model](https://docs.ollama.com/api/pull) — Define o endpoint, o padrão de streaming e as respostas de status. Consulta: 2026-10-04.
- [Ollama API — List models](https://docs.ollama.com/api/tags) — Permite confirmar separadamente quais modelos aparecem no catálogo local. Consulta: 2026-10-04.
