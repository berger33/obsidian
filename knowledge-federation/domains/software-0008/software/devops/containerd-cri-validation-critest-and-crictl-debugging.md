---
id: software.devops.tranche01.000078
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://github.com/containerd/containerd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Validação e depuração de setups CRI com `cri-tools`: `critest` e `crictl`

## Em uma frase
Nas subseções Validating Your `cri` Setup e CRI Guides do README oficial, a documentação destaca o projeto `cri-tools` (`github.com/kubernetes-sigs/cri-tools`) e duas ferramentas essenciais para quem opera o containerd sob o Kubernetes: o programa `critest` (usado para executar a suíte oficial de CRI Validation Testing, complementado por `./docs/cri/testing.md`) e o utilitário `crictl` (com guia dedicado em `./docs/cri/crictl.md` para depurar Pods, Containers e Images).

## Por que importa
Quando um nó Kubernetes apresenta falhas ao iniciar pods ou puxar imagens, depurar pelo `crictl` enxerga exatamente os objetos da camada CRI (Pods, containers e imagens no escopo do Kubernetes), enquanto rodar o `critest` valida formalmente se a instalação e a configuração do plugin `cri` cumprem toda a especificação do `sig-node`.

## Como funciona
Siga `./docs/cri/crictl.md` para inspecionar e depurar Pods, contêineres e imagens em nós Kubernetes com `crictl`, e execute o `critest` (conforme `./docs/cri/testing.md`) ao homologar novas imagens de sistema operacional de nós ou configurações customizadas do containerd.

## Exemplo
A lista CRI Guides do README inclui ainda dois roteiros completos de provisionamento de cluster: instalação com Ansible e Kubeadm (`contrib/ansible/README.md`) e instalação customizada usando o tarball de release e Kubeadm (`docs/getting-started.md`).

## Limites e trade-offs
Lembre-se da diferença de abstração: `crictl` conversa com o endpoint CRI (entendendo o conceito de Pod do Kubernetes), enquanto `ctr` conversa com a API interna do containerd.

## Como verificar
Conferi as subseções Validating Your `cri` Setup e CRI Guides no README oficial de `containerd/containerd`.

## Conexões
- [[containerd-cri-plugin-ga-kubernetes-integration]] — Veja também: O plugin nativo `cri` (GA): integração direta com a Container Runtime Interface do Kubernetes.
- [[containerd-nightly-builds-and-production-warning]] — Veja também: Builds noturnos para Linux e Windows via GitHub Actions e restrição estrita contra uso em produção.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
