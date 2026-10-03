---
id: software.testes.tranche18.001251
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
fontes: ["https://allurereport.org/docs/categories/", "https://allurereport.org/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Allure: classificar falhas por categoria

## Em uma frase
O arquivo de configuração define categorias por status e por expressões sobre mensagem e rastro, agrupando falhas segundo a origem provável.

## Por que importa
A classificação automática acelera a triagem e separa defeito de produto, problema de teste e instabilidade de ambiente.

## Como funciona
Declare categorias com nomes claros e padrões que correspondam a mensagens conhecidas, mantendo o arquivo versionado com o projeto.

## Exemplo
Uma categoria pode agrupar falhas por tempo esgotado em dependência externa, separando-as de erros de asserção.

## Limites e trade-offs
Padrões muito amplos classificam falhas de naturezas diferentes no mesmo grupo, e categorias desatualizadas deixam de reconhecer os erros atuais.

## Como verificar
Introduza um erro de tipo conhecido e confirme que ele aparece na categoria correspondente do relatório.

## Conexões
- [[allure-attachments]] — Veja também: Allure: anexar evidências ao resultado.
- [[allure-severity-and-annotations]] — Veja também: Allure: declarar severidade e metadados.

## Fontes
- [Allure Report — Categories](https://allurereport.org/docs/categories/) — classificação automática de falhas por status e padrões; consultado em 2026-10-03.
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
