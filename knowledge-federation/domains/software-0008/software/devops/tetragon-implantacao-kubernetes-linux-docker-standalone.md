---
id: software.devops.tranche07.000629
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
fontes: ["https://raw.githubusercontent.com/cilium/tetragon/main/README.md", "https://tetragon.io/docs/overview/", "https://github.com/cilium/tetragon"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cilium Tetragon: implantação em Kubernetes (DaemonSet) e em hosts Linux via Docker ou pacotes nativos

## Em uma frase
O Cilium Tetragon pode ser implantado em clusters Kubernetes via Helm como um DaemonSet ou executado diretamente em servidores Linux via container Docker ou pacotes de sistema para proteção de hosts bare-metal e VMs.

## Por que importa
A superfície de ataque de uma infraestrutura moderna não se restringe a clusters Kubernetes: servidores Linux standalone, nós de bancos de dados, runners de CI/CD em máquinas virtuais e instâncias de borda também exigem observabilidade de segurança e runtime enforcement via eBPF. Segundo o README oficial do Tetragon (`Getting started`), o projeto suporta tanto a implantação nativa em Kubernetes quanto a execução direta em Linux e Docker.

## Como funciona
Em Kubernetes, o Helm chart `cilium/tetragon` implanta o `tetragon-operator` (que gerencia os CRDs `TracingPolicy` e `TracingPolicyNamespaced`) e o DaemonSet `tetragon` em cada nó do cluster, montando `/sys/kernel/btf/vmlinux`, `/sys/fs/bpf` e `/proc` do hospedeiro para carregar os sensores eBPF e enriquecer eventos com metadados de pods. Em servidores Linux fora do Kubernetes, o Tetragon pode ser executado como um container privilegiado (`quay.io/cilium/tetragon`) compartilhando o namespace de PID e os diretórios de BPF/BTF do host, ou instalado diretamente como serviço systemd a partir de pacotes `.deb`/`.rpm`/tarball, carregando políticas `TracingPolicy` a partir de arquivos YAML locais no disco.

## Exemplo
```bash
# Execução do Cilium Tetragon em um host Linux via Docker com carregamento de políticas locais
docker run -d --name tetragon --privileged --pid=host --cgroupns=host \
  -v /sys/kernel/btf/vmlinux:/var/lib/tetragon/btf:ro \
  -v /sys/fs/bpf:/sys/fs/bpf \
  quay.io/cilium/tetragon:latest

# Uso da CLI tetra dentro do container Docker no host Linux
docker exec -ti tetragon tetra getevents -o compact
```

## Limites e trade-offs
Quando executado em hosts Linux puros ou Docker sem Kubernetes, os campos de enriquecimento específicos de Kubernetes (`pod`, `namespace`, `workload`) não estarão presentes nos eventos (embora o ID do container e os namespaces Linux continuem sendo reportados), e as políticas devem usar o tipo `TracingPolicy` padrão sem seletores exclusivos de pods Kubernetes (`podSelector`).

## Como verificar
No host Linux ou no cluster Kubernetes, confirme nos logs de inicialização do Tetragon que o arquivo BTF do kernel (`vmlinux`) foi detectado com sucesso e que os sensores base (`base_sensor`) foram carregados no kernel sem erros do verificador eBPF.

## Conexões
- [[tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes]] — Veja também: Cilium Tetragon: uso da CLI Tetra para inspeção de eventos, filtros e administração de sensores.
- [[tetragon-exportacao-logs-json-metricas-prometheus-siem]] — Veja também: Cilium Tetragon: exportação de eventos JSON com rotação, filtros de exportação e métricas Prometheus.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl]] — Referência cruzada direta com inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
