---
id: software.testes.tranche14.000836
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
fontes: ["https://laravel.com/framework/docs/13.x/events#testing", "https://laravel.com/framework/docs/13.x/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Laravel: usar Event fake sem ocultar listener necessário

## Em uma frase
Fakes de eventos permitem verificar dispatch sem executar listeners reais que podem enviar notificações, chamar rede ou alterar outros sistemas.

## Por que importa
O teste fica determinístico e comprova o ponto de publicação, mas deixa explícito que não cobriu efeitos do listener.

## Como funciona
Ative o fake antes da operação, use assertions de evento e considere fakes seletivos quando algum listener ainda precisa executar.

## Exemplo
Depois de publicar um pedido, o caso verifica que `OrderPlaced` foi disparado com o identificador correto sem enviar email real.

## Limites e trade-offs
Fake global pode impedir listeners e interações encadeadas que a asserção principal não percebe.

## Como verificar
Adicione teste separado para comportamento essencial do listener e use o mecanismo documentado de fake parcial quando apropriado.

## Conexões
- [[laravel-http-client-fake-prevent-network]] — Veja também: Laravel: impedir tráfego HTTP real com Http::fake.
- [[laravel-queue-fake-job-contract]] — Veja também: Laravel: testar dispatch de job com queue fake.

## Fontes
- [Laravel 13 — Event testing](https://laravel.com/framework/docs/13.x/events#testing) — fakes e assertions de eventos sem depender de listeners externos; consultado em 2026-10-02.
- [Laravel 13 — Testing](https://laravel.com/framework/docs/13.x/testing) — tipos de testes, ambiente testing, banco, helpers e execução paralela; consultado em 2026-10-02.
