---
id: software.testes.tranche09.000341
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
fontes: ["https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html", "https://docs.spring.io/spring-boot/reference/testing/test-utilities.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spring Boot: distinguir MockMvc de servidor em porta aleatória

## Em uma frase
MockMvc exercita a pilha MVC em ambiente de mock, enquanto RANDOM_PORT inicia servidor embutido e recebe tráfego HTTP real no processo.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Os dois testes têm limites diferentes para sockets, filtros, serialização e comportamento de transações.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Use MockMvc para feedback de endpoint sem porta e cliente HTTP com RANDOM_PORT para validar integração pelo servidor.

## Exemplo
Teste compara cabeçalho e body por MockMvc; smoke test separado chama URI da porta aleatória em aplicação iniciada.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. HTTP real acrescenta custo e pode depender de porta, startup e serviços do ambiente.

## Como verificar
Verifique no teste qual client foi injetado, se havia servidor e quais filtros/configurações atravessaram a requisição.

## Conexões
- [[spring-webmvctest-vs-springboottest]] — Veja também: Spring Boot: escolher @WebMvcTest ou @SpringBootTest.
- [[spring-datajpatest-database-boundary]] — Veja também: Spring Boot: delimitar @DataJpaTest e o banco usado.

## Fontes
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
- [Spring Boot — Test utilities](https://docs.spring.io/spring-boot/reference/testing/test-utilities.html) — RestTestClient e TestRestTemplate em testes de integração; consultado em 2026-10-02.
