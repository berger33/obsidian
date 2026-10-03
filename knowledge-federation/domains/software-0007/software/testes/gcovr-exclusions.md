---
id: software.testes.tranche22.001654
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
fontes: ["https://gcovr.com/en/stable/manpage.html", "https://gcovr.com/en/stable/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: excluir linha, branch e função

## Em uma frase
A referência traz um arsenal de exclusão declarativa: --exclude-unreachable-branches retira branches de linhas sem código útil (o tal dead code gerado pelo compilador), --exclude-function-lines ignora linhas de definição de função, e --exclude-lines-by-pattern / --exclude-branches-by-pattern operam por regex sobre a linha.

## Por que importa
C++ é o campeão do branch que ninguém escreveu — construtores implícitos, exceções sintéticas; sem exclusões, a métrica pune o padrão de linguagem em vez de medir o teste.

## Como funciona
Além dos patterns, o gcovr honra os marcadores de exclusão no próprio código (estilo LCOV/GCOV), e --no-markers desliga esse reconhecimento.

## Exemplo
Cada uma dessas opções declara na própria doc um Config key(s) homônimo — dá para fixar as regras num arquivo de configuração em vez de repetir 6 flags no Makefile.

## Limites e trade-offs
Excluir demais é autoindulgência métrica: --exclude-lines-by-pattern amplo some com linhas de erro reais; a exclusão precisa de revisão como todo ignore.

## Como verificar
Compare um mesmo build com e sem --exclude-unreachable-branches e conte a diferença de branches reportados num arquivo cheio de construtores default.

## Conexões
- [[gcovr-output-formats]] — Veja também: gcovr: quinze formatos, uma flag cada.
- [[gcovr-config-file]] — Veja também: gcovr: configuração em arquivo, chave por opção.

## Fontes
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
