---
id: software.testes.tranche15.000884
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Spec.html", "https://docs.seattlerb.org/minitest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: usar a DSL de spec

## Em uma frase
`Minitest::Spec` oferece `describe` e `it` com hooks `before`, `after` e `around`, além de matchers de expectativa para testes escritos em estilo de especificação.

## Por que importa
A DSL muda a forma de expressar o caso, mas não o motor de execução; misturar estilos sem critério dificulta a leitura e a padronização da suíte.

## Como funciona
Use spec quando o time preferir linguagem de comportamento por exemplo e mantenha classes `Minitest::Test` quando a estrutura for mais simples.

## Exemplo
`describe Conta do; before { @conta = Conta.new }; it('inicia zerada') { _( @conta.saldo ).must_equal 0 }; end` mostra exemplo com hook.

## Limites e trade-offs
Hooks compartilhados em blocos aninhados podem preparar estado mais amplo do que o caso precisa, e a ordem de execução entre níveis precisa ser aprendida para evitar surpresas.

## Como verificar
Execute um exemplo que depende de hook aninhado e outro que depende apenas do hook externo e confirme que cada um recebeu o estado esperado.

## Conexões
- [[minitest-setup-teardown]] — Veja também: Minitest: preparar e limpar cada caso.
- [[minitest-mock-and-stub]] — Veja também: Minitest: isolar colaboradores com mock e stub.

## Fontes
- [Minitest — Spec](https://docs.seattlerb.org/minitest/Minitest/Spec.html) — DSL describe/it, hooks before, after e around e matchers de expectativa; consultado em 2026-10-02.
- [Minitest — README](https://docs.seattlerb.org/minitest/) — visão geral do projeto, plugins e formas de execução; consultado em 2026-10-02.
