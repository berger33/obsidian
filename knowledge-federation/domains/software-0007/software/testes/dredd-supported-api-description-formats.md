---
id: software.testes.tranche25.001921
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

# Os três formatos de descrição de API: API Blueprint, OpenAPI 2 e OpenAPI 3 experimental

## Em uma frase
Na subseção Supported API Description Formats, o README lista os três formatos aceitos pelo Dredd: API Blueprint (apiblueprint.org), OpenAPI 2 (anteriormente conhecido como Swagger, versão 2.0) e OpenAPI 3 — este último acompanhado da nota explícita "(experimental, contributions welcome!)" com link para o documento STATUS.md do parser no repositório api-elements.js.

## Por que importa
Equipes trabalham tanto com especificações em Markdown (API Blueprint) quanto com contratos em YAML/JSON (Swagger/OpenAPI); saber de antemão que API Blueprint e OpenAPI 2 têm suporte maduro enquanto OpenAPI 3 é marcado como experimental evita surpresas ao adotar recursos avançados do OpenAPI 3.

## Como funciona
Use arquivos API Blueprint (.apib) ou OpenAPI 2 (Swagger 2.0) diretamente no fluxo padrão do Dredd; ao validar especificações em OpenAPI 3, consulte antes o arquivo STATUS.md do openapi3-parser linkado no README para conferir quais construções da especificação já são suportadas.

## Exemplo
No próprio Quick Start do README, o primeiro exemplo cria um arquivo API Blueprint chamado api-description.apib a partir do tutorial ou dos exemplos oficiais do API Blueprint.

## Limites e trade-offs
A marcação experimental do OpenAPI 3 é declarada pelo próprio README oficial; recursos não implementados no parser de OpenAPI 3 podem exigir ajustes na especificação ou uso de hooks.

## Como verificar
Conferi a subseção Supported API Description Formats no README oficial do Dredd.

## Conexões
- [[dredd-what-it-is]] — Veja também: Dredd: validar o documento de descrição da API contra a implementação do backend.
- [[dredd-language-agnostic-architecture]] — Veja também: CLI agnóstico de linguagem de backend: testar qualquer stack HTTP.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Dredd — documentação oficial (en/latest)](https://dredd.org/en/latest/) — Documentação oficial do Dredd sobre funcionamento, formatos de especificação, hooks multi-linguagem e integração contínua.; consultado em 2026-10-03.
