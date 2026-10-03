---
id: software.testes.tranche18.001189
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://google.github.io/googletest/primer.html", "https://github.com/google/googletest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: comparar valores com veredito claro

## Em uma frase
As macros de comparação cobrem igualdade, desigualdade, comparações numéricas, texto e valores de ponto flutuante com tolerância declarada.

## Por que importa
A mensagem da macro de comparação mostra os dois valores, e a tolerância explícita evita tratar imprecisão de ponto flutuante como defeito.

## Como funciona
Escolha a comparação adequada ao tipo, informe a tolerância em cálculos com ponto flutuante e evite comparar estruturas complexas sem descrever a diferença.

## Exemplo
Um cálculo de média pode ser verificado com tolerância definida, reconhecendo que a representação binária não é exata.

## Limites e trade-offs
Comparar ponteiros por identidade quando o teste pretendia comparar conteúdo é um engano que passa despercebido.

## Como verificar
Ajuste o valor esperado para fora da tolerância e confirme que a mensagem apresenta a diferença observada.

## Conexões
- [[googletest-assertions]] — Veja também: GoogleTest: escolher entre asserção fatal e não fatal.
- [[googletest-fixtures]] — Veja também: GoogleTest: compartilhar preparação com fixtures.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — macros de caso, asserções, comparações e execução; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
