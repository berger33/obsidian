---
id: software.testes.tranche09.000344
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

# Spring Boot: não presumir rollback do cliente em RANDOM_PORT

## Em uma frase
Em teste transacional com RANDOM_PORT, cliente e servidor executam em threads separadas e usam transações diferentes.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Rollback da transação do método de teste não desfaz automaticamente escrita que o request HTTP fez no servidor.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Use limpeza explícita, fixture de banco ou transação do lado do servidor e escolha ambiente de teste descartável.

## Exemplo
Teste HTTP cria registro via aplicação em porta aleatória; teardown consulta e remove o registro apesar do rollback do teste cliente.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. O comportamento muda entre mock e servidor real; isolamento do banco deve ser avaliado separadamente.

## Como verificar
Após request, abra nova conexão e confirme persistência ou limpeza do estado antes de concluir a suíte.

## Conexões
- [[spring-testcontext-cache-dirties-context]] — Veja também: Spring TestContext: controlar estado em ApplicationContext cacheado.
- [[spring-testresttemplate-status-assertions]] — Veja também: Spring Boot: afirmar status com TestRestTemplate explicitamente.

## Fontes
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
- [Spring Boot — Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html) — módulos de teste focados e slices auto-configurados; consultado em 2026-10-02.
