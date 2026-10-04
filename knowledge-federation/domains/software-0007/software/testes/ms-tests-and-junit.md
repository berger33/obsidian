---
id: software.testes.tranche20.001385
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
fontes: ["https://github.com/mock-server/mockserver", "https://www.mock-server.com/mock_server/creating_expectations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: integrar com a suíte de testes

## Em uma frase
O serviço pode ser iniciado durante a suíte, com terminadores e regras de ciclo de vida que sobem e derrubam o servidor por classe ou por execução.

## Por que importa
O ciclo de vida controlado pelo teste garante isolamento entre execuções e dispensa ambiente preparado manualmente.

## Como funciona
Inicie o serviço na preparação, registre expectativas no início de cada caso e zere o estado ao final do caso ou da classe.

## Exemplo
Uma classe de teste de integração pode subir o serviço, registrar as expectativas do caso e limpar tudo antes do caso seguinte.

## Limites e trade-offs
Estado residual entre casos faz expectativas antigas responderem pedidos novos, e servidor não finalizado mantém portas ocupadas.

## Como verificar
Execute a classe inteira e confirme que cada caso passa isoladamente e em ordem invertida.

## Conexões
- [[ms-openapi-contract]] — Veja também: MockServer: usar especificação de contrato.
- [[ms-scenarios-and-state]] — Veja também: MockServer: modelar fluxos com estado.

## Fontes
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
- [MockServer — Criar expectativas](https://www.mock-server.com/mock_server/creating_expectations.html) — correspondentes de pedido, ações, prioridade e cenários; consultado em 2026-10-03.
