---
id: software.devops.tranche17.001688
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

# k0s: suporte nativo a `x86-64`, `ARM64`, `ARMv7` e `RISC-V` e execução de clusters em containers Docker

## Em uma frase
O `k0s` compila e distribui binários oficiais para quatro arquiteturas de processador — **`x86-64` (`amd64`)**, **`ARM64`**, **`ARMv7` (`arm`)** e **`RISC-V` (`riscv64`)** — além de fornecer imagens oficiais `k0sproject/k0s` para rodar controladores e workers diretamente dentro de containers Docker.

## Por que importa
Laboratórios de IoT heterogêneos combinam servidores x86, placas ARM de 32/64 bits e novas placas RISC-V, enquanto pipelines de CI precisam subir um cluster Kubernetes completo em segundos usando um simples `docker run` sem VM intermediária.

## Como funciona
Como o plano de controle do `k0s` não exige `kubelet` nem `containerd` por padrão, subir um plano de controle Kubernetes completo para testar operadores ou CRDs em CI requer apenas iniciar um container `docker run -d --name k0s-cp --privileged -p 6443:6443 docker.io/k0sproject/k0s:latest k0s controller`, gastando uma fração da memória de um cluster completo.

## Exemplo
```bash
docker run -d --name k0s-single \
  --hostname k0s-single \
  --privileged \
  -v /var/lib/k0s \
  -p 6443:6443 \
  docker.io/k0sproject/k0s:latest k0s controller --single
docker exec k0s-single k0s kubeconfig admin > k0s-docker.kubeconfig
```

## Limites e trade-offs
Ao executar o `k0s` com `--single` (ou worker) dentro de um container Docker, é obrigatório montar `-v /var/lib/k0s` como volume dedicado para que o overlayfs do `containerd` interno não tente aninhar sobre o overlayfs da camada raiz do container Docker host.

## Como verificar
Extraia o `kubeconfig` com `docker exec k0s-single k0s kubeconfig admin` e execute `kubectl --kubeconfig k0s-docker.kubeconfig get nodes`.

## Conexões
- [[k0s-autopilot-upgrades-declarativos-in-cluster-controlplanes-workers]] — Veja também: k0s `Autopilot`: atualizações declarativas in-cluster de controladores, workers e imagens airgap via CRD `Plan`.
- [[k0s-cri-runtimes-containerd-padrao-custom-cri-gvisor-kata]] — Veja também: k0s: gerenciamento do `containerd` embutido, importação de bundles airgap e configuração de CRI customizado.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
