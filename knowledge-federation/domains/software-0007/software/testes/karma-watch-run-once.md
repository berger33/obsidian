---
id: software.testes.tranche23.001668
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
fontes: ["https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md", "https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Watch contínuo no dev, single run no CI

## Em uma frase
autoWatch (padrão true) habilita observar os arquivos e reexecutar os testes a cada mudança; autoWatchBatchDelay (padrão 250 ms) agrupa múltiplas mudanças em uma única execução usando debounce — o timer reinicia a cada arquivo alterado.

## Por que importa
Rodar no save é a proposta central do runner ("executar testes a cada save" está na lista de quando usá-lo), e o batch delay evita reiniciar a suíte enquanto um build está escrevendo arquivos pela metade.

## Como funciona
No CI, o comportamento de watch é indesejado: a doc de introdução mostra o override pela linha de comando com karma start my.conf.js --single-run, que executa cada navegador capturado uma única vez, e também --log-level debug no mesmo exemplo.

## Exemplo
Em dev, rode karma start e altere um spec: a execução reaparece no terminal sem intervenção; em CI, rode karma start --single-run e confirme que o processo encerra sozinho com código de saída adequado.

## Limites e trade-offs
A flag CLI --single-run só funciona bem com navegador headless ou com display disponível; ambientes de CI sem navegador configurado precisam do launcher certo e às vezes de flags extras de Chrome — detalhe de integração, não do CLI.

## Como verificar
Abra a seção Starting Karma e o exemplo de command line arguments na página de configuração da doc oficial e as duas opções autoWatch na referência; confirme os padrões 250 e true.

## Conexões
- [[karma-timeouts-flakiness]] — Veja também: Três opções para conexões instáveis com o navegador.
- [[karma-frameworks-plugins]] — Veja também: Launchers, reporters e preprocessors são todos plugins.

## Fontes
- [Karma — Configuration (intro)](https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md) — assistente karma init, start e overrides de CLI; consultado em 2026-10-03.
- [Karma — Configuration file reference](https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md) — descoberta do arquivo, File Patterns e opções do objeto de configuração; consultado em 2026-10-03.
