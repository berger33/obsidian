---
id: software.testes.tranche17.001108
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
fontes: ["https://appium.io/docs/en/latest/", "https://github.com/appium/appium-uiautomator2-driver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: escolher seletores móveis

## Em uma frase
Os seletores variam por plataforma, incluindo identificador de acessibilidade, atributos nativos e estratégias específicas de cada automação.

## Por que importa
Identificadores de acessibilidade atravessam plataformas e sobrevivem a mudanças de layout, enquanto seletores por coordenadas quebram a cada ajuste visual.

## Como funciona
Prefira identificadores estáveis definidos pela equipe, limite seletores nativos a casos necessários e evite posição na tela como critério.

## Exemplo
Um botão de confirmação pode ser localizado por identificador de acessibilidade tanto em Android quanto em iOS, mantendo o mesmo teste para as duas plataformas.

## Limites e trade-offs
Hierarquias nativas mudam entre versões do sistema, e seletores por texto quebram com localização do aplicativo.

## Como verificar
Execute o mesmo fluxo em duas versões de sistema e confirme que os seletores baseados em identificador continuam encontrando os elementos.

## Conexões
- [[appium-drivers-architecture]] — Veja também: Appium: entender a arquitetura de drivers.
- [[appium-mobile-gestures]] — Veja também: Appium: executar gestos e comandos móveis.

## Fontes
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
- [Appium — UiAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver) — capacidades do driver Android, sessões paralelas e opções de porta; consultado em 2026-10-03.
