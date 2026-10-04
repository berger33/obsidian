---
id: software.testes.tranche09.000348
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
fontes: ["https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html", "https://docs.spring.io/spring-boot/reference/testing/test-modules.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spring Boot: testar WebTestClient em mock e servidor

## Em uma frase
WebTestClient pode ser usado com ambiente mock e, quando configurado, com servidor rodando para exercitar o protocolo HTTP integrado.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Teste que muda de modalidade sem perceber pode afirmar cobertura de socket ou startup que não ocorreu.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Documente ambiente, autoconfigure o cliente adequado e separe testes de contrato de controller dos smoke tests reais.

## Exemplo
Um teste usa WebFlux mock para respostas reativas; outro usa porta aleatória e verifica acesso pelo serviço iniciado.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. Disponibilidade do módulo e configuração dependem da pilha WebFlux e do Spring Boot adotado.

## Como verificar
Inspecione annotations e logs de inicialização e confirme se há porta ativa no teste de integração.

## Conexões
- [[spring-active-profiles-test-configuration]] — Veja também: Spring Boot: declarar perfil de teste sem depender do ambiente local.
- [[spring-graphql-test-slice-boundary]] — Veja também: Spring Boot: delimitar @GraphQlTest e integração GraphQL.

## Fontes
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
- [Spring Boot — Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html) — módulos de teste focados e slices auto-configurados; consultado em 2026-10-02.
