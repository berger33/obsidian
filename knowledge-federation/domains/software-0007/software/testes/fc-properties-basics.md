---
id: software.testes.tranche20.001429
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://fast-check.dev/docs/introduction/getting-started/", "https://github.com/dubzzz/fast-check"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# fast-check: declarar propriedades

## Em uma frase
Uma propriedade combina geradores de entrada com um predicado que deve valer para todos os valores produzidos.

## Por que importa
A verificação por propriedade cobre a regra geral, em vez de exemplos escolhidos a dedo, encontrando entradas que o autor não imaginou.

## Como funciona
Declare o gerador de cada entrada, escreva o predicado como regra geral e execute a propriedade pelo asseridor da biblioteca.

## Exemplo
A propriedade pode afirmar que reverter duas vezes uma lista devolve a lista original para qualquer conteúdo gerado.

## Limites e trade-offs
Escrever o predicado como cópia da implementação não verifica nada, e afirmar algo que não é regra do domínio gera falhas sem significado.

## Como verificar
Introduza um defeito na função sob teste e confirme que a propriedade encontra um contraexemplo.

## Conexões
- [[fc-arbitraries]] — Veja também: fast-check: gerar dados com geradores.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — repositório oficial](https://github.com/dubzzz/fast-check) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
