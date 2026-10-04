---
id: software.testes.tranche14.000843
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

# Python unittest: registrar cleanup junto à criação do recurso

## Em uma frase
`addCleanup()` registra funções que rodam em ordem inversa de registro ao finalizar o caso, inclusive quando `setUp()` falha depois do registro.

## Por que importa
Cleanup associado imediatamente à aquisição reduz vazamentos em exceções e evita depender de um `tearDown()` que talvez não rode para setup incompleto.

## Como funciona
Registre a liberação logo após abrir arquivo, socket ou recurso temporário e empilhe cleanups na ordem correspondente à dependência.

## Exemplo
Um teste abre servidor, registra `server.stop`, prepara client e registra `client.close`; a pilha finaliza client antes do servidor.

## Limites e trade-offs
Limpeza em LIFO só é segura se cada callback puder concluir e reportar falhas sem impedir o restante da política do runner.

## Como verificar
Provoque falha intermediária no setup e verifique que recursos previamente registrados foram fechados em ordem reversa.

## Conexões
- [[python-unittest-setuptestdata-lifecycle]] — Veja também: Python unittest: escolher setup por caso ou por classe.
- [[python-unittest-assert-raises-regex]] — Veja também: Python unittest: afirmar tipo e mensagem relevante de exceção.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
