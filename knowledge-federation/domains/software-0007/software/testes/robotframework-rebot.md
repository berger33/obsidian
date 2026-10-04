---
id: software.testes.tranche24.001764
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

# rebot: pós-processamento e junção de resultados

## Em uma frase
Junto com o robot, o projeto distribui o "rebot", ferramenta para combinar resultados e fazer pós-processamento — o exemplo do roda "rebot --name Example output1.xml output2.xml", e "rebot --help" traz a documentação da linha de comando.

## Por que importa
Suítes executadas em paralelo ou em máquinas diferentes produzem output.xml separados; sem o rebot, o time precisaria manter um relatório por executador, e a visão única de falhas — que é o que a triagem consome — se perde.

## Como funciona
Gere output.xml por partição (por shard, plataforma ou navegador) e rode rebot sobre os XMLs, dando um nome ao agregado com --name; o rebot relança log e relatório HTML a partir dos dados combinados sem reexecutar nada.

## Exemplo
Duas execuções em paralelo geram shard1/output.xml e shard2/output.xml; "rebot --name Integration shard1/output.xml shard2/output.xml" produz o relatório único que vai para a página de artefatos do CI.

## Limites e trade-offs
O rebot trabalha sobre os arquivos de saída existentes; ele não reexecuta testes nem reconstrói dados que não foram gravados, e o README remete ao User Guide para o comportamento completo.

## Como verificar
Reproduzi o comando de exemplo da seção Usage do README oficial contra dois output.xml gerados por execuções locais.

## Conexões
- [[robotframework-robot-cli]] — Veja também: Execução pela linha de comando: robot, variáveis e outputdir.
- [[robotframework-foundation-license]] — Veja também: Fundação, marca e o duplo licenciamento do projeto.

## Fontes
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
