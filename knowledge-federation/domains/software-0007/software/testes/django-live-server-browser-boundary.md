---
id: software.testes.tranche14.000784
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.LiveServerTestCase", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: escolher LiveServerTestCase para cliente externo

## Em uma frase
`LiveServerTestCase` inicia um servidor de teste em thread para permitir que Selenium ou outro cliente real interaja com a aplicação.

## Por que importa
A camada externa cobre navegação e protocolo que `Client` em memória não representa, conectando o caso à experiência web observável.

## Como funciona
Use o host e a porta disponibilizados pela classe de teste e sincronize o browser com o estado da aplicação.

## Exemplo
Um teste de login com JavaScript pode abrir no navegador o endereço fornecido pelo servidor vivo e confirmar a próxima tela após enviar o formulário.

## Limites e trade-offs
O servidor e browser adicionam tempo, dependência de driver e concorrência; não são necessários para cada regra de view.

## Como verificar
Execute smoke tests em browser separado dos testes de Client e confira teardown do servidor mesmo quando uma assertion falha.

## Conexões
- [[django-setuptestdata-class-fixture]] — Veja também: Django: reservar setUpTestData para dados imutáveis da classe.
- [[django-assert-num-queries-scope]] — Veja também: Django: usar assertNumQueries como orçamento local.

## Fontes
- [Django 6.1 — LiveServerTestCase](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.LiveServerTestCase) — servidor de teste em thread para clientes externos e interação ao vivo; consultado em 2026-10-02.
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
