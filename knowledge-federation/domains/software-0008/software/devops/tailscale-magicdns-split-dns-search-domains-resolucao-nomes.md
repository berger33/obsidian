---
id: software.devops.tranche19.001858
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/tailscale/tailscale/main/README.md", "https://tailscale.com/docs/kubernetes-operator", "https://github.com/tailscale/tailscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Tailscale MagicDNS e Split DNS: resolução automática de nomes `.ts.net` e encaminhamento seletivo por domínio

## Em uma frase
O **MagicDNS** registra automaticamente um nome DNS único (`<hostname>.<tailnet-name>.ts.net`) para cada dispositivo e proxy Kubernetes na *tailnet* através de um resolvedor DNS local embutido no `tailscaled` (`100.100.100.100`), suportando também **Split DNS** (nameservers restritos a domínios internos específicos como `.corp.internal`).

## Por que importa
Memorizar endereços IP `100.x.y.z` ou manter arquivos `/etc/hosts` sincronizados entre laptops e servidores não escala quando serviços mudam ou são recriados pelo operador Kubernetes.

## Como funciona
O resolvedor local em `100.100.100.100` intercepta consultas para a zona da *tailnet* (respondendo instantaneamente com os IPs IPv4 `100.x.y.z` e IPv6 `fd7a:115c:a1e0::/48` do nó) e encaminha consultas de zonas corporativas configuradas em *Split DNS* para os servidores DNS privados alcançáveis via *Subnet Router*.

## Exemplo
```bash
tailscale dns status
dig @100.100.100.100 grafana-prod
```

## Limites e trade-offs
O subcomando `tailscale dns status` exibe toda a configuração de DNS ativa no host local, incluindo os servidores upstream por domínio (Split DNS), domínios de busca e estado do sistema operacional (`/etc/resolv.conf` ou `systemd-resolved`).

## Como verificar
Execute `tailscale dns status` e `tailscale ip -4 <hostname>` para testar a resolução MagicDNS de um par da rede.

## Conexões
- [[tailscale-ssh-session-recording-tsrecorder-kubernetes-auditoria]] — Veja também: Tailscale SSH e `Recorder` (`tsrecorder`): autenticação SSH sem chaves pela *tailnet* e gravação de sessões no Kubernetes.
- [[tailscale-userspace-networking-container-sidecar-tun-device]] — Veja também: Tailscale em Containers: diferença entre modo Kernel `TUN` (`/dev/net/tun`) e `Userspace Networking` (`--tun=userspace-networking`).

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://tailscale.com/docs/kubernetes-operator) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
