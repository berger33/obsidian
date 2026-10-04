---
id: software.testes.tranche15.000891
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/counters.html", "https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: interpretar os contadores

## Em uma frase
O JaCoCo contabiliza instruções, ramos, linhas, complexidade, métodos e classes, cada qual respondendo a uma pergunta distinta sobre a execução.

## Por que importa
Usar um único número de cobertura para tudo mistura granularidade de bytecode com legibilidade de fonte e esconde a ausência de caminhos condicionais exercitados.

## Como funciona
Escolha o contador conforme a decisão que o indicador precisa apoiar e documente qual deles é usado como limite no projeto.

## Exemplo
Cobertura de linhas conta linhas com alguma instrução executada, enquanto cobertura de ramos conta desfechos de decisões e revela condições não exercitadas.

## Limites e trade-offs
Instrução é a unidade mais fina e não se traduz diretamente em linhas de código; complexidade coberta mede apenas a parcela de caminhos exercitada pela suíte.

## Como verificar
Compare o relatório de linhas com o de ramos em uma classe com muitos condicionais e explique a diferença observada entre os dois indicadores.

## Conexões
- [[jacoco-agent-on-the-fly]] — Veja também: JaCoCo: medir cobertura com o agente Java.
- [[jacoco-branch-vs-line]] — Veja também: JaCoCo: usar cobertura de ramos para decisões.

## Fontes
- [JaCoCo — Coverage counters](https://www.jacoco.org/jacoco/trunk/doc/counters.html) — definições de instruction, branch, line, complexity, method e class; consultado em 2026-10-02.
- [JaCoCo — jacoco:report](https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html) — formatos de relatório, fontes, agregação e configuração do goal; consultado em 2026-10-02.
