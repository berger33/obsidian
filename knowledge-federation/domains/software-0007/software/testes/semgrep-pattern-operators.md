---
id: software.testes.tranche18.001229
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://semgrep.dev/docs/writing-rules/overview", "https://semgrep.dev/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: combinar condições com operadores

## Em uma frase
Operadores permitem exigir várias condições, alternativas, negação, contexto interno e correspondência por expressão regular sobre metavariáveis.

## Por que importa
Problemas reais raramente dependem de um único trecho, e a combinação de condições reduz achados irrelevantes.

## Como funciona
Use exigência de condições para regras precisas, alternativas quando houver formas equivalentes e restrinja com padrões textuais apenas o necessário.

## Exemplo
Uma regra pode exigir que a chamada apareça dentro de um bloco de tratamento de erro e que o argumento corresponda a padrão textual específico.

## Limites e trade-offs
Condições amplas geram muitos achados e levam a equipe a ignorar a regra, enquanto restrições excessivas deixam casos reais fora.

## Como verificar
Compare a contagem de achados antes e depois de acrescentar uma condição e verifique se os casos descartados eram falsos positivos.

## Conexões
- [[semgrep-rule-structure]] — Veja também: Semgrep: estruturar uma regra própria.
- [[semgrep-metavariables]] — Veja também: Semgrep: capturar valores com metavariáveis.

## Fontes
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
