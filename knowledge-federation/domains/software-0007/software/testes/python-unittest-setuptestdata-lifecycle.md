---
id: software.testes.tranche14.000842
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

# Python unittest: escolher setup por caso ou por classe

## Em uma frase
`setUp()` e `tearDown()` executam em torno de cada método de teste, enquanto setup de classe é compartilhado por métodos da mesma classe.

## Por que importa
Fixture por método simplifica isolamento; setup compartilhado pode economizar recurso caro, mas introduz estado mutável entre casos.

## Como funciona
Prefira setup local para dados que mudam e reserve `setUpClass` para infraestrutura imutável ou cara com teardown simétrico.

## Exemplo
Uma conexão de servidor de teste pode ser aberta uma vez por classe, enquanto cada método cria sua própria entidade de domínio.

## Limites e trade-offs
Se `setUpClass` falha antes de concluir, o ciclo de `tearDownClass` não equivale a cleanup registrado depois de cada etapa.

## Como verificar
Execute testes em ordem alterada e confirme que setup compartilhado não carrega dados escritos pelo método anterior.

## Conexões
- [[python-unittest-subtest-dimensions]] — Veja também: Python unittest: usar subTest para variações que compartilham contexto.
- [[python-unittest-addcleanup-lifo]] — Veja também: Python unittest: registrar cleanup junto à criação do recurso.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
