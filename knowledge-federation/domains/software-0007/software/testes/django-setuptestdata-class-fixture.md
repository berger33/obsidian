---
id: software.testes.tranche14.000783
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase", "https://docs.djangoproject.com/en/6.1/topics/testing/overview/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: reservar setUpTestData para dados imutáveis da classe

## Em uma frase
`setUpTestData()` prepara dados de banco uma vez por classe `TestCase`, ao passo que `setUp()` roda antes de cada método de teste.

## Por que importa
Dados caros e compartilhados reduzem o custo da suite, enquanto estado que muda por caso deve continuar isolado.

## Como funciona
Crie em `setUpTestData` apenas objetos que cada teste possa tratar como referência estável; mantenha mutações locais em cada teste e siga as regras de isolamento documentadas.

## Exemplo
Uma classe de catálogo cria produtos base em `setUpTestData` e cada método cria seu próprio pedido para evitar compartilhar alterações.

## Limites e trade-offs
A otimização não autoriza modificar estado compartilhado esperando que Django clone todo tipo de objeto arbitrário com a mesma semântica.

## Como verificar
Rode métodos em ordens diferentes e confirme que um teste que altera a instância não muda premissas dos demais.

## Conexões
- [[django-requestfactory-middleware-boundary]] — Veja também: Django: usar RequestFactory para testar a view diretamente.
- [[django-live-server-browser-boundary]] — Veja também: Django: escolher LiveServerTestCase para cliente externo.

## Fontes
- [Django 6.1 — TestCase](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase) — isolamento transacional, fixtures e preparação de dados em TestCase; consultado em 2026-10-02.
- [Django 6.1 — Writing and running tests](https://docs.djangoproject.com/en/6.1/topics/testing/overview/) — descoberta, execução, seletores, classes de teste e ciclo de banco; consultado em 2026-10-02.
