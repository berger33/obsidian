---
id: software.testes.tranche22.001651
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
fontes: ["https://gcovr.com/en/stable/getting-started.html", "https://gcovr.com/en/stable/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: três passos do build ao relatório

## Em uma frase
O fluxo oficial tem três movimentos: recompilar com --coverage -g -O0, rodar a suíte de testes para gerar os arquivos brutos de cobertura e então invocar gcovr, que imprime o relatório tabular no console.

## Por que importa
--coverage habilita as duas metades da instrumentação do GCC (-fprofile-arcs -ftest-coverage), o -g traz o mapeamento para fontes reais e o -O0 evita que otimizações embaralhem linhas contadas.

## Como funciona
Para HTML há duas portas documentadas: gcovr --html-details coverage.html e gcovr --html-nested coverage.html; o nested gera um relatório por arquivo e, adicionalmente, um por diretório.

## Exemplo
O exemplo de build separado diz "cd build; gcovr -r .." — o -r aponta a raiz do projeto quando os gcda não moram junto das fontes.

## Limites e trade-offs
Sem o -r correto em out-of-source builds, o relatório sai vazio ou com caminhos quebrados; a flag não é cosmética nesse arranjo.

## Como verificar
Compile um main.c minúsculo com --coverage, rode-o, e veja o sumário tabular listar a porcentagem de linhas antes e depois de um printf extra.

## Conexões
- [[gcovr-what-it-is]] — Veja também: gcovr: o gcov resumido em texto e XML.
- [[gcovr-root-filter]] — Veja também: gcovr: a raiz é o filtro padrão.

## Fontes
- [gcovr — Getting Started](https://gcovr.com/en/stable/getting-started.html) — flags de build, -r, html-details e html-nested; consultado em 2026-10-03.
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
