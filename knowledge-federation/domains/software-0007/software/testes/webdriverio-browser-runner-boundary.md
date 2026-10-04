---
id: software.testes.tranche13.000675
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://webdriver.io/docs/runner/", "https://webdriver.io/docs/configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: escolher Browser Runner para teste de componentes

## Em uma frase
Browser Runner executa framework de teste dentro de browser real e é diferente do Local Runner que inicia framework em processo Node.

## Por que importa
Um DOM simulado é útil para unidade, mas não oferece exatamente as mesmas APIs e renderização que a plataforma do usuário.

## Como funciona
Use Browser Runner para componente que depende de Web APIs reais, escolha preset suportado ou config Vite apropriada e reserve E2E remoto para fluxo que precisa de aplicação completa.

## Exemplo
Um componente que usa canvas pode ser testado num browser real para validar API e interação sem subir toda a infraestrutura de produção.

## Limites e trade-offs
Browser Runner não converte teste unitário em cobertura de fluxo ponta a ponta; cada teste e arquivo ainda precisam de isolamento e dados determinísticos.

## Como verificar
Compare o mesmo componente em runner de browser e ambiente simulado, identificando qual requisito depende de comportamento real do navegador.

## Conexões
- [[webdriverio-local-worker-isolation]] — Veja também: WebdriverIO: entender isolamento do Local Runner.
- [[webdriverio-selector-contract]] — Veja também: WebdriverIO: escolher seletor que sobreviva a refatoração visual.

## Fontes
- [WebdriverIO — Runner](https://webdriver.io/docs/runner/) — local and browser runners, workers and isolation; consultado em 2026-10-02.
- [WebdriverIO — Configuration](https://webdriver.io/docs/configuration) — specs, capabilities, hooks and runner options; consultado em 2026-10-02.
