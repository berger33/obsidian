---
id: software.devops.tranche19.001885
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

# Nebula Stateful Firewall: filtragem de tráfego `inbound`/`outbound` baseada em `group`/`groups`, `proto`, `port` e `cidr`

## Em uma frase
Todo nó Nebula possui um **firewall stateful de pacotes embutido** configurado na seção `firewall:` do `config.yml`, que avalia cada pacote nos sentidos `outbound` e `inbound` com base nas propriedades criptograficamente autenticadas no certificado do par remoto (`group`, `groups`, `host`, `cidr`, `ca_name`, `ca_sha`).

## Por que importa
Em firewalls tradicionais baseados apenas em IP (`iptables`), se um endereço IP muda ou é realocado, a regra quebra ou libera acesso indevido; no firewall do Nebula, uma regra `groups: ["prod-k8s-worker", "sre"]` verifica se o certificado apresentado no handshake Noise contém ambos os grupos assinados pela CA.

## Como funciona
Por padrão, o firewall do Nebula nega todo tráfego que não corresponda explicitamente a uma regra (`default deny`), e o rastreamento de estado (`conntrack`) garante que pacotes de resposta a conexões permitidas fluam automaticamente. Usar `group: sre` exige pertencer a um único grupo (OR quando múltiplos itens), enquanto `groups: ["sre", "prod"]` exige que o certificado remoto possua **todos** os grupos listados (AND lógico).

## Exemplo
```yaml
firewall:
  outbound:
    - port: any
      proto: any
      host: any
  inbound:
    - port: any
      proto: icmp
      host: any
    - port: 22
      proto: tcp
      groups:
        - sre
        - ssh-bastion
    - port: 5432
      proto: tcp
      group: app-backend
```

## Limites e trade-offs
A seção `firewall:` suporta recarga a quente via `SIGHUP`, permitindo atualizar regras de firewall em produção sem reiniciar a interface `nebula1` nem interromper conexões permitidas.

## Como verificar
Edite uma regra em `firewall.inbound`, teste a sintaxe com `nebula -test -config config.yml` e aplique a mudança a quente com `kill -HUP <pid>`.

## Conexões
- [[nebula-lighthouses-static-host-map-descoberta-peers-dns]] — Veja também: Nebula `Lighthouses` e `static_host_map`: arquitetura de descoberta de pares de baixíssimo custo e DNS opcional.
- [[nebula-nat-traversal-punchy-relay-am-relay-use-relays]] — Veja também: Nebula NAT Traversal e `Relay`: configuração de `punchy` (UDP hole punching) e nós de `relay` para NATs simétricos.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
