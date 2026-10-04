---
id: software.testes.tranche25.001915
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

# Instalação de usuário em cinco passos: rustup, opam, ./INSTALL e cargo creusot --help

## Em uma frase
A seção Installing Creusot as a user documenta o procedimento passo a passo: (1) instalar o rustup para obter o toolchain Rust adequado, (2) instalar o opam (gerenciador de pacotes para OCaml), (3/4) clonar https://github.com/creusot-rs/creusot e entrar na pasta creusot, (5) rodar ./INSTALL e (6) verificar o sucesso da instalação executando cargo creusot --help, remetendo também a https://guide.creusot.rs/installation.html para mais detalhes.

## Por que importa
Como o Creusot se integra ao Cargo como subcomando (cargo creusot) mas compila componentes que dependem do ecossistema Why3/OCaml, a instalação não é um simples cargo install isolado: ela exige tanto o rustup quanto o opam antes de executar o script ./INSTALL.

## Como funciona
Em uma máquina nova ou imagem de CI, instale rustup e opam primeiro, clone o repositório oficial creusot-rs/creusot, execute ./INSTALL na raiz do clone e valide o subcomando com cargo creusot --help; em caso de dúvida sobre provadores SMT externos, consulte guide.creusot.rs/installation.html.

## Exemplo
O comando de validação final após ./INSTALL é cargo creusot --help, que confirma que o binário foi registrado como subcomando do Cargo no PATH do usuário.

## Limites e trade-offs
A numeração no próprio README salta do item 2 para o 4 na lista markdown original (1, 2, 4, 5, 6); o conteúdo essencial são os quatro estágios: pré-requisitos rustup + opam, clone, ./INSTALL e checagem com cargo creusot --help.

## Como verificar
Conferi a seção Installing Creusot as a user no README oficial.

## Conexões
- [[creusot-real-world-projects-creusat-krabka]] — Veja também: Projetos reais verificados com Creusot: CreuSAT e Krabka.
- [[creusot-upgrading-workflow]] — Veja também: Fluxo de atualização do Creusot: git pull, opam update e ./INSTALL.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Creusot Guide — Installation e documentação oficial](https://guide.creusot.rs/installation.html) — Guia oficial do Creusot sobre instalação, linguagem de especificação e uso com cargo creusot.; consultado em 2026-10-03.
