---
id: software.testes.tranche17.001141
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
fontes: ["https://pkg.go.dev/github.com/stretchr/testify/mock", "https://github.com/stretchr/testify"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testify: casar argumentos de forma flexível

## Em uma frase
Os dublês aceitam funções de correspondência nos argumentos, permitindo casar por tipo ou por parte do valor em vez de exigir igualdade exata.

## Por que importa
Valores gerados pelo código sob teste, como identificadores e datas, impedem comparação literal e escondem o que realmente importa verificar.

## Como funciona
Use correspondência por tipo para campos variáveis e correspondência parcial quando apenas parte do argumento for relevante ao caso.

## Exemplo
A expectativa de um evento publicado pode casar com qualquer data e exigir que o identificador do pedido seja o mesmo do cenário.

## Limites e trade-offs
Correspondências amplas aceitam qualquer coisa e tornam a expectativa decorativa, então o critério precisa refletir o que o caso verifica.

## Como verificar
Mude o valor do campo verificado pela correspondência e confirme que a expectativa falha ao final da execução.

## Conexões
- [[testify-mock-expectations]] — Veja também: Testify: declarar expectativas de chamada.
- [[testify-mock-generation]] — Veja também: Testify: gerar dublês a partir de interfaces.

## Fontes
- [Testify — Mock package](https://pkg.go.dev/github.com/stretchr/testify/mock) — expectativas de chamada, correspondência de argumentos e verificação final; consultado em 2026-10-03.
- [Testify — repositório oficial](https://github.com/stretchr/testify) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
