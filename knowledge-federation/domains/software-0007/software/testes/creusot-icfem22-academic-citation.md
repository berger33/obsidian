---
id: software.testes.tranche25.001917
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

# Base científica e citação acadêmica: publicação no ICFEM'22

## Em uma frase
Na seção Citing Creusot, o README orienta quem utiliza a ferramenta em contextos acadêmicos a citar a publicação oficial do projeto no ICFEM'22, hospedada no arquivo aberto do INRIA (https://hal.inria.fr/hal-03737878/file/main.pdf).

## Por que importa
A fundamentação teórica do Creusot — como o tratamento de empréstimos mutáveis do Rust via lógica profética sem sobrecarga de memória em tempo de execução — está formalizada nesse artigo revisado por pares, que serve tanto de citação acadêmica quanto de referência conceitual profunda.

## Como funciona
Ao publicar artigos, relatórios técnicos ou dissertações que utilizem o Creusot para verificar código Rust, inclua a referência do artigo do ICFEM'22 disponível no link do HAL-INRIA indicado no README.

## Exemplo
Enquanto ARCHITECTURE.md resume a engenharia do compilador e a tradução para Coma, o PDF do ICFEM'22 no HAL-INRIA apresenta a fundamentação formal do verificador.

## Limites e trade-offs
O artigo de 2022 descreve o modelo fundacional da ferramenta; para a sintaxe atualizada de atributos, macros de especificação e representação intermediária Coma vigente hoje, consulte o guia em guide.creusot.rs e o ARCHITECTURE.md.

## Como verificar
Conferi a seção Citing Creusot no README oficial.

## Conexões
- [[creusot-upgrading-workflow]] — Veja também: Fluxo de atualização do Creusot: git pull, opam update e ./INSTALL.
- [[creusot-learning-resources-guide-api-tutorial]] — Veja também: Trinca de aprendizado oficial: Guide, API creusot-std, Tutorial e Devlog.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
