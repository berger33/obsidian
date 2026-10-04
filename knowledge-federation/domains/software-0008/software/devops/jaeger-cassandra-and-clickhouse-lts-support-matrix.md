---
id: software.devops.tranche01.000088
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

# Suporte oficial a Apache Cassandra e ClickHouse no Jaeger: versões maiores mantidas e foco em releases LTS

## Em uma frase
Completando a matriz de Storage Backend Version Support Policy no README oficial, o Jaeger define as regras para **Cassandra** e **ClickHouse**: para o Apache Cassandra, acompanha as linhas de release mantidas na página oficial de downloads para a versão maior atual e a anterior — cobrindo `5.0.x` e as linhas `4.x` mantidas (`4.1.x` e `4.0.x`), excluindo `3.x` e anteriores; já para o ClickHouse, o Jaeger trata especificamente as **LTS releases** como suas linhas de suporte (cobrindo a LTS atual e a LTS anterior, que o ClickHouse mantém simultaneamente por pelo menos 12 meses — exemplificadas na tabela por `26.3 LTS` e `25.8 LTS`), deixando as releases estáveis mensais (monthly stable releases) e branches LTS mais antigas fora da cobertura da política.

## Por que importa
No caso do ClickHouse, muitas equipes instalam uma release mensal (`monthly stable`) sem perceber que a política formal do Jaeger cobre apenas as duas releases **LTS** vigentes; optar pela trilha LTS do ClickHouse alinha a operação exatamente ao alvo de suporte de 12 meses usado pelo Jaeger.

## Como funciona
Ao operar o Jaeger sobre ClickHouse em produção, implante uma versão da trilha LTS atual ou imediatamente anterior (conforme `clickhouse.com/docs/development/backports`); ao operar sobre Apache Cassandra, utilize a série `5.0.x` ou as linhas `4.0.x`/`4.1.x` mantidas pela Apache.

## Exemplo
Mesmo que uma release mensal do ClickHouse funcione tecnicamente ou apareça em testes de CI do repositório, a política do README declara expressamente que releases estáveis mensais não são cobertas pelo compromisso de suporte.

## Limites e trade-offs
Verifique periodicamente a página de downloads do Cassandra e a documentação de backports/produção do ClickHouse linkadas no README ao agendar janelas de manutenção de banco.

## Como verificar
Conferi os itens e as linhas de Cassandra e ClickHouse na seção Storage Backend Version Support Policy do README oficial.

## Conexões
- [[jaeger-elasticsearch-and-opensearch-support-matrix]] — Veja também: Suporte oficial a Elasticsearch e OpenSearch no Jaeger: alinhamento às políticas de EOL e manutenção.
- [[jaeger-security-audits-and-mechanisms]] — Veja também: Auditorias de segurança independentes (`jaegertracing/security-audits`) e resumo de mecanismos de segurança.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
