---
id: software.testes.tranche14.000788
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
fontes: ["https://docs.djangoproject.com/en/6.1/topics/testing/overview/", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Django: combinar descoberta padrão e labels explícitos

## Em uma frase
O comando `manage.py test` descobre por padrão módulos que seguem o padrão de nomes de teste e aceita labels para reduzir o escopo.

## Por que importa
Convenções reconhecíveis evitam que arquivos com lógica de teste fiquem fora da suite por nome ou localização acidental.

## Como funciona
Mantenha arquivos `test*.py` no pacote de aplicação ou forneça `--pattern`; use label de pacote, módulo, classe ou método para executar um alvo específico.

## Exemplo
`python manage.py test orders.tests.test_api.OrderApiTests` roda apenas a classe indicada e deixa a seleção registrada na linha de comando.

## Limites e trade-offs
Um resultado focado não comprova descoberta total; um padrão customizado pode ampliar ou estreitar o escopo sem alterar os arquivos.

## Como verificar
Compare discovery da suite completa antes de merge e verifique contagem e casos esperados no output do runner.

## Conexões
- [[django-override-settings-scope]] — Veja também: Django: limitar override_settings ao teste que o requer.
- [[django-client-csrf-enforcement]] — Veja também: Django: ativar verificação CSRF ao testar requests.

## Fontes
- [Django 6.1 — Writing and running tests](https://docs.djangoproject.com/en/6.1/topics/testing/overview/) — descoberta, execução, seletores, classes de teste e ciclo de banco; consultado em 2026-10-02.
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
