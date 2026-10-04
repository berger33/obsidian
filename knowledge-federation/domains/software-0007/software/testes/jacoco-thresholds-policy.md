---
id: software.testes.tranche15.000898
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html", "https://www.jacoco.org/jacoco/trunk/doc/counters.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: tratar cobertura como política, não como meta

## Em uma frase
Cobertura descreve o que foi executado e não prova qualidade das asserções, portanto o limite deve expressar uma política de proteção contra regressão.

## Por que importa
Perseguir percentuais altos como objetivo incentiva testes sem verificação significativa e desloca esforço de cenários de risco para linhas triviais.

## Como funciona
Defina limites por área crítica, acompanhe a tendência entre revisões e use o número para levantar perguntas, não para encerrar a discussão sobre qualidade.

## Exemplo
Uma regra que impede queda de cobertura em relação à revisão anterior costuma ser mais útil que um piso global único para toda a base de código.

## Limites e trade-offs
Métricas podem ser infladas por exclusões e ramos triviais, e um build reprovado por décimos pode esconder a ausência de testes para um risco funcional relevante.

## Como verificar
Revise as regras junto do time, proponha uma mudança de limite e verifique se a política resultante ainda protege os módulos críticos identificados.

## Conexões
- [[jacoco-excludes-filtering]] — Veja também: JaCoCo: excluir código gerado da medição.
- [[jacoco-build-integration]] — Veja também: JaCoCo: integrar a medição ao ciclo de build.

## Fontes
- [JaCoCo — jacoco:check](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html) — regras, elementos, limites, ratios e controle de falha do build; consultado em 2026-10-02.
- [JaCoCo — Coverage counters](https://www.jacoco.org/jacoco/trunk/doc/counters.html) — definições de instruction, branch, line, complexity, method e class; consultado em 2026-10-02.
