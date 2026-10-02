---
id: software.testes.tranche09.000343
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
fontes: ["https://docs.spring.io/spring-framework/reference/testing/testcontext-framework.html", "https://docs.spring.io/spring-boot/reference/testing/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spring TestContext: controlar estado em ApplicationContext cacheado

## Em uma frase
Spring TestContext pode reutilizar ApplicationContext entre classes compatíveis para reduzir custo; @DirtiesContext o remove do cache quando o contexto foi realmente alterado.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Singleton mutável alterado por um teste pode vazar para o próximo embora cada método tenha fixtures diferentes.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Prefira beans stateless e cleanup explícito; reserve @DirtiesContext para mudanças que não podem ser revertidas e limite a anotação ao menor escopo.

## Exemplo
Um bean de configuração impossível de restaurar é alterado; a classe marca o contexto sujo após validar esse cenário.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. Reconstruir o ApplicationContext aumenta custo e não remove estado de banco, filesystem ou serviço externo.

## Como verificar
Execute classes em ordens diferentes, confirme novo contexto somente no caso alterado e observe bean e recursos externos separadamente.

## Conexões
- [[spring-datajpatest-database-boundary]] — Veja também: Spring Boot: delimitar @DataJpaTest e o banco usado.
- [[spring-transactional-test-real-server-threads]] — Veja também: Spring Boot: não presumir rollback do cliente em RANDOM_PORT.

## Fontes
- [Spring Framework — Testing](https://docs.spring.io/spring-framework/reference/testing/testcontext-framework.html) — TestContext, contexto de aplicação e infraestrutura de teste; consultado em 2026-10-02.
- [Spring Boot — Testing](https://docs.spring.io/spring-boot/reference/testing/index.html) — módulos de teste e integração com JUnit Jupiter e AssertJ; consultado em 2026-10-02.
