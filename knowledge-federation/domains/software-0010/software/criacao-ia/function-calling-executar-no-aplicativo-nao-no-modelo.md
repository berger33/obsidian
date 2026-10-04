---
id: software.criacao_ia.tranche01.000023
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://platform.openai.com/docs/guides/function-calling", "https://platform.openai.com/docs/guides/structured-outputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Function calling: executar no aplicativo, não no modelo

## Em uma frase

A chamada retornada pelo modelo é uma proposta de operação; é o código do aplicativo que decide validá-la e executá-la.

## Por que importa

Esta separação evita tratar texto gerado como uma ação já autorizada ou como resultado de banco de dados.

## Como funciona

Receba o item de chamada, verifique nome e argumentos, execute somente a função correspondente e envie o resultado pelo mecanismo documentado.

## Exemplo

Se o modelo sugere `consultar_inventario`, o servidor consulta os dados do jogador autenticado e retorna uma resposta filtrada.

## Limites e trade-offs

Não execute conteúdo arbitrário, nomes de função dinâmicos ou comandos de shell recebidos na chamada.

## Como verificar

Teste que uma chamada desconhecida é rejeitada e que operações reais só acontecem após autorização do servidor.

## Conexões
- [[saida-estruturada-usar-json-schema-estrito]] — Saída estruturada: usar JSON Schema estrito.
- [[function-calling-correlacionar-chamadas-pelo-identificador]] — Function calling: correlacionar chamadas pelo identificador.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
