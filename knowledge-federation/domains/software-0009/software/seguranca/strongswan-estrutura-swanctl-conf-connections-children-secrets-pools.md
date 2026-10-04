---
id: software.seguranca.tranche13.001262
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

# Anatomia do **`/etc/swanctl/swanctl.conf`**: As 4 Seções Principais (**`connections`, `children`, `secrets`, `pools`**) e Diretórios `/etc/swanctl/x509*`

## Em uma frase
Como é organizado o arquivo de configuração declarativo **`/etc/swanctl/swanctl.conf`** e a hierarquia de diretórios de chaves e certificados de `/etc/swanctl/` no strongSwan moderno?

## Por que importa
O arquivo `swanctl.conf` é estruturado em **quatro seções de topo** claras e legíveis: **(1) `connections { ... }`** — define os túneis **IKE SA (Fase 1)**, especificando `version = 2` (IKEv2!), endereços `local_addrs` / `remote_addrs`, propostas criptográficas `proposals` e blocos de autenticação `local { auth = ... }` e `remote { auth = ... }`; **(2) `children { ... }` (aninhado dentro de cada conexão)** — define os túneis de dados **CHILD SA / ESP (Fase 2)**, especificando seletores de tráfego `local_ts` e `remote_ts`, `esp_proposals` e a ação inicial `start_action = trap|start|none`; **(3) `secrets { ... }`** — define chaves pré-compartilhadas (`ike-...`), credenciais EAP ou senhas de chaves privadas; e **(4) `pools { ... }`** — define pools de IPs virtuais para clientes Roadwarrior!

## Como funciona
Além disso, o `swanctl --load-creds` carrega automaticamente certificados e chaves dos subdiretórios padronizados: **`/etc/swanctl/x509/`** (certificados locais), **`/etc/swanctl/x509ca/`** (Autoridades Certificadoras raiz/intermediárias confiáveis!), **`/etc/swanctl/x509crl/`** e **`/etc/swanctl/private/`** (chaves privadas com permissão `0600`)!

## Exemplo
```text
# Estrutura essencial de /etc/swanctl/swanctl.conf com IKEv2 (version = 2), autenticacao mútua por certificado X.509 e Child SA ESP
connections {
    matriz-filial {
        version = 2
        local_addrs  = 198.51.100.10
        remote_addrs = 203.0.113.20
        proposals = aes256gcm16-prfsha384-ecp384
        local {
            auth = pubkey
            certs = gateway-matriz.pem
            id = matriz.vpn.exemplo.br
        }
        remote {
            auth = pubkey
            id = filial.vpn.exemplo.br
        }
        children {
            rede-interna {
                local_ts  = 10.1.0.0/16
                remote_ts = 10.2.0.0/16
                esp_proposals = aes256gcm16-ecp384
                start_action = trap
            }
        }
    }
}
```

## Limites e trade-offs
Sempre defina explicitamente **`version = 2`** em todas as conexões do `swanctl.conf` para aceitar exclusivamente o protocolo moderno **IKEv2 (`RFC 7296`)** e rejeitar negociações legadas IKEv1!

## Como verificar
Ao editar apenas as conexões, você pode recarregar sem afetar túneis ativos usando **`swanctl --load-conns`**!

## Conexões
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Veja também: Arquitetura Moderna do **strongSwan (`strongswan/strongswan`)**: Daemon **`charon`**, Protocolo **`vici`** e Configuração Declarativa **`swanctl.conf`**.
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Veja também: VPN **Site-to-Site IKEv2** com strongSwan: Geração de PKI com **`pki`**, Autenticação Mútua X.509 (`auth = pubkey`) e Sob Demanda (**`start_action = trap`**).
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Referência cruzada direta com strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
