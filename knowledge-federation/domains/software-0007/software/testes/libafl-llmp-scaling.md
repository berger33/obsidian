---
id: software.testes.tranche24.001801
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
fontes: ["https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md", "https://github.com/AFLplusplus/LibAFL"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LLMP: escala quase linear por núcleo e TCP entre máquinas

## Em uma frase
Sob o destaque "scalable", o README explica o mecanismo: "Low Level Message Passing, LLMP for short, allows LibAFL to scale almost linearly over cores, and via TCP to multiple machines" — a passagem de mensagens de baixo nível é o que conecta as partes do fuzzador entre núcleos e hosts.

## Por que importa
O gargalo de paralelismo em fuzzing é a sincronização do corpus compartilhado; um protocolo de mensagem próprio que atravessa TCP sem camada extra transforma a pergunta "quantas máquinas cabem na campanha?" em questão de configuração, não de arquitetura.

## Como funciona
Monte o fuzzador com os componentes de monitor/broker do framework — os exemplos multicore em fuzzers/ usam LLMP internamente — e distribua a campanha apontando peers via TCP conforme o design descrito.

## Exemplo
A frase do README cobre dois planos de escala: núcleos de uma máquina e máquinas separadas; o exemplo libfuzzer_libpng multicore demonstra o primeiro.

## Limites e trade-offs
"Almost linearly" é a qualificação do README, não uma medida garantida: o resultado observado depende do alvo, do feedback e da rede; números de benchmark próprios são obrigação do time que escala a campanha.

## Como verificar
A descrição do LLMP está no bullet "scalable" da lista Key highlights do README oficial.

## Conexões
- [[libafl-what-it-is]] — Veja também: LibAFL: encaixe o seu fuzzador em Rust.
- [[libafl-compile-time-speed]] — Veja também: Overhead mínimo por decisão de compilação.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
