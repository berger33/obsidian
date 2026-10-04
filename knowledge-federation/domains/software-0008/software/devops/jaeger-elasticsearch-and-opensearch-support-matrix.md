---
id: software.devops.tranche01.000087
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://github.com/jaegertracing/jaeger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte oficial a Elasticsearch e OpenSearch no Jaeger: alinhamento às políticas de EOL e manutenção

## Em uma frase
Na lista e na tabela da seção Storage Backend Version Support Policy (atualizada na referência de 6 de julho de 2026 do README), o Jaeger detalha a cobertura para os dois motores de busca documentais: para **Elasticsearch**, segue a Product and Version End of Life Policy da Elastic, cobrindo `9.x` e `8.19.x` (até o fim da janela publicada de manutenção da linha 8.x, deixando `8.18.x` e anteriores fora da cobertura); para **OpenSearch**, segue a Release Schedule and Maintenance Policy do OpenSearch (versão maior atual e a anterior enquanto mantidas), cobrindo `3.x` e `2.x` (com `2.19.x` como linha 2.x mantida, deixando `1.x` e anteriores fora da cobertura).

## Por que importa
Elasticsearch e OpenSearch estão entre os backends de produção mais usados com o Jaeger; saber que apenas `9.x` e a última linha `8.19.x` do Elasticsearch (e `3.x` / `2.19.x` do OpenSearch) estão no escopo de suporte proativo orienta o planejamento de upgrade dos clusters de armazenamento de observabilidade.

## Como funciona
Mantenha seus clusters Elasticsearch na série `9.x` (ou `8.19.x` dentro da janela da Elastic) e seus clusters OpenSearch em `3.x` ou na linha `2.x` mantida (`2.19.x`), consultando as páginas oficiais `elastic.co/support/eol` e `opensearch.org/releases/` referenciadas pelo Jaeger.

## Exemplo
A tabela do README explicita lado a lado as colunas `Versions covered by policy` e `Versions not covered` (`8.18.x and earlier` no Elasticsearch; `1.x and earlier` no OpenSearch).

## Limites e trade-offs
Como nota o próprio README, a tabela é informativa e acompanha a evolução das políticas e linhas de manutenção publicadas pelos respectivos projetos upstream.

## Como verificar
Conferi os itens e as linhas de Elasticsearch e OpenSearch na seção Storage Backend Version Support Policy do README oficial.

## Conexões
- [[jaeger-storage-backend-support-policy-principles]] — Veja também: Princípios da política de suporte a backends de armazenamento e a diferença entre suporte e presença no CI.
- [[jaeger-cassandra-and-clickhouse-lts-support-matrix]] — Veja também: Suporte oficial a Apache Cassandra e ClickHouse no Jaeger: versões maiores mantidas e foco em releases LTS.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
