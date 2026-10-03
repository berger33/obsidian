---
id: software.testes.tranche18.001171
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://webdriver.io/docs/gettingstarted", "https://github.com/webdriverio/webdriverio"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: orquestrar serviços de teste

## Em uma frase
Os serviços preparam e encerram componentes externos, como servidor de navegador, emulador ou servidor de aplicação, integrados ao ciclo da suíte.

## Por que importa
A suíte precisa de ambiente reproduzível, e o serviço evita comandos manuais antes de cada execução.

## Como funciona
Declare os serviços na configuração, informe as opções de cada um e mantenha versões fixadas para reduzir variação entre máquinas.

## Exemplo
Um serviço pode subir o servidor de automação e encerrá-lo ao final, liberando portas usadas pela execução.

## Limites e trade-offs
Serviços mal configurados deixam processos ativos entre execuções, e a sobreposição de dois serviços na mesma porta causa falha intermitente.

## Como verificar
Inicie a suíte duas vezes seguidas e confirme no log que processos e portas foram liberados ao final da primeira.

## Conexões
- [[wdio-element-commands]] — Veja também: WebdriverIO: compor ações de elemento.
- [[wdio-custom-commands]] — Veja também: WebdriverIO: definir comandos próprios.

## Fontes
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
- [WebdriverIO — repositório oficial](https://github.com/webdriverio/webdriverio) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
