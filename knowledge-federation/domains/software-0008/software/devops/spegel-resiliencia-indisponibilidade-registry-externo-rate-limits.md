---
id: software.devops.tranche15.001467
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
fontes: ["https://raw.githubusercontent.com/spegel-org/spegel/main/README.md", "https://spegel.dev/docs/getting-started/", "https://github.com/spegel-org/spegel"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Spegel: resiliência contra quedas de registries externos, mitigação de rate-limiting e redução de tráfego egress

## Em uma frase
Ao servir camadas OCI diretamente da rede interna do cluster a partir do primeiro nó que realizou o pull, o Spegel protege o cluster contra indisponibilidades temporárias do registry externo e evita bloqueios de `429 Too Many Requests` (como os limites de pull do Docker Hub).

## Por que importa
Em um incidente de queda do registry externo ou durante um evento de auto-scaling rápido de 50 nós, sem um cache local no cluster os novos Pods ficariam presos em `ImagePullBackOff` mesmo que outros nós vizinhos já tivessem a imagem em disco.

## Como funciona
Com o Spegel ativo, desde que pelo menos um nó saudável do cluster já tenha a imagem armazenada no seu `containerd` (e a política não force consulta obrigatória de tag mutável bloqueada no upstream), qualquer outro nó consegue puxar o manifesto e as camadas pela LAN do cluster em velocidade gigabit.

## Exemplo
```bash
kubectl get events --field-selector reason=Pulled -A
```

## Limites e trade-offs
Se um Pod utilizar `imagePullPolicy: Always` com uma tag mutável (em vez de digest `@sha256:...`), o Kubelet ainda precisará resolver a referência atualizada ou consultar os espelhos configurados; fixar imagens por digest imutável maximiza a eficácia do cache P2P em quedas externas.

## Como verificar
Meça o tempo de pull nos eventos do Pod (`Successfully pulled image ... in Xms`) no segundo nó e compare com o tempo de download externo do primeiro nó.

## Conexões
- [[spegel-implantacao-gitops-flux-helmrepository-oci-helmrelease]] — Veja também: Spegel: implantação declarativa via GitOps com Flux (`HelmRepository` OCI e `HelmRelease`).
- [[spegel-roteamento-containerd-registry-mirroring-certs-d-hosts-toml]] — Veja também: Spegel: funcionamento do roteamento via Containerd Registry Mirroring (`/etc/containerd/certs.d` e `hosts.toml`).

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://spegel.dev/docs/getting-started/) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
