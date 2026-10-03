---
id: software.testes.tranche23.001660
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/karma-runner/karma/blob/master/README.md", "https://karma-runner.github.io/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karma: um executor de JavaScript em navegadores reais

## Em uma frase
O Karma é descrito no seu README como uma ferramenta simples que permite executar código JavaScript em múltiplos navegadores reais; nasceu no time do AngularJS, que usava o JSTD e queria um runner próprio, estável e rápido, construído sobre Socket.io e Node.js.

## Por que importa
Para código que depende de DOM, timers ou APIs de navegador, unit tests em Node não bastam; o Karma roda os mesmos testes em Chrome, Firefox e até dispositivos móveis, e o resultado aparece no terminal que o desenvolvedor já usa.

## Como funciona
O Karma lança um servidor HTTP, abre (ou captura) os navegadores configurados, serve o test runner HTML e coleta os resultados de volta pela conexão Socket.io; salvar um arquivo dispara nova execução no modo watch.

## Exemplo
Instale com npm install karma, gere um karma.conf.js e execute testes com jasmine ou mocha em dois navegadores; a filosofia está resumida no lema "test on real devices, control the whole workflow from the command line".

## Limites e trade-offs
A documentação do próprio projeto lista cenários em que ele faz sentido — múltiplos navegadores, execução local e em CI, coverage via Istanbul, RequireJS — o que pressupõe um projeto web servido como arquivos estáticos.

## Como verificar
Abra o README oficial e confirme a frase "A simple tool that allows you to execute JavaScript code in multiple real browsers" e a origem JSTD/AngularJS declarada na seção de motivação.

## Conexões
- [[karma-deprecated-officially]] — Veja também: Karma está descontinuado: só correções de segurança.

## Fontes
- [Karma — README oficial](https://github.com/karma-runner/karma/blob/master/README.md) — proposta, descontinuação, adaptadores e quando usar; consultado em 2026-10-03.
- [Karma — página inicial da documentação](https://karma-runner.github.io/latest/index.html) — destaques: real devices, remote control, frameworks, CI; consultado em 2026-10-03.
