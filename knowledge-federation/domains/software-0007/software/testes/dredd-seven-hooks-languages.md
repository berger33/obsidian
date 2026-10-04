---
id: software.testes.tranche25.001923
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
fontes: ["https://raw.githubusercontent.com/apiaryio/dredd/master/README.md", "https://dredd.org/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hooks para setup e teardown em sete linguagens (e guia para adicionar novas)

## Em uma frase
A subseção Supported Hooks Languages explica que o Dredd suporta a escrita de hooks — código de colagem (glue code) para o setup e teardown de cada teste — em sete linguagens com documentação própria: Go (hooks-go), Node.js/JavaScript (hooks-nodejs), Perl (hooks-perl), PHP (hooks-php), Python (hooks-python), Ruby (hooks-ruby) e Rust (hooks-rust), além de oferecer o guia "Add a new one!" (hooks-new-language) para integrar outras linguagens.

## Por que importa
Validar uma API real passo a passo quase sempre exige preparar estado no banco de dados antes de um POST/DELETE ou injetar um token de autenticação nos cabeçalhos; permitir que os hooks sejam escritos na mesma linguagem do backend (como Python, Go, PHP, Ruby ou Rust) dá acesso direto aos modelos, ORMs e fábricas de teste da aplicação.

## Como funciona
Escolha o runner de hooks correspondente à linguagem do seu backend (consultando dredd.org/en/latest/hooks-<linguagem>/) para semear dados antes das transações HTTP e limpar o estado ao final de cada teste.

## Exemplo
Em um backend escrito em Go ou Rust, a equipe escreve os hooks de banco e autenticação em Go ou Rust usando os pacotes documentados em hooks-go ou hooks-rust, sem precisar manipular o banco a partir de JavaScript.

## Limites e trade-offs
Se a linguagem do seu projeto não estiver entre as sete listadas, o protocolo de comunicação de hooks do Dredd é aberto e documentado em dredd.org/en/latest/hooks-new-language/.

## Como verificar
Conferi a subseção Supported Hooks Languages no README oficial do Dredd.

## Conexões
- [[dredd-language-agnostic-architecture]] — Veja também: CLI agnóstico de linguagem de backend: testar qualquer stack HTTP.
- [[dredd-npm-install-and-quickstart-flow]] — Veja também: Instalação com npm install -g dredd e o fluxo de três passos do Quick Start.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Dredd — documentação oficial (en/latest)](https://dredd.org/en/latest/) — Documentação oficial do Dredd sobre funcionamento, formatos de especificação, hooks multi-linguagem e integração contínua.; consultado em 2026-10-03.
