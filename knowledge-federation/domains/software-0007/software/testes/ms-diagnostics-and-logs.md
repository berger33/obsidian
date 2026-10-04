---
id: software.testes.tranche20.001387
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
fontes: ["https://www.mock-server.com/mock_server/verification.html", "https://www.mock-server.com/mock_server/creating_expectations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: investigar falhas com os registros

## Em uma frase
O serviço expõe os pedidos recebidos, as expectativas registradas e as mensagens de erro de correspondência, consultáveis durante a execução.

## Por que importa
Consultar o registro do que chegou ao serviço distingue rapidamente falha do sistema sob teste de expectativa incorreta.

## Como funciona
Consulte os pedidos registrados ao investigar falha de correspondência, leia a mensagem de erro que lista as expectativas avaliadas e ajuste a expectativa.

## Exemplo
Quando um pedido não corresponde a nenhuma expectativa, a resposta de erro indica o motivo e o conteúdo recebido.

## Limites e trade-offs
Ignorar a mensagem de erro leva a ajustes por tentativa, e registros volumosos sem filtro dificultam encontrar o pedido relevante.

## Como verificar
Provoque uma falha de correspondência de propósito e use a mensagem para corrigir a expectativa em uma única tentativa.

## Conexões
- [[ms-scenarios-and-state]] — Veja também: MockServer: modelar fluxos com estado.
- [[ms-limits-and-practices]] — Veja também: MockServer: reconhecer limites.

## Fontes
- [MockServer — Verificar pedidos](https://www.mock-server.com/mock_server/verification.html) — verificação por quantidade e por sequência; consultado em 2026-10-03.
- [MockServer — Criar expectativas](https://www.mock-server.com/mock_server/creating_expectations.html) — correspondentes de pedido, ações, prioridade e cenários; consultado em 2026-10-03.
