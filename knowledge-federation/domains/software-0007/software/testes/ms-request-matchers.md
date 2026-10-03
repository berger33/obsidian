---
id: software.testes.tranche20.001380
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://www.mock-server.com/mock_server/creating_expectations.html", "https://github.com/mock-server/mockserver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: corresponder pedidos com precisão

## Em uma frase
Os correspondentes cobrem método, caminho, consulta, cabeçalhos, cookies e corpo, com comparação exata, por padrão ou por esquema.

## Por que importa
A precisão da correspondência determina se o teste detecta o pedido errado ou o aceita como equivalente.

## Como funciona
Combine os campos relevantes, prefira correspondência por esquema em corpo estruturado e evite expressões amplas sem necessidade.

## Exemplo
Uma expectativa pode exigir o envio no caminho de criação com corpo contendo os dois campos obrigatórios.

## Limites e trade-offs
Correspondência ampla aceita pedidos que deveriam falhar, e a comparação campo a campo de corpo inteiro quebra com campos gerados.

## Como verificar
Altere um campo do corpo e confirme que o pedido deixa de corresponder à expectativa, seguindo para outra resposta.

## Conexões
- [[ms-expectations]] — Veja também: MockServer: criar expectativas de resposta.
- [[ms-verification]] — Veja também: MockServer: verificar o que foi recebido.

## Fontes
- [MockServer — Criar expectativas](https://www.mock-server.com/mock_server/creating_expectations.html) — correspondentes de pedido, ações, prioridade e cenários; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
