---
id: software.testes.tranche14.000782
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/advanced/", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: usar RequestFactory para testar a view diretamente

## Em uma frase
`RequestFactory` cria objetos request para passar diretamente a uma view, sem executar o ciclo de roteamento e middleware.

## Por que importa
Teste focal pode isolar transformação da view, mas deixa explícita a responsabilidade de fornecer atributos que middleware normalmente acrescentaria.

## Como funciona
Crie a requisição com método e caminho, configure manualmente usuário ou sessão necessários e invoque a função ou `as_view()` da classe.

## Exemplo
Uma view que lê `request.user` recebe esse atributo no objeto construído pelo factory antes da chamada direta.

## Limites e trade-offs
RequestFactory não simula client completo nem aplica middleware, autenticação, sessão ou resolução de URL automaticamente.

## Como verificar
Compare o teste focal com pelo menos um teste de integração via Client quando a regra depender do middleware ou da rota.

## Conexões
- [[django-client-without-live-server]] — Veja também: Django: usar Client sem iniciar servidor HTTP.
- [[django-setuptestdata-class-fixture]] — Veja também: Django: reservar setUpTestData para dados imutáveis da classe.

## Fontes
- [Django 6.1 — Advanced testing topics](https://docs.djangoproject.com/en/6.1/topics/testing/advanced/) — RequestFactory, views diretas, middleware e testes de aplicações reutilizáveis; consultado em 2026-10-02.
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
