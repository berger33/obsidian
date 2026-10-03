---
id: software.devops.tranche01.000085
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

# Política de versões do Go (N como mínimo e remoção de N-1) e pacotes movidos para `internal`

## Em uma frase
A seção Go Version Compatibility Guarantees do README oficial documenta que, desde o Go 1.21, o suporte a versões do Go no Jaeger segue duas regras após o lançamento de uma nova versão menor `N` do Go: (1) logo após o lançamento de `N`, o build e os testes são atualizados para acomodar a versão `N`; e (2) logo após o lançamento de `N`, o suporte para a versão `N-1` é removido e `N` torna-se a versão mínima exigida — explicando na nota que todo o código importável foi movido para pacotes `internal`, de modo que não há mais necessidade de manter compatibilidade retroativa com compiladores mais antigos (antes mantinha-se `N-1`).

## Por que importa
Compare essa política com a do OpenTelemetry Collector vista no primeiro grupo desta tranche: como o Collector é consumido como biblioteca pública em Go, ele mantém `N` e `N-1` (removendo `N-2`); já o Jaeger moveu seu código para pacotes `internal` (não sendo uma biblioteca pública importável por terceiros) e por isso pode exigir imediatamente a versão menor `N` mais recente do Go.

## Como funciona
Ao compilar o Jaeger a partir do código-fonte ou abrir pull requests no repositório `jaegertracing/jaeger`, utilize sempre a versão menor `N` mais recente do compilador Go.

## Exemplo
Remover o suporte a uma versão antiga do Go no Jaeger não é considerado um breaking change pela política oficial do projeto.

## Limites e trade-offs
Não tente importar pacotes internos do repositório `jaegertracing/jaeger` como biblioteca externa em projetos Go, pois o projeto encapsulou o código em `internal` deliberadamente.

## Como verificar
Conferi a seção Go Version Compatibility Guarantees no README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-config-deprecation-grace-period-policy]] — Veja também: Garantia de compatibilidade de configuração: carência mínima de 3 meses ou duas versões menores.
- [[jaeger-storage-backend-support-policy-principles]] — Veja também: Princípios da política de suporte a backends de armazenamento e a diferença entre suporte e presença no CI.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
