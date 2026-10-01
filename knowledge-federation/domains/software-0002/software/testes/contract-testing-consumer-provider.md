---
id: software.testes.contract-testing.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://docs.pact.io/", "https://docs.pact.io/implementation_guides/python/docs/consumer", "https://docs.pact.io/implementation_guides/javascript/readme"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Consumer-driven contract testing, Teste de contrato]
---

# Teste de contrato entre consumidor e provedor

## Em uma frase
Teste de contrato verifica, de forma isolada, se as mensagens enviadas ou recebidas por dois componentes respeitam as expectativas compartilhadas na fronteira de integração.

## Por que importa
Testes end-to-end cobrem fluxos amplos, mas podem ser lentos, frágeis e caros para diagnosticar. Testes unitários não exercitam o acordo entre serviços. Um contrato executável oferece uma camada intermediária: permite que consumidor e provedor validem compatibilidade sem iniciar todo o ecossistema a cada alteração.

## Como funciona
No modelo consumer-driven usado pelo Pact, o consumidor registra interações que representam os dados e comportamentos de que realmente precisa. O artefato do contrato é compartilhado; o provedor o verifica contra sua implementação. Matchers permitem expressar tipos e padrões quando valores literais seriam rígidos demais. A publicação e a verificação precisam estar ligadas à versão dos aplicativos para que a equipe saiba quais combinações foram testadas.

## Exemplo
Um cliente de usuários precisa de `GET /users/123` com status de sucesso e campos `id` e `name`. O teste do consumidor configura uma resposta simulada e executa o cliente real contra ela. Depois, a verificação do provedor confirma que a API oferece a interação registrada. Se o provedor renomear `name`, a verificação sinaliza a incompatibilidade antes do deploy.

## Limites e trade-offs
O contrato cobre as interações registradas, não todo estado possível da API nem qualidade funcional do produto. Um consumidor que omite uma necessidade não ganha cobertura por usar Pact. Contratos muito estritos podem bloquear mudanças compatíveis; contratos permissivos demais escondem quebras. Mantenha testes de integração, testes de segurança e validações de schema onde cada um for apropriado.

## Como verificar
Confirme que o consumidor gera o contrato a partir dos seus testes, que o provedor o verifica contra a versão candidata e que a CI associa resultados às versões corretas. Inclua ao menos uma mudança compatível e uma incompatível no teste do pipeline para conferir se o sinal de falha funciona.

## Conexões
- [[contrato-openapi-http]] — descrição estática e testes por exemplos respondem a perguntas diferentes.
- [[gates-de-qualidade-no-merge]] — as verificações de contrato precisam bloquear regressões no ponto de integração.
- [[idempotencia-http-api]] — efeitos repetidos também podem fazer parte do comportamento acordado.

## Fontes
- [Pact — Introduction](https://docs.pact.io/) — definição e vocabulário de consumer/provider contract testing; acesso em 2026-10-01.
- [Pact Python — Consumer Testing](https://docs.pact.io/implementation_guides/python/docs/consumer) — geração de interações e artefatos de contrato; acesso em 2026-10-01.
- [Pact JavaScript — Overview](https://docs.pact.io/implementation_guides/javascript/readme) — ciclo de teste do consumidor e verificação; acesso em 2026-10-01.
