---
id: software.testes.tranche24.001786
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

# CI nativo: o action model-checking/kani-github-action

## Em uma frase
Para integração contínua, o README oficial fornece o caminho curto: usar Kani no CI com "model-checking/kani-github-action@VERSION", e a seção "GitHub Action" do livro para os detalhes de configuração.

## Por que importa
Verificação que corre uma vez na máquina do autor vira documentação morta; o pin por @VERSION permite congelar o verificador com o resto da toolchain e atualizar deliberadamente, enquanto a prova corre a cada PR que toca o código sob contrato.

## Como funciona
Adicione o step da action no workflow do GitHub (com o pin de versão explícito, não latest), e trate a falha da prova como falha de build — a mesma semântica de status que o cargo test já tem no pipeline.

## Exemplo
Um workflow YAML com uses: model-checking/kani-github-action@VERSION na sequência do cargo check — a linha de uso vem do próprio README, que é o documento canônico que o action referencia.

## Limites e trade-offs
O README não descreve inputs da action (versão do toolchain, flags do kani, tamanho de harness); o detalhe contratual está na seção do livro linkada, que esta nota apenas endereça.

## Como verificar
A existência da action, o formato de uso e o destino da documentação foram conferidos na seção "GitHub Action" do README oficial.

## Conexões
- [[kani-vs-testing]] — Veja também: Verificação com cara de teste, garantia de outra ordem.
- [[kani-citation]] — Veja também: Base acadêmica rastreável: o paper ASE 2026.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
