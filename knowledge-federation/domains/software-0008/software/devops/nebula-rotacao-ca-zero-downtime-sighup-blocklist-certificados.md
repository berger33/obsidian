---
id: software.devops.tranche19.001883
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

# Nebula Rotação de CA e Revogação: recarga de certificados sem downtime via `SIGHUP` e `pki.blocklist`

## Em uma frase
A seção **`pki:`** do `config.yml` do Nebula suporta recarga a quente via sinal **`SIGHUP`** (recarregando `ca.crt`, `host.crt` e `host.key` do disco sem derrubar túneis existentes), múltiplos certificados CA concatenados em `ca.crt` para rotação de CA sem downtime, **`blocklist`** de fingerprints SHA-256 e **`disconnect_invalid: true`**.

## Por que importa
Como os certificados Nebula têm validade finita (1 ano por padrão) e não consultam um servidor OCSP central a cada pacote, operadores precisam saber como rotacionar a CA sem interromper milhares de conexões e como revogar imediatamente um laptop roubado.

## Como funciona
Para **rotacionar a CA**, você gera a nova CA (`ca-new.crt`), concatena o conteúdo de `ca-old.crt` e `ca-new.crt` no arquivo `ca.crt` de todos os nós, emite novos certificados de host assinados pela nova CA e envia `kill -HUP $(pidof nebula)`. Para **revogar** um certificado comprometido antes de expirar, basta obter seu `fingerprint` com `nebula-cert print` e adicioná-lo à lista `pki.blocklist` no `config.yml`.

## Exemplo
```yaml
pki:
  ca: /etc/nebula/ca.crt
  cert: /etc/nebula/host.crt
  key: /etc/nebula/host.key
  disconnect_invalid: true
  blocklist:
    - c99d4e650533b92061b09918e838a5a0a6aaee21eed1d12fd937682865936c72
```

## Limites e trade-offs
Habilite sempre `disconnect_invalid: true` na seção `pki:` para garantir que clientes cujos certificados expiraram após o túnel já estar aberto sejam desconectados imediatamente.

## Como verificar
Obtenha o fingerprint de um certificado com `nebula-cert print -path host.crt` e valide a configuração com `nebula -test -config /etc/nebula/config.yml`.

## Conexões
- [[nebula-cert-ca-sign-groups-subnets-curve-p256-fips]] — Veja também: Nebula PKI (`nebula-cert`): emissão de certificados com grupos de segurança, restrições de sub-rede e modo `P256` / FIPS 140-3.
- [[nebula-lighthouses-static-host-map-descoberta-peers-dns]] — Veja também: Nebula `Lighthouses` e `static_host_map`: arquitetura de descoberta de pares de baixíssimo custo e DNS opcional.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
