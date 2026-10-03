---
id: software.testes.tranche25.001888
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://gitlab.com/akihe/radamsa/-/raw/master/README.md", "https://gitlab.com/akihe/radamsa"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trade-off entre fuzzing em pipe contínuo e uma execução por arquivo

## Em uma frase
Na seção Fuzzing with Radamsa, o autor contrasta duas abordagens: jogar milhares de saídas de uma vez por pipe (como gzip -c /bin/bash | radamsa -n 1000 | gzip -d > /dev/null ou o laço sem arquivo intermediário) versus gravar fuzzed.gz a cada iteração e checar o código de retorno.

## Por que importa
O pipe direto é ótimo para um smoke test rápido de segundos na linha de comando (como o exemplo que trava o bc na linha 1424 com memory exhausted), mas descarta a entrada exata que provocou o problema; já o laço com arquivo em disco é mais lento em I/O, porém preserva o reproducer automaticamente.

## Como funciona
Comece com um pipe rápido (-n 1000 ou -n 10000) para descobrir se o parser apresenta falhas óbvias ou travamentos, e migre para o laço que grava o arquivo fuzzed antes de cada execução assim que quiser capturar o artefato reprodutor ou rodar em CI.

## Exemplo
No exemplo do bc no README, o pipe mostra "(standard_in) 1424: memory exhausted [hang]", provando a existência do problema, enquanto o padrão com fuzzed.gz e test $? -gt 127 entrega o arquivo pronto para abrir no depurador.

## Limites e trade-offs
Quando o problema encontrado é um hang (loop infinito) em vez de término por sinal, test $? -gt 127 nunca é alcançado sozinho; em campanhas automatizadas, combine a execução por arquivo com um utilitário de timeout por processo.

## Como verificar
Conferi a progressão de exemplos (pipe com bc/ol/gzip, while true em pipe e while true com fuzzed.gz) no README oficial.

## Conexões
- [[radamsa-crash-loop-exit-gt-127]] — Veja também: O laço shell de captura de falha: arquivo fuzzed e código de saída > 127.
- [[radamsa-multi-sample-and-network-capabilities]] — Veja também: Amostras múltiplas e modos TCP cliente/servidor.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
