---
id: software.testes.tranche20.001430
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
fontes: ["https://fast-check.dev/docs/introduction/getting-started/", "https://www.npmjs.com/package/fast-check"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# fast-check: gerar dados com geradores

## Em uma frase
Os geradores descrevem domínios de valores por tipo, com versões para inteiros, textos, listas, registros, opções e combinações.

## Por que importa
Modelar o domínio de entrada corretamente é o que torna a propriedade significativa e a redução eficaz.

## Como funciona
Use geradores simples e componha por mapas e encadeamentos, restringindo as faixas ao domínio válido.

## Exemplo
Um identificador de pedido pode ser gerado por prefixo fixo com número dentro da faixa aceita pela aplicação.

## Limites e trade-offs
Geradores que produzem valores fora do domínio geram falsos positivos, e composições com funções opacas impedem a redução dos casos.

## Como verificar
Gere cem valores e inspecione a amostra para confirmar que ela cobre vazios, limites e valores típicos.

## Conexões
- [[fc-properties-basics]] — Veja também: fast-check: declarar propriedades.
- [[fc-custom-arbitraries]] — Veja também: fast-check: construir geradores próprios.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — Pacote publicado](https://www.npmjs.com/package/fast-check) — versões, documentação de uso e recursos do pacote; consultado em 2026-10-03.
