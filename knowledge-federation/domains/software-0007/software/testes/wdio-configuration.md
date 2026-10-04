---
id: software.testes.tranche18.001173
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

# WebdriverIO: estruturar a configuração

## Em uma frase
O arquivo de configuração declara navegadores, capacidades, estrutura de testes, relatórios, serviços e opções de execução.

## Por que importa
A configuração versionada garante que execução local e pipeline usem as mesmas regras e facilita acrescentar alvos sem duplicar arquivos.

## Como funciona
Declare um bloco por capacidade, fatora o que é comum e mantenha variáveis de ambiente apenas para o que muda entre máquinas.

## Exemplo
Um bloco pode apontar para o navegador principal com opções sem interface, enquanto outro cobre dispositivo móvel simulado.

## Limites e trade-offs
Cópias divergentes de configuração produzem resultados diferentes sem que ninguém saiba qual foi aplicada, e a herança parcial confunde a leitura.

## Como verificar
Execute a suíte informando dois blocos diferentes e confirme no log qual configuração foi efetivamente usada.

## Conexões
- [[wdio-custom-commands]] — Veja também: WebdriverIO: definir comandos próprios.
- [[wdio-reporters-and-artifacts]] — Veja também: WebdriverIO: escolher relatórios e evidências.

## Fontes
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
- [WebdriverIO — repositório oficial](https://github.com/webdriverio/webdriverio) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
