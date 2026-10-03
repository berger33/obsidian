---
id: software.testes.tranche24.001783
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
fontes: ["https://raw.githubusercontent.com/model-checking/kani/main/README.md", "https://model-checking.github.io/kani/kani-tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação: cargo install mais o setup explícito

## Em uma frase
A instalação oficial tem dois passos: "cargo install --locked kani-verifier" seguido de "cargo kani setup", com o README fixando o chão de versão — Rust 1.58 ou mais novo, em Linux ou Mac — e apontando o guia de instalação do livro para os detalhes.

## Por que importa
O --locked não é decorativo: congela a árvore de dependências da ferramenta na versão testada pelos mantenedores, e o passo de setup separado explica que o Kani traz componentes próprios (o solver e o CBMC) que a instalação do crate sozinha não resolveria.

## Como funciona
Instale a ferramenta do canal normal do Rust, rode o setup uma vez por máquina (ou por imagem de CI), e em Docker fixe uma imagem com o toolchain >= 1.58; quem usa Windows não encontra o suporte declarado no README e precisa de alternativa.

## Exemplo
cargo install --locked kani-verifier && cargo kani setup; na sequência, "cargo kani" dentro do crate já resolve o harness — o README mostra exatamente esse par de comandos como única preparação necessária.

## Limites e trade-offs
O README lista apenas Linux e Mac como plataformas; para container ou outros ambientes, a referência canônica é o install guide linkado, que o README cobre só por apontamento.

## Como verificar
Os dois comandos, o piso 1.58 e as plataformas constam da seção Installation do README oficial.

## Conexões
- [[kani-automatic-checks]] — Veja também: O que a ferramenta checa mesmo sem você pedir.
- [[kani-proof-harness]] — Veja também: O harness de prova: kani::any e assert.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
