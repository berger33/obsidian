---
id: software.devops.tranche15.001411
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

# Kepler v0.10+: reescrita arquitetural do exportador Prometheus de consumo de energia para Kubernetes

## Em uma frase
O Kepler (*Kubernetes-based Efficient Power Level Exporter*, CNCF Sandbox) é um exportador Prometheus que mede o consumo de energia (em Joules) e potência (em Watts) no nível de nó, container, pod, processo e máquina virtual em clusters Kubernetes.

## Por que importa
Com o crescimento explosivo do consumo energético em datacenters e clusters de IA, equipes de FinOps e GreenOps precisam atribuir com precisão o gasto elétrico e a pegada de carbono a cada workload sem impor alto overhead ou privilégios excessivos nos nós.

## Como funciona
A partir da versão `0.10.0`, o Kepler passou por uma reescrita completa orientada a serviços e thread-safe: eliminou zonas RAPL hardcoded em favor de detecção dinâmica, passou a atribuir potência com base no uso ativo de CPU e reduziu drasticamente os requisitos de segurança para acesso somente leitura a `/proc` e `/sys`, dispensando `CAP_SYSADMIN` e `CAP_BPF`.

## Exemplo
```bash
helm install kepler oci://quay.io/sustainable_computing_io/charts/kepler \
  --namespace kepler \
  --create-namespace
kubectl wait --for=condition=ready --timeout=120s pod -n kepler --all
```

## Limites e trade-offs
A versão legada (`0.9.x` e anteriores, preservada na branch `archived`) está congelada sem correções de bugs ou novas funcionalidades; migrações para `0.10.0+` exigem revisão do formato de configuração e dos nomes atualizados de métricas.

## Como verificar
Execute `kubectl port-forward -n kepler svc/kepler 28282:28282` e consulte `curl -s http://localhost:28282/metrics | grep kepler_node_cpu_watts` para validar a exportação.

## Conexões
- [[kepler-zonas-energia-rapl-psys-package-core-uncore-dram]] — Veja também: Kepler: zonas de energia RAPL (`psys`, `package`, `core`, `uncore`, `dram`) e regra de não soma.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
