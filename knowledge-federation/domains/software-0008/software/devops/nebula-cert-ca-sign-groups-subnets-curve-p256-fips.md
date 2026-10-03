---
id: software.devops.tranche19.001882
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
fontes: ["https://raw.githubusercontent.com/slackhq/nebula/master/README.md", "https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml", "https://github.com/slackhq/nebula"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nebula PKI (`nebula-cert`): emissão de certificados com grupos de segurança, restrições de sub-rede e modo `P256` / FIPS 140-3

## Em uma frase
O binário **`nebula-cert`** gerencia toda a Autoridade Certificadora (CA) e os certificados de hosts do Nebula, permitindo assinar nos próprios certificados o nome do nó (`-name`), o IP e máscara da rede overlay (`-ip`), a lista de grupos de segurança (`-groups`), sub-redes roteáveis (`-subnets`) e a curva criptográfica (`Curve25519` padrão ou NIST **`P256`** para conformidade **FIPS 140-3**).

## Por que importa
Se uma CA intermediária de uma equipe de desenvolvimento pudesse assinar certificados para qualquer IP da rede de produção ou adicionar o grupo `prod-dba`, ela comprometeria o isolamento da malha.

## Como funciona
O `nebula-cert ca` aceita as flags `-groups`, `-ips` e `-subnets` na própria criação da CA para restringir criptograficamente quais grupos e faixas de IP aquela CA tem permissão para assinar nos certificados filhos. Além disso, `nebula-cert ca -curve P256` combinado com binários compilados com `GOFIPS140=v1.0.0` habilita handshakes ECDH/ECDSA P256 e `AES-256-GCM` compatíveis com FIPS 140-3.

## Exemplo
```bash
# Criando uma CA restrita a assinar apenas IPs na faixa 10.42.0.0/16 e grupos específicos:
nebula-cert ca -name "Prod CA" \
  -ips "10.42.0.0/16" \
  -groups "prod-web,prod-db,prod-k8s" \
  -duration 8760h
nebula-cert print -path ca.crt -json
```

## Limites e trade-offs
Por padrão, uma CA criada com `nebula-cert ca` tem validade de **1 ano** e os certificados de host expiram 1 segundo antes da CA; planeje a rotação da CA com antecedência.

## Como verificar
Execute `nebula-cert verify -ca ca.crt -crt host.crt` para validar criptograficamente se um certificado de host é válido perante o bundle de CAs.

## Conexões
- [[nebula-arquitetura-overlay-network-noise-protocol-pki-lighthouses]] — Veja também: Nebula: arquitetura de rede overlay escalável baseada no Noise Protocol Framework, certificados PKI e `Lighthouses`.
- [[nebula-rotacao-ca-zero-downtime-sighup-blocklist-certificados]] — Veja também: Nebula Rotação de CA e Revogação: recarga de certificados sem downtime via `SIGHUP` e `pki.blocklist`.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
