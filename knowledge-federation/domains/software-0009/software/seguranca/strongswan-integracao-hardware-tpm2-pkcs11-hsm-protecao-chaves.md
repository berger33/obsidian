---
id: software.seguranca.tranche13.001269
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

# Proteção de Chaves Privadas de VPN em Hardware com o strongSwan: Integração Nativa com **TPM 2.0 (`handle`)**, **Smartcards / YubiKey (`PKCS#11`)** e HSMs

## Em uma frase
Se um invasor conseguir acesso `root` temporário a um servidor de borda Linux que atua como gateway VPN IPsec e copiar o diretório `/etc/swanctl/private/`, como impedir matematicamente que ele consiga roubar a chave privada do gateway VPN e personificar a matriz da empresa a partir de outra máquina?

## Por que importa
Armazenando a chave privada do gateway dentro do chip criptográfico de hardware **TPM 2.0 (*Trusted Platform Module*)** da placa-mãe do servidor (ou em um token **YubiKey PIV / Smartcard / HSM via `PKCS#11`**) em vez de salvá-la como um arquivo `.pem` em disco!

## Como funciona
O strongSwan possui suporte nativo de primeira classe a **TPM 2.0 (`tpm` plugin + `tss2`)** e a **PKCS#11 (`pkcs11` plugin)**: quando a chave privada RSA/ECDSA é gerada ou selada dentro do objeto persistente do TPM 2.0 (ex.: handle hexadecimal **`0x81010002`**), ela **jamais pode ser exportada do chip físico**. No `swanctl.conf`, basta declarar uma seção `secrets { token-gw { handle = 0x81010002 } }` — toda vez que o daemon `charon` precisa assinar o handshake IKEv2 (`IKE_AUTH`), ele envia o hash do desafio para o chip TPM 2.0 / HSM assinar internamente!

## Exemplo
```text
# Referenciar no /etc/swanctl/swanctl.conf uma chave privada e um certificado X.509 armazenados dentro do chip de hardware TPM 2.0
connections {
    matriz-segura {
        version = 2
        local {
            auth = pubkey
            cert_1 {
                handle = 0x01800004
            }
        }
    }
}
secrets {
    private-tpm-gateway {
        handle = 0x81010002
    }
}
```

## Limites e trade-offs
Você pode inspecionar a chave pública de um objeto do TPM 2.0 diretamente com a ferramenta **`pki --pub --in 0x81010002 --type priv`** do strongSwan para gerar a CSR (*Certificate Signing Request*) sem que a chave privada jamais saia do chip TPM!

## Como verificar
Para estações Linux de administradores (Roadwarriors), referenciar `slot = 0` e `module = opensc-pkcs11` na seção `secrets { token-yubikey { ... } }` permite autenticar na VPN IKEv2 exigindo o PIN e a presença física da **YubiKey PIV** na porta USB.

## Conexões
- [[strongswan-validacao-revogacao-certificados-crl-ocsp-authorities]] — Veja também: Autoridades Certificadoras (**`authorities`**), Validação **OCSP / CRL** e Políticas Estritas de Revogação (`revocation = strict`) no strongSwan.
- [[strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump]] — Veja também: Diagnóstico e Troubleshooting Avançado de Túneis IPsec no Linux: **`swanctl --list-sas`**, **`swanctl --log`**, **`ip -s xfrm state/policy`** e NAT-Traversal (`UDP 4500`).
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Referência cruzada direta com strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap.
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Referência cruzada direta com keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
