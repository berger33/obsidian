---
id: software.devops.tranche17.001683
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/k0sproject/k0s/main/README.md", "https://docs.k0sproject.io/stable/architecture/", "https://github.com/k0sproject/k0s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# k0s: comunicação reversa entre Control Plane e Workers via `Konnectivity` (`konnectivity-server` e `konnectivity-agent`)

## Em uma frase
Devido ao isolamento padrão do plano de controle (onde os nós controladores não participam da malha de rede CNI dos Pods), o `k0s` inclui e configura por padrão o serviço **Konnectivity** (`konnectivity-server` no controller e `konnectivity-agent` nos workers) para intermediar toda comunicação do `kube-apiserver` para os nós e Pods.

## Por que importa
Quando o `kube-apiserver` roda fora da rede CNI dos workers (ou quando os workers estão em sub-redes remotas atrás de NAT), chamadas originadas no `kube-apiserver` — como `kubectl logs`, `kubectl exec`, `kubectl port-forward` e chamadas a admission webhooks ou aggregated apiservers hospedados em Pods — não teriam rota direta.

## Como funciona
Os `konnectivity-agents` (implantados como DaemonSet nos workers) abrem conexões TCP/gRPC persistentes de saída na porta `8132` até o `konnectivity-server` (supervisionado pelo `k0s controller`). Assim, o `kube-apiserver` roteia todo o tráfego destinado a IPs de Nós, Pods e Services por dentro desse túnel seguro sem exigir CNI nos nós controladores.

## Exemplo
```bash
sudo k0s kubectl get daemonset konnectivity-agent -n kube-system
sudo k0s kubectl get pods -n kube-system -l k8s-app=konnectivity-agent
```

## Limites e trade-offs
Em clusters multi-controller de alta disponibilidade com balanceador de carga externo, a porta `8132` (Konnectivity) também deve ser balanceada junto à porta `6443` (`kube-apiserver`) e `9443` (k0s join API).

## Como verificar
Execute `sudo k0s kubectl logs -n kube-system -l k8s-app=konnectivity-agent` e teste um `kubectl exec` em qualquer Pod worker para validar o túnel Konnectivity.

## Conexões
- [[k0s-isolamento-control-plane-processos-naked-sem-container-engine]] — Veja também: k0s: isolamento de Control Plane executando componentes como processos *naked* sem CRI nem Kubelet no controller.
- [[k0s-storage-backends-etcd-gerenciado-kine-sqlite-mysql-postgres]] — Veja também: k0s: armazenamento de estado com `etcd` gerenciado ou bancos SQL via `kine` (`SQLite`, `MySQL`, `PostgreSQL`).

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
