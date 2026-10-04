---
id: software.testes.tranche23.001737
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
fontes: ["https://hyperfoil.io/docs/getting-started/quickstart1/", "https://hyperfoil.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Do zero ao primeiro run: download, start-local, upload, run, stats

## Em uma frase
O Quickstart 1 oficial conduz o primeiro benchmark em quatro passos mecânicos: baixar e descompactar o release (exemplo com a versão 0.29.3 do GitHub Hyperfoil/Hyperfoil releases), iniciar o modo interativo com bin/cli.sh, digitar start-local para subir um controller embutido (saída mostra o controller ouvindo em 127.0.0.1:41621 e a conexão estabelecida) e então upload de um arquivo single-request.hf.yaml seguido de run nomeando o benchmark.

## Por que importa
Esse caminho mínimo existe para provar que a arquitetura distribuída roda local sem cluster nem orquestrador externo: o mesmo CLI que dispara start-local é o que dispara upload/run contra um controller remoto, mudando só o destino da conexão.

## Como funciona
O benchmark de exemplo é deliberadamente minimalista: name single-request (a doc recomenda manter o nome em sincronia com o nome do arquivo com o sufixo .hf.yaml), um bloco http com host (o default de todos os requests do benchmark), e uma fase example com atOnce users 1 rodando uma sequência com um único GET sincrono para http://hyperfoil.io/.

## Exemplo
Reproduza o quickstart contra o próprio site oficial e compare a tabela impressa: Started/Terminated com duração em milissegundos e a nota "174 ms (exceeded by 174 ms)" — o relógio do run aparece antes de qualquer métrica avançada.

## Limites e trade-offs
O exemplo declara (e a doc ri disso) que "doing one request is not much of a benchmark and the statistics above are moot": ele exercita o mecanismo, não a metodologia — números de latência dele não significam nada sobre o alvo.

## Como verificar
Abra o Quickstart 1 e confira os quatro passos com os blocos de comando e YAML na íntegra, incluindo o caminho do zip do release 0.29.3.

## Conexões
- [[hyperfoil-scenario-steps]] — Veja também: Cenário = sequências = steps: a gramática do teste de carga.
- [[hyperfoil-stats]] — Veja também: O stats por dentro: percentis, classes de status e os contadores de erro.

## Fontes
- [Hyperfoil — Quickstart 1: First benchmark](https://hyperfoil.io/docs/getting-started/quickstart1/) — download, start-local, upload, run e stats; consultado em 2026-10-03.
- [Hyperfoil — índice da documentação](https://hyperfoil.io/docs/) — nove seções: overview, quickstarts, user guide, API REST, extensions; consultado em 2026-10-03.
