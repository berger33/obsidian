---
id: software.testes.tranche17.001132
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
fontes: ["https://docs.pact.io/pact_broker/can_i_deploy", "https://docs.pact.io/pact_broker"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: autorizar implantação pelo histórico

## Em uma frase
A consulta de autorização verifica se a versão prestes a ser implantada tem todos os contratos e verificações compatíveis com o ambiente de destino.

## Por que importa
É a verificação que impede que dois serviços evoluam de forma independente e se quebrem justamente no momento da implantação.

## Como funciona
Execute a consulta no pipeline imediatamente antes da implantação, informando aplicativo, versão e ambiente de destino.

## Exemplo
Uma implantação de provedor pode ser bloqueada porque um consumidor registrou contrato novo ainda não verificado pelo provedor.

## Limites e trade-offs
A consulta depende de resultados publicados por ambos os lados e falha quando uma das esteiras não reporta o resultado da verificação.

## Como verificar
Registre uma verificação bem-sucedida, execute a consulta e confirme a autorização; remova o registro e confirme que a consulta bloqueia.

## Conexões
- [[pact-publish-and-broker]] — Veja também: Pact: publicar contratos no intermediário.
- [[pact-versioning-and-selectors]] — Veja também: Pact: controlar versões e seleção de contratos.

## Fontes
- [Pact — can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy) — consulta que autoriza implantação pelo histórico de verificações; consultado em 2026-10-03.
- [Pact — Broker](https://docs.pact.io/pact_broker) — publicação de contratos, histórico e metadados de versão; consultado em 2026-10-03.
