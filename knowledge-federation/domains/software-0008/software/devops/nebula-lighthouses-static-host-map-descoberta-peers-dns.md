---
id: software.devops.tranche19.001884
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

# Nebula `Lighthouses` e `static_host_map`: arquitetura de descoberta de pares de baixíssimo custo e DNS opcional

## Em uma frase
No Nebula, um **Lighthouse** (`lighthouse.am_lighthouse: true`) é um nó de descoberta leve com endereço IP ou DNS público fixo (normalmente na porta UDP `4242`) que mantém em memória os endereços IP reais reportados pelos demais nós da malha para que eles possam se encontrar e abrir túneis diretos.

## Por que importa
Como o Lighthouse não roteia o tráfego de dados dos demais nós nem armazena estado em banco de dados, ele consome pouquíssima CPU e memória (uma VM básica de $6/mês atende milhares de nós).

## Como funciona
Na configuração dos nós comuns (`am_lighthouse: false`), a seção **`static_host_map`** mapeia o IP Nebula de cada Lighthouse (ex.: `"192.168.100.1"`) para a lista de seus endereços reais na internet (`["203.0.113.10:4242"]`), e a seção `lighthouse.hosts` lista os IPs Nebula dos Lighthouses (`["192.168.100.1"]`). Nos próprios nós Lighthouse, `am_lighthouse: true` deve estar ativo e `lighthouse.hosts` **deve ficar vazio (`[]`)**.

## Exemplo
```yaml
static_host_map:
  "192.168.100.1": ["203.0.113.10:4242"]
  "192.168.100.2": ["198.51.100.20:4242"]

lighthouse:
  am_lighthouse: false
  interval: 60
  hosts:
    - "192.168.100.1"
    - "192.168.100.2"
```

## Limites e trade-offs
Atenção às duas regras de ouro documentadas no `config.yml` oficial: 1) em um nó Lighthouse (`am_lighthouse: true`), a lista `lighthouse.hosts` deve ser vazia; e 2) nos demais nós, `lighthouse.hosts` deve conter os **IPs Nebula** dos Lighthouses, e nunca seus IPs públicos reais.

## Como verificar
Valide o `config.yml` de um Lighthouse e de um nó cliente executando `nebula -test -config config.yml`.

## Conexões
- [[nebula-rotacao-ca-zero-downtime-sighup-blocklist-certificados]] — Veja também: Nebula Rotação de CA e Revogação: recarga de certificados sem downtime via `SIGHUP` e `pki.blocklist`.
- [[nebula-firewall-stateful-inbound-outbound-groups-cidr-ca-sha]] — Veja também: Nebula Stateful Firewall: filtragem de tráfego `inbound`/`outbound` baseada em `group`/`groups`, `proto`, `port` e `cidr`.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
