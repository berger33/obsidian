---
id: software.testes.tranche14.000845
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
fontes: ["https://docs.python.org/3/library/unittest.html", "https://docs.python.org/3/library/unittest.mock-examples.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Python unittest: distinguir caso indisponível de falha prevista

## Em uma frase
Skip remove temporariamente um teste da execução com motivo; `expectedFailure` marca que o caso deve falhar e registra sucesso inesperado como resultado distinto.

## Por que importa
A distinção evita esconder uma regressão como dependência ausente ou tratar uma correção bem-sucedida como falha normal.

## Como funciona
Use skip para pré-condição ambiental documentada e expected failure somente para defeito conhecido com referência e plano de remoção.

## Exemplo
Uma checagem dependente de sistema operacional pode pular com razão explícita; um caso de issue aberta pode ser esperado falhar por prazo definido.

## Limites e trade-offs
Skip permanente e expected failure sem responsável podem permanecer invisíveis por muito tempo.

## Como verificar
Monitore contagem de skips e sucessos inesperados e remova marcadores quando a causa deixar de existir.

## Conexões
- [[python-unittest-assert-raises-regex]] — Veja também: Python unittest: afirmar tipo e mensagem relevante de exceção.
- [[python-mock-patch-lookup-namespace]] — Veja também: Python unittest.mock: aplicar patch no namespace consultado.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
