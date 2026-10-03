---
id: software.devops.tranche02.000166
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
fontes: ["https://raw.githubusercontent.com/grafana/loki/main/README.md", "https://grafana.com/docs/loki/latest/get-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Seções essenciais da documentação: API de ingestão, Labels, Docker Driver Client e Grafana

## Em uma frase
A seção `Documentation` do README aponta para a documentação da versão estável (`grafana.com/docs/loki/latest/`) e da próxima release (`grafana.com/docs/loki/next/`) e destaca entre as seções mais utilizadas: `API documentation` (para enviar logs ao Loki), `Labels` (`getting-started/labels/`), `Operations`, `Docker Driver Client` (plugin do Docker para enviar logs diretamente de contêineres Docker ao Loki) e `Loki in Grafana` (configuração do datasource Loki no Grafana).

## Por que importa
Conhecer tanto a API HTTP de ingestão quanto o plugin `Docker Driver Client` e o guia oficial de `Labels` permite integrar desde hosts Docker simples até clusters Kubernetes completos sem cair na armadilha de cardinalidade alta de labels.

## Como funciona
Consulte o guia `Labels` antes de definir regras de extração de metadados nos agentes e utilize o `Docker Driver Client` quando precisar coletar logs diretamente de hosts Docker sem instalar um agente separado.

## Exemplo
Em uma máquina virtual que executa apenas contêineres via Docker Compose, o operador configura o `Docker Driver Client` para encaminhar os logs diretamente à API do Loki.

## Limites e trade-offs
Alterar o esquema de labels exige atenção nas consultas e alertas existentes no Grafana; documente o dicionário de labels da plataforma.

## Como verificar
Conferi a seção Documentation no README oficial de `grafana/loki`.

## Conexões
- [[loki-helm-chart-migration-march-2026]] — Veja também: Migração do Helm chart do Grafana Loki em março de 2026 para grafana-community/helm-charts.
- [[loki-logcli-and-loki-canary-auditing]] — Veja também: Operação e verificação: interface de linha de comando LogCLI e monitoramento com Loki Canary.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki Documentation — Get Started & Operations](https://grafana.com/docs/loki/latest/get-started/) — Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.; consultado em 2026-10-03.
