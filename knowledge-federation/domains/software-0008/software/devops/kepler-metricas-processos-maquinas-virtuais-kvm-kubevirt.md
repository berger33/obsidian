---
id: software.devops.tranche15.001416
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

# Kepler: visibilidade energética por processo Linux (`kepler_process_*`) e máquinas virtuais (`kepler_vm_*`)

## Em uma frase
Além de containers Kubernetes, o Kepler exporta métricas granulares por processo individual do sistema operacional (`pid`, `comm`, `exe`) e por máquina virtual gerenciada por hipervisores no host (`vm_id`, `vm_name`, `hypervisor`).

## Por que importa
Permite auditar o gasto energético de daemons de sistema que rodam diretamente no host Linux (como `kubelet`, `containerd`, agentes de segurança e armazenamento) e de máquinas virtuais executadas via KubeVirt ou QEMU/KVM no mesmo cluster.

## Como funciona
As métricas `kepler_process_cpu_watts` e `kepler_process_cpu_joules_total` correlacionam cada PID com seu `container_id` ou `vm_id` quando aplicável, enquanto `kepler_vm_cpu_watts` e `kepler_vm_cpu_joules_total` agregam o consumo energético das VMs por `hypervisor`, `state` e `zone`.

## Exemplo
```promql
# Potência de CPU consumida por máquinas virtuais por hipervisor
sum by (vm_name, hypervisor, node_name) (
  kepler_vm_cpu_watts{zone="package"}
)
```

## Limites e trade-offs
A exportação de métricas por PID (`kepler_process_*`) em servidores com milhares de processos efêmeros de curta duração pode elevar a cardinalidade no Prometheus se o intervalo de retenção ou *metric relabeling* não for dimensionado.

## Como verificar
Filtre métricas de processos específicos da infraestrutura (`kepler_process_cpu_watts{comm="containerd",zone="package"}`) para medir o custo energético do runtime de containers.

## Conexões
- [[kepler-monitoramento-gpu-nvidia-active-idle-watts-joules]] — Veja também: Kepler: monitoramento energético de GPUs (`kepler_node_gpu_*`, `kepler_container_gpu_*` e `kepler_process_gpu_*`).
- [[kepler-reducao-privilegios-seguranca-readonly-proc-sys-sem-cap-bpf]] — Veja também: Kepler: endurecimento de segurança na série v0.10+ com acesso somente leitura a `/proc` e `/sys`.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
