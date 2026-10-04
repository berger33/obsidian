---
id: software.criacao_ia.tranche01.000028
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

# Ferramentas: pedir confirmação antes de efeitos externos

## Em uma frase

Ações irreversíveis, financeiras ou visíveis a terceiros devem exigir confirmação e política do aplicativo, não apenas intenção inferida pelo modelo.

## Por que importa

Confirmação protege usuários de interpretações erradas em operações cujo custo não pode ser desfeito facilmente.

## Como funciona

Separe proposta de execução, apresente resumo claro para aprovação e revalide permissões e dados quando a pessoa confirmar.

## Exemplo

Um assistente de app prepara um post de anúncio, mostra destino e texto, e só publica depois do clique explícito do responsável.

## Limites e trade-offs

Confirmação não cobre fluxos silenciosos ou delegações já autorizadas; requisitos legais e controles de acesso continuam necessários.

## Como verificar

Verifique que cancelamento não executa a ação, confirmação usa dados ainda válidos e logs identificam quem autorizou.

## Conexões
- [[ferramentas-restringir-acoes-de-gameplay]] — Ferramentas: restringir ações de gameplay.
- [[function-calling-minimizar-dados-retornados]] — Function calling: minimizar dados retornados.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
