---
id: software.testes.tranche14.000844
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
fontes: ["https://docs.python.org/3/library/unittest.html", "https://docs.python.org/3/library/unittest.mock.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Python unittest: afirmar tipo e mensagem relevante de exceção

## Em uma frase
`assertRaisesRegex` verifica que uma chamada lança o tipo de exceção esperado e que sua mensagem combina com uma expressão regular.

## Por que importa
Testar somente que algo falhou pode aceitar erro de validação diferente daquele previsto pelo contrato.

## Como funciona
Use como context manager ao redor da operação e mantenha o padrão da mensagem específico o bastante para distinguir motivo sem fixar detalhes efêmeros.

## Exemplo
Um parser inválido deve levantar `ValueError` com fragmento de mensagem que identifique formato não suportado.

## Limites e trade-offs
Expressões regulares amplas podem aceitar exceção incorreta; textos completos costumam ser frágeis quando mensagens mudam por versão.

## Como verificar
Crie casos com exceção correta, tipo errado e mensagem divergente para comprovar a força da assertion.

## Conexões
- [[python-unittest-addcleanup-lifo]] — Veja também: Python unittest: registrar cleanup junto à criação do recurso.
- [[python-unittest-skip-vs-expected-failure]] — Veja também: Python unittest: distinguir caso indisponível de falha prevista.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — Mock, patch, autospec, spec_set, calls e escopo de substituições; consultado em 2026-10-02.
