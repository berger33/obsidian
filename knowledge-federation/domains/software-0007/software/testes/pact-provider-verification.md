---
id: software.testes.tranche17.001130
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
fontes: ["https://docs.pact.io/implementation_guides/javascript/docs/provider", "https://docs.pact.io/pact_broker"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: verificar contratos no provedor

## Em uma frase
A ferramenta de verificação lê os contratos publicados, executa cada interação contra o serviço real e reporta o resultado por contrato.

## Por que importa
A verificação confirma que o provedor atende às expectativas registradas pelos consumidores, sem exigir que os consumidores estejam em execução.

## Como funciona
Aponte a verificação para o endereço do serviço, informe as fontes de contrato e implemente os ganchos de estado antes de rodar.

## Exemplo
O provedor de pagamentos pode verificar os contratos dos aplicativos cliente durante o próprio pipeline de publicação.

## Limites e trade-offs
Contratos obsoletos no broker fazem a verificação falhar por expectativas que ninguém mais usa, e a filtragem por consumidor precisa ser compreendida.

## Como verificar
Aprove um provedor alterado em um campo que o contrato verifica e confirme que a verificação falha indicando a interação afetada.

## Conexões
- [[pact-provider-states]] — Veja também: Pact: preparar estados do provedor.
- [[pact-publish-and-broker]] — Veja também: Pact: publicar contratos no intermediário.

## Fontes
- [Pact — Provider verification](https://docs.pact.io/implementation_guides/javascript/docs/provider) — verificação do provedor e implementação de estados; consultado em 2026-10-03.
- [Pact — Broker](https://docs.pact.io/pact_broker) — publicação de contratos, histórico e metadados de versão; consultado em 2026-10-03.
