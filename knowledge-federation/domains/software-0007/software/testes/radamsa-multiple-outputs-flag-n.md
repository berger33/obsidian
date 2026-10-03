---
id: software.testes.tranche25.001886
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

# Geração de múltiplas saídas com -n e unicidade estatística

## Em uma frase
O README documenta o parâmetro -n para gerar mais de uma saída por invocação — como em echo "1 + (2 + (3 + 4))" | radamsa --seed 12 -n 4 ou radamsa -n 10000 —, esclarecendo que não há garantia matemática de que todas as saídas sejam únicas, mas que com amostras não triviais saídas iguais tendem a ser extremamente raras.

## Por que importa
Quando o programa alvo processa múltiplas linhas ou registros em lote pela entrada padrão, gerar milhares de casos numa única chamada a radamsa -n 10000 evita o custo de criar dez mil processos do fuzzer no sistema operacional.

## Como funciona
Use -n <quantidade> ao alimentar interpretadores de linha ou descompressores em streaming pela stdin, ajustando o volume de acordo com o tempo disponível no job de teste.

## Exemplo
O README demonstra três pipelines diretos com -n: echo "100 * (1 + (2 / 3))" | radamsa -n 10000 | bc (que leva o bc a memory exhausted e hang), uma expressão lambda enviada com -n 10000 para o compilador ol e gzip -c /bin/bash | radamsa -n 1000 | gzip -d > /dev/null.

## Limites e trade-offs
Enviar -n 10000 num único pipe mistura todas as entradas numa única execução do programa alvo; se o alvo abortar na centésima entrada ou acumular estado, você não saberá imediatamente qual das entradas isoladas causou a falha.

## Como verificar
Conferi os exemplos de -n 4, -n 10000 e -n 1000 na seção Fuzzing with Radamsa do README oficial.

## Conexões
- [[radamsa-textual-number-mutator]] — Veja também: Mutação semântica de números textuais: o caso 4294967296 e inteiros gigantes.
- [[radamsa-crash-loop-exit-gt-127]] — Veja também: O laço shell de captura de falha: arquivo fuzzed e código de saída > 127.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
