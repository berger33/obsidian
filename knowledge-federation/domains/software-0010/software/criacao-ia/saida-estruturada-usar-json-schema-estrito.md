---
id: software.criacao_ia.tranche01.000022
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

# Saída estruturada: usar JSON Schema estrito

## Em uma frase

Structured Outputs pode restringir a forma da resposta ao esquema aceito pelo aplicativo, quando o modelo e o modo escolhido suportam esse recurso.

## Por que importa

Contrato previsível diminui parsing frágil para formulários, diálogos e integrações que precisam de campos tipados.

## Como funciona

Declare propriedades, tipos e obrigatoriedade segundo a documentação, e escolha modo estrito quando for apropriado ao endpoint e ao esquema.

## Exemplo

Um editor de quests solicita objeto com `titulo`, `objetivos` e `nivel_recomendado`, todos com limites definidos pelo app.

## Limites e trade-offs

Conformidade estrutural não prova verdade factual nem elimina estados de recusa ou saída incompleta.

## Como verificar

Valide saída de sucesso e casos de recusa, erro e truncamento; rejeite qualquer valor que não passe também pelas regras de domínio.

## Conexões
- [[function-calling-declarar-contrato-de-ferramenta]] — Function calling: declarar contrato de ferramenta.
- [[function-calling-executar-no-aplicativo-nao-no-modelo]] — Function calling: executar no aplicativo, não no modelo.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
