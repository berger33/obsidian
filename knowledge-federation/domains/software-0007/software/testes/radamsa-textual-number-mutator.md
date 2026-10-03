---
id: software.testes.tranche25.001885
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

# Mutação semântica de números textuais: o caso 4294967296 e inteiros gigantes

## Em uma frase
Ao comentar o exemplo echo "Fuzztron 2000" | radamsa --seed 4 -> "Fuzztron 4294967296" e o exemplo com expressões aritméticas, o README destaca que o Radamsa possui um mutador de números que reconhece números textuais na entrada e os substitui por valores de fronteira interessantes para programadores, como 2^32 (4294967296), 2^64-1 (18446744073709551615) e 2^127-1 (170141183460469231731687303715884105727).

## Por que importa
Se um fuzzer apenas trocasse bytes aleatórios, a chance de transformar a string ASCII "2000" exatamente na representação decimal de 2^32 ou UINT64_MAX seria praticamente nula; o mutador numérico ataca overflows de parser diretamente no texto.

## Como funciona
Incorpore números representativos nas amostras de entrada (tamanhos, contadores, coordenadas, IDs, expressões) para que o mutador numérico do Radamsa tenha pontos de ancoragem onde injetar limites de 32, 64 e 128 bits.

## Exemplo
Em echo "1 + (2 + (3 + 4))" | radamsa --seed 12 -n 4, a terceira e a quarta saídas geradas no README trocam operandos por 18446744073709551615 e 170141183460469231731687303715884105727.

## Limites e trade-offs
A escolha de qual mutador aplicar em cada rodada é heurística e pseudoaleatória; o Radamsa alterna entre mutações numéricas, duplicações de parênteses, inserções de bytes e bit flips sem exigir configuração.

## Como verificar
Conferi os exemplos com --seed 4 e --seed 12 -n 4 na seção Fuzzing with Radamsa do README oficial.

## Conexões
- [[radamsa-urandom-and-seed-flag]] — Veja também: Entropia de /dev/urandom por padrão e reprodutibilidade com -s / --seed.
- [[radamsa-multiple-outputs-flag-n]] — Veja também: Geração de múltiplas saídas com -n e unicidade estatística.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
