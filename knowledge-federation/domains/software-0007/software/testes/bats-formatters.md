---
id: software.testes.tranche22.001568
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://bats-core.readthedocs.io/en/latest/usage.html", "https://bats-core.readthedocs.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: pretty, TAP, tap13 e JUnit

## Em uma frase
O Bats escolhe o formato de saída sozinho: no terminal mostra ✓ e ✗ com resumo humano; sem terminal (CI, pipe) despeja TAP. O flag -F/--formatter força pretty, tap, tap13, junit ou um executável absoluto customizado.

## Por que importa
Integrar um framework de shell a agregadores de relatório depende de falar a língua deles; trocar o formatter não muda um único caractere dos testes.

## Como funciona
--report-formatter aceita as mesmas opções e grava o arquivo de relatório no diretório atual ou em --output; no histórico, o flag separou o stdout do arquivo justamente para o formato junit.

## Exemplo
bats --report-formatter junit teste.bats --output /tmp gera /tmp/report.xml com <testsuite name="teste.bats" tests="2" failures="0" .../> e tempos por caso.

## Limites e trade-offs
A linha "T" de timing e o -T do CLI são controles separados do formatter; quem confunde as duas coisas perde horas comparando diffs de relatório.

## Como verificar
Compare byte a byte a saída com --formatter tap contra a saída redirecionada sem terminal e confirme que ambas começam com o plano "1..2".

## Conexões
- [[bats-parallel]] — Veja também: bats-core: --jobs com GNU parallel.
- [[bats-fork-history]] — Veja também: bats-core: do repositório parado ao fork comunitário.

## Fontes
- [Bats-core — Usage](https://bats-core.readthedocs.io/en/latest/usage.html) — opções do CLI, formatters, relatórios e execução paralela; consultado em 2026-10-03.
- [Bats-core — Documentação oficial (página inicial)](https://bats-core.readthedocs.io/en/latest/index.html) — índice: tutorial, instalação, usage, gotchas e FAQ; consultado em 2026-10-03.
