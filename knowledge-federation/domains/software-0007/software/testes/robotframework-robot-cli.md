---
id: software.testes.tranche24.001763
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Execução pela linha de comando: robot, variáveis e outputdir

## Em uma frase
O README define a execução pelo comando "robot" (ou "python -m robot"), passando o caminho de um arquivo ou diretório de testes como argumento, com opções de linha de comando antes do caminho — o exemplo oficial usa --variable BROWSER:Firefox e --outputdir results.

## Por que importa
Colocar as opções antes do caminho não é capricho estético: variáveis como BROWSER parametrizam o mesmo suíte contra Firefox ou Chrome, e --outputdir organiza artefatos (log, relatório, xunit) para o CI coletar sem glob improvisado.

## Como funciona
Execute "robot tests.robot" para um arquivo único, "robot --variable BROWSER:Firefox --outputdir results path/to/tests/" para um diretório parametrizado, e recorra a "robot --help" para a lista completa de opções.

## Exemplo
No CI, um passo "robot --outputdir results --variable BROWSER:Firefox acceptance/" gera os resultados em results/ e permite publicar só essa pasta como artefato.

## Limites e trade-offs
O README documenta o formato básico; a referência completa de opções está no User Guide, que é o manual citado como documento de linha de comando.

## Como verificar
Executei "robot --help" e comparei as duas linhas de exemplo da seção Usage do README.

## Conexões
- [[robotframework-suite-syntax]] — Veja também: A anatomia de uma suíte: tabelas Settings e Test Cases.
- [[robotframework-rebot]] — Veja também: rebot: pós-processamento e junção de resultados.

## Fontes
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
