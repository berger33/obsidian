---
id: software.devops.tranche02.000168
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/grafana/loki/main/README.md", "https://github.com/grafana/loki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Compilação a partir do código-fonte em Go e execução local sem dependências

## Em uma frase
A subseção `Building from source` na seção `Contributing` do README mostra que o Loki pode ser executado em um único host em modo sem dependências (`single host, no-dependencies mode`) compilando o binário com uma versão atualizada do Go (recomendando a versão definida no `Makefile` do repositório): `git clone https://github.com/grafana/loki`, `cd loki`, `go build ./cmd/loki` (ou `make` em sistemas Unix) e `./loki -config.file=./cmd/loki/loki-local-config.yaml`.

## Por que importa
Poder compilar e subir o Loki localmente em segundos com um único arquivo `./cmd/loki/loki-local-config.yaml` sem precisar provisionar Cassandra, Elasticsearch ou Object Storage externo facilita testes de integração, desenvolvimento de pipelines de coleta e reprodução de bugs.

## Como funciona
Utilize `./loki -config.file=./cmd/loki/loki-local-config.yaml` em ambientes locais de desenvolvimento ou pipelines de CI para validar configurações de agentes (como Alloy, Fluent Bit ou Vector) contra uma instância real do Loki.

## Exemplo
Um engenheiro de observabilidade sobe o Loki local com `loki-local-config.yaml` na própria estação para testar uma regra de transformação de logs antes de abrir o pull request.

## Limites e trade-offs
O arquivo `loki-local-config.yaml` usa armazenamento local voltado a desenvolvimento e testes; em produção, configure sempre armazenamento durável, limites por tenant e guia de `Upgrading` (`grafana.com/docs/loki/latest/upgrading/`).

## Como verificar
Conferi as seções Upgrading e Building from source no README oficial de `grafana/loki`.

## Conexões
- [[loki-logcli-and-loki-canary-auditing]] — Veja também: Operação e verificação: interface de linha de comando LogCLI e monitoramento com Loki Canary.
- [[loki-design-doc-and-architecture-reading]] — Veja também: Documento original de design do Loki e referências históricas de arquitetura.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki — Repositório Oficial no GitHub](https://github.com/grafana/loki) — Repositório oficial do Grafana Loki com código-fonte em Go, cmd/loki/loki-local-config.yaml e Makefile.; consultado em 2026-10-03.
