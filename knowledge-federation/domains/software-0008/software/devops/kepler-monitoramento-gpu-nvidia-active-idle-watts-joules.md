---
id: software.devops.tranche15.001415
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

# Kepler: monitoramento energético de GPUs (`kepler_node_gpu_*`, `kepler_container_gpu_*` e `kepler_process_gpu_*`)

## Em uma frase
O Kepler oferece suporte ao monitoramento de energia e potência de GPUs (como aceleradores NVIDIA), detalhando o consumo total, ativo e ocioso por GPU física e atribuindo o gasto energético aos containers e processos consumidores.

## Por que importa
Em clusters de treinamento e inferência de LLMs, as GPUs frequentemente representam mais de 70% do consumo elétrico total do servidor; monitorar apenas a CPU subestimaria drasticamente o custo energético das cargas de IA.

## Como funciona
No nível do nó, o Kepler exporta `kepler_node_gpu_watts`, `kepler_node_gpu_active_watts` (total menos idle), `kepler_node_gpu_idle_watts` (mínimo autodetectado) e seus contadores `_joules_total`, rotulados com `gpu`, `gpu_uuid`, `gpu_name` e `vendor`. No nível de workload, atribui esse consumo em `kepler_container_gpu_watts` e `kepler_process_gpu_watts`.

## Exemplo
```promql
# Potência total e ativa por GPU física no cluster
kepler_node_gpu_watts
kepler_node_gpu_active_watts
```

## Limites e trade-offs
O suporte a GPU e medidores adicionais como HWMon e Redfish BMC na série `0.10.0+` depende da exposição dos drivers e bibliotecas de telemetria do fabricante (como NVML para NVIDIA) no nó monitorado.

## Como verificar
Consulte `curl -s http://localhost:28282/metrics | grep kepler_node_gpu_` em um nó com GPU para validar a detecção de `gpu_uuid` e `gpu_name`.

## Conexões
- [[kepler-metricas-containers-pods-atribuicao-energia-cpu-gpu]] — Veja também: Kepler: atribuição de potência e energia por container e Pod (`kepler_container_cpu_watts` e `joules_total`).
- [[kepler-metricas-processos-maquinas-virtuais-kvm-kubevirt]] — Veja também: Kepler: visibilidade energética por processo Linux (`kepler_process_*`) e máquinas virtuais (`kepler_vm_*`).

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
