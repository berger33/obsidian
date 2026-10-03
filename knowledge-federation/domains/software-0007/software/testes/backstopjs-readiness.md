---
id: software.testes.tranche19.001321
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
fontes: ["https://github.com/garris/BackstopJS/blob/master/README.md", "https://garris.github.io/BackstopJS/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# BackstopJS: controlar o momento da captura

## Em uma frase
O cenário pode esperar por seletor presente, evento registrado no console, tempo fixo ou interação prévia antes de capturar.

## Por que importa
Capturar antes de a página estabilizar produz diferenças falsas e mina a confiança no resultado da verificação.

## Como funciona
Prefira espera por seletor ou evento, use interação para alcançar estados específicos e reserve o tempo fixo para animações conhecidas.

## Exemplo
O cenário pode aguardar o seletor do painel renderizado, passar o ponteiro sobre o menu e só então capturar.

## Limites e trade-offs
Esperas fixas curtas geram intermitência em máquinas lentas, e esperas longas alongam a suíte sem garantir estabilidade.

## Como verificar
Reduza a velocidade do ambiente de propósito e confirme que a captura continua estável por causa da espera por condição.

## Conexões
- [[backstopjs-selectors]] — Veja também: BackstopJS: limitar a captura a elementos.
- [[backstopjs-mismatch-threshold]] — Veja também: BackstopJS: ajustar a tolerância de diferença.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — Página do projeto](https://garris.github.io/BackstopJS/) — demonstração e documentação publicada; consultado em 2026-10-03.
