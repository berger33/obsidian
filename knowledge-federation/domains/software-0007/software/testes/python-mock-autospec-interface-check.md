---
id: software.testes.tranche14.000847
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
fontes: ["https://docs.python.org/3/library/unittest.mock.html", "https://docs.python.org/3/library/unittest.mock-examples.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Python unittest.mock: restringir mock com autospec

## Em uma frase
`autospec` cria mocks guiados pela assinatura ou interface do objeto real e pode rejeitar atributos que não existem.

## Por que importa
Mocks permissivos aceitam typos e APIs inventadas que produção nunca oferece, enfraquecendo confiança no contrato testado.

## Como funciona
Use `create_autospec` ou `patch(..., autospec=True)` quando a dependência real pode fornecer uma spec útil.

## Exemplo
Um mock de client com autospec falha imediatamente se código chama `fetch_user` com argumento ou nome de método incompatível.

## Limites e trade-offs
A spec pode não refletir atributos criados dinamicamente em `__init__` ou objetos com interfaces construídas em runtime.

## Como verificar
Compare o mock com a API pública da dependência e execute caso real em teste de integração quando a assinatura não basta.

## Conexões
- [[python-mock-patch-lookup-namespace]] — Veja também: Python unittest.mock: aplicar patch no namespace consultado.
- [[python-isolated-asyncio-testcase-lifecycle]] — Veja também: Python unittest: isolar ciclo de vida de caso assíncrono.

## Fontes
- [Python 3.14 — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — Mock, patch, autospec, spec_set, calls e escopo de substituições; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
