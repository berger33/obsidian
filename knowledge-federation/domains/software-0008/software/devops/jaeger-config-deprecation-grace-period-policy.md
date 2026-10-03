---
id: software.devops.tranche01.000084
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://github.com/jaegertracing/jaeger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Garantia de compatibilidade de configuração: carência mínima de 3 meses ou duas versões menores

## Em uma frase
A seção Version Compatibility Guarantees do README oficial explica que, quando uma opção de configuração no Jaeger (ou flag de CLI da v1) precisa ser depreciada, a documentação ou as notas de release exibem o aviso padronizado `(deprecated, will be removed after yyyy-mm-dd or in release vX.Y.Z, whichever is later)`, garantindo um período de carência de **pelo menos 3 meses** ou **dois incrementos de versão menor (two minor version bumps)** — o que ocorrer por último — antes que a opção possa ser removida.

## Por que importa
Em plataformas que atualizam coletores e serviços de tracing continuamente, ter uma regra matemática clara ("o que ocorrer por último entre 3 meses e 2 versões menores") impede que uma equipe que atualiza duas versões menores num único mês (ou que pula uma atualização trimestral) tenha sua configuração quebrada sem aviso prévio.

## Como funciona
Ao planejar o upgrade do Jaeger, procure a string `deprecated, will be removed after` nas notas de release e migre qualquer opção depreciada dentro da janela garantida de 3 meses / 2 versões menores.

## Exemplo
O próprio README traz um exemplo concreto: se a `v2.0.0` for lançada em `01-Sep-2024` com um aviso de depreciação, a opção permanecerá depreciada até o que ocorrer por último entre `01-Dec-2024` e o lançamento da `v2.2.0`, só podendo ser removida nessa data/versão ou depois.

## Limites e trade-offs
Desenvolvedores que introduzem uma depreciação no código do Jaeger são obrigados a seguir as diretrizes detalhadas em `./CONTRIBUTING.md#deprecating-cli-flags`.

## Como verificar
Conferi a seção Version Compatibility Guarantees no README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-architecture-components-and-data-flow]] — Veja também: Arquitetura de componentes do Jaeger: OpenTelemetry SDK, Collector, Storage/Plugin, Query Service e UI.
- [[jaeger-go-version-policy-and-internal-packages]] — Veja também: Política de versões do Go (N como mínimo e remoção de N-1) e pacotes movidos para `internal`.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
