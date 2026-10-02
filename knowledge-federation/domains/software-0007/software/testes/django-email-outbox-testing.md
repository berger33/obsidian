---
id: software.testes.tranche14.000786
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/#email-services", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: inspecionar mensagens sem enviar e-mail real

## Em uma frase
Durante testes, Django fornece uma caixa de saída em memória para observar mensagens enviadas pelo código da aplicação.

## Por que importa
Validar destinatário, assunto e conteúdo sem serviço SMTP evita efeitos externos, dados de usuários reais e dependência de rede.

## Como funciona
Execute a ação dentro do test runner e examine a coleção `mail.outbox`, verificando quantidade e campos relevantes da mensagem.

## Exemplo
Um fluxo de recuperação de senha pode confirmar que uma mensagem foi gerada para o endereço de teste sem tentar entregá-la fora do processo.

## Limites e trade-offs
A caixa em memória confirma geração e conteúdo, não entrega, reputação, servidor SMTP ou renderização final em todos os clientes.

## Como verificar
Limpe ou isole mensagens por caso e mantenha uma verificação de entrega real em ambiente de integração quando isso fizer parte do risco.

## Conexões
- [[django-assert-num-queries-scope]] — Veja também: Django: usar assertNumQueries como orçamento local.
- [[django-override-settings-scope]] — Veja também: Django: limitar override_settings ao teste que o requer.

## Fontes
- [Django 6.1 — Testing tools and email](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#email-services) — backend de e-mail em memória e inspeção das mensagens durante testes; consultado em 2026-10-02.
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
