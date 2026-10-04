---
id: software.testes.tranche18.001234
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
fontes: ["https://semgrep.dev/docs/", "https://semgrep.dev/docs/writing-rules/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: registrar exceções de forma auditável

## Em uma frase
Achados podem ser silenciados com anotação no código, e a supressão pode ser restrita ao escopo onde o risco é aceito.

## Por que importa
Exceções explícitas mantêm o histórico da decisão e evitam que a regra seja desligada inteira por causa de um caso isolado.

## Como funciona
Anote a supressão próxima ao trecho, indique o motivo e reavalie as exceções em cada ciclo de revisão.

## Exemplo
Um trecho legado pode ser marcado como exceção com prazo enquanto a correção definitiva é planejada.

## Limites e trade-offs
Supressões sem justificativa acumulam risco invisível, e anotações amplas escondem arquivos inteiros da análise.

## Como verificar
Remova temporariamente uma supressão e confirme quais achados ela estava ocultando antes de mantê-la.

## Conexões
- [[semgrep-ci-integration]] — Veja também: Semgrep: integrar a análise ao pipeline.
- [[semgrep-severity-and-policy]] — Veja também: Semgrep: definir severidade e política de bloqueio.

## Fontes
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
