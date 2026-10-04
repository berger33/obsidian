---
id: software.testes.tranche12.000627
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.DocTest.html", "https://ex-unit.hexdocs.pm/ExUnit.Assertions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: transformar exemplos de documentação em testes

## Em uma frase
`doctest` extrai exemplos formatados na documentação de um módulo e os executa como verificações de comportamento.

## Por que importa
Executar exemplos evita que instruções de uso fiquem desatualizadas enquanto o código evolui e oferece exemplos concretos de chamadas públicas.

## Como funciona
Inclua `doctest NomeDoModulo` no caso apropriado, escreva blocos compatíveis com o formato esperado e mantenha efeitos externos fora dos exemplos que devem rodar repetidamente.

## Exemplo
Um módulo de conversão pode documentar uma chamada simples com resultado esperado; o doctest confirma que o exemplo continua válido após refatoração.

## Limites e trade-offs
Exemplos de documentação são uma amostra de interface, não substituem casos para erros, limites e combinações de estado que não cabem no texto introdutório.

## Como verificar
Rode o caso de doctest junto da suite e confirme que cada bloco destacado está sendo descoberto e executado pelo ExUnit.

## Conexões
- [[exunit-capture-io-isolamento]] — Veja também: ExUnit: capturar IO com segurança em testes async.
- [[exunit-tags-select-filters]] — Veja também: ExUnit: selecionar execução com tags e filtros.

## Fontes
- [ExUnit 1.20.4 — ExUnit.DocTest](https://ex-unit.hexdocs.pm/ExUnit.DocTest.html) — extração e execução de exemplos em documentação Elixir; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Assertions](https://ex-unit.hexdocs.pm/ExUnit.Assertions.html) — assertions e diagnósticos de expressões de teste; consultado em 2026-10-02.
