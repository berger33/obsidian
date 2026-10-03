---
id: software.devops.tranche15.001413
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
fontes: ["https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md", "https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md", "https://github.com/sustainable-computing-io/kepler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kepler: métricas de energia e potência de CPU no nível do nó (`active`, `idle`, `joules_total` e `watts`)

## Em uma frase
No nível de nó, o Kepler exporta contadores cumulativos em Joules (`_joules_total`) e gauges instantâneos em Watts (`_watts`) subdivididos entre consumo total, estado ativo (`active`) e estado ocioso (`idle`), além da taxa de utilização `kepler_node_cpu_usage_ratio`.

## Por que importa
Separar o consumo energético basal de um servidor ocioso (`idle`) do consumo adicional provocado pelo processamento de cargas de trabalho (`active`) permite identificar servidores subutilizados que desperdiçam energia apenas por estarem ligados.

## Como funciona
Para cada zona detectada e caminho de sysfs (`path`), o Kepler publica `kepler_node_cpu_joules_total`, `kepler_node_cpu_active_joules_total` e `kepler_node_cpu_idle_joules_total` (tipo `COUNTER`), bem como seus equivalentes instantâneos `kepler_node_cpu_watts`, `kepler_node_cpu_active_watts` e `kepler_node_cpu_idle_watts` (tipo `GAUGE`), todos enriquecidos com o label constante `node_name` e metadados de hardware em `kepler_node_cpu_info`.

## Exemplo
```promql
# Proporção da potência de CPU gasta em trabalho ativo no pacote da CPU
kepler_node_cpu_active_watts{zone="package"}
  /
kepler_node_cpu_watts{zone="package"}
```

## Limites e trade-offs
Em máquinas virtuais de nuvem pública onde o hipervisor bloqueia o acesso aos registradores MSR/powercap (`RAPL`) do host físico, as zonas de hardware podem não estar disponíveis diretamente sem estimadores ou exposição de contadores pelo provedor.

## Como verificar
Verifique a presença de `kepler_node_cpu_info` e `kepler_node_cpu_usage_ratio` (valor entre `0.0` e `1.0`) no endpoint `/metrics` de cada nó.

## Conexões
- [[kepler-zonas-energia-rapl-psys-package-core-uncore-dram]] — Veja também: Kepler: zonas de energia RAPL (`psys`, `package`, `core`, `uncore`, `dram`) e regra de não soma.
- [[kepler-metricas-containers-pods-atribuicao-energia-cpu-gpu]] — Veja também: Kepler: atribuição de potência e energia por container e Pod (`kepler_container_cpu_watts` e `joules_total`).

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
