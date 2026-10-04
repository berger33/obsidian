---
id: software.testes.tranche14.000838
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
fontes: ["https://laravel.com/framework/docs/13.x/mail", "https://laravel.com/framework/docs/13.x/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Laravel: verificar Mailable sem entregar e-mail externo

## Em uma frase
`Mail::fake()` registra mailables enviados para que testes verifiquem destinatário e conteúdo sem acessar transporte externo.

## Por que importa
Separar composição do email de entrega evita que execução comum envie mensagens reais ou dependa de fornecedor de mail.

## Como funciona
Ative o fake antes do fluxo, use assertions de envio e complemente com assertions de conteúdo quando o contrato exigir.

## Exemplo
Um caso confirma que uma confirmação de pedido foi enviada ao endereço gerado e inspeciona assunto ou view do mailable.

## Limites e trade-offs
O fake não valida aceitação SMTP, reputação, layout em cliente ou entrega na caixa postal.

## Como verificar
Mantenha testes de transporte fora da suite rápida e use conta ou sink controlado apenas em ambiente de integração seguro.

## Conexões
- [[laravel-queue-fake-job-contract]] — Veja também: Laravel: testar dispatch de job com queue fake.
- [[laravel-parallel-test-database-tokens]] — Veja também: Laravel: isolar bancos de testes paralelos por processo.

## Fontes
- [Laravel 13 — Mail testing](https://laravel.com/framework/docs/13.x/mail) — fakes de mail, assertions de envio e testes de conteúdo de Mailable; consultado em 2026-10-02.
- [Laravel 13 — Testing](https://laravel.com/framework/docs/13.x/testing) — tipos de testes, ambiente testing, banco, helpers e execução paralela; consultado em 2026-10-02.
