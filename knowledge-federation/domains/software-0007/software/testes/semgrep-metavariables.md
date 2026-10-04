---
id: software.testes.tranche18.001230
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

# Semgrep: capturar valores com metavariáveis

## Em uma frase
As metavariáveis representam trechos variáveis do código e podem ser reutilizadas para exigir que duas posições correspondam ao mesmo valor.

## Por que importa
A reutilização da metavariável expressa relações entre argumentos que uma correspondência textual não captura.

## Como funciona
Nomeie a metavariável de forma expressiva e reutilize-a apenas quando a igualdade entre as posições for realmente exigida.

## Exemplo
Uma regra pode exigir que a variável atribuída seja a mesma usada na validação seguinte, ignorando casos em que os valores diferem.

## Limites e trade-offs
Reutilizar a metavariável sem intenção perde achados legítimos, e nomes obscuros tornam a regra difícil de revisar.

## Como verificar
Introduza um caso em que os valores diferem e confirme que a regra deixa de acusar, como esperado.

## Conexões
- [[semgrep-pattern-operators]] — Veja também: Semgrep: combinar condições com operadores.
- [[semgrep-taint-mode]] — Veja também: Semgrep: analisar fluxo com modo de propagação.

## Fontes
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
