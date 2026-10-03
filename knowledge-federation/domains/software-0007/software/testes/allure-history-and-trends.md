---
id: software.testes.tranche18.001253
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
fontes: ["https://allurereport.org/docs/", "https://github.com/allure-framework/allure2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Allure: acompanhar histórico e tendências

## Em uma frase
Ao manter relatórios anteriores acessíveis, o gerador calcula tendências de resultado e duração entre execuções.

## Por que importa
A tendência distingue variação normal de regressão recorrente e mostra a evolução da estabilidade ao longo do tempo.

## Como funciona
Preserve o diretório de histórico entre execuções, gere a tendência na esteira e use a duração como sinal de degradação.

## Exemplo
Um caso que passa a durar o dobro em várias execuções seguidas pode indicar regressão de desempenho antes de falhar.

## Limites e trade-offs
Histórico corrompido ou parcial distorce a tendência, e a comparação entre execuções com conjuntos de testes diferentes confunde a leitura.

## Como verificar
Compare a tendência antes e depois de uma mudança ampla e confirme que a variação observada faz sentido.

## Conexões
- [[allure-severity-and-annotations]] — Veja também: Allure: declarar severidade e metadados.
- [[allure-retries-and-flaky]] — Veja também: Allure: registrar reexecuções e instabilidade.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
