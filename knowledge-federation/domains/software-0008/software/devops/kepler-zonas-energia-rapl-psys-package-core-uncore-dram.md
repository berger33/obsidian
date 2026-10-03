---
id: software.devops.tranche15.001412
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

# Kepler: zonas de energia RAPL (`psys`, `package`, `core`, `uncore`, `dram`) e regra de não soma

## Em uma frase
As métricas de energia e potência de CPU do Kepler incluem o rótulo `zone`, que identifica o domínio físico de hardware reportado pelo medidor RAPL (*Running Average Power Limiting*) do kernel Linux.

## Por que importa
Compreender a hierarquia física das zonas RAPL é indispensável ao escrever consultas PromQL: como os domínios se sobrepõem fisicamente no processador, somar cegamente todas as zonas (`sum(kepler_node_cpu_watts)`) duplica ou triplica o consumo real do servidor.

## Como funciona
Com o medidor RAPL padrão (`powercap`), o Kepler detecta dinamicamente e exporta apenas as zonas suportadas pela CPU do host: `psys` (todo o SoC/plataforma), `package` (todo o soquete da CPU, incluindo cores, cache, controlador de memória e GPU integrada), `core` (apenas os núcleos da CPU), `uncore` (partes fora dos núcleos no pacote) e `dram` (memória acoplada ao controlador).

## Exemplo
```promql
# Correto: filtrar por uma única zona abrangente (ex.: package ou psys)
sum by (node_name) (kepler_node_cpu_watts{zone="package"})

# Comparar potência de CPU (package) com memória (dram) separadamente
kepler_node_cpu_watts{zone=~"package|dram"}
```

## Limites e trade-offs
Nunca execute agregações PromQL como `sum by (node_name) (kepler_node_cpu_watts)` sem filtrar o label `zone`, pois a zona `package` já engloba `core` e `uncore`, e `psys` engloba parte do `package`.

## Como verificar
Consulte `curl -s http://localhost:28282/metrics | grep kepler_node_cpu_watts` no nó para verificar quais valores de `zone` o processador físico daquela máquina expõe.

## Conexões
- [[kepler-arquitetura-rewrite-v010-prometheus-energy-exporter]] — Veja também: Kepler v0.10+: reescrita arquitetural do exportador Prometheus de consumo de energia para Kubernetes.
- [[kepler-metricas-nivel-no-active-idle-joules-watts-cpu-usage]] — Veja também: Kepler: métricas de energia e potência de CPU no nível do nó (`active`, `idle`, `joules_total` e `watts`).

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
