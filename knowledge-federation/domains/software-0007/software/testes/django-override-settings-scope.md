---
id: software.testes.tranche14.000787
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.override_settings", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: limitar override_settings ao teste que o requer

## Em uma frase
`override_settings` substitui temporariamente valores de settings e restaura o contexto ao final do escopo gerenciado.

## Por que importa
Uma configuração global alterada pode contaminar testes vizinhos ou criar uma diferença entre execução isolada e suite inteira.

## Como funciona
Aplique o decorator ou context manager à menor unidade que precisa do valor, e use `modify_settings` quando a operação apropriada for alterar uma lista.

## Exemplo
Um teste de upload pode reduzir `FILE_UPLOAD_MAX_MEMORY_SIZE` apenas durante sua execução, sem deixar a configuração ativa para outras classes.

## Limites e trade-offs
Nem todo consumidor reage a mudanças de settings em runtime; inicializações em cache podem exigir limpar cache ou configurar antes da construção.

## Como verificar
Faça uma asserção dentro do escopo e outra depois dele para comprovar que o valor original foi recuperado.

## Conexões
- [[django-email-outbox-testing]] — Veja também: Django: inspecionar mensagens sem enviar e-mail real.
- [[django-test-discovery-and-labels]] — Veja também: Django: combinar descoberta padrão e labels explícitos.

## Fontes
- [Django 6.1 — override_settings](https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.override_settings) — substituição temporária de settings durante testes; consultado em 2026-10-02.
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
