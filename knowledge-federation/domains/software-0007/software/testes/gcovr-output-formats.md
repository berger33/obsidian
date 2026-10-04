---
id: software.testes.tranche22.001653
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
fontes: ["https://gcovr.com/en/stable/index.html", "https://gcovr.com/en/stable/manpage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: quinze formatos, uma flag cada

## Em uma frase
A matriz oficial de saídas cobre --txt (default) e --html/--html-details/--html-nested para humanos, --csv, --json e --json-summary para dados, --markdown e --markdown-summary para PRs, e os dialetos de portal: --clover, --cobertura, --coveralls, --jacoco, --lcov e --sonarqube.

## Por que importa
Times poliglotas padronizam um único formato de ingestão (Cobertura ou JaCoCo, digamos) entre C, JS e JVM; gcovr fala todos os seis XML/JSON sem plugin extra.

## Como funciona
--html-template-dir completa o quadro para quem quer o HTML com a cara da empresa: uma custom set of Jinja2 templates plugável por flag.

## Exemplo
O guia tem página própria de "Multiple Output Formats" — dá para emitir sumário em console, Cobertura para o CI e JSON para um dashboard na mesma execução.

## Limites e trade-offs
Nem todo portal lê todo dialeto igualmente: --sonarqube é output próprio, não o genérico de plugin, e há campos (branches) que só aparecem conforme a flag de contagem usada.

## Como verificar
Emita --json e --json-summary no mesmo run e compare as duas chaves de percentual para entender o que cada portal consome.

## Conexões
- [[gcovr-root-filter]] — Veja também: gcovr: a raiz é o filtro padrão.
- [[gcovr-exclusions]] — Veja também: gcovr: excluir linha, branch e função.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
