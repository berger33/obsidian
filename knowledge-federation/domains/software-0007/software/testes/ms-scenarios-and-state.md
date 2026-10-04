---
id: software.testes.tranche20.001386
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

# MockServer: modelar fluxos com estado

## Em uma frase
Cenários permitem que a resposta mude conforme as interações anteriores, avançando o estado a cada correspondência.

## Por que importa
Fluxos com estado verificam sequências reais de chamada, como primeira tentativa falha e repetição bem-sucedida.

## Como funciona
Declare as etapas do cenário, avance o estado pelas transições e finalize o caso com o estado esperado.

## Exemplo
O cenário pode responder indisponível na primeira chamada de confirmação e sucesso na segunda, verificando a repetição do cliente.

## Limites e trade-offs
Cenários paralelos que compartilham o mesmo nome interferem entre si, e esquecer de reiniciar o estado contamina a execução seguinte.

## Como verificar
Reinicie o cenário e repita o fluxo, confirmando que o comportamento se repete do primeiro estado.

## Conexões
- [[ms-tests-and-junit]] — Veja também: MockServer: integrar com a suíte de testes.
- [[ms-diagnostics-and-logs]] — Veja também: MockServer: investigar falhas com os registros.

## Fontes
- [MockServer — Criar expectativas](https://www.mock-server.com/mock_server/creating_expectations.html) — correspondentes de pedido, ações, prioridade e cenários; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
