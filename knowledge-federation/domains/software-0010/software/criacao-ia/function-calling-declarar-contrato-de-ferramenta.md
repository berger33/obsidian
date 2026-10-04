---
id: software.criacao_ia.tranche01.000021
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

# Function calling: declarar contrato de ferramenta

## Em uma frase

Uma ferramenta descreve nome, finalidade e parâmetros que o modelo pode propor ao aplicativo para resolver uma tarefa.

## Por que importa

Um contrato estreito limita ambiguidades entre a intenção gerada e as operações que o servidor realmente suporta.

## Como funciona

Defina uma função por capacidade, use nomes semânticos e descreva campos e tipos sem incluir segredos ou poderes administrativos desnecessários.

## Exemplo

Um jogo oferece `consultar_missao` com identificador de missão, em vez de uma ferramenta genérica que execute qualquer comando.

## Limites e trade-offs

Descrições claras não tornam uma operação autorizada; o código precisa validar permissão e escopo.

## Como verificar

Inspecione o esquema publicado e confirme que cada ferramenta pode fazer somente as ações esperadas para aquele usuário.

## Conexões
- [[responses-api-avaliar-geracao-com-exemplos]] — Responses API: avaliar geração com exemplos.
- [[saida-estruturada-usar-json-schema-estrito]] — Saída estruturada: usar JSON Schema estrito.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
