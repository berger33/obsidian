---
id: software.devops.tranche15.001414
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

# Kepler: atribuição de potência e energia por container e Pod (`kepler_container_cpu_watts` e `joules_total`)

## Em uma frase
O Kepler atribui a potência ativa do nó aos containers e Pods em execução proporcionalmente ao tempo de CPU e uso de GPU de cada container, exportando métricas como `kepler_container_cpu_watts`, `kepler_container_cpu_joules_total` e `kepler_container_gpu_watts`.

## Por que importa
Em clusters multi-tenant compartilhados por dezenas de microsserviços, medir apenas a energia total do nó não diz qual equipe ou serviço é responsável pelo consumo elétrico; a atribuição por container viabiliza *showback* e *chargeback* energético por Pod.

## Como funciona
O Kepler monitora o tempo total de CPU em modo usuário e sistema de cada container (`kepler_container_cpu_seconds_total`) e distribui a energia ativa medida em cada zona RAPL entre os containers ativos, anexando os rótulos `container_id`, `container_name`, `pod_id`, `runtime`, `state`, `zone` e `node_name`.

## Exemplo
```promql
# Top 10 containers por consumo médio de potência (Watts) na zona package
topk(10, sum by (container_name, pod_id, node_name) (
  kepler_container_cpu_watts{zone="package"}
))
```

## Limites e trade-offs
Na arquitetura `0.10.0+`, a atribuição de potência para workloads baseia-se no uso ativo de CPU (não dividindo mais os containers em métricas separadas de `idle`/`dynamic` por container como ocorria na série `0.9.x`).

## Como verificar
Execute uma carga sintética de CPU em um Pod de teste e observe a subida imediata de `kepler_container_cpu_watts{zone="package"}` para aquele `container_name`.

## Conexões
- [[kepler-metricas-nivel-no-active-idle-joules-watts-cpu-usage]] — Veja também: Kepler: métricas de energia e potência de CPU no nível do nó (`active`, `idle`, `joules_total` e `watts`).
- [[kepler-monitoramento-gpu-nvidia-active-idle-watts-joules]] — Veja também: Kepler: monitoramento energético de GPUs (`kepler_node_gpu_*`, `kepler_container_gpu_*` e `kepler_process_gpu_*`).

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
