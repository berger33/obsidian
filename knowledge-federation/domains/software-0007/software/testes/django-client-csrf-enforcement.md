---
id: software.testes.tranche14.000789
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

# Django: ativar verificação CSRF ao testar requests

## Em uma frase
O cliente Django desativa verificações CSRF por padrão, então um POST aceito pelo Client não prova sozinho que a proteção foi aplicada.

## Por que importa
Teste que ignora a checagem pode deixar uma regressão de configuração ou integração de segurança sem sinal.

## Como funciona
Crie um `Client` com `enforce_csrf_checks=True` para os casos que devem verificar token e compare uma submissão legítima com uma sem token.

## Exemplo
Um teste pode esperar rejeição do POST sem token e sucesso após obter cookie e encaminhar token válido conforme o fluxo da aplicação.

## Limites e trade-offs
O modo explícito de CSRF muda o contrato do Client e exige configurar o request de acordo com o middleware real.

## Como verificar
Faça ao menos uma tentativa negativa e outra positiva para demonstrar que o teste diferencia política de bloqueio de indisponibilidade da view.

## Conexões
- [[django-test-discovery-and-labels]] — Veja também: Django: combinar descoberta padrão e labels explícitos.

## Fontes
- [Django 6.1 — Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/) — Client, TestCase, LiveServerTestCase, assertions, e-mail e settings; consultado em 2026-10-02.
- [Django 6.1 — Writing and running tests](https://docs.djangoproject.com/en/6.1/topics/testing/overview/) — descoberta, execução, seletores, classes de teste e ciclo de banco; consultado em 2026-10-02.
