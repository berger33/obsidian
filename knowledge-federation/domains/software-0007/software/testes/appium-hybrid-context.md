---
id: software.testes.tranche17.001110
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
fontes: ["https://appium.io/docs/en/latest/", "https://github.com/appium/appium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: alternar entre contexto nativo e web

## Em uma frase
Aplicativos híbridos expõem contextos distintos, e a sessão precisa mudar para o contexto web antes de usar seletores de página.

## Por que importa
Sem a troca de contexto, os elementos da página embutida não são encontrados, e o teste falha como se a tela estivesse vazia.

## Como funciona
Consulte os contextos disponíveis, mude para o correto antes de agir e retorne ao contexto nativo ao terminar.

## Exemplo
Um fluxo de pagamento pode preencher dados em página embutida e depois voltar ao aplicativo para confirmar o recibo.

## Limites e trade-offs
A troca depende do carregamento da página embutida e pode exigir espera; permanecer no contexto errado contamina os passos seguintes.

## Como verificar
Liste os contextos antes e depois da navegação e confirme que a troca ocorre no momento esperado do fluxo.

## Conexões
- [[appium-mobile-gestures]] — Veja também: Appium: executar gestos e comandos móveis.
- [[appium-session-reset]] — Veja também: Appium: controlar reinício e limpeza da sessão.

## Fontes
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
- [Appium — repositório oficial](https://github.com/appium/appium) — arquitetura de drivers e plugins, CLI de extensões e servidor; consultado em 2026-10-03.
