---
id: software.seguranca.tranche13.001266
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

# VPNs **Pós-Quânticas Híbridas (PQC)** no strongSwan: Implementando **RFC 9370 (*Multiple Key Exchanges in IKEv2*)** com **ML-KEM (`ke1_mlkem768` / `mlkem1024`)**

## Em uma frase
Qual é a maior ameaça de longo prazo contra túneis VPN IPsec/IKEv2 que transportam segredos industriais, financeiros, diplomáticos ou de estado? O ataque **"Harvest Now, Decrypt Later" (*Coletar Agora, Descriptografar Depois*)**: um adversário intercepta e grava hoje na internet o handshake IKEv2 e os pacotes ESP cifrados; quando computadores quânticos criptograficamente relevantes (CRQCs) estiverem disponíveis, o algoritmo de Shor quebrará retroativamente a troca de chaves clássica ECDH (`ecp384`/`curve25519`) e descriptografará todo o tráfego gravado!

## Por que importa
O **strongSwan (6.0+)** é pioneiro mundial na implementação da **RFC 9370 (*Multiple Key Exchanges in IKEv2*)** e do padrão pós-quântico do NIST **FIPS 203 (`ML-KEM`, antigo Crystals-Kyber)**!

## Como funciona
Como funciona a proposta híbrida no `swanctl.conf`? Você combina a troca de chaves clássica (**`ecp384` ou `curve25519`**) com até 7 trocas de chaves adicionais (`ke1_...` a `ke7_...`) usando **`ke1_mlkem768`** ou **`ke1_mlkem1024`**: **`proposals = aes256gcm16-prfsha384-ecp384-ke1_mlkem768`**! O segredo final do túnel é derivado da combinação criptográfica de **ambos** os algoritmos (ECDH clássico + ML-KEM pós-quântico via troca `IKE_INTERMEDIATE`), garantindo segurança mesmo que um dos dois paradigmas matemáticos sofra qualquer avanço futuro!

## Exemplo
```text
# Configuracao de proposta IKEv2 e ESP Hibrida Pos-Quantica (ECDH P-384 + NIST FIPS 203 ML-KEM-768 / ML-KEM-1024 via RFC 9370) no swanctl.conf
connections {
    tunel-pqc-hibrido {
        version = 2
        proposals = aes256gcm16-prfsha384-ecp384-ke1_mlkem768
        children {
            dados-criticos {
                esp_proposals = aes256gcm16-ecp384-ke1_mlkem768
            }
        }
    }
}
```

## Limites e trade-offs
Como as chaves públicas e *ciphertexts* do **ML-KEM-768 / ML-KEM-1024** têm mais de 1.000 bytes (podendo ultrapassar o MTU UDP padrão de 1.500 bytes na internet), o strongSwan habilita por padrão nas conexões IKEv2 a diretiva **`fragmentation = yes` (`RFC 7383` — *IKEv2 Message Fragmentation*)**, fragmentando os pacotes IKE ao nível da aplicação antes do envio UDP para que nunca sejam descartados por firewalls no caminho!

## Como verificar
Verifique com `swanctl --list-algs | grep -i mlkem` se o plugin de suporte a `mlkem` (nativo ou via `openssl` / `oqs` / `wolfssl`) está ativo na sua versão do strongSwan.

## Conexões
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Veja também: Engenharia Criptográfica no strongSwan: Configurando **`proposals`** e **`esp_proposals`** com AEAD (**`aes256gcm16`**, **`chacha20poly1305`**) e **PFS (`ecp384`, `curve25519`)**.
- [[strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf]] — Veja também: VPN Baseada em Rota (**Route-Based VPN**) no strongSwan: Interfaces Virtuais do Kernel Linux (**XFRM Interfaces `xfrmi`** com **`if_id_in` / `if_id_out`**) e BGP/OSPF.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
