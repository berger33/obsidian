---
id: software.testes.tranche14.000841
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

# Python unittest: usar subTest para variações que compartilham contexto

## Em uma frase
`subTest()` marca uma subexecução com parâmetros durante o mesmo método e permite identificar qual combinação falhou.

## Por que importa
Tabelas de dados pequenas podem compartilhar setup e ainda produzir diagnóstico por input sem criar classe ou método repetido para cada linha.

## Como funciona
Itere sobre casos e envolva cada assertion em `self.subTest` com identificadores estáveis, mantendo setup comum fora do loop.

## Exemplo
Um método testa vários formatos de moeda e inclui `currency` e `amount` nos parâmetros do subtest.

## Limites e trade-offs
Subtest não é isolamento completo nem processo independente; mutação de estado dentro de uma iteração pode contaminar a próxima.

## Como verificar
Introduza uma falha para uma combinação e confira se o runner informa contexto sem perder o resultado das outras combinações.

## Conexões
- [[python-unittest-discovery-names]] — Veja também: Python unittest: alinhar nomes de arquivos à descoberta.
- [[python-unittest-setuptestdata-lifecycle]] — Veja também: Python unittest: escolher setup por caso ou por classe.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
