---
id: software.testes.tranche25.001925
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
fontes: ["https://raw.githubusercontent.com/apiaryio/dredd/master/README.md", "https://github.com/apiaryio/dredd"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Suporte multiplataforma e integração com Travis CI, CircleCI, Jenkins e AppVeyor

## Em uma frase
Na subseção Supported Systems, o README declara suporte aos sistemas operacionais Linux, macOS e Windows e destaca integração com plataformas de integração contínua como Travis CI, CircleCI, Jenkins e AppVeyor — o próprio repositório do Dredd exibe no topo badges de build em CircleCI (Linux/macOS) e AppVeyor (Windows), além de verificação de vulnerabilidades no Snyk e documentação no Read the Docs.

## Por que importa
O valor principal de testar documentação contra o backend aparece quando o check roda automaticamente a cada pull request no CI; suportar Linux, macOS e Windows e os principais servidores de CI permite travar merges sempre que um endpoint deixar de corresponder à especificação.

## Como funciona
Gere a configuração do projeto com dredd init e adicione a execução do comando dredd ao pipeline de CI (CircleCI, Jenkins, AppVeyor, Travis CI ou equivalente) logo após a etapa de build do serviço HTTP.

## Exemplo
Em um pipeline de CI, o job sobe a aplicação em ambiente de teste e invoca dredd; se qualquer rota responder diferente do documento de API, o processo falha e bloqueia a publicação de documentação mentirosa.

## Limites e trade-offs
A lista da subseção Supported Systems termina com reticências ("Linux, macOS, Windows, ..." e "Travis CI, CircleCI, Jenkins, AppVeyor, ..."), indicando que qualquer ambiente capaz de rodar Node.js e alcançar o backend HTTP pode executar o CLI.

## Como verificar
Conferi o cabeçalho de badges e a subseção Supported Systems no README oficial.

## Conexões
- [[dredd-npm-install-and-quickstart-flow]] — Veja também: Instalação com npm install -g dredd e o fluxo de três passos do Quick Start.
- [[dredd-design-first-and-honest-docs-workflow]] — Veja também: O fluxo Design-First e o princípio de manter a documentação honesta.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Repositório oficial apiaryio/dredd](https://github.com/apiaryio/dredd) — Repositório oficial do Dredd no GitHub com código-fonte, releases e pipelines de CI.; consultado em 2026-10-03.
