---
id: software.devops.tranche07.000607
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/grafana/mimir/main/README.md", "https://grafana.com/docs/mimir/latest/references/architecture/components.md", "https://github.com/grafana/mimir"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Mimir: Ruler e Alertmanager opcionais para avaliação de regras e alertas multi-tenant

## Em uma frase
Os componentes opcionais `ruler` e `alertmanager` do Grafana Mimir avaliam regras de gravação (recording rules) e regras de alerta por tenant de forma distribuída e altamente disponível sobre o armazenamento global.

## Por que importa
Quando métricas de múltiplos clusters Kubernetes são centralizadas no Grafana Mimir, avaliar regras de gravação e alertas diretamente nos servidores Prometheus locais impede correlações globais entre regiões e exige sincronizar arquivos de regras em dezenas de instâncias. Segundo a documentação de arquitetura do Mimir, os módulos `ruler` e `alertmanager` integram a avaliação de regras e o roteamento de notificações diretamente à arquitetura escalável e multi-tenant do Mimir.

## Como funciona
O componente `ruler` armazena os grupos de regras de cada tenant no object storage e utiliza um hash ring próprio para distribuir os grupos de regras entre as réplicas de `ruler` disponíveis no cluster, avaliando periodicamente as expressões PromQL (internamente ou despachando para o `query-frontend`) e gravando as séries resultantes de volta no caminho de escrita dos `ingesters`. Quando uma regra de alerta dispara, o `ruler` notifica o `alertmanager` multi-tenant do Mimir, que também opera em cluster replicado via hash ring e memberlist, deduplicando alertas, aplicando silenciamentos (`silences`), agrupamentos e enviando notificações para receptores externos (Slack, PagerDuty, Webhook) conforme a configuração individual de cada tenant.

## Exemplo
```bash
# Uso da CLI mimirtool para carregar regras e configuração de Alertmanager de um tenant
mimirtool rules load ./regras-slo.yaml \
  --address=http://localhost:8080 \
  --id=tenant-producao

mimirtool alertmanager load ./alertmanager-tenant.yaml \
  --address=http://localhost:8080/alertmanager \
  --id=tenant-producao
```

## Limites e trade-offs
Avaliar milhares de regras pesadas simultaneamente no `ruler` em intervalos curtos (como 15s) pode gerar picos periódicos de leitura e escrita no cluster Mimir; para evitar que o `ruler` sobrecarregue os `ingesters` ou `store-gateways`, recomenda-se configurar o `ruler` para enviar suas consultas através do `query-frontend` (`-ruler.query-frontend.address`), aproveitando o cache, o escalonamento de filas e a paralelização de consultas.

## Como verificar
Execute `mimirtool rules check` e `mimirtool rules list` contra o endpoint do `ruler`, e inspecione `/ruler/ring` e `/multitenant_alertmanager/ring` para confirmar que os grupos de regras e os estados de alerta estão distribuídos e ativos.

## Conexões
- [[mimir-multi-tenancy-isolamento-limites-overrides-exporter]] — Veja também: Grafana Mimir: multi-tenancy nativo, isolamento por X-Scope-OrgID, limites de QoS e Overrides-Exporter.
- [[mimir-motor-consulta-promql-otimizacoes-memoria]] — Veja também: Grafana Mimir: motor de consulta PromQL do Mimir (MQE) e redução de consumo de memória.
- [[mimir-caminho-leitura-query-frontend-scheduler-querier-sharding]] — Referência cruzada direta com mimir-caminho-leitura-query-frontend-scheduler-querier-sharding.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
