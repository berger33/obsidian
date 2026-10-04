---
id: software.testes.tranche09.000340
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

# Spring Boot: escolher @WebMvcTest ou @SpringBootTest

## Em uma frase
@WebMvcTest foca a camada MVC, enquanto @SpringBootTest carrega a aplicação conforme configuração e ambiente escolhidos.

## Por que importa
O suporte de teste Spring oferece contextos reduzidos e testes com servidor real; cada modalidade cobre camadas e transações diferentes. Subir todo o contexto para testar binding ou status de controller aumenta acoplamento e tempo sem necessariamente cobrir mais comportamento relevante.

## Como funciona
Escolha módulo e anotação pela fronteira sob teste, configure ambiente mínimo e valide explicitamente status, dependências e rollback observável. Use slice MVC para contrato HTTP da camada web com colaboradores controlados e teste de aplicação completa quando integração de contexto é objetivo.

## Exemplo
Teste de controller verifica validação e status com beans necessários; outro teste inicia aplicação para validar configuração integrada.

## Limites e trade-offs
Auto-configuração depende de módulos no classpath e versão Spring Boot; contexto de mock e servidor executam em threads e transações diferentes. Slice pode omitir beans que o controller realmente exige e precisa de configuração explícita para colaboração.

## Como verificar
Compare beans carregados, tempo e fronteira executada e inclua um caso de integração para wiring essencial.

## Conexões
- [[spring-mockmvc-vs-random-port]] — Veja também: Spring Boot: distinguir MockMvc de servidor em porta aleatória.

## Fontes
- [Spring Boot — Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html) — módulos de teste focados e slices auto-configurados; consultado em 2026-10-02.
- [Spring Boot — Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) — MockMvc, servidor real, slices e testes transacionais; consultado em 2026-10-02.
