---
id: software.testes.tranche17.001126
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
fontes: ["https://docs.pact.io/getting_started/how_pact_works", "https://github.com/pact-foundation/pact-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: entender o contrato dirigido pelo consumidor

## Em uma frase
O consumidor escreve expectativas sobre as requisições que faz e as respostas que espera, e esse registro vira um artefato verificável pelo provedor.

## Por que importa
Contratos documentados do lado do provedor descrevem a intenção de quem oferece o serviço, mas não o que os consumidores realmente usam.

## Como funciona
Escreva apenas as interações que o consumidor de fato executa, mantendo o contrato pequeno e focado no que é necessário.

## Exemplo
Um consumidor de catálogo pode declarar que precisa dos campos de nome e preço, sem exigir todos os atributos que o provedor devolve.

## Limites e trade-offs
Contratos que exigem o corpo inteiro travam a evolução do provedor e criam manutenção constante a cada campo novo irrelevante.

## Como verificar
Compare o contrato com o código do consumidor e verifique se cada campo declarado é realmente lido por algum trecho da aplicação.

## Conexões
- [[pact-consumer-test-dsl]] — Veja também: Pact: escrever a interação de teste.

## Fontes
- [Pact — How Pact works](https://docs.pact.io/getting_started/how_pact_works) — fluxo dirigido pelo consumidor, publicação e verificação de contratos; consultado em 2026-10-03.
- [Pact — repositório oficial](https://github.com/pact-foundation/pact-js) — implementação de referência em JavaScript e exemplos; consultado em 2026-10-03.
