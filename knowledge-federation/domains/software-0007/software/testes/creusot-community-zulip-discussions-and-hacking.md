---
id: software.testes.tranche25.001919
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
fontes: ["https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md", "https://github.com/creusot-rs/creusot"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Comunidade no Zulip do Why3, GitHub Discussions e guia CONTRIBUTING.md

## Em uma frase
As seções Help and Discussion e Hacking on Creusot apontam os canais oficiais de interação e desenvolvimento: o fórum GitHub Discussions (github.com/creusot-rs/creusot/discussions), o canal #creusot dentro do chat Zulip da comunidade Why3 (why3.zulipchat.com/#narrow/channel/341707-creusot) e o arquivo CONTRIBUTING.md com o fluxo de trabalho para quem deseja desenvolver o próprio código-fonte do Creusot.

## Por que importa
Como o Creusot descarrega provas na plataforma Why3, hospedar o chat em tempo real no mesmo servidor Zulip do Why3 aproxima os usuários do verificador Rust dos especialistas em Coma, Why3 e provadores SMT.

## Como funciona
Use o GitHub Discussions ou o canal #creusot no Zulip do Why3 quando travar numa prova ou quiser discutir modelagem de especificações, e leia o CONTRIBUTING.md antes de modificar o compilador ou a biblioteca creusot-std.

## Exemplo
Uma dúvida sobre como estruturar um invariante de laço ou por que um solver não descarregou uma VC em Coma é encaminhada ao Discussions ou ao canal #creusot no why3.zulipchat.com.

## Limites e trade-offs
Os canais comunitários não representam suporte comercial com SLA; são fóruns colaborativos mantidos pelos pesquisadores e desenvolvedores do projeto.

## Como verificar
Conferi as seções Help and Discussion e Hacking on Creusot no README oficial.

## Conexões
- [[creusot-learning-resources-guide-api-tutorial]] — Veja também: Trinca de aprendizado oficial: Guide, API creusot-std, Tutorial e Devlog.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
