---
id: software.testes.tranche12.000624
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

# ExUnit: habilitar `async: true` com estado independente

## Em uma frase
Com `async: true`, casos de teste podem executar em paralelo com outros módulos, enquanto testes do mesmo módulo permanecem seriais.

## Por que importa
A concorrência diminui tempo de suíte quando os casos são independentes, mas gravações em estado global ou recursos remotos compartilhados tornam o resultado não determinístico.

## Como funciona
Marque somente módulos seguros para execução concorrente e substitua nomes fixos, tabelas globais e diretórios comuns por recursos exclusivos por teste.

## Exemplo
Dois módulos podem testar parsers puros em paralelo, enquanto a suite que altera a mesma conta de staging fica síncrona ou usa identidades separadas.

## Limites e trade-offs
Um teste que passa sozinho pode competir por registro ou configuração de sistema quando rodado ao lado de outro módulo async.

## Como verificar
Repita a suite com maior concorrência, procure colisões e desative async apenas para os casos que realmente compartilham estado global.

## Conexões
- [[exunit-on-exit-separar-cleanup]] — Veja também: ExUnit: usar `on_exit` sem presumir o processo do teste.
- [[exunit-case-template-reuso]] — Veja também: ExUnit: compartilhar convenções com `CaseTemplate`.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit](https://ex-unit.hexdocs.pm/ExUnit.html) — configuração de max_cases, seed e execução paralela por módulo; consultado em 2026-10-02.
