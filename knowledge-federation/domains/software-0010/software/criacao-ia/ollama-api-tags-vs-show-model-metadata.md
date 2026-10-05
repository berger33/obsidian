---
id: software.criacao_ia.tranche05.000407
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
fontes: ["https://docs.ollama.com/api/tags", "https://docs.ollama.com/api-reference/show-model-details"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: usar tags para inventário e show para metadados de um modelo

## Em uma frase
`GET /api/tags` enumera modelos disponíveis, enquanto `POST /api/show` consulta detalhes de um modelo nomeado; são leituras com propósitos diferentes.

## Por que importa
Um seletor de modelos precisa de inventário para preencher opções e de metadados específicos para exibir capacidades ou conferir parâmetros sem inferi-los pelo nome.

## Como funciona
Use o array `models` de `/api/tags` para descobrir nomes e detalhes resumidos; em seguida, envie o nome escolhido a `/api/show`. A resposta de show pode incluir capacidades, parâmetros e informações adicionais do modelo.

## Exemplo
Uma tela carrega a lista de modelos, deixa o usuário escolher um deles e chama show apenas para a seleção atual, exibindo capacidades reportadas em vez de assumir que todo modelo aceita imagem ou thinking.

## Limites e trade-offs
Os detalhes dependem do modelo e alguns campos podem estar ausentes; uma listagem não substitui autorização nem prova que o modelo seguirá uma capacidade com qualidade adequada.

## Como verificar
Compare os nomes retornados pelo inventário com a seleção e trate um modelo removido entre as duas chamadas; teste campos opcionais ausentes e a opção `verbose` de show quando necessária.

## Conexões
- [[ollama-api-pull-acompanhar-progresso]] — Ollama API: acompanhar o progresso do pull sem fixar mensagens de status.
- [[ollama-api-create-configurar-modelo-derivado]] — Ollama API: criar um modelo derivado com parâmetros e instruções explícitas.

## Fontes
- [Ollama API — List models](https://docs.ollama.com/api/tags) — Mostra o endpoint de inventário e os campos resumidos de cada modelo. Consulta: 2026-10-04.
- [Ollama API — Show model details](https://docs.ollama.com/api-reference/show-model-details) — Documenta `/api/show`, campos de capacidades e resposta de metadados. Consulta: 2026-10-04.
