---
id: software.testes.tranche25.001880
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

# Radamsa: gerador de casos de teste para testes de robustez

## Em uma frase
O README oficial apresenta o Radamsa como um gerador de casos de teste para testes de robustez (fuzzer), usado para testar quão bem um programa resiste a entradas malformadas e potencialmente maliciosas: ele lê arquivos de amostra com dados válidos e gera saídas diferentes a partir deles.

## Por que importa
Enquanto testes unitários e de integração verificam o caminho feliz (positive testing), o README enquadra o fuzzing como negative testing — tentar refutar na prática o teorema de que, para todas as entradas, o serviço não sofre crash, exaustão exponencial de memória ou loop infinito.

## Como funciona
Forneça uma ou mais amostras válidas na entrada padrão ou como argumentos de arquivo; o Radamsa aplica heurísticas e padrões de mutação variados (de uma única alteração ou bit flip até transformações estruturais) e escreve a entrada mutada na saída padrão.

## Exemplo
O exemplo mínimo da seção Nutshell resume o fluxo em uma linha de pipe: echo "HAL 9000" | radamsa.

## Limites e trade-offs
O Radamsa resolve apenas a primeira metade do fuzzing (gerar entradas variadas); a segunda metade (executar o programa alvo e observar se algo ruim aconteceu) fica a cargo de um script ou harness externo.

## Como verificar
Conferi as seções de abertura, Nutshell e What the Fuzz do README oficial do Radamsa.

## Conexões
- [[radamsa-black-box-and-protos-origin]] — Veja também: Abordagem estritamente black-box e origem no Protos Genome Project.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
