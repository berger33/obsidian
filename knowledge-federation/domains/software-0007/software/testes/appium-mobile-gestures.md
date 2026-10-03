---
id: software.testes.tranche17.001109
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://github.com/appium/appium-uiautomator2-driver", "https://appium.io/docs/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: executar gestos e comandos móveis

## Em uma frase
A sessão expõe comandos para deslizar, tocar em coordenadas, pressionar por tempo e executar ações encadeadas com o ponteiro.

## Por que importa
Fluxos móveis dependem de gestos que não existem na web, e ignorá-los deixa caminhos importantes do produto sem verificação.

## Como funciona
Use os comandos de gesto com referências relativas ao tamanho da tela, verifique o efeito observável e evite coordenadas absolutas.

## Exemplo
Uma lista longa pode ser percorrida com deslize calculado a partir da altura da janela, procurando o item até encontrá-lo.

## Limites e trade-offs
Gestos dependem de tempo e de velocidade e podem ser interpretados como rolagem inercial; a verificação seguinte precisa aguardar a estabilização.

## Como verificar
Repita o gesto em duas resoluções diferentes e confirme que o resultado não depende de valores fixos de coordenada.

## Conexões
- [[appium-locator-strategies]] — Veja também: Appium: escolher seletores móveis.
- [[appium-hybrid-context]] — Veja também: Appium: alternar entre contexto nativo e web.

## Fontes
- [Appium — UiAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver) — capacidades do driver Android, sessões paralelas e opções de porta; consultado em 2026-10-03.
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
