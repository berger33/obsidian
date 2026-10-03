---
id: software.devops.tranche19.001859
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

# Tailscale em Containers: diferença entre modo Kernel `TUN` (`/dev/net/tun`) e `Userspace Networking` (`--tun=userspace-networking`)

## Em uma frase
Ao executar o `tailscaled` dentro de containers Docker, Pods Kubernetes sem privilégio ou ambientes serverless (Cloud Run, AWS App Runner, Fly.io), o Tailscale pode operar em dois modos de rede: **Kernel TUN** (usando `/dev/net/tun` e `CAP_NET_ADMIN`) ou **Userspace Networking** (`--tun=userspace-networking`, que inclui pilha TCP/IP netstack em espaço de usuário e proxies SOCKS5/HTTP).

## Por que importa
Em plataformas de container restritas ou FaaS onde o container não tem permissão para criar interfaces de rede virtuais `/dev/net/tun` nem modificar tabelas de roteamento do kernel, uma VPN tradicional simplesmente não inicia.

## Como funciona
Com `--tun=userspace-networking --socks5-server=localhost:1055 --outbound-http-proxy-listen=localhost:1055`, o `tailscaled` roda 100% sem privilégios de rede do kernel: conexões de entrada da *tailnet* são encaminhadas para `localhost` no container, e conexões de saída da aplicação podem usar `ALL_PROXY=socks5://localhost:1055`.

## Exemplo
```bash
tailscaled --tun=userspace-networking \
  --socks5-server=localhost:1055 \
  --outbound-http-proxy-listen=localhost:1055 &
tailscale up --auth-key="${TS_AUTHKEY}"
```

## Limites e trade-offs
Sempre que o ambiente permitir conceder `CAP_NET_ADMIN` e acesso a `/dev/net/tun` (como nos proxies gerenciados pelo Tailscale Kubernetes Operator em modo padrão), prefira o modo TUN por oferecer maior throughput e transparência para conexões de saída sem exigir proxy SOCKS5.

## Como verificar
Verifique nos logs de inicialização do `tailscaled` se ele abriu o dispositivo TUN do sistema ou iniciou o `userspace-networking` netstack.

## Conexões
- [[tailscale-magicdns-split-dns-search-domains-resolucao-nomes]] — Veja também: Tailscale MagicDNS e Split DNS: resolução automática de nomes `.ts.net` e encaminhamento seletivo por domínio.
- [[tailscale-serve-funnel-compartilhamento-local-https-webhooks]] — Veja também: Tailscale `serve` e `funnel`: exposição rápida de portas locais via HTTPS na *tailnet* (`serve`) ou na internet pública (`funnel`).

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://tailscale.com/docs/kubernetes-operator) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
