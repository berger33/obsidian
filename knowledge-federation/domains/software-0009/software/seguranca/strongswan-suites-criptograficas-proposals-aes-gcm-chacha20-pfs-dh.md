---
id: software.seguranca.tranche13.001265
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

# Engenharia Criptográfica no strongSwan: Configurando **`proposals`** e **`esp_proposals`** com AEAD (**`aes256gcm16`**, **`chacha20poly1305`**) e **PFS (`ecp384`, `curve25519`)**

## Em uma frase
Qual é o perigo de não definir explicitamente as diretivas **`proposals`** (na conexão IKE) e **`esp_proposals`** (no bloco `children`) ou de aceitar algoritmos legados como `3des`, `aes128-sha1` ou `modp1024` (DH Group 2 / 5)?

## Por que importa
Algoritmos legados sem autenticação integrada (*non-AEAD* ou grupos Diffie-Hellman abaixo de 2048 bits) são lentos em software e vulneráveis a ataques criptográficos ou de downgrade! No strongSwan moderno, toda proposta criptográfica é uma string separada por hífens que combina: **(1) Cifra AEAD (`aes256gcm16` ou `chacha20poly1305`)**, **(2) Pseudo-Random Function (`prfsha384` ou `prfsha256`, usada apenas no IKE SA)** e **(3) Grupo Diffie-Hellman de Curva Elíptica (`ecp384` = NIST P-384 / DH Group 20, ou `curve25519` = X25519 / DH Group 31)**!

## Como funciona
Ponto crítico de segurança: **SEMPRE inclua o grupo Diffie-Hellman (`ecp384` ou `curve25519`) também dentro de `esp_proposals` (na Child SA)**! Por quê? Porque é a presença do grupo DH em `esp_proposals` que habilita o **Perfect Forward Secrecy (PFS)** a cada *rekey* periódico (`rekey_time = 1h`) do túnel de dados ESP — garantindo que cada hora de tráfego use um segredo efêmero novo e independente!

## Exemplo
```bash
# Listar todos os algoritmos criptograficos AEAD, PRFs e grupos Diffie-Hellman (ECDH / ML-KEM) carregados pelos plugins do strongSwan
swanctl --list-algs
```

## Limites e trade-offs
Por que usar cifras **AEAD (`aes256gcm16` ou `chacha20poly1305`)** em `esp_proposals` é duplamente superior ao antigo `aes256-sha256` (CBC + HMAC separado)? Porque além de ser imune a oráculos de padding, a instrução `AES-GCM` das CPUs modernas calcula a criptografia e a tag de autenticidade de 128 bits (`16` bytes) **em uma única passada de hardware**, reduzindo pela metade a latência e o uso de CPU do Kernel Linux!

## Como verificar
Em dispositivos ARM/móveis sem aceleração AES por hardware, inclua `chacha20poly1305-prfsha256-curve25519` como opção na lista de propostas.

## Conexões
- [[strongswan-roadwarrior-virtual-ip-pools-eap-tls-eap-mschapv2]] — Veja também: VPN de Acesso Remoto (**Roadwarrior**) com strongSwan: **Virtual IP `pools`**, `local_ts = 0.0.0.0/0` e Clientes Nativos (**Windows, macOS, iOS, Android**).
- [[strongswan-criptografia-pos-quantica-pqc-ikev2-rfc9370-ml-kem-hibrido]] — Veja também: VPNs **Pós-Quânticas Híbridas (PQC)** no strongSwan: Implementando **RFC 9370 (*Multiple Key Exchanges in IKEv2*)** com **ML-KEM (`ke1_mlkem768` / `mlkem1024`)**.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
