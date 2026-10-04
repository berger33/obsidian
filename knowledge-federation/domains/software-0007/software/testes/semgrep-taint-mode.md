---
id: software.testes.tranche18.001231
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

# Semgrep: analisar fluxo com modo de propagação

## Em uma frase
O modo de propagação descreve fontes, destinos e saneadores, acompanhando a passagem de dados não confiáveis até operações sensíveis.

## Por que importa
A análise de fluxo detecta problemas que dependem do caminho percorrido entre a entrada e a operação perigosa, reduzindo falsos positivos.

## Como funciona
Declare fontes pela origem externa, destinos pelas operações sensíveis e saneadores que efetivamente neutralizam o risco.

## Exemplo
Uma regra pode acompanhar dado de requisição até consulta de banco, ignorando caminhos em que a validação já ocorreu.

## Limites e trade-offs
Saneadores incompletos geram falsa tranquilidade, e fontes mal declaradas deixam de encontrar entradas relevantes da aplicação.

## Como verificar
Remova o saneador da regra e confirme que o caminho antes ignorado passa a ser reportado.

## Conexões
- [[semgrep-metavariables]] — Veja também: Semgrep: capturar valores com metavariáveis.
- [[semgrep-rule-defined-fix]] — Veja também: Semgrep: sugerir correção automática.

## Fontes
- [Semgrep — Writing rules](https://semgrep.dev/docs/writing-rules/overview) — estrutura de regra, operadores, metavariáveis e modo de propagação; consultado em 2026-10-03.
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
