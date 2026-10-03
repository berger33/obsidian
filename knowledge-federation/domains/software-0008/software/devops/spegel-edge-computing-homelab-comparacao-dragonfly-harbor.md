---
id: software.devops.tranche15.001469
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

# Spegel: aplicação em clusters Edge, homelabs e comparação arquitetural com Dragonfly e Harbor

## Em uma frase
Desenvolvido originalmente na Xenit AB, o Spegel posiciona-se como uma alternativa ultraleve e *zero-storage* a sistemas pesados como Harbor ou Dragonfly para clusters de borda (edge), homelabs e clusters Kubernetes que já utilizam `containerd`.

## Por que importa
Enquanto o Harbor exige banco PostgreSQL, Redis e storage dedicado, e o Dragonfly opera um plano de controle completo (Manager, Scheduler e Seed Peers), o Spegel roda como um único DaemonSet stateless sem nenhuma dependência de banco de dados.

## Como funciona
Em implantações de borda onde múltiplos nós compartilham um link WAN lento ou caro com a nuvem, o Spegel garante que uma imagem baixada uma única vez pelo link WAN seja distribuída localmente via LAN entre os nós daquela localidade.

## Exemplo
```bash
kubectl top pods -n spegel
```

## Limites e trade-offs
A documentação oficial do repositório destaca que o Spegel possui uma API em evolução focada em simplicidade e casos de uso de homelab e contribuidores individuais, com suporte comunitário em regime *best-effort*.

## Como verificar
Monitore o baixo consumo de CPU e memória dos Pods do Spegel com `kubectl top pods -n spegel`.

## Conexões
- [[spegel-roteamento-containerd-registry-mirroring-certs-d-hosts-toml]] — Veja também: Spegel: funcionamento do roteamento via Containerd Registry Mirroring (`/etc/containerd/certs.d` e `hosts.toml`).
- [[spegel-seguranca-isolamento-registries-privados-limites]] — Veja também: Spegel: considerações de segurança no compartilhamento de camadas entre nós e registries privados.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://spegel.dev/docs/getting-started/) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
