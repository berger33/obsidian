---
id: software.testes.tranche20.001432
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

# fast-check: usar a redução de contraexemplos

## Em uma frase
Ao encontrar falha, a ferramenta reduz a entrada ao menor caso que ainda reproduz o erro, exibindo o valor mínimo.

## Por que importa
A redução transforma um caso grande e confuso em um relato legível, que vira teste de regressão direto.

## Como funciona
Use os geradores da própria biblioteca, aceite o contraexemplo reduzido como ponto de partida e registre-o em teste dedicado.

## Exemplo
Um erro de limite em processamento de listas costuma reduzir a um caso com um ou dois elementos, apontando a causa.

## Limites e trade-offs
Escrever a entrada à mão em arquivo de teste sem o caso reduzido perde a informação que a redução produziu.

## Como verificar
Verifique se o contraexemplo exibido é realmente o menor caso possível executando-o isoladamente.

## Conexões
- [[fc-custom-arbitraries]] — Veja também: fast-check: construir geradores próprios.
- [[fc-seed-and-reproducibility]] — Veja também: fast-check: reproduzir execuções pela semente.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — repositório oficial](https://github.com/dubzzz/fast-check) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
