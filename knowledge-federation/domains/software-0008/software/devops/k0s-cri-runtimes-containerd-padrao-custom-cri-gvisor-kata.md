---
id: software.devops.tranche17.001689
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

# k0s: gerenciamento do `containerd` embutido, importação de bundles airgap e configuração de CRI customizado

## Em uma frase
Nos worker nodes, o `k0s` supervisiona como processos *naked* o `containerd` (runtime de alto nível) e o `runc` (runtime OCI de baixo nível), permitindo customizar configurações em `/etc/k0s/containerd.d/`, pré-carregar bundles de imagens airgap em `/var/lib/k0s/images/` ou apontar para um CRI externo (`--cri-socket`).

## Por que importa
Em ambientes air-gapped ou que exigem isolamento reforçado de containers (como `gVisor` `runsc`, `Kata Containers` ou `Docker`/`CRI-O` preexistente), o worker node precisa mesclar novos runtimes OCI sem editar o arquivo principal gerenciado pelo supervisor.

## Como funciona
Qualquer arquivo `.toml` colocado em `/etc/k0s/containerd.d/` nos workers é automaticamente importado pelo `containerd` gerenciado pelo `k0s` (permitindo registrar mirrors de registry ou runtimes secundários como `gVisor`). Além disso, arquivos `.tar` de imagens OCI colocados em `/var/lib/k0s/images/` são importados automaticamente no namespace `k8s.io` do `containerd` durante a partida do worker.

## Exemplo
```bash
sudo mkdir -p /var/lib/k0s/images
sudo k0s ctr images ls
```

## Limites e trade-offs
Para usar o cliente `ctr` contra o `containerd` embutido do `k0s`, invoque sempre `sudo k0s ctr` (que já aponta automaticamente para o socket `/run/k0s/containerd.sock` e para o namespace `k8s.io`), em vez de um `ctr` avulso do host.

## Como verificar
Execute `sudo k0s ctr images ls` em um nó worker para listar todas as imagens carregadas no runtime do `k0s`.

## Conexões
- [[k0s-suporte-multi-arquitetura-x86-arm64-armv7-riscv-docker]] — Veja também: k0s: suporte nativo a `x86-64`, `ARM64`, `ARMv7` e `RISC-V` e execução de clusters em containers Docker.
- [[k0s-backup-restore-cluster-state-tokens-join-controller-worker]] — Veja também: k0s: geração de tokens de ingresso (`k0s token create`) com expiração por papel e backup/restore nativo (`k0s backup`).

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://docs.k0sproject.io/stable/architecture/) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
