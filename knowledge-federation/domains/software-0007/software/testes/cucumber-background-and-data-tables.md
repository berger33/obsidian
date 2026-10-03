---
id: software.testes.tranche17.001091
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://cucumber.io/docs/cucumber/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: compartilhar contexto e tabelas

## Em uma frase
O antecedente repete um contexto no início de cada cenário da funcionalidade, e tabelas nos passos organizam dados estruturados de forma legível.

## Por que importa
Contexto comum escrito uma vez reduz duplicação, e tabelas dão forma a listas e mapas sem quebrar a leitura do cenário.

## Como funciona
Mantenha o antecedente curto, descreva apenas a pré-condição necessária e prefira tabelas com cabeçalho quando os dados têm campos nomeados.

## Exemplo
Um antecedente pode autenticar um usuário, e um passo seguinte pode receber tabela com itens do pedido e quantidades.

## Limites e trade-offs
Antecedentes extensos tornam cada cenário mais lento e escondem dependências; tabelas muito grandes sugerem que o dado deveria vir de arquivo externo.

## Como verificar
Remova temporariamente o antecedente e confirme que os cenários falham por falta de contexto, evidenciando a dependência declarada.

## Conexões
- [[cucumber-tags-and-expressions]] — Veja também: Cucumber: filtrar execuções com etiquetas.
- [[cucumber-parallel-execution]] — Veja também: Cucumber: executar cenários em paralelo.

## Fontes
- [Cucumber — Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — funcionalidades, cenários, antecedentes, esquemas de cenário e tabelas; consultado em 2026-10-03.
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
