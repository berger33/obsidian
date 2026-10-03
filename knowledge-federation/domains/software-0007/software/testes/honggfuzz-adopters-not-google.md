---
id: software.testes.tranche24.001799
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
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Quem adota — e o disclaimer de que não é produto Google

## Em uma frase
O README encerra com a seção "Projects Using Honggfuzz": Google OSS-Fuzz (fuzzing contínuo de open source), a equipe de segurança do Android, o crate honggfuzz-rs para Rust, Bitcoin Core, Apache HTTP Server e Systemd em CI, Cifasis QuickFuzz e Mozilla FuzzOS — e finaliza, em negrito, "__This is NOT an official Google product__", sob Apache License 2.0.

## Por que importa
A lista de adotantes é a validação de produção: OSS-Fuzz rodando o motor contra o ecossistema open source inteiro, e o disclaimer importante para o jurídico entender a natureza do projeto (código Google, governança de projeto aberto, sem contrato de suporte).

## Como funciona
Ao escolher um fuzz-engine, compare adotantes em produção com o seu perfil (CI de servidor? kernel? criptografia?) — o próprio README remete aos "hundreds more" nos bugs do OSS-Fuzz com filtro por honggfuzz.

## Exemplo
O parágrafo de Rust cita o "honggfuzz-rs crate for fuzzing Rust code" como caminho da comunidade Rust, separado do wrapper C — um motor, dois pontos de entrada.

## Limites e trade-offs
O status "not official Google product" vem do próprio README; nada aqui descreve SLA, suporte ou política de release que o projeto não afirme por escrito.

## Como verificar
As duas últimas seções do README oficial — Projects Using Honggfuzz e License — sustentam a nota literalmente.

## Conexões
- [[honggfuzz-trophies]] — Veja também: Trophies: a lista de CVEs como currículo.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Repositório oficial google/honggfuzz](https://github.com/google/honggfuzz) — Repositório oficial do Honggfuzz no GitHub com código-fonte, wrappers hfuzz_cc, exemplos e documentação.; consultado em 2026-10-03.
