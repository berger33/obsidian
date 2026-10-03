---
id: software.devops.tranche15.001462
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

# Spegel: requisitos obrigatórios do `containerd` (`config_path` e `discard_unpacked_layers = false`)

## Em uma frase
Para funcionar, o Spegel exige exclusivamente o runtime `containerd` com duas configurações obrigatórias em `/etc/containerd/config.toml`: `config_path = "/etc/containerd/certs.d"` e `discard_unpacked_layers = false`.

## Por que importa
Se `discard_unpacked_layers` estiver habilitado (`true`), o `containerd` apaga os blobs comprimidos originais do content store logo após descompactá-los no snapshotter, impedindo que o Spegel sirva aquelas camadas para outros nós do cluster.

## Como funciona
Na inicialização, o Spegel executa verificações de sanidade na configuração do `containerd` e encerra com erro explícito se os pré-requisitos não forem atendidos. Como o Spegel não pode reiniciar o `containerd` do host sozinho, distribuições que não trazem esses ajustes de fábrica exigem configuração prévia do nó.

## Exemplo
```toml
version = 3

[plugins."io.containerd.cri.v1.images".registry]
  config_path = "/etc/containerd/certs.d"
[plugins."io.containerd.cri.v1.images"]
  discard_unpacked_layers = false
```

## Limites e trade-offs
Qualquer alteração em `/etc/containerd/config.toml` para habilitar `config_path` ou desativar `discard_unpacked_layers` requer reiniciar o daemon `containerd` (`systemctl restart containerd`) em cada nó antes que o Spegel possa operar.

## Como verificar
Inspecione os logs do Pod do Spegel (`kubectl logs -n spegel -l app.kubernetes.io/name=spegel`) para confirmar que as checagens de startup do containerd passaram sem erros.

## Conexões
- [[spegel-arquitetura-stateless-cluster-local-oci-registry-mirror]] — Veja também: Spegel: espelho de registro OCI stateless e peer-to-peer local ao cluster Kubernetes.
- [[spegel-matriz-compatibilidade-distribuicoes-aks-eks-gke-k3s-talos]] — Veja também: Spegel: matriz de compatibilidade entre distribuições Kubernetes (AKS, Minikube, EKS, GKE, K3s, kind e Talos).

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
