---
id: software.testes.tranche25.001929
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

# Contribuição ao projeto e criação de novos runners de hooks

## Em uma frase
O README convida contribuições em três pontos explícitos: nas Contributor's Guidelines gerais (https://dredd.org/en/latest/contributing/), no suporte experimental a OpenAPI 3 ("contributions welcome!" com link para o parser em api-elements.js) e na lista de linguagens de hooks ("Didn't find your favorite language? Add a new one!" apontando para https://dredd.org/en/latest/hooks-new-language/).

## Por que importa
A arquitetura desacoplada entre o núcleo do Dredd e os servidores de hooks por linguagem permite que a comunidade adicione suporte a uma nova linguagem de backend implementando o protocolo de hooks, sem precisar reescrever o motor principal do Dredd.

## Como funciona
Se quiser contribuir com o núcleo ou com a documentação, siga dredd.org/en/latest/contributing/; se precisar de hooks em uma linguagem ainda não listada entre as sete oficiais, implemente um handler seguindo a especificação em dredd.org/en/latest/hooks-new-language/.

## Exemplo
Um time que utiliza uma linguagem de backend fora da lista Go/Node/Perl/PHP/Python/Ruby/Rust pode seguir o guia hooks-new-language para integrar seu próprio executor de setup/teardown ao ciclo do Dredd.

## Limites e trade-offs
Esta nota registra apenas os caminhos de extensão e contribuição declarados no README oficial; os detalhes do protocolo de socket/mensagens de hooks estão no documento hooks-new-language linkado.

## Como verificar
Conferi os links de Contributor's Guidelines, OpenAPI 3 e hooks-new-language no README oficial.

## Conexões
- [[dredd-documentation-and-changelog-channels]] — Veja também: Canais oficiais de referência: dredd.org/en/latest e releases no GitHub.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Dredd — documentação oficial (en/latest)](https://dredd.org/en/latest/) — Documentação oficial do Dredd sobre funcionamento, formatos de especificação, hooks multi-linguagem e integração contínua.; consultado em 2026-10-03.
