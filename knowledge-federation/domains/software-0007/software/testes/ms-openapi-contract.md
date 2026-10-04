---
id: software.testes.tranche20.001384
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
fontes: ["https://mock-server.com/mock_server/using_openapi.html", "https://github.com/mock-server/mockserver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: usar especificação de contrato

## Em uma frase
Uma especificação de interface pode gerar expectativas automaticamente e servir como correspondente para verificar se os pedidos recebidos respeitam o contrato.

## Por que importa
Usar o contrato como fonte de expectativas mantém a simulação e a verificação alinhadas à definição que o time publica.

## Como funciona
Carregue a especificação, gere as expectativas quando a simulação for util e use-a como correspondente em verificações de conformidade.

## Exemplo
O teste pode verificar que os pedidos reais enviados à interface respeitam os campos e códigos declarados na especificação.

## Limites e trade-offs
Especificações desatualizadas geram expectativas que não refletem a interface vigente, e o contrato verificado não garante que a implementação real se comporta como declarado.

## Como verificar
Envie um pedido com campo fora do contrato e confirme que a correspondência por especificação o rejeita.

## Conexões
- [[ms-proxy-and-record-replay]] — Veja também: MockServer: gravar tráfego com proxy.
- [[ms-tests-and-junit]] — Veja também: MockServer: integrar com a suíte de testes.

## Fontes
- [MockServer — OpenAPI e WSDL](https://mock-server.com/mock_server/using_openapi.html) — geração de expectativas e verificação por contrato; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
