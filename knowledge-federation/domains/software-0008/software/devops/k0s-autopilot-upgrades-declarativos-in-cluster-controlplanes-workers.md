---
id: software.devops.tranche17.001687
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

# k0s `Autopilot`: atualizações declarativas in-cluster de controladores, workers e imagens airgap via CRD `Plan`

## Em uma frase
Além de upgrades externos via SSH com `k0sctl`, o `k0s` inclui um operador nativo in-cluster chamado **Autopilot** (`autopilot.k0sproject.io/v1beta2`) que executa atualizações coordenadas de versão do `k0s` e de pacotes airgap por meio de objetos Custom Resource `Plan`.

## Por que importa
Em frotas de borda onde os nós não aceitam conexões SSH de entrada a partir de uma estação central (ou em fluxos puramente GitOps com Argo CD / Flux), o próprio cluster precisa ser capaz de atualizar seu binário `k0s` declarativamente via API do Kubernetes.

## Como funciona
Cada nó do cluster registra um objeto `ControlNode` no Autopilot. Quando o administrador aplica um objeto `Plan` especificando a nova versão do `k0s` e a estratégia de atualização (por exemplo, atualizando lote por lote de controladores e depois os workers), os agentes do Autopilot baixam o novo binário `k0s`, validam o hash SHA-256, substituem o executável no host e reiniciam o serviço de forma sequencial.

## Exemplo
```yaml
apiVersion: autopilot.k0sproject.io/v1beta2
kind: Plan
metadata:
  name: autopilot
spec:
  id: upgrade-to-1-31-2
  timestamp: "now"
  commands:
    - k0supdate:
        version: v1.31.2+k0s.0
        platforms:
          linux-amd64:
            url: https://github.com/k0sproject/k0s/releases/download/v1.31.2+k0s.0/k0s-v1.31.2+k0s.0-amd64
        targets:
          controllers:
            discovery:
              static:
                nodes:
                  - controller-01
```

## Limites e trade-offs
O objeto `Plan` processado pelo Autopilot deve ter obrigatoriamente `metadata.name: autopilot`; planos criados com outros nomes são ignorados pelo controlador por design para impedir múltiplos upgrades concorrentes.

## Como verificar
Execute `sudo k0s kubectl get controlnodes` e acompanhe `sudo k0s kubectl get plan autopilot -o yaml` durante o rollout.

## Conexões
- [[k0s-cni-kube-router-padrao-calico-custom-cni-networking]] — Veja também: k0s: opções de rede CNI (`kube-router` padrão, `calico` pré-configurado e CNI customizada).
- [[k0s-suporte-multi-arquitetura-x86-arm64-armv7-riscv-docker]] — Veja também: k0s: suporte nativo a `x86-64`, `ARM64`, `ARMv7` e `RISC-V` e execução de clusters em containers Docker.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
