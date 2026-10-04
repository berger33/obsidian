---
id: software.testes.tranche19.001322
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/garris/BackstopJS/blob/master/README.md", "https://github.com/garris/BackstopJS"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# BackstopJS: ajustar a tolerância de diferença

## Em uma frase
O limite define a porcentagem de pixels diferentes aceita antes de o cenário ser marcado como falho, e a exigência de mesmas dimensões pode ser ativada.

## Por que importa
a tolerância absorve variações de renderização entre ambientes sem deixar passar mudanças relevantes de layout.

## Como funciona
Comece com tolerância baixa, aumente apenas com justificativa registrada e mantenha a exigência de dimensões iguais em componentes críticos.

## Exemplo
Antialiasing de fontes entre sistemas pode exigir tolerância pequena, enquanto uma mudança de cor deve continuar sendo detectada.

## Limites e trade-offs
Tolerância alta esconde regressões reais, e exigir dimensões idênticas em conteúdo de texto variável gera falhas espúrias.

## Como verificar
Ajuste um pixel de cor em área de teste e confirme que a diferença é detectada com a tolerância vigente.

## Conexões
- [[backstopjs-readiness]] — Veja também: BackstopJS: controlar o momento da captura.
- [[backstopjs-hiding-dynamic-content]] — Veja também: BackstopJS: isolar conteúdo dinâmico.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — repositório oficial](https://github.com/garris/BackstopJS) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
