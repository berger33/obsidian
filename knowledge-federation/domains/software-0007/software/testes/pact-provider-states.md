---
id: software.testes.tranche17.001129
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
fontes: ["https://docs.pact.io/implementation_guides/javascript/docs/provider", "https://docs.pact.io/getting_started/how_pact_works"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: preparar estados do provedor

## Em uma frase
Cada interação pode declarar o estado em que o provedor deve estar, e o lado do provedor implementa a preparação correspondente àquele estado.

## Por que importa
Uma verificação sem preparação depende de dados preexistentes e falha de forma imprevisível em ambientes limpos.

## Como funciona
Nomeie os estados pela condição de negócio, implemente a preparação no provedor e mantenha os nomes estáveis entre as partes.

## Exemplo
Um estado pode declarar que existe um pedido aprovado, e o provedor cria esse registro antes de responder à verificação.

## Limites e trade-offs
Estados com nomes vagos acumulam lógica divergente, e a preparação que apaga dados afeta outras verificações em execução.

## Como verificar
Verifique o mesmo contrato em um banco vazio e confirme que a preparação de estado cria os registros necessários.

## Conexões
- [[pact-matching-rules]] — Veja também: Pact: usar correspondência flexível.
- [[pact-provider-verification]] — Veja também: Pact: verificar contratos no provedor.

## Fontes
- [Pact — Provider verification](https://docs.pact.io/implementation_guides/javascript/docs/provider) — verificação do provedor e implementação de estados; consultado em 2026-10-03.
- [Pact — How Pact works](https://docs.pact.io/getting_started/how_pact_works) — fluxo dirigido pelo consumidor, publicação e verificação de contratos; consultado em 2026-10-03.
