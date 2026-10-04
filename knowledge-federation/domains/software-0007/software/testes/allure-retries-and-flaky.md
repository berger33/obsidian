---
id: software.testes.tranche18.001254
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

# Allure: registrar reexecuções e instabilidade

## Em uma frase
O relatório mostra tentativas do mesmo caso, distinguindo o resultado final do histórico de execuções intermediárias.

## Por que importa
Reexecuções automáticas escondem instabilidade se não forem visíveis, e o registro explícito permite investigar casos intermitentes.

## Como funciona
Registre cada tentativa como resultado próprio, marque o caso instável quando houver divergência entre tentativas e acompanhe a frequência.

## Exemplo
Um caso que falha na primeira tentativa e passa na segunda aparece marcado, orientando a investigação da causa.

## Limites e trade-offs
Aceitar reexecuções como norma elimina o sinal de instabilidade, e casos mascarados por repetição acumulam dívida de diagnóstico.

## Como verificar
Force uma falha na primeira tentativa e confirme que o relatório mostra as duas execuções com resultados distintos.

## Conexões
- [[allure-history-and-trends]] — Veja também: Allure: acompanhar histórico e tendências.
- [[allure-suites-and-behaviors]] — Veja também: Allure: navegar por suítes e comportamentos.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
