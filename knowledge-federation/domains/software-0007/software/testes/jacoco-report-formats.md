---
id: software.testes.tranche15.000893
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
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html", "https://www.jacoco.org/jacoco/trunk/doc/counters.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: escolher o formato de relatório

## Em uma frase
O goal de relatório gera HTML para leitura humana e pode produzir XML e CSV para consumo por outras ferramentas, todos derivados do mesmo arquivo de execução.

## Por que importa
Um formato só atende uma finalidade: HTML explica, mas não é consumível por pipeline; XML e CSV integram, mas não mostram o código destacado.

## Como funciona
Gere HTML para revisão local e XML para o pipeline, configurando diretórios de fontes para que o relatório HTML possa destacar as linhas cobertas.

## Exemplo
Sem as fontes configuradas, o HTML mostra cobertura por classe sem exibir o código destacado, o que dificulta localizar exatamente o ramo descoberto.

## Limites e trade-offs
Relatórios diferentes gerados de fontes desatualizadas apontam para linhas que mudaram; a geração precisa acompanhar a mesma revisão do código compilado.

## Como verificar
Gere os dois formatos a partir do mesmo arquivo de execução e confirme que os totais de cobertura coincidem entre eles.

## Conexões
- [[jacoco-branch-vs-line]] — Veja também: JaCoCo: usar cobertura de ramos para decisões.
- [[jacoco-check-rules-limits]] — Veja também: JaCoCo: verificar cobertura com regras.

## Fontes
- [JaCoCo — jacoco:report](https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html) — formatos de relatório, fontes, agregação e configuração do goal; consultado em 2026-10-02.
- [JaCoCo — Coverage counters](https://www.jacoco.org/jacoco/trunk/doc/counters.html) — definições de instruction, branch, line, complexity, method e class; consultado em 2026-10-02.
