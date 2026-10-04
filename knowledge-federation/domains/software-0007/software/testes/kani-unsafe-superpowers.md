---
id: software.testes.tranche24.001781
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

# Onde o compilador não olha: os blocos unsafe

## Em uma frase
O README posiciona o Kani como particularmente útil para verificar código em blocos unsafe, onde as "unsafe superpowers" do Rust são explicitamente não verificadas pelo compilador — a ferramenta checa automaticamente muitas formas de comportamento indefinido, seguindo a classificação documentada na página oficial de undefined behaviour do projeto.

## Por que importa
O contrato de segurança do Rust transfere para o programador toda a responsabilidade dentro de unsafe; testes unitários normais raramente pegam a dereferência de ponteiro fora dos limites no input certo — um model checker que trata UB como propriedade de primeira classe é a contraparte sistemática dessa transferência.

## Como funciona
Delimite a superfície do bloco unsafe, exponha uma função de verificação que chame o caminho inseguro com entradas não-determinísticas e deixe o Kani procurar UB; cada padrão de ponteiro, slice ou cast precisa estar exercitável pelo harness.

## Exemplo
Para um wrapper de FFI que interpreta um buffer de bytes recebido, o harness recebe a largura e o conteúdo como kani::any() e chama o parsing — ponteiros desalinhados e leituras fora do buffer deixam de depender de sorte de fuzzing.

## Limites e trade-offs
O README diz que "muitas formas" de UB são checadas — não todas; a página de undefined behaviour do livro enumera o escopo real, e o harness pode não alcançar certas construções se elas dependerem de estado externo não modelado.

## Como verificar
Conferi o bloco de Safety do README e o link oficial para undefined-behaviour.html que ele usa como definição do escopo.

## Conexões
- [[kani-what-it-is]] — Veja também: Kani: model checker bit-preciso para o Rust.
- [[kani-automatic-checks]] — Veja também: O que a ferramenta checa mesmo sem você pedir.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
