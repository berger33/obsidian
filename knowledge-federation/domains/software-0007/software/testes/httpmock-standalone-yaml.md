---
id: software.testes.tranche24.001858
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

# Standalone mode com Docker e mocks em YAML

## Em uma frase
A lista de Features da crate inclui "Standalone mode with an accompanying Docker image" — linkando hub.docker.com/r/httpmock/httpmock — e "Support for mock configuration using YAML files", com destino apontado na própria crate para a seção "file-based mock specification" no repositório httpmock/httpmock.

## Por que importa
O modo standalone muda quem consome a biblioteca: o mock server deixa de ser código de teste em Rust e vira contêiner de infra de teste que qualquer serviço — poliglota, shell, smoke manual — pode apontar, configurado por YAML sem recompilar nada.

## Como funciona
Para um contrato compartilhado entre frontend, backend Go e serviço Python, suba o httpmock standalone via Docker com a especificação YAML dos mocks; cada equipe testa contra o mesmo arquivo de contrato.

## Exemplo
Os links da página de features definem os dois destinos: a imagem no Docker Hub e a especificação de mocks por arquivo na página do repositório — o exemplo YAML concreto mora lá, não na doc da crate.

## Limites e trade-offs
A página da crate lista as capacidades e aponta os destinos; o formato do YAML, opções da imagem e variáveis de ambiente não constam do material lido nesta nota.

## Como verificar
As duas features (standalone/Docker e YAML) e seus links aparecem na seção Features da página docs.rs oficial.

## Conexões
- [[httpmock-forward-proxy]] — Veja também: Forward e Proxy mode: o mock que sabe encaminhar.
- [[httpmock-async-license-meta]] — Veja também: Núcleo assíncrono, APIs sync e async — e a letra miúda.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
