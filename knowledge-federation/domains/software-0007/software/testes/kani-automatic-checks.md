---
id: software.testes.tranche24.001782
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

# O que a ferramenta checa mesmo sem você pedir

## Em uma frase
Além das asserções do autor do harness, o README lista os checadores automáticos do Kani: panics (o exemplo dado é unwrap() em Option::None), overflows aritméticos e propriedades de correção customizadas — estas últimas ou como assert!() ou como function contracts, marcador como recurso experimental no livro.

## Por que importa
Essa lista muda o custo de escrever provas: o harness não precisa afirmar o óbvio — o caminho de panic por unwrap e a aritmética que estoura já são violações detectadas por default, o que captura a classe de bugs que testes aleatórios encontram tarde demais.

## Como funciona
Ao escrever a prova, concentre as asserções manuais na especificação do domínio e confie que o overflow e o unwrap são monitorados; para invariantes mais fortes, considere contracts quando o projeto aceitar a marca experimental documentada.

## Exemplo
Uma função de parsing que soma offsets: com kani::any() no input, um overflow na soma é reportado como violação sem que o harness mencione aritmética — o mesmo vale para slice indices fora do limite via panic.

## Limites e trade-offs
Function contracts aparecem no README com URL da seção "experimental" do livro; tratar contratos como estáveis é extrapolar o rótulo que o próprio projeto dá a eles.

## Como verificar
Os três itens checados automaticamente e o status experimental dos contracts estão no bloco "Correctness" do README oficial.

## Conexões
- [[kani-unsafe-superpowers]] — Veja também: Onde o compilador não olha: os blocos unsafe.
- [[kani-install]] — Veja também: Instalação: cargo install mais o setup explícito.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
