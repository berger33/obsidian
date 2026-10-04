---
id: software.devops.tranche19.001888
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

# Nebula `local_allow_list` e `remote_allow_list`: filtragem de interfaces virtuais (`docker.*`, `cni.*`) anunciadas ao Lighthouse

## Em uma frase
Em servidores que executam Docker ou Kubernetes, as opções **`lighthouse.local_allow_list`** e **`lighthouse.remote_allow_list`** evitam que o nó Nebula anuncie ao Lighthouse endereços IP internos irrelevantes de bridges de containers (`docker0`, `br-*`, `cni0`, `flannel.1`, `cali*`) ou tente fazer handshake para faixas privadas colidentes.

## Por que importa
Se dois servidores em data centers distintos tiverem ambos uma bridge `docker0` com o IP `172.17.0.1` e anunciarem esse IP ao Lighthouse, quando tentarem se conectar o Nebula poderá enviar pacotes UDP para a própria bridge `172.17.0.1` local em vez do IP roteável real.

## Como funciona
Em `lighthouse.local_allow_list.interfaces`, é possível passar expressões regulares de nomes de interface com `false` (ex.: `'docker.*': false`, `'br-.*': false`, `'veth.*': false`) e restringir quais CIDRs locais são reportados ao Lighthouse.

## Exemplo
```yaml
lighthouse:
  am_lighthouse: false
  hosts:
    - "192.168.100.1"
  local_allow_list:
    interfaces:
      tun0: false
      'docker.*': false
      'br-.*': false
      'veth.*': false
```

## Limites e trade-offs
Conforme documentado no `config.yml`, se você combinar regras `true` (allow) e `false` (deny) de CIDRs IPv4 em `remote_allow_list`, você **deve** definir explicitamente uma regra padrão para `"0.0.0.0/0"` (e `"::/0"` para IPv6).

## Como verificar
Teste as regras de `local_allow_list` com `nebula -test -config config.yml` antes de reiniciar o serviço.

## Conexões
- [[nebula-unsafe-routes-roteamento-sub-redes-externas-subnet-routing]] — Veja também: Nebula `unsafe_routes`: roteamento de tráfego para sub-redes externas que não executam o agente Nebula.
- [[nebula-tuning-performance-listen-batch-routines-buffers-mtu]] — Veja também: Nebula Tuning de Alta Performance: ajuste de `routines`, `listen.batch`, buffers de socket (`read_buffer`/`write_buffer`) e MTU.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
