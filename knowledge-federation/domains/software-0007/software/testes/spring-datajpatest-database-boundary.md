---
id: software.testes.tranche09.000342
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

# Spring Boot: delimitar @DataJpaTest e o banco usado

## Em uma frase
@DataJpaTest configura uma fatia de persistência e pode usar banco embutido conforme dependências e configuração do projeto.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Diferenças de dialeto, constraint ou comportamento de produção podem passar despercebidas quando teste usa outro banco.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Valide repositories rapidamente na slice e inclua execução direcionada no banco compatível com produção para contratos críticos.

## Exemplo
Teste de repository usa datasource configurado pelo perfil de CI e outro job confirma migração e consulta no PostgreSQL do produto.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. A presença de banco embutido e rollback dependem da configuração; não assuma substituição ou transação sem verificar.

## Como verificar
Inspecione datasource efetivo no contexto, aplique migrations e valide constraints que diferem entre bancos suportados.

## Conexões
- [[spring-mockmvc-vs-random-port]] — Veja também: Spring Boot: distinguir MockMvc de servidor em porta aleatória.
- [[spring-testcontext-cache-dirties-context]] — Veja também: Spring TestContext: controlar estado em ApplicationContext cacheado.

## Fontes
- [Spring Boot — Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html) — módulos de teste focados e slices auto-configurados; consultado em 2026-10-02.
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
