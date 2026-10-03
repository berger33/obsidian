---
id: software.devops.tranche19.001887
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
fontes: ["https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml", "https://raw.githubusercontent.com/slackhq/nebula/master/README.md", "https://github.com/slackhq/nebula"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nebula `unsafe_routes`: roteamento de tráfego para sub-redes externas que não executam o agente Nebula

## Em uma frase
O recurso **`tun.unsafe_routes`** do Nebula (junto à flag `-subnets` na assinatura do certificado via `nebula-cert sign`) permite que um nó Nebula atue como gateway para uma sub-rede externa (como uma CIDR de VPC, impressoras, equipamentos de rede ou serviços gerenciados) onde o binário Nebula não está instalado.

## Por que importa
O recurso chama-se `unsafe_routes` porque, ao sair do nó gateway Nebula em direção à sub-rede física final, o tráfego deixa de estar encapsulado pelo túnel Noise e pelas garantias de identidade de certificado do Nebula.

## Como funciona
Para configurar o roteamento com segurança: 1) assine o certificado do nó gateway incluindo `-subnets "10.50.0.0/24"` no `nebula-cert sign` (sem isso os demais nós recusarão enviar tráfego dessa sub-rede para ele); 2) habilite IP forwarding no kernel do gateway (`net.ipv4.ip_forward=1`); e 3) adicione a entrada `unsafe_routes` no `config.yml` dos nós clientes apontando `route: 10.50.0.0/24` para `via: 192.168.100.10`.

## Exemplo
```yaml
tun:
  disabled: false
  dev: nebula1
  mtu: 1300
  unsafe_routes:
    - route: 10.50.0.0/24
      via: 192.168.100.10
      mtu: 1300
      metric: 100
```

## Limites e trade-offs
Se o certificado do nó `via` (`192.168.100.10`) não tiver a sub-rede `10.50.0.0/24` explicitamente autorizada em seu campo `subnets` assinado pela CA, o handshake rejeitará o roteamento.

## Como verificar
Verifique com `nebula-cert print -path gateway.crt` se a sub-rede consta na lista `Subnets` do certificado do gateway.

## Conexões
- [[nebula-nat-traversal-punchy-relay-am-relay-use-relays]] — Veja também: Nebula NAT Traversal e `Relay`: configuração de `punchy` (UDP hole punching) e nós de `relay` para NATs simétricos.
- [[nebula-local-remote-allow-list-filtragem-interfaces-docker-cni]] — Veja também: Nebula `local_allow_list` e `remote_allow_list`: filtragem de interfaces virtuais (`docker.*`, `cni.*`) anunciadas ao Lighthouse.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
