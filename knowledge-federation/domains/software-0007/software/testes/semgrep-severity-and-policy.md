---
id: software.testes.tranche18.001235
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
fontes: ["https://semgrep.dev/docs/", "https://github.com/semgrep/semgrep"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: definir severidade e política de bloqueio

## Em uma frase
As regras declaram severidade, e a execução pode falhar por severidade mínima ou por regra específica conforme a política do projeto.

## Por que importa
A política converte a análise em critério objetivo e permite começar bloqueando apenas o que é inequivocamente relevante.

## Como funciona
Ajuste a severidade conforme o impacto real, comece bloqueando pelos níveis mais altos e revise a política quando o passivo diminuir.

## Exemplo
Um projeto pode bloquear apenas achados de alta severidade enquanto o restante é reportado para triagem.

## Limites e trade-offs
Bloquear tudo desde o início paralisa o fluxo, e nunca bloquear faz o relatório perder consequência.

## Como verificar
Reduza temporariamente o limite de bloqueio e confirme que o trabalho passa a falhar em achados antes apenas reportados.

## Conexões
- [[semgrep-suppressions]] — Veja também: Semgrep: registrar exceções de forma auditável.
- [[semgrep-custom-rules]] — Veja também: Semgrep: manter regras próprias do projeto.

## Fontes
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
- [Semgrep — repositório oficial](https://github.com/semgrep/semgrep) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
