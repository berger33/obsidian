---
id: software.devops.tranche15.001468
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

# Spegel: funcionamento do roteamento via Containerd Registry Mirroring (`/etc/containerd/certs.d` e `hosts.toml`)

## Em uma frase
O Spegel utiliza o mecanismo nativo de *Registry Mirroring* do `containerd` (diretório `/etc/containerd/certs.d` e arquivos `hosts.toml`) para interceptar pulls de imagens sem exigir que os desenvolvedores alterem os nomes das imagens nos manifestos dos Pods.

## Por que importa
Outras soluções de cache obrigam as equipes a reescrever `docker.io/library/nginx` para `meu-cache.interno/library/nginx` em todos os Deployments; o Spegel opera de forma 100% transparente mantendo as URLs originais das imagens.

## Como funciona
O Pod do Spegel em cada nó escreve e mantém automaticamente as entradas `hosts.toml` dentro de `/etc/containerd/certs.d`, instruindo o `containerd` local a consultar primeiro o endpoint local do Spegel antes de recorrer ao registry público de origem.

## Exemplo
```bash
kubectl exec -n spegel daemonset/spegel -- ls -la /etc/containerd/certs.d || true
```

## Limites e trade-offs
Se outro daemon ou script no nó sobrescrever ou limpar o diretório `/etc/containerd/certs.d`, o roteamento para o Spegel será interrompido até que a configuração seja restaurada.

## Como verificar
Verifique a presença dos diretórios de registros e arquivos `hosts.toml` gerados sob `/etc/containerd/certs.d` nos nós do cluster.

## Conexões
- [[spegel-resiliencia-indisponibilidade-registry-externo-rate-limits]] — Veja também: Spegel: resiliência contra quedas de registries externos, mitigação de rate-limiting e redução de tráfego egress.
- [[spegel-edge-computing-homelab-comparacao-dragonfly-harbor]] — Veja também: Spegel: aplicação em clusters Edge, homelabs e comparação arquitetural com Dragonfly e Harbor.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
