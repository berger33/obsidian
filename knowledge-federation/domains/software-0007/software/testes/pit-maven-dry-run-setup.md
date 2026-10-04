---
id: software.testes.tranche12.000597
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://pitest.org/quickstart/maven/", "https://pitest.org/quickstart/commandline/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: usar dry run ao configurar a análise

## Em uma frase
O modo dry run, documentado desde PIT 1.17.3, reúne cobertura e gera mutantes sem executar a suíte contra cada mutação.

## Por que importa
Essa etapa permite validar descoberta de classes, filtros e geração de mutantes antes de pagar o custo completo de mutation testing.

## Como funciona
Ative `dryRun` só para diagnóstico inicial ou manutenção da configuração, examine erros de build e remova o modo ao solicitar resultados de sensibilidade dos testes.

## Exemplo
Uma pipeline pode usar dry run numa etapa rápida para detectar mudança de filtros que eliminou todos os alvos antes de agendar o job completo.

## Limites e trade-offs
Dry run não calcula se as assertions matariam os mutantes, portanto seu sucesso não deve ser comunicado como mutation score aprovado.

## Como verificar
Compare explicitamente os relatórios e a linha de comando configurada para ter certeza de que a execução de qualidade não manteve o modo de diagnóstico ligado.

## Conexões
- [[pit-incremental-history-assumptions]] — Veja também: PIT: tratar histórico incremental como otimização.
- [[pit-maven-goal-relatorio]] — Veja também: PIT: executar `mutationCoverage` e guardar o relatório.

## Fontes
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
- [PIT — Command Line Quick Start](https://pitest.org/quickstart/commandline/) — filtros de target classes/tests, execução e parâmetros de linha de comando; consultado em 2026-10-02.
