---
id: software.devops.tranche01.000086
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
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://www.jaegertracing.io/docs/latest/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Princípios da política de suporte a backends de armazenamento e a diferença entre suporte e presença no CI

## Em uma frase
A seção Storage Backend Version Support Policy do README oficial estabelece como o Jaeger define quais versões de bancos de dados são suportadas para uso em produção: para backends com ciclo de vida upstream publicado, o Jaeger baseia sua política na janela de suporte/EOL do próprio projeto ou fornecedor do banco; para backends sem ciclo claro, cobre a versão maior estável atual e a imediatamente anterior; e enfatiza que **cobertura de CI não é a matriz definitiva de suporte** ("CI coverage alone does not make a backend version supported").

## Por que importa
Muitas equipes olham um arquivo de workflow do GitHub Actions do Jaeger, veem um container de banco de dados antigo rodando em best-effort e assumem que aquela versão tem suporte oficial; o README deixa claro que, uma vez encerrado o suporte upstream do banco, o Jaeger pode remover a cobertura de CI, parar de corrigir problemas específicos daquela versão e exigir upgrade antes de investigar chamados.

## Como funciona
Ao escolher e atualizar o banco de dados de traces do Jaeger em produção, alinhe sua versão às linhas ativamente suportadas pelo upstream do banco (e pela tabela da política do Jaeger), sem usar a presença eventual de uma imagem antiga no CI como garantia de suporte.

## Exemplo
A política também esclarece os limites de responsabilidade: o projeto Jaeger garante correções proativas de compatibilidade para versões cobertas, mas não fornece suporte para o produto de banco de dados em si, distribuições específicas de fornecedores ou versões fora da janela de manutenção upstream.

## Limites e trade-offs
Versões mais antigas mantidas apenas em regime best-effort podem ser removidas assim que bloquearem o desenvolvimento, correções de segurança, atualizações de dependências ou a confiabilidade do CI.

## Como verificar
Conferi os parágrafos gerais da seção Storage Backend Version Support Policy no README oficial.

## Conexões
- [[jaeger-go-version-policy-and-internal-packages]] — Veja também: Política de versões do Go (N como mínimo e remoção de N-1) e pacotes movidos para `internal`.
- [[jaeger-elasticsearch-and-opensearch-support-matrix]] — Veja também: Suporte oficial a Elasticsearch e OpenSearch no Jaeger: alinhamento às políticas de EOL e manutenção.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Jaeger — Getting Started Guide oficial](https://www.jaegertracing.io/docs/latest/getting-started/) — Guia oficial Getting Started da documentação do Jaeger para implantação e uso da plataforma de tracing distribuído.; consultado em 2026-10-03.
