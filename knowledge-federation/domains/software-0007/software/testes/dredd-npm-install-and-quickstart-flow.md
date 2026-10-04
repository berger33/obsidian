---
id: software.testes.tranche25.001924
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

# Instalação com npm install -g dredd e o fluxo de três passos do Quick Start

## Em uma frase
As seções Installation e Quick Start mostram a entrada mais curta na ferramenta: instalar globalmente com npm install -g dredd e seguir três passos — (1) criar um arquivo de descrição (no exemplo, api-description.apib), (2) rodar a configuração interativa com dredd init e (3) executar a validação com o comando dredd.

## Por que importa
Separar a configuração inicial num assistente interativo (dredd init) gera o arquivo de configuração do projeto respondendo perguntas sobre caminho da especificação, comando para subir o servidor e linguagem de hooks, permitindo que as execuções seguintes no dia a dia e no CI sejam apenas o comando dredd sem argumentos.

## Como funciona
Instale o pacote com npm install -g dredd, crie ou posicione o documento de especificação da API na árvore do projeto, execute dredd init uma vez para gravar a configuração no repositório e rode dredd a cada alteração na API ou na documentação.

## Exemplo
Após concluir o dredd init com um arquivo api-description.apib, basta digitar dredd na raiz do projeto para reexecutar toda a bateria de validação contra o backend.

## Limites e trade-offs
Em projetos que preferem fixar a versão da ferramenta por repositório em vez de instalação global na máquina, a versão publicada no npm (visível no badge npm version do README) pode ser invocada dentro dos scripts de build do projeto.

## Como verificar
Conferi as seções Installation e Quick Start no README oficial.

## Conexões
- [[dredd-seven-hooks-languages]] — Veja também: Hooks para setup e teardown em sete linguagens (e guia para adicionar novas).
- [[dredd-interactive-init-and-ci-systems]] — Veja também: Suporte multiplataforma e integração com Travis CI, CircleCI, Jenkins e AppVeyor.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Dredd — documentação oficial (en/latest)](https://dredd.org/en/latest/) — Documentação oficial do Dredd sobre funcionamento, formatos de especificação, hooks multi-linguagem e integração contínua.; consultado em 2026-10-03.
