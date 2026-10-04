---
id: software.testes.tranche14.000780
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/overview/", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: escolher TestCase quando a asserção acessa o banco

## Em uma frase
`django.test.TestCase` executa cada teste com isolamento transacional e é a base adequada para a maioria dos casos que consultam ou alteram o banco.

## Por que importa
Usar `unittest.TestCase` para operações de ORM pode deixar dados compartilhados e fazer a ordem da suite influenciar o resultado.

## Como funciona
Herde de `TestCase` para testes comuns de modelos e views; reserve `TransactionTestCase` para comportamentos que dependem de commit, rollback ou transações reais.

## Exemplo
Um teste de criação de pedido usa `TestCase` e cria seus registros de apoio dentro da fixture do próprio caso.

## Limites e trade-offs
`TestCase` não substitui toda semântica real de commit; testes de `on_commit` e transações especiais podem precisar de outra classe ou helper.

## Como verificar
Execute o teste isolado e junto da suite em ordem alterada, verificando que dados do caso não vazam para outro teste.

## Conexões
- [[django-client-without-live-server]] — Veja também: Django: usar Client sem iniciar servidor HTTP.

## Fontes
- [Django 6.1 — Writing and running tests](https://docs.djangoproject.com/en/6.1/topics/testing/overview/) — descoberta, execução, seletores, classes de teste e ciclo de banco; consultado em 2026-10-02.
- [Django 6.1 — TestCase](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase) — isolamento transacional, fixtures e preparação de dados em TestCase; consultado em 2026-10-02.
