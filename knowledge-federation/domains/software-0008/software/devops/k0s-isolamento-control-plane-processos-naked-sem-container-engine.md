---
id: software.devops.tranche17.001682
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
fontes: ["https://docs.k0sproject.io/stable/architecture/", "https://raw.githubusercontent.com/k0sproject/k0s/main/README.md", "https://github.com/k0sproject/k0s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# k0s: isolamento de Control Plane executando componentes como processos *naked* sem CRI nem Kubelet no controller

## Em uma frase
Por padrão, um nó controlador do `k0s` (`k0s controller`) executa todos os componentes do plano de controle (`etcd`/`kine`, `kube-apiserver`, `kube-scheduler`, `kube-controller-manager` e `konnectivity-server`) diretamente como processos filhos do sistema operacional (*naked processes*) supervisionados pelo `k0s`, sem rodar `containerd` nem `kubelet` no nó controlador.

## Por que importa
Em distribuições baseadas em Static Pods (`kubeadm`, `RKE2`), cada nó master ainda precisa rodar um container runtime (`containerd`) e um `kubelet` apenas para subir o próprio control plane, consumindo RAM adicional e registrando o nó master na API onde cargas de usuário poderiam ser agendadas se um taint fosse removido.

## Como funciona
Como o `k0s controller` padrão não inicia nem `containerd` nem `kubelet`, os nós controladores nem sequer aparecem na lista de `kubectl get nodes`! Isso cria um isolamento físico estrito entre control plane e data plane, além de permitir escalar planos de controle muito densos ou rodar controladores dentro de containers leves.

## Exemplo
```bash
sudo k0s status
ps -ef | grep "/var/lib/k0s/bin/kube-apiserver"
```

## Limites e trade-offs
Quando o administrador deseja explicitamente um cluster de nó único ou quer que os nós controladores também executem Pods de trabalho, basta passar a flag `--single` ou `--enable-worker` (`k0s controller --enable-worker`), que ativa o `kubelet` e o `containerd` junto ao controlador.

## Como verificar
Em um nó iniciado apenas com `k0s controller` (sem `--enable-worker`), execute `sudo k0s kubectl get nodes` e confirme que a lista de worker nodes está vazia enquanto a API responde normalmente.

## Conexões
- [[k0s-arquitetura-zero-friction-binario-unico-sem-dependencias-os]] — Veja também: k0s: arquitetura *Zero Friction* em binário único auto-extraível sem dependências de sistema operacional.
- [[k0s-konnectivity-server-agent-comunicacao-control-plane-workers]] — Veja também: k0s: comunicação reversa entre Control Plane e Workers via `Konnectivity` (`konnectivity-server` e `konnectivity-agent`).

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://docs.k0sproject.io/stable/architecture/) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
