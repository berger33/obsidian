---
id: software.testes.tranche17.001111
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

# Appium: controlar reinício e limpeza da sessão

## Em uma frase
Opções de sessão definem se o aplicativo é reinstalado, se os dados são apagados e se o estado é preservado entre execuções.

## Por que importa
Cada caso precisa de estado inicial conhecido, e o excesso de limpeza encarece a execução sem necessidade.

## Como funciona
Escolha a política de limpeza por suíte, preserve sessão apenas para fluxos que dependem de estado acumulado e documente a decisão.

## Exemplo
Um caso de primeiro acesso exige instalação limpa, enquanto casos de navegação podem reutilizar dados já preparados.

## Limites e trade-offs
Limpeza total entre casos aumenta muito o tempo, e a preservação indevida faz o caso seguinte herdar telas e credenciais anteriores.

## Como verificar
Rode o mesmo caso duas vezes seguidas e confirme que o resultado não depende de sessão ou dados deixados pela execução anterior.

## Conexões
- [[appium-hybrid-context]] — Veja também: Appium: alternar entre contexto nativo e web.
- [[appium-parallel-sessions]] — Veja também: Appium: paralelizar sessões com segurança.

## Fontes
- [Appium — UiAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver) — capacidades do driver Android, sessões paralelas e opções de porta; consultado em 2026-10-03.
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
