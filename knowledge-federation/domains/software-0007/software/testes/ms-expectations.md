---
id: software.testes.tranche20.001379
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

# MockServer: criar expectativas de resposta

## Em uma frase
Uma expectativa declara o pedido que deve corresponder e a ação a executar, com limites opcionais de número de usos, validade e prioridade.

## Por que importa
A declaração explícita do pedido esperado documenta o contrato usado pelo teste e evita respostas genéricas que escondem divergências.

## Como funciona
Declare a correspondência pelo pedido, escolha a ação de resposta e limite a quantidade de usos quando o cenário exigir.

## Exemplo
Uma expectativa pode responder ao pedido de sessão com o código de redirecionamento e o cabeçalho de localização esperados.

## Limites e trade-offs
Sem limite de usos, a expectativa atende pedidos posteriores que deveriam seguir outro caminho, e ordem de prioridade mal definida faz a expectativa errada responder primeiro.

## Como verificar
Envie um pedido que não corresponde e confirme que a resposta devolvida não é a da expectativa declarada.

## Conexões
- [[ms-request-matchers]] — Veja também: MockServer: corresponder pedidos com precisão.

## Fontes
- [MockServer — Criar expectativas](https://www.mock-server.com/mock_server/creating_expectations.html) — correspondentes de pedido, ações, prioridade e cenários; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
