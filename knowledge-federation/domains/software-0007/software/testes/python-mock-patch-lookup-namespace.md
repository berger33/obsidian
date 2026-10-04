---
id: software.testes.tranche14.000846
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

# Python unittest.mock: aplicar patch no namespace consultado

## Em uma frase
`patch()` substitui um objeto no namespace em que o código sob teste procura o nome, não necessariamente onde a classe foi originalmente definida.

## Por que importa
Patch no módulo errado deixa a dependência real ativa e pode fazer um teste passar por caminho diferente do imaginado.

## Como funciona
Siga os imports do módulo sob teste e patch o símbolo qualificado que sua função resolve durante a execução.

## Exemplo
Se `service.py` importou `Client` em seu próprio namespace, o teste substitui `service.Client`, não somente `library.Client`.

## Limites e trade-offs
Reexport, import tardio e objeto capturado antes do patch podem alterar o ponto efetivo de lookup.

## Como verificar
Faça assertion de chamada no mock e confirme que uma configuração de retorno ou exceção afetou o resultado sob teste.

## Conexões
- [[python-unittest-skip-vs-expected-failure]] — Veja também: Python unittest: distinguir caso indisponível de falha prevista.
- [[python-mock-autospec-interface-check]] — Veja também: Python unittest.mock: restringir mock com autospec.

## Fontes
- [Python 3.14 — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — Mock, patch, autospec, spec_set, calls e escopo de substituições; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
