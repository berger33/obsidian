---
id: software.testes.tranche14.000785
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: usar assertNumQueries como orçamento local

## Em uma frase
`assertNumQueries` verifica quantas queries SQL foram executadas dentro de um bloco ou por uma operação específica do teste.

## Por que importa
A asserção detecta regressões de N+1 e acessos desnecessários sem substituir medição de performance de ponta a ponta.

## Como funciona
Envolva apenas a operação cujo custo quer proteger e use o número esperado compatível com a fixture e a configuração do banco.

## Exemplo
Em uma página de lista, envolver a chamada de renderização com limite pequeno pode revelar que cada linha passou a buscar sua relação separadamente.

## Limites e trade-offs
O total varia com backend, middleware, cache e preparação de dados; contar queries sem cenário estável produz teste frágil.

## Como verificar
Registre versão do framework, backend e ponto exato da operação, depois verifique se a falha aponta a mudança de consulta.

## Conexões
- [[django-live-server-browser-boundary]] — Veja também: Django: escolher LiveServerTestCase para cliente externo.
- [[django-email-outbox-testing]] — Veja também: Django: inspecionar mensagens sem enviar e-mail real.

## Fontes
- [Django 6.1 — assertNumQueries](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries) — asserção contextual do número de consultas SQL executadas; consultado em 2026-10-02.
- [Django 6.1 — TestCase](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase) — isolamento transacional, fixtures e preparação de dados em TestCase; consultado em 2026-10-02.
