---
id: software.devops.tranche15.001464
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

# Spegel: configuração de nós Amazon EKS em AMIs AL2023 (`nodeadm`) e Bottlerocket

## Em uma frase
Em clusters Amazon EKS baseados no Amazon Linux 2023 (AL2023), a flag `discard_unpacked_layers` vem habilitada por padrão, exigindo customização via `NodeConfig` (`node.eks.aws/v1alpha1`) do `nodeadm` no UserData dos nós.

## Por que importa
Sem desabilitar `discard_unpacked_layers` no UserData das instâncias EC2 do EKS AL2023, o `containerd` remove os artefatos necessários após o primeiro pull e inviabiliza o espelhamento peer-to-peer no cluster.

## Como funciona
O administrador inclui no UserData multipart MIME da AMI AL2023 um recurso `NodeConfig` que injeta `config_path = "/etc/containerd/certs.d"` e `discard_unpacked_layers = false` na seção `spec.containerd.config`.

## Exemplo
```yaml
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  containerd:
    config: |
      [plugins."io.containerd.cri.v1.images".registry]
        config_path = "/etc/containerd/certs.d"
      [plugins.'io.containerd.cri.v1.images']
        discard_unpacked_layers = false
```

## Limites e trade-offs
Desabilitar `discard_unpacked_layers` faz com que o nó mantenha tanto as camadas compactadas no content store quanto o rootfs descompactado no snapshotter, aumentando ligeiramente o uso de disco local das instâncias EC2.

## Como verificar
Em um nó EKS AL2023 provisionado, verifique `/etc/containerd/config.toml` e confirme que `discard_unpacked_layers` está definido como `false`.

## Conexões
- [[spegel-matriz-compatibilidade-distribuicoes-aks-eks-gke-k3s-talos]] — Veja também: Spegel: matriz de compatibilidade entre distribuições Kubernetes (AKS, Minikube, EKS, GKE, K3s, kind e Talos).
- [[spegel-verificacao-funcional-debug-web-last-mirror-success]] — Veja também: Spegel: verificação funcional de espelhamento P2P e página de diagnóstico `/debug/web`.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
