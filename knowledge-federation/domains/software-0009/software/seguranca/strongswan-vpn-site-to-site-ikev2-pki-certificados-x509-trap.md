---
id: software.seguranca.tranche13.001263
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/strongswan/strongswan/master/README.md", "https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# VPN **Site-to-Site IKEv2** com strongSwan: Geração de PKI com **`pki`**, Autenticação Mútua X.509 (`auth = pubkey`) e Sob Demanda (**`start_action = trap`**)

## Em uma frase
Ao conectar duas redes corporativas ou VPCs de nuvem via **Site-to-Site IPsec VPN**, por que usar **Autenticação Mútua por Certificados X.509 (`auth = pubkey`)** em vez de senhas pré-compartilhadas (`PSK`), e o que faz a diretiva **`start_action = trap`**?

## Por que importa
Com **Certificados X.509 emitidos por uma CA interna dedicada**, cada gateway possui sua própria chave privada exclusiva (`ECDSA P-384` ou `Ed25519`), eliminando o compartilhamento de segredos simétricos (`PSK`) e permitindo adicionar ou revogar filiais sem tocar na configuração dos demais gateways! O próprio strongSwan inclui a ferramenta oficial de linha de comando **`pki`** (`pki --gen`, `pki --self`, `pki --pub`, `pki --issue`) para criar a CA raiz e emitir os certificados dos gateways com a extensão obrigatória **`--flag serverAuth`** e **`--san <fqdn_ou_ip>`**!

## Como funciona
Já a diretiva **`start_action = trap`** no bloco `children` instala imediatamente as **Políticas de Segurança (`XFRM Trap Policies`)** no Kernel Linux: no exato milissegundo em que o primeiro pacote IP da sub-rede `10.1.0.0/16` tenta sair rumo a `10.2.0.0/16`, o Kernel Linux avisa o daemon `charon`, que fecha o túnel IKEv2/ESP automaticamente sob demanda!

## Exemplo
```bash
# Gerar uma chave privada Ed25519 e emitir um certificado de gateway VPN com a ferramenta nativa 'pki' do strongSwan
pki --gen --type ed25519 --outform pem > /etc/swanctl/private/gw-matrizKey.pem
chmod 600 /etc/swanctl/private/gw-matrizKey.pem
swanctl --list-Pols
```

## Limites e trade-offs
Combine sempre **`start_action = trap`** com **`dpd_delay = 30s`** (*Dead Peer Detection* no bloco da conexão): assim o strongSwan envia *keepalives* IKEv2 a cada 30 segundos quando não há tráfego de retorno e renegocia a Child SA automaticamente se o link WAN do parceiro oscilar!

## Como verificar
Verifique no firewall (`nftables` / `iptables` / Security Group) que as portas **UDP `500`** (IKE), **UDP `4500`** (NAT-Traversal) e o protocolo IP **`50` (`ESP`)** estão liberados entre os IPs públicos dos dois gateways.

## Conexões
- [[strongswan-estrutura-swanctl-conf-connections-children-secrets-pools]] — Veja também: Anatomia do **`/etc/swanctl/swanctl.conf`**: As 4 Seções Principais (**`connections`, `children`, `secrets`, `pools`**) e Diretórios `/etc/swanctl/x509*`.
- [[strongswan-roadwarrior-virtual-ip-pools-eap-tls-eap-mschapv2]] — Veja também: VPN de Acesso Remoto (**Roadwarrior**) com strongSwan: **Virtual IP `pools`**, `local_ts = 0.0.0.0/0` e Clientes Nativos (**Windows, macOS, iOS, Android**).
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf]] — Referência cruzada direta com strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
