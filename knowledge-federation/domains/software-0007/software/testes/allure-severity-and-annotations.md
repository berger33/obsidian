---
id: software.testes.tranche18.001252
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

# Allure: declarar severidade e metadados

## Em uma frase
Anotações registram gravidade, descrição, vínculo com requisito e agrupamento por épico, funcionalidade e história.

## Por que importa
Metadados permitem filtrar o relatório por risco e ligar a execução à documentação de produto.

## Como funciona
Declare severidade conforme o impacto da falha, associe o caso ao requisito correspondente e mantenha a nomenclatura de agrupamento estável.

## Exemplo
Um caso de fluxo de pagamento pode ser marcado com gravidade alta e vinculado ao requisito que ele verifica.

## Limites e trade-offs
Severidade atribuída de forma uniforme não ajuda a priorizar, e vínculos quebrados levam a relatórios que não encontram o requisito.

## Como verificar
Filtre o relatório pela severidade mais alta e confirme que os casos retornados são os que realmente criticam a operação.

## Conexões
- [[allure-categories]] — Veja também: Allure: classificar falhas por categoria.
- [[allure-history-and-trends]] — Veja também: Allure: acompanhar histórico e tendências.

## Fontes
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
- [Allure — repositório oficial](https://github.com/allure-framework/allure2) — gerador de relatório, exemplos e documentação do projeto; consultado em 2026-10-03.
