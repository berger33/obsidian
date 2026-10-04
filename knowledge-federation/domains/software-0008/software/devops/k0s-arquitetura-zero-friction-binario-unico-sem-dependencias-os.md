---
id: software.devops.tranche17.001681
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

# k0s: arquitetura *Zero Friction* em binário único auto-extraível sem dependências de sistema operacional

## Em uma frase
O `k0s` (projeto CNCF Sandbox, licenciado sob Apache 2.0) é uma distribuição Kubernetes 100% upstream e certificada empacotada como um único binário estático auto-extraível que não possui nenhuma dependência de pacotes do sistema operacional host além do próprio kernel Linux.

## Por que importa
Na operação tradicional de Kubernetes, atualizações de pacotes do sistema operacional host (`systemd`, `containerd`, `iptables`, `socat`, `conntrack` via `apt`/`rpm`) podem quebrar o cluster ou introduzir vulnerabilidades originadas na distro Linux. O `k0s` embute absolutamente todos os binários e bibliotecas necessários com controle total de versão.

## Como funciona
Quando iniciado, o binário `k0s` extrai seus binários internos (incluindo `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `etcd`, `kine`, `konnectivity-server`, `containerd`, `runc`, `kubelet`) para `/var/lib/k0s/bin` e atua diretamente como supervisor de processos (*process supervisor*), exigindo apenas 1 vCPU e 1 GB de RAM.

## Exemplo
```bash
curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
sudo k0s install controller --single
sudo k0s start
sudo k0s status
sudo k0s kubectl get nodes
```

## Limites e trade-offs
Como o `k0s` embute o cliente `kubectl`, o comando `sudo k0s kubectl` funciona imediatamente após a partida do controlador sem precisar instalar nada adicional na máquina.

## Como verificar
Execute `sudo k0s status` e `sudo k0s sysinfo` para validar os pré-requisitos do kernel Linux e o estado de supervisão do processo.

## Conexões
- [[k0s-isolamento-control-plane-processos-naked-sem-container-engine]] — Veja também: k0s: isolamento de Control Plane executando componentes como processos *naked* sem CRI nem Kubelet no controller.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
