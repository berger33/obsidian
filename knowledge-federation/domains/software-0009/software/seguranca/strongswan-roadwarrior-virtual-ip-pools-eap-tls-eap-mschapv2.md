---
id: software.seguranca.tranche13.001264
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

# VPN de Acesso Remoto (**Roadwarrior**) com strongSwan: **Virtual IP `pools`**, `local_ts = 0.0.0.0/0` e Clientes Nativos (**Windows, macOS, iOS, Android**)

## Em uma frase
Uma das maiores vantagens operacionais do **strongSwan com IKEv2** para acesso remoto de funcionários (**Roadwarrior VPN**) é que **Windows 10/11, macOS, iOS, iPadOS e Android já possuem clientes IKEv2 nativos embutidos no próprio sistema operacional**, dispensando a instalação e atualização de softwares de terceiros nas estações!

## Por que importa
Além de simplificar a distribuição em toda a frota, o suporte nativo do sistema operacional permite reconexão transparente (*MOBIKE* `RFC 4555`) quando o notebook ou celular alterna entre Wi-Fi e 5G.

## Como funciona
Como configurar um gateway Roadwarrior no `swanctl.conf`? **(1)** Na seção **`pools`**, você define a faixa de IPs virtuais internos (`addrs = 10.10.10.0/24`) e os servidores DNS internos (`dns = 10.1.0.53`) que serão atribuídos aos clientes conectados; **(2)** Na conexão `rw`, você referencia **`pools = rw_pool`** (que instrui o strongSwan a responder ao *Configuration Payload (`CP`)* do cliente entregando um IP `/32` do pool!) e deixas `remote_ts` em branco (pois o strongSwan substitui automaticamente `remote_ts` pelo IP virtual atribuído ao cliente!); e **(3)** Na autenticação do cliente (`remote`), você exige **Certificado de Cliente (`auth = pubkey` / `eap-tls`)** ou **EAP (`auth = eap-mschapv2` / `eap-radius`)** integrado ao FreeRADIUS/Active Directory!

## Exemplo
```text
# Exemplo de bloco Roadwarrior com Virtual IP Pool no /etc/swanctl/swanctl.conf
connections {
    rw-corporativo {
        version = 2
        pools = pool-clientes-vpn
        send_cert = always
        local {
            auth = pubkey
            certs = vpn-gateway.pem
            id = vpn.empresa.exemplo.br
        }
        remote {
            auth = eap-tls
        }
        children {
            acesso-interno {
                local_ts = 10.1.0.0/16
                esp_proposals = aes256gcm16-ecp384
            }
        }
    }
}
pools {
    pool-clientes-vpn {
        addrs = 10.10.10.10-10.10.10.250
        dns = 10.1.0.53
    }
}
```

## Limites e trade-offs
Atenção aos requisitos exigidos pelos clientes nativos IKEv2 do **Windows 11, macOS e iOS** sobre o certificado X.509 do gateway (`vpn-gateway.pem`): **(1)** Ele **deve** conter o FQDN exato do servidor na extensão **`subjectAltName` (`--san vpn.empresa.exemplo.br`)**; **(2)** Ele **deve** conter a extensão Extended Key Usage **`serverAuth` (`1.3.6.1.5.5.7.3.1` / `--flag serverAuth`)**; e **(3)** Deve-se configurar **`send_cert = always`** na conexão para que o gateway sempre envie o certificado completo no handshake IKE_AUTH!

## Como verificar
Para máxima segurança Zero Trust sem senhas, utilize **`auth = eap-tls`** (ou `auth = pubkey`) com certificados de cliente gravados em **YubiKey PIV / Smartcard / TPM**!

## Conexões
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Veja também: VPN **Site-to-Site IKEv2** com strongSwan: Geração de PKI com **`pki`**, Autenticação Mútua X.509 (`auth = pubkey`) e Sob Demanda (**`start_action = trap`**).
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Veja também: Engenharia Criptográfica no strongSwan: Configurando **`proposals`** e **`esp_proposals`** com AEAD (**`aes256gcm16`**, **`chacha20poly1305`**) e **PFS (`ecp384`, `curve25519`)**.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-estrutura-swanctl-conf-connections-children-secrets-pools]] — Referência cruzada direta com strongswan-estrutura-swanctl-conf-connections-children-secrets-pools.
- [[strongswan-integracao-hardware-tpm2-pkcs11-hsm-protecao-chaves]] — Referência cruzada direta com strongswan-integracao-hardware-tpm2-pkcs11-hsm-protecao-chaves.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
