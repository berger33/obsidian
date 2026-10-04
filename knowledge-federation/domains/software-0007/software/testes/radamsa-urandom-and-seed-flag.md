---
id: software.testes.tranche25.001884
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

# Entropia de /dev/urandom por padrão e reprodutibilidade com -s / --seed

## Em uma frase
O README explica que, quando nenhum estado aleatório inicial é informado, o Radamsa lê uma semente aleatória de /dev/urandom, gerando em geral um resultado diferente a cada invocação; para fixar o estado aleatório, usa-se o parâmetro -s (ou --seed) seguido de um número, garantindo que a mesma semente produza exatamente os mesmos dados.

## Por que importa
Em pipelines de CI e na triagem de bugs, aleatoriedade pura sem semente registrada impede reproduzir a entrada exata que derrubou o alvo; passar --seed transforma qualquer caso gerado num teste determinístico.

## Como funciona
Durante campanhas exploratórias deixe o padrão com /dev/urandom ou sorteie uma semente explícita por rodada e grave-a no log; ao encontrar uma falha, reexecute com -s <numero> (ou --seed <numero>) para regenerar o input idêntico.

## Exemplo
O exemplo oficial mostra a reprodutibilidade e o mutador numérico em ação: echo "Fuzztron 2000" | radamsa --seed 4 produz deterministicamente "Fuzztron 4294967296".

## Limites e trade-offs
Para entradas muito pequenas sem semente fixa, o README observa que é comum ver a mesma saída ou até a entrada original se repetir com certa frequência devido ao espaço reduzido de mutação.

## Como verificar
Conferi os parágrafos sobre /dev/urandom e -s/--seed na seção Fuzzing with Radamsa do README oficial.

## Conexões
- [[radamsa-unix-cat-pipe-model]] — Veja também: O modelo mental do cat UNIX que quebra dados no caminho.
- [[radamsa-textual-number-mutator]] — Veja também: Mutação semântica de números textuais: o caso 4294967296 e inteiros gigantes.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
