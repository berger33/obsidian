---
id: software.testes.tranche16.001017
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "https://github.com/GoogleChrome/lighthouse-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Lighthouse CI: definir limites numéricos e agregação

## Em uma frase
Asserções podem fixar pontuação mínima ou valor máximo de métrica, com escolha do método de agregação entre as repetições.

## Por que importa
O método de agregação muda a leitura: otimista escolhe o melhor caso, pessimista o pior e mediano o valor central da série.

## Como funciona
Escolha o limite a partir de medição de referência e declare a agregação coerente com o risco que se quer capturar.

## Exemplo
Uma métrica de carregamento pode ser verificada com limite superior absoluto e agregação pessimista para proteger a experiência no pior caso.

## Limites e trade-offs
Limites absolutos ignoram diferenças entre tipos de página, e agregação otimista pode esconder regressão recorrente nos piores casos.

## Como verificar
Registre os valores das repetições e confirme qual valor foi comparado com o limite, verificando a coerência com a agregação escolhida.

## Conexões
- [[lighthouseci-assertions-presets]] — Veja também: Lighthouse CI: escolher conjuntos de asserções.
- [[lighthouseci-performance-budgets]] — Veja também: Lighthouse CI: usar orçamento de desempenho.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
