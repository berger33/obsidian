---
id: software.devops.tranche19.001886
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

# Nebula NAT Traversal e `Relay`: configuração de `punchy` (UDP hole punching) e nós de `relay` para NATs simétricos

## Em uma frase
Para atravessar firewalls e roteadores NAT domésticos ou corporativos, o Nebula utiliza a seção **`punchy:`** (que mantém o *UDP hole punching* ativo) combinada com a seção **`relay:`** (`am_relay: true` / `use_relays: true`), que encaminha pacotes criptografados através de um nó intermediário caso a conexão UDP direta falhe.

## Por que importa
Quando dois nós estão atrás de NATs simétricos estritos ou firewalls corporativos que bloqueiam UDP arbitrário entre pares, o *UDP hole punching* sozinho não consegue abrir o caminho direto.

## Como funciona
Habilitar `punchy.punch: true` e `punchy.respond: true` instrui os nós a enviarem pacotes de perfuração NAT coordenados pelo Lighthouse. Se ainda assim o caminho direto falhar, nós configurados com `relay.am_relay: true` (frequentemente os próprios Lighthouses quando o tráfego de fallback é moderado) encaminham os pacotes cifrados ponta-a-ponto para os nós que listam seus IPs Nebula em `relay.relays`.

## Exemplo
```yaml
punchy:
  punch: true
  respond: true
  delay: 1s

relay:
  am_relay: false
  use_relays: true
  relays:
    - 192.168.100.1
```

## Limites e trade-offs
Mesmo quando uma conexão transita por um nó `relay`, o handshake Noise e a criptografia `AES-256-GCM` permanecem estritamente ponta-a-ponto entre o nó de origem e o nó de destino; o nó relay não consegue descriptografar o tráfego.

## Como verificar
Valide a configuração das seções `punchy` e `relay` com `nebula -test -config config.yml`.

## Conexões
- [[nebula-firewall-stateful-inbound-outbound-groups-cidr-ca-sha]] — Veja também: Nebula Stateful Firewall: filtragem de tráfego `inbound`/`outbound` baseada em `group`/`groups`, `proto`, `port` e `cidr`.
- [[nebula-unsafe-routes-roteamento-sub-redes-externas-subnet-routing]] — Veja também: Nebula `unsafe_routes`: roteamento de tráfego para sub-redes externas que não executam o agente Nebula.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
