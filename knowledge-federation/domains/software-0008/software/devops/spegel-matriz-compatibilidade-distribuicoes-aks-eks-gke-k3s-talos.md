---
id: software.devops.tranche15.001463
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
fontes: ["https://spegel.dev/docs/getting-started/", "https://raw.githubusercontent.com/spegel-org/spegel/main/README.md", "https://github.com/spegel-org/spegel"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Spegel: matriz de compatibilidade entre distribuições Kubernetes (AKS, Minikube, EKS, GKE, K3s, kind e Talos)

## Em uma frase
O comportamento de fábrica do `containerd` varia entre distribuições Kubernetes: plataformas como AKS, CoreWeave (CKS), DigitalOcean, Minikube, Scaleway Kapsule e Nutanix NKP funcionam com o Spegel *out of the box*, enquanto EKS, GKE, K0s, K3s/RKE2, kind e Talos requerem ajustes de configuração.

## Por que importa
Tentar instalar o Helm chart do Spegel em um cluster EKS (AL2023 ou Bottlerocket), K3s ou Talos sem ajustar os parâmetros específicos daquela distribuição fará com que os Pods do Spegel falhem na validação de startup ou nunca interceptem os pulls.

## Como funciona
Em distribuições com status verde (como AKS e Minikube), basta instalar o Helm chart. Nas distribuições com status amarelo, é preciso ajustar o caminho do socket/certs do containerd (por exemplo em K3s/RKE2) ou aplicar manifestos de configuração de nó (como `NodeConfig` no EKS AL2023 ou patches de `MachineConfig` no Talos).

## Exemplo
```bash
kubectl get nodes -o wide
kubectl get daemonset -n spegel
```

## Limites e trade-offs
Em nós Bottlerocket no EKS, a configuração do `containerd` não pode ser editada manualmente após o deploy da AMI, exigindo o uso de *bootstrap containers* no Bottlerocket v1.56+ para registrar o mirror do Spegel.

## Como verificar
Consulte a tabela de compatibilidade oficial da distribuição antes do deploy e verifique que `READY` atingiu `1/1` em todos os nós no DaemonSet `spegel`.

## Conexões
- [[spegel-pre-requisitos-containerd-config-path-discard-unpacked-layers]] — Veja também: Spegel: requisitos obrigatórios do `containerd` (`config_path` e `discard_unpacked_layers = false`).
- [[spegel-configuracao-eks-al2023-nodeadm-nodeconfig-bottlerocket]] — Veja também: Spegel: configuração de nós Amazon EKS em AMIs AL2023 (`nodeadm`) e Bottlerocket.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
