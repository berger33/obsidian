---
id: software.testes.tranche24.001859
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

# Núcleo assíncrono, APIs sync e async — e a letra miúda

## Em uma frase
As Features declaram "Fully asynchronous core with synchronous and asynchronous APIs" e "Parallel test execution", e a página carrega os metadados públicos: httpmock 0.8.3 (13 de setembro de 2026), licença MIT, owner alexliesenfeld no crates.io, repositório github.com/httpmock/httpmock — e a frase de garantia: "distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE"; detalhamento da API remete ao site oficial httpmock.rs, e exemplos adicionais ao diretório de testes blob/master/tests da própria crate.

## Por que importa
A arquitetura explica o encaixe em qualquer teste Rust: o núcleo é tokio/async por natureza (hyper 1.x na árvore de dependências da página), mas expõe API síncrona para testes que não querem runtime — o mesmo motor, duas superfícies — com execução paralela declarada como feature, o requisito silencioso de suítes de teste que sobem um servidor por teste em portas aleatórias.

## Como funciona
Em suíte de integração, cada #[tokio::test] ou teste bloqueante cria seu MockServer::start() independentemente — a paralelização é suportada sem orquestração de porta fixa; para comportamento fino, os testes da própria crate (diretório tests/) funcionam como corpus de exemplos verificados.

## Exemplo
A página docs.rs também mede "8.19% of the crate is documented" — dado bruto do próprio indexador sobre a versão 0.8.3; quem depende da doc embutida deve esperar encontrar a API no site oficial e nos exemplos citados.

## Limites e trade-offs
O selo MIT/sem-garantia é o texto da crate; a nota não especula sobre política de segurança ou roadmap além do publicado nos links oficiais.

## Como verificar
Os itens de Features, o rodapé de licença e os metadados da página docs.rs compõem a nota.

## Conexões
- [[httpmock-standalone-yaml]] — Veja também: Standalone mode com Docker e mocks em YAML.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
