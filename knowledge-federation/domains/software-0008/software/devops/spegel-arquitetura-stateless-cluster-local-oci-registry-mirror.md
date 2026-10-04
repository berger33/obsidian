---
id: software.devops.tranche15.001461
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

# Spegel: espelho de registro OCI stateless e peer-to-peer local ao cluster Kubernetes

## Em uma frase
O Spegel ("espelho" em sueco) é um mirror de registro OCI *stateless* (sem estado próprio de banco ou storage externo) que roda como DaemonSet no Kubernetes, permitindo que os nós do cluster compartilhem entre si camadas de imagens já baixadas no `containerd`.

## Por que importa
Quando um Deployment escala ou um DaemonSet inicia em dezenas de nós simultaneamente, todos os nós baixam os mesmos gigabytes do registry externo, gerando custos de tráfego de saída (NAT/egress), lentidão no startup dos Pods e bloqueios por *rate-limiting* (como no Docker Hub).

## Como funciona
O Spegel não duplica imagens em um bucket S3 nem exige PVCs: ele lê diretamente o content store local do `containerd` em cada nó, anuncia os digests de blobs e manifestos disponíveis em uma tabela hash distribuída (DHT) peer-to-peer entre os Pods do Spegel e responde às requisições de mirror do `containerd` dos nós vizinhos.

## Exemplo
```bash
helm upgrade --create-namespace --namespace spegel --install \
  spegel oci://ghcr.io/spegel-org/helm-charts/spegel
kubectl get pods -n spegel -o wide
```

## Limites e trade-offs
O Spegel possui fallback transparente: se nenhum nó do cluster possuir a imagem solicitada ou se o Spegel estiver indisponível, o `containerd` faz fallback silencioso para o registry upstream original.

## Como verificar
Verifique que todos os Pods do DaemonSet `spegel` no namespace `spegel` estão em estado `Running` e sem reinicializações.

## Conexões
- [[spegel-pre-requisitos-containerd-config-path-discard-unpacked-layers]] — Veja também: Spegel: requisitos obrigatórios do `containerd` (`config_path` e `discard_unpacked_layers = false`).

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://spegel.dev/docs/getting-started/) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
