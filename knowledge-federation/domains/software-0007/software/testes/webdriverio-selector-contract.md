---
id: software.testes.tranche13.000676
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
fontes: ["https://webdriver.io/docs/selectors", "https://webdriver.io/docs/runner/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: escolher seletor que sobreviva a refatoração visual

## Em uma frase
WebdriverIO aceita estratégias de seletor diferentes, que variam em estabilidade e relação com a interface de usuário.

## Por que importa
Uma mudança de classe de estilo não deveria quebrar todo teste se o contrato do controle e seu nome acessível permanecerem iguais.

## Como funciona
Prefira um identificador semântico disponibilizado pelo produto quando o projeto o mantém estável; reserve seletores estruturais para detalhe de layout que realmente faça parte do requisito.

## Exemplo
Uma ação no botão “Confirmar compra” pode procurar o controle pelo papel ou nome acessível em vez de depender da posição do quarto `div` na página.

## Limites e trade-offs
Nenhum seletor elimina a necessidade de checar unicidade e contexto; nome acessível pode mudar intencionalmente quando o conteúdo muda.

## Como verificar
Renomeie classe CSS sem mudar a interface e confirme se o teste permanece estável; depois altere o nome acessível e verifique que a falha é relevante.

## Conexões
- [[webdriverio-browser-runner-boundary]] — Veja também: WebdriverIO: escolher Browser Runner para teste de componentes.
- [[webdriverio-capability-concurrency]] — Veja também: WebdriverIO: limitar workers pela capacidade disponível.

## Fontes
- [WebdriverIO — Selectors](https://webdriver.io/docs/selectors) — selector strategies and element lookup; consultado em 2026-10-02.
- [WebdriverIO — Runner](https://webdriver.io/docs/runner/) — local and browser runners, workers and isolation; consultado em 2026-10-02.
