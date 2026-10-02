---
id: software.testes.tranche12.000628
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
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.Case.html", "https://ex-unit.hexdocs.pm/ExUnit.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: selecionar execução com tags e filtros

## Em uma frase
Tags associadas a casos ou grupos adicionam metadata ao contexto e podem ser incluídas ou excluídas pela configuração do ExUnit.

## Por que importa
Filtros criam uma suite operacional sem copiar arquivos e ajudam a separar casos externos, lentos ou dependentes de plataforma.

## Como funciona
Atribua tags com `@tag` ou metadados de módulo, configure inclusão e exclusão no comando de teste e lembre que inclusões não restringem a suite enquanto tudo ainda estiver incluído.

## Exemplo
Um job padrão pode excluir `:external`, enquanto um job com credenciais seleciona essa categoria e mantém os demais testes no fluxo habitual.

## Limites e trade-offs
Uma tag aplicada ao módulo pode atingir todos os testes, inclusive casos que não precisam da dependência indicada pelo nome.

## Como verificar
Inspecione quantos testes são executados com cada combinação de filtros e confirme que nenhum job obrigatório termina com seleção vazia.

## Conexões
- [[exunit-doctest-documentacao]] — Veja também: ExUnit: transformar exemplos de documentação em testes.
- [[exunit-seed-cases-concorrencia]] — Veja também: ExUnit: reproduzir ordem com seed e controlar `max_cases`.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit](https://ex-unit.hexdocs.pm/ExUnit.html) — configuração de max_cases, seed e execução paralela por módulo; consultado em 2026-10-02.
