---
id: software.devops.tranche15.001466
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

# Spegel: implantação declarativa via GitOps com Flux (`HelmRepository` OCI e `HelmRelease`)

## Em uma frase
O chart oficial do Spegel é distribuído como artefato OCI no GitHub Container Registry (`oci://ghcr.io/spegel-org/helm-charts/spegel`), integrando-se nativamente a controladores GitOps como Flux CD e Argo CD.

## Por que importa
Permite padronizar a instalação do mirror P2P em toda a frota de clusters Kubernetes como componente base de infraestrutura logo após o bootstrap do CNI.

## Como funciona
No Flux CD, declara-se um `HelmRepository` com `spec.type: "oci"` apontando para `oci://ghcr.io/spegel-org/helm-charts` no namespace `spegel` e um `HelmRelease` que reconcilia continuamente o chart `spegel`.

## Exemplo
```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: spegel
  namespace: spegel
spec:
  type: "oci"
  interval: 5m0s
  url: oci://ghcr.io/spegel-org/helm-charts
```

## Limites e trade-offs
Ao implantar via GitOps em clusters recém-criados, certifique-se de que a imagem do próprio Spegel seja acessível pelos nós (pois o Spegel não pode espelhar sua própria imagem antes de estar rodando).

## Como verificar
Execute `flux get helmreleases -n spegel` ou `helm status spegel -n spegel` para confirmar a reconciliação bem-sucedida.

## Conexões
- [[spegel-verificacao-funcional-debug-web-last-mirror-success]] — Veja também: Spegel: verificação funcional de espelhamento P2P e página de diagnóstico `/debug/web`.
- [[spegel-resiliencia-indisponibilidade-registry-externo-rate-limits]] — Veja também: Spegel: resiliência contra quedas de registries externos, mitigação de rate-limiting e redução de tráfego egress.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
