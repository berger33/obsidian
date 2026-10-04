---
id: software.testes.tranche09.000349
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.spring.io/spring-boot/reference/testing/test-modules.html", "https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spring Boot: delimitar @GraphQlTest e integração GraphQL

## Em uma frase
O módulo de teste GraphQL fornece uma slice dedicada à camada GraphQL, com escopo diferente da aplicação completa.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Mockar resolvers pode validar mapeamento e resposta sem exercitar datasource, autenticação integrada ou transporte HTTP.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Use slice para execução de operações e wiring GraphQL selecionado; complemente com teste de aplicação nas fronteiras que importam.

## Exemplo
Slice executa query GraphQL contra controller/resolver preparado; smoke test separado valida endpoint HTTP e autenticação completa.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. Auto-configuração varia conforme versão e dependências e não equivale a contrato externo publicado.

## Como verificar
Liste beans disponíveis, envie operação válida/inválida e verifique quais integrações ficaram fora do contexto.

## Conexões
- [[spring-webtestclient-mock-vs-server]] — Veja também: Spring Boot: testar WebTestClient em mock e servidor.

## Fontes
- [Spring Boot — Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html) — módulos de teste focados e slices auto-configurados; consultado em 2026-10-02.
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
