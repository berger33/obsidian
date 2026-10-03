---
id: software.testes.tranche24.001803
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

# BytesInput é opcional: o formato de input é seu

## Em uma frase
Na lista de destaques, "adaptable" é exemplificado com precisão: "You can replace each part of LibAFL. For example, BytesInput is just one potential form input: feel free to add an AST-based input for structured fuzzing, and more." — o tipo do input é um parâmetro do framework, não uma decisão embutida.

## Por que importa
Estruturas de dados customizadas no núcleo (AST, gramática, protobuf) são o que separa fuzzing de formato real de fuzzer de bytes aleatórios; aqui isso não exige fork do fuzzer, porque o input é parte substituível por design.

## Como funciona
Defina um tipo próprio que implemente as operações esperadas (mutação, escrita, comparação) e ligue-o ao executor e aos mutators dos seus módulos — o README cita explicitamente o caso AST-based como bem-vindo.

## Exemplo
O fuzzador libfuzzer_libpng usa bytes porque libpng consome PNG bruto; um harness de parser de linguagem trocaria por sua árvore, mantendo os mesmos executors e feedbacks em volta.

## Limites e trade-offs
O README enuncia a extensibilidade e dá um exemplo de direção, mas não documenta os traits exatos do tipo de input — a API atual vive no docs.rs e nos exemplos, que a nota aponta como verificação.

## Como verificar
A frase do BytesInput "just one potential form input" é o texto do bullet adaptable no README oficial.

## Conexões
- [[libafl-compile-time-speed]] — Veja também: Overhead mínimo por decisão de compilação.
- [[libafl-no-std-embedded]] — Veja também: no_std: fuzzador dentro de firmware e hypervisor.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
