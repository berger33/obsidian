---
id: software.testes.tranche14.000840
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

# Python unittest: alinhar nomes de arquivos à descoberta

## Em uma frase
`unittest` descobre métodos pelo padrão `test` e o discovery recursivo usa convenções de nomes de arquivos e pacotes.

## Por que importa
Um teste que não segue o padrão esperado pode existir no repositório sem fazer parte da suite executada.

## Como funciona
Use `python -m unittest` ou `TestLoader.discover` com diretório, padrão e top-level adequados ao layout do projeto.

## Exemplo
Um pacote organiza `test_models.py` e `test_api.py` e confirma que ambos aparecem na descoberta antes de merge.

## Limites e trade-offs
Importabilidade e estrutura de pacotes afetam descoberta; mudar diretório raiz pode alterar nomes qualificados dos módulos.

## Como verificar
Inspecione a lista de testes descobertos e compare uma execução direcionada por módulo com a suite completa.

## Conexões
- [[python-unittest-subtest-dimensions]] — Veja também: Python unittest: usar subTest para variações que compartilham contexto.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock examples](https://docs.python.org/3/library/unittest.mock-examples.html) — padrões de patch, criação de mocks e assertions de chamadas; consultado em 2026-10-02.
