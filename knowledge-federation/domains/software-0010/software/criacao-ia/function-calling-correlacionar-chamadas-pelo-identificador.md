---
id: software.criacao_ia.tranche01.000024
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

# Function calling: correlacionar chamadas pelo identificador

## Em uma frase

O identificador retornado junto a uma chamada relaciona a resposta da ferramenta à solicitação que a originou.

## Por que importa

Correlacionar evita misturar resultados quando uma rodada contém mais de uma ferramenta ou quando o fluxo é assíncrono.

## Como funciona

Preserve o call ID conforme o protocolo de resposta e associe cada resultado à chamada e ao estado de conversa corretos.

## Exemplo

Uma aplicação que consulta inventário e clima em paralelo devolve cada resultado à chamada correspondente antes de continuar a rodada.

## Limites e trade-offs

IDs não são autorização, segredo ou chave de deduplicação de negócio por si sós.

## Como verificar

Force duas chamadas numa mesma resposta e verifique que a aplicação não troca resultados nem usa dados de um usuário em outra sessão.

## Conexões
- [[function-calling-executar-no-aplicativo-nao-no-modelo]] — Function calling: executar no aplicativo, não no modelo.
- [[function-calling-lidar-com-zero-ou-varias-chamadas]] — Function calling: lidar com zero ou várias chamadas.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
