---
id: software.devops.tranche15.001420
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md", "https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md", "https://github.com/sustainable-computing-io/kepler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kepler: integração com KEDA, OpenCost e ambiente local Docker Compose com Prometheus e Grafana

## Em uma frase
As métricas Prometheus exportadas pelo Kepler na porta `28282` integram-se a pilhas de observabilidade (Prometheus/Grafana), ferramentas de FinOps e escalonadores orientados a eventos como o KEDA para decisões de *carbon-aware scheduling*.

## Por que importa
Permite não apenas visualizar painéis de eficiência energética, mas também automatizar ações operacionais — como escalar jobs batch quando o consumo energético do cluster está baixo ou auditar regressões de potência de código em ambientes de desenvolvimento.

## Como funciona
O repositório oficial inclui uma pilha pronta em `compose/dev` (`docker compose up -d`) que sobe o Kepler conectado ao Prometheus e Grafana locais para testes rápidos, além de binários locais (`make build && sudo ./bin/kepler`) para validação direta em servidores Linux bare-metal.

## Exemplo
```bash
kubectl get svc -n kepler
curl -s http://localhost:28282/metrics | grep -E "^kepler_(node|container)_cpu_watts"
```

## Limites e trade-offs
Em ambientes de desenvolvimento dentro de containers ou máquinas virtuais sem passthrough de contadores RAPL de CPU, o Kepler só conseguirá reportar métricas reais de energia se o kernel hospedeiro expuser `/sys/class/powercap` para o ambiente.

## Como verificar
Confirme no target discovery do Prometheus que o Service `kepler` na porta `28282` está com estado `UP` e ingerindo as famílias `kepler_node_*` e `kepler_container_*`.

## Conexões
- [[kepler-calculo-kwh-intensidade-carbono-promql-greenops]] — Veja também: Kepler: conversão de Joules para kWh e cálculo de pegada de carbono em consultas PromQL.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
