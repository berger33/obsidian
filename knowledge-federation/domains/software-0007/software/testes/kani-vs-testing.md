---
id: software.testes.tranche24.001785
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

# Verificação com cara de teste, garantia de outra ordem

## Em uma frase
A primeira linha da seção de uso do README marca o contraste: "Similar to testing, you write a harness, but with Kani you can check all possible values using kani::any()" — a mecânica de escrita se parece com a de um teste unitário, mas a garantia declarada é sobre a totalidade das entradas (dentro do tipo e das restrições), não sobre as amostras escolhidas.

## Por que importa
Times que já mantêm suítes de fuzzing com corpus reconhecem a forma; a nota ancora a decisão de ferramenta: Kani não substitui testes de integração com dados reais — ele remove a classe "a entrada que importa não foi amostrada" para a função verificada.

## Como funciona
Escolha funções puras e críticas (parsing, validação, aritmética de protocolo), escreva a prova como faria com um teste parametrizado, e mantenha os testes normais para o que envolve I/O e ambiente que o harness não modela.

## Exemplo
Uma função que decide "meets_specification" sobre bytes: com o harness, o verificador considera os 256 valores; com amostragem, cada nova versão do parser renova o azar de não testar a fronteira exata.

## Limites e trade-offs
"Todos os valores" é tipado: kani::any() gera o domínio do tipo (u8 aqui); restrição a subdomínios e precondições exigem trabalho adicional que o README do exemplo não mostra — o tutorial linkado cobre o que além disso existe.

## Como verificar
A frase de comparação com testes abre a seção "How to use Kani" do README oficial.

## Conexões
- [[kani-proof-harness]] — Veja também: O harness de prova: kani::any e assert.
- [[kani-github-action]] — Veja também: CI nativo: o action model-checking/kani-github-action.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
