---
id: software.devops.tranche17.001685
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

# k0s `k0sctl`: provisionamento declarativo, upgrades zero-downtime, backup e restore de clusters multi-nó via SSH

## Em uma frase
O `k0sctl` é a ferramenta oficial de linha de comando do ecossistema `k0s` que gerencia o ciclo de vida completo de clusters multi-nó (instalação, adição de nós, atualização de versão do Kubernetes, backup e restauração) a partir de um único arquivo declarativo `k0sctl.yaml` via SSH.

## Por que importa
Conectar-se manualmente via SSH em 20 servidores para baixar o binário `k0s`, gerar tokens de controller e worker, distribuir arquivos de configuração e coordenar upgrades sequenciais é trabalhoso e propenso a erros humanos.

## Como funciona
O engenheiro declara em `k0sctl.yaml` a lista de `hosts` (endereços SSH, chaves e `role`: `controller`, `controller+worker` ou `worker`) e a seção `k0s` (versão e configuração `k0s.yaml`). Ao executar `k0sctl apply --config k0sctl.yaml`, a ferramenta conecta-se em paralelo aos hosts, instala o binário `k0s`, inicializa o primeiro controller, gera e aplica os tokens de join nos demais controllers e workers e entrega o `kubeconfig` pronto com `k0sctl kubeconfig`.

## Exemplo
```yaml
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
  name: prod-k0s-cluster
spec:
  hosts:
    - ssh:
        address: 10.0.0.10
        user: ubuntu
        port: 22
        keyPath: ~/.ssh/id_ed25519
      role: controller
    - ssh:
        address: 10.0.0.21
        user: ubuntu
        port: 22
        keyPath: ~/.ssh/id_ed25519
      role: worker
  k0s:
    version: 1.31.2+k0s.0
```

## Limites e trade-offs
Para atualizar o cluster inteiro para uma nova versão do `k0s`, basta incrementar `spec.k0s.version` no `k0sctl.yaml` e reexecutar `k0sctl apply`: o `k0sctl` orquestra o upgrade rolling dos controladores e workers mantendo a disponibilidade.

## Como verificar
Execute `k0sctl apply --config k0sctl.yaml` seguido de `k0sctl kubeconfig --config k0sctl.yaml > kubeconfig` para validar o acesso ao cluster provisionado.

## Conexões
- [[k0s-storage-backends-etcd-gerenciado-kine-sqlite-mysql-postgres]] — Veja também: k0s: armazenamento de estado com `etcd` gerenciado ou bancos SQL via `kine` (`SQLite`, `MySQL`, `PostgreSQL`).
- [[k0s-cni-kube-router-padrao-calico-custom-cni-networking]] — Veja também: k0s: opções de rede CNI (`kube-router` padrão, `calico` pré-configurado e CNI customizada).

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
