---
id: software.devops.tranche17.001684
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

# k0s: armazenamento de estado com `etcd` gerenciado ou bancos SQL via `kine` (`SQLite`, `MySQL`, `PostgreSQL`)

## Em uma frase
Na camada de persistência (`spec.storage` em `k0s.yaml`), o `k0s` suporta tanto um cluster **etcd** totalmente gerenciado pelo supervisor (padrão para clusters multi-node) quanto o shim **kine** embutido para usar **SQLite** (padrão no modo `--single`), **MySQL**, **PostgreSQL** ou **dqlite**.

## Por que importa
Em dispositivos de borda de 1 GB de RAM, rodar um `etcd` completo consome memória e IOPS de disco flash excessivos; já em nuvens públicas que já possuem um banco RDS PostgreSQL/Aurora altamente disponível, usar `kine` elimina a manutenção de discos de `etcd`.

## Como funciona
Quando configurado com `type: etcd`, unir um novo controlador com `k0s controller <join-token>` faz o `k0s` reconfigurar automaticamente a lista de membros do cluster `etcd` via API interna na porta `9443`. Quando configurado com `type: kine`, o `k0s` inicia o processo `kine` traduzindo a API gRPC do `etcd` para a string `dataSource` do banco SQL escolhido.

## Exemplo
```yaml
apiVersion: k0s.k0sproject.io/v1beta1
kind: ClusterConfig
metadata:
  name: k0s-cluster
spec:
  storage:
    type: kine
    kine:
      dataSource: "postgres://k0s:secret@pg-ha.internal:5432/k0s_state?sslmode=require"
```

## Limites e trade-offs
Conforme documentado na arquitetura do `k0s`, o `k0s` adiciona membros ao `etcd` automaticamente no join, mas não reduz (*shrink*) o cluster `etcd` sozinho: antes de desligar permanentemente um nó controlador de um cluster `etcd`, o membro deve ser removido explicitamente com `k0s etcd leave`.

## Como verificar
Execute `sudo k0s etcd member-list` em um cluster multi-controller baseado em `etcd` para auditar os pares ativos do quórum.

## Conexões
- [[k0s-konnectivity-server-agent-comunicacao-control-plane-workers]] — Veja também: k0s: comunicação reversa entre Control Plane e Workers via `Konnectivity` (`konnectivity-server` e `konnectivity-agent`).
- [[k0s-k0sctl-gerenciamento-ciclo-vida-multi-node-upgrades-backups]] — Veja também: k0s `k0sctl`: provisionamento declarativo, upgrades zero-downtime, backup e restore de clusters multi-nó via SSH.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://docs.k0sproject.io/stable/architecture/) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
