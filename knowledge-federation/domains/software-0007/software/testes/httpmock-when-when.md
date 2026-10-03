---
id: software.testes.tranche24.001852
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://docs.rs/httpmock/latest/httpmock/", "https://github.com/httpmock/httpmock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# When: as condições que o request tem que satisfazer

## Em uma frase
A página da crate define o struct When como "the conditions that an incoming HTTP request must satisfy to be handled by the mock server", e o sumário do Getting Started mostra os matchers de base: method(GET), path("/translate") e query_param("word", "hello"), com os helpers embutidos listados nas Features: Regex, JSON, serde, cookies "and more", além de "Custom request matchers" como capacidade declarada.

## Por que importa
O núcleo da utilidade de um mock é a seletividade: responder certo a um request e ignorar o resto é o que permite que um mesmo servidor teste múltiplos estados de um cliente (auth presente vs. ausente, payload válido vs. corrompido) sem virar uma suíte de condicionais.

## Como funciona
Combine matchers simples por encadeamento no builder when (método, caminho, query, headers e corpo conforme os helpers) e, para formas de igualdade fora dos helpers, escreva matcher customizado — o type alias Regex (= regex::Regex) da crate facilita o caminho de padrão sobre texto.

## Exemplo
O exemplo usa o matcher mais simples com dois campos (query_param chave=valor); a página do struct When no docs.rs linkada pelo próprio erro de assert documenta cada matcher individualmente.

## Limites e trade-offs
A lista de Features nomeia as famílias de matcher (Regex, JSON, serde, cookies) sem enumerar todos os métodos do builder; a referência por método é a página do struct, não a lista.

## Como verificar
A definição do struct vem da lista de itens da crate e os matchers do exemplo e das Features da página oficial no docs.rs.

## Conexões
- [[httpmock-getting-started]] — Veja também: Getting Started: dev-dependency e o exemplo canônico.
- [[httpmock-then-and-response]] — Veja também: Then: a resposta predeterminada.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
