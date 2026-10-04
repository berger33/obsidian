---
id: software.testes.tranche25.001912
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
fontes: ["https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md", "https://guide.creusot.rs/installation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dois degraus de verificação: ausência de panics/overflows e correção funcional por anotações

## Em uma frase
O README separa a proposta de valor em duas frases complementares: primeiro, verificar que o código é seguro contra panics, overflows e falhas de asserção; segundo, "By adding annotations you can take it further and verify your code does the correct thing".

## Por que importa
Essa escada gradual permite adotar o verificador em etapas: uma equipe pode começar provando apenas que um módulo crítico não sofre panic por índice fora de faixa nem overflow inteiro, e só depois investir em especificações completas de pré e pós-condição nas funções centrais.

## Como funciona
Comece rodando o verificador sobre funções pequenas para eliminar possibilidades de panic e overflow aritmético; em seguida, consulte o guia oficial (guide.creusot.rs) e a referência da biblioteca padrão de especificação (doc.creusot.rs/creusot_std) para adicionar anotações de contrato.

## Exemplo
Nos exemplos do próprio repositório, all_zero.rs prova que zerar um vetor realmente deixa todos os elementos iguais a zero, indo além da mera ausência de panic no acesso por índice.

## Limites e trade-offs
Mesmo para provar apenas ausência de panic dentro de um laço ou chamada auxiliar, o verificador dedutivo frequentemente precisa de invariantes de laço ou pré-condições anotadas para saber quais valores os índices podem assumir.

## Como verificar
Conferi a seção About e os links de Guide e API (creusot_std) no topo do README oficial.

## Conexões
- [[creusot-coma-and-why3-pipeline]] — Veja também: A arquitetura de tradução: de Rust para Coma e a plataforma Why3.
- [[creusot-canonical-examples-suite]] — Veja também: Os cinco exemplos de entrada na suíte oficial do repositório.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Creusot Guide — Installation e documentação oficial](https://guide.creusot.rs/installation.html) — Guia oficial do Creusot sobre instalação, linguagem de especificação e uso com cargo creusot.; consultado em 2026-10-03.
