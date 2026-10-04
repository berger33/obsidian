---
id: software.testes.tranche24.001780
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
fontes: ["https://raw.githubusercontent.com/model-checking/kani/main/README.md", "https://github.com/model-checking/kani"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kani: model checker bit-preciso para o Rust

## Em uma frase
O README oficial define o Kani Rust Verifier como "a bit-precise model checker for Rust", útil para verificar tanto segurança (safety) quanto correção do código Rust, com badges de regressão contínua e compatibilidade testada contra o CBMC mais recente.

## Por que importa
Diferente de testes que exploram entradas amostradas, um model checker bit-preciso considera a aritmética de máquina com exatidão e busca provar (ou refutar) propriedades sobre todas as execuções possíveis — encaixando exatamente onde o compilador do Rust para: nos trechos unsafe e nas invariantes que só dependência de convenção garante.

## Como funciona
O fluxo é escrever um harness de prova como função anotada, alimentar entradas não-determinísticas fornecidas pela ferramenta e deixar o verificador explorar os caminhos; cada violação de asserção, panic ou comportamento indefinido encontrado vira um contraexemplo concreto.

## Exemplo
cargo install --locked kani-verifier instala a ferramenta; dentro do crate, um harness com kani::any() cobre o domínio do tipo da entrada sem que ninguém escreva casos à mão.

## Limites e trade-offs
A nota cobre o que o README afirma; prova sobre todas as execuções depende do harness cobrir o comportamento relevante — entradas restringidas a partes do domínio ficam fora da garantia, como em qualquer verificação por harness.

## Como verificar
A definição, os dois usos (safety e correctness) e a relação com o CBMC constam das três primeiras seções do README oficial.

## Conexões
- [[kani-unsafe-superpowers]] — Veja também: Onde o compilador não olha: os blocos unsafe.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial model-checking/kani](https://github.com/model-checking/kani) — Repositório oficial do Kani Rust Verifier no GitHub com código-fonte, workflows, CITATION.cff e política de segurança.; consultado em 2026-10-03.
