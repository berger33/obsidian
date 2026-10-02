---
id: software.testes.tranche09.000347
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
fontes: ["https://docs.spring.io/spring-boot/reference/testing/index.html", "https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spring Boot: declarar perfil de teste sem depender do ambiente local

## Em uma frase
Ativar perfil por anotação ou configuração de teste torna explícitas as propriedades usadas durante o carregamento do contexto.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Um perfil herdado de IDE pode conectar suite à infraestrutura errada ou omitir beans presentes na CI.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Defina perfil no teste, controle precedência de propriedades e não armazene credenciais de produção em configuração versionada.

## Exemplo
Teste inicia com perfil `integration`, usa endpoint local descartável e confirma bean de datasource esperado.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. Profiles selecionam configuração mas não isolam serviços externos nem garantem que valores sejam seguros.

## Como verificar
Imprima apenas nomes de perfil e tipo de datasource, rode sem variáveis locais e valide fail-fast para endpoint ausente.

## Conexões
- [[spring-restclient-test-slice-mockserver]] — Veja também: Spring Boot: usar @RestClientTest para cliente HTTP.
- [[spring-webtestclient-mock-vs-server]] — Veja também: Spring Boot: testar WebTestClient em mock e servidor.

## Fontes
- [Spring Boot — Testing](https://docs.spring.io/spring-boot/reference/testing/index.html) — módulos de teste e integração com JUnit Jupiter e AssertJ; consultado em 2026-10-02.
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
