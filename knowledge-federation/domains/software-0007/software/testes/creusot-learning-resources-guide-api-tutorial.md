---
id: software.testes.tranche25.001918
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

# Trinca de aprendizado oficial: Guide, API creusot-std, Tutorial e Devlog

## Em uma frase
O cabeçalho do README oficial organiza quatro recursos de documentação e aprendizado: o Guide em https://guide.creusot.rs (livro mdBook), a documentação da API creusot-std em https://doc.creusot.rs/creusot_std, o repositório interativo de Tutorial em https://github.com/creusot-rs/tutorial e o Devlog em https://devlog.creusot.rs (além da homepage https://creusot.rs).

## Por que importa
Quem começa em verificação dedutiva precisa de três materiais diferentes: um livro conceitual passo a passo (Guide), exercícios guiados para praticar (Tutorial) e um dicionário de tipos e predicados lógicos da biblioteca padrão (API creusot-std); o projeto separa claramente cada um.

## Como funciona
Siga o repositório creusot-rs/tutorial em paralelo à leitura de guide.creusot.rs para aprender a sintaxe de especificação e mantenha doc.creusot.rs/creusot_std aberto como referência dos contratos da biblioteca padrão durante a escrita de provas.

## Exemplo
Ao precisar saber qual especificação lógica o Creusot associa a Vec ou a iteradores na biblioteca padrão de verificação, o destino direto é doc.creusot.rs/creusot_std.

## Limites e trade-offs
O README funciona como portal para esses endereços oficiais; detalhes de cada macro de especificação e dos exercícios residem nos próprios sites e repositórios linkados.

## Como verificar
Conferi a fileira de badges e links no topo do README oficial do Creusot.

## Conexões
- [[creusot-icfem22-academic-citation]] — Veja também: Base científica e citação acadêmica: publicação no ICFEM'22.
- [[creusot-community-zulip-discussions-and-hacking]] — Veja também: Comunidade no Zulip do Why3, GitHub Discussions e guia CONTRIBUTING.md.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Creusot Guide — Installation e documentação oficial](https://guide.creusot.rs/installation.html) — Guia oficial do Creusot sobre instalação, linguagem de especificação e uso com cargo creusot.; consultado em 2026-10-03.
