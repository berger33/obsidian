---
id: software.testes.tranche15.000892
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/counters.html", "https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: usar cobertura de ramos para decisões

## Em uma frase
A cobertura de ramos mede quantos desfechos de estruturas condicionais foram executados, incluindo os caminhos de `if` e de `switch`.

## Por que importa
Uma linha pode aparecer coberta quando apenas um lado da condição rodou, e o relatório de linhas sozinho não revela o ramo ausente.

## Como funciona
Combine o limite de linhas com um limite de ramos nos pontos críticos e investigue ramos não cobertos como comportamentos ainda não verificados.

## Exemplo
Uma condição de autorização com dois desfechos pode mostrar linha coberta e ramo parcial, sinalizando que o caso de negação não foi testado.

## Limites e trade-offs
Ramos triviais de verificação de nulo inflam a contagem e podem dominar o denominador; excluir classes de configuração ajuda, mas exige critério para não mascarar código relevante.

## Como verificar
Escolha uma condição de negócio, execute apenas o caminho favorável e confirme no relatório que o ramo restante aparece como não coberto.

## Conexões
- [[jacoco-counters-meaning]] — Veja também: JaCoCo: interpretar os contadores.
- [[jacoco-report-formats]] — Veja também: JaCoCo: escolher o formato de relatório.

## Fontes
- [JaCoCo — Coverage counters](https://www.jacoco.org/jacoco/trunk/doc/counters.html) — definições de instruction, branch, line, complexity, method e class; consultado em 2026-10-02.
- [JaCoCo — jacoco:check](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html) — regras, elementos, limites, ratios e controle de falha do build; consultado em 2026-10-02.
