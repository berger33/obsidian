---
id: software.testes.tranche14.000781
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/", "https://docs.djangoproject.com/en/6.1/topics/testing/overview/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: usar Client sem iniciar servidor HTTP

## Em uma frase
O `django.test.Client` simula requisições à aplicação sem exigir que um servidor de desenvolvimento esteja rodando.

## Por que importa
Isso mantém rápidos testes de rotas, status, contexto e conteúdo sem incluir protocolo de rede ou navegador real na unidade de teste.

## Como funciona
Instancie `Client` ou use `self.client` de um `TestCase`, envie caminho relativo da aplicação e examine a resposta.

## Exemplo
`client.get("/catalog/")` valida a view e o contexto, enquanto uma URL de domínio externo não representa um alvo atendido pelo projeto.

## Limites e trade-offs
O Client não testa JavaScript ou o comportamento renderizado em browser; essas propriedades pertencem a uma camada de navegador.

## Como verificar
Confira status, redirect chain, template e conteúdo usando assertions do Django e reserve browser tests para comportamento de front-end.

## Conexões
- [[django-testcase-database-isolation]] — Veja também: Django: escolher TestCase quando a asserção acessa o banco.
- [[django-requestfactory-middleware-boundary]] — Veja também: Django: usar RequestFactory para testar a view diretamente.

## Fontes
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
- [Django 6.1 — Writing and running tests](https://docs.djangoproject.com/en/6.1/topics/testing/overview/) — descoberta, execução, seletores, classes de teste e ciclo de banco; consultado em 2026-10-02.
