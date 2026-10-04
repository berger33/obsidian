---
id: software.testes.tranche20.001431
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

# fast-check: construir geradores próprios

## Em uma frase
Geradores existentes podem ser transformados por mapeamento ou encadeados quando a próxima entrada depende do valor anterior.

## Por que importa
Encadeamento permite expressar tipos do domínio em que campos dependem uns dos outros, mantendo a capacidade de redução.

## Como funciona
Prefira encadear quando houver dependência, manter o mapeamento simples e testar o próprio gerador com amostras.

## Exemplo
Um intervalo de datas pode ser gerado a partir da data inicial, garantindo sempre o par válido para a regra.

## Limites e trade-offs
Encadear funções aleatórias próprias dentro do gerador impede a redução e esconde casos inválidos.

## Como verificar
Envie um valor fora do domínio ao gerador e confirme que ele é rejeitado ou ajustado conforme a regra declarada.

## Conexões
- [[fc-arbitraries]] — Veja também: fast-check: gerar dados com geradores.
- [[fc-shrinking]] — Veja também: fast-check: usar a redução de contraexemplos.

## Fontes
- [fast-check — Primeiros passos](https://fast-check.dev/docs/introduction/getting-started/) — propriedades, geradores, redução de casos e sementes; consultado em 2026-10-03.
- [fast-check — repositório oficial](https://github.com/dubzzz/fast-check) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
