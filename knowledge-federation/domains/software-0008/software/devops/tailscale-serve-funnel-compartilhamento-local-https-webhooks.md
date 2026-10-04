---
id: software.devops.tranche19.001860
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
fontes: ["https://raw.githubusercontent.com/tailscale/tailscale/main/README.md", "https://headscale.net/stable/about/features/", "https://github.com/tailscale/tailscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Tailscale `serve` e `funnel`: exposição rápida de portas locais via HTTPS na *tailnet* (`serve`) ou na internet pública (`funnel`)

## Em uma frase
Os subcomandos **`tailscale serve`** e **`tailscale funnel`** transformam o próprio cliente `tailscaled` em um proxy reverso HTTP/HTTPS/TCP com certificado TLS automático: o `serve` expõe um serviço local (`localhost:3000`) apenas para membros da sua *tailnet*, enquanto o `funnel` abre o tráfego da internet pública para o seu nó através dos servidores de ingress da Tailscale.

## Por que importa
Quando um desenvolvedor precisa receber um webhook real do GitHub ou Stripe em seu servidor local na porta `8080` ou compartilhar um preview com um colega da equipe, configurar túneis de terceiros inseguros ou subir ambientes completos de cloud atrasa o ciclo de feedback.

## Como funciona
Com `tailscale serve --bg 8080`, qualquer dispositivo autorizado na *tailnet* acessa `https://<node>.<tailnet>.ts.net` com TLS válido. Com `tailscale funnel --bg 8080` (desde que o atributo de nó `funnel` seja permitido na política ACL), os servidores públicos da Tailscale terminam o TCP na borda e repassam o fluxo TLS criptografado (SNI passthrough) até o `tailscaled` local, que detém a chave privada do certificado.

## Exemplo
```bash
# Expondo a porta local 8080 via HTTPS apenas para a tailnet:
tailscale serve --bg 8080
tailscale serve status

# Desativando a exposição:
tailscale serve reset
```

## Limites e trade-offs
Como no `tailscale funnel` o certificado TLS é gerado localmente no seu dispositivo e os servidores de borda da Tailscale fazem apenas *TLS passthrough* baseado em SNI, os servidores de relay nunca têm acesso à chave privada TLS nem ao conteúdo HTTP descriptografado.

## Como verificar
Execute `tailscale serve status` para auditar se há alguma porta local exposta via `serve` ou `funnel` na máquina.

## Conexões
- [[tailscale-userspace-networking-container-sidecar-tun-device]] — Veja também: Tailscale em Containers: diferença entre modo Kernel `TUN` (`/dev/net/tun`) e `Userspace Networking` (`--tun=userspace-networking`).

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://headscale.net/stable/about/features/) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
