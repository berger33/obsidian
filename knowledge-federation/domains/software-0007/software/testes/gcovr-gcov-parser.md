---
id: software.testes.tranche22.001656
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

# gcovr: o parser do gcov por trás do número

## Em uma frase
O guia dedica páginas próprias ao gcov parser e ao "Compiling for Coverage" porque a fidelidade do relatório depende de como o gcovr interpreta os .gcov/.gcda/.gcno e dos flags com que chama o gcov.

## Por que importa
Discrepância de contagem entre lcov, gcov direto e gcovr raramente é bug de um só lado: é definição de "linha executável" — a doc admite isso ao responder por que C++ tem tantos branches descobertos.

## Como funciona
A FAQ lista as perguntas que o parser enfrenta: diferença entre lcov e gcovr, branches inflados em C++, arquivos nunca instrumentados ausentes do relatório e as opções usadas para invocar o gcov.

## Exemplo
"Why are uncovered files not reported?" na FAQ é o ponto de partida para quem exige zero-coverage no medidor — comportamento que tem flag própria de rastreamento.

## Limites e trade-offs
O parser acompanha formatos que mudam entre versões do GCC; uma nota "funcional com meu gcov" só vale para a dupla gcovr+GCC testada pela sua versão da doc.

## Como verificar
Abra as duas páginas do guia (compiling e gcov parser) e confira qual variante de chamada do gcov a sua versão usa hoje.

## Conexões
- [[gcovr-config-file]] — Veja também: gcovr: configuração em arquivo, chave por opção.
- [[gcovr-cookbook]] — Veja também: gcovr: receitas de build difícil.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
