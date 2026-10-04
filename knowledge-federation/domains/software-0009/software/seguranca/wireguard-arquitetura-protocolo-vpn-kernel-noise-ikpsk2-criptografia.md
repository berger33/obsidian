---
id: software.seguranca.tranche12.001171
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://www.wireguard.com/protocol/", "https://www.wireguard.com/quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **WireGuard**: VPN Criptográfica no Kernel Linux, Handshake **`Noise_IKpsk2`** e Primitivas Fixas (**ChaCha20-Poly1305, Curve25519, BLAKE2s**)

## Em uma frase
Por que protocolos VPN legados como **IPsec (IKEv2/StrongSwan)** e **OpenVPN** acumularam centenas de milhares de linhas de código e dezenas de CVEs históricas de negociação de cifras (*cipher downgrade attacks*) e parsing ASN.1/X.509, enquanto o **WireGuard** revolucionou a engenharia de redes seguras com menos de 4.000 linhas de código auditáveis integradas diretamente na árvore principal do **Kernel Linux**?

## Por que importa
Criado por **Jason A. Donenfeld (`zx2c4`)**, o WireGuard elimina completamente a "agilidade de cifras" (*cipher agility*) em tempo de pacote: todo túnel WireGuard v1 utiliza a construção criptográfica fixa e estado-da-arte **`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`** do **Noise Protocol Framework** de Trevor Perrin!

## Como funciona
Suas cinco primitivas criptográficas são imutáveis e livres de escolhas inseguras: **(1) `ChaCha20-Poly1305` (RFC 7539)** para criptografia simétrica autenticada (AEAD) dos pacotes de dados; **(2) `Curve25519`** para acordo de chaves Elliptic-Curve Diffie-Hellman (ECDH); **(3) `BLAKE2s` (RFC 7693)** para hashing criptográfico e MACs; **(4) `HKDF` (RFC 5869)** para derivação de chaves de sessão; e **(5) `SipHash24`** para chaves de hashtables no kernel!

## Exemplo
```bash
# Gerar um par de chaves Curve25519 (privada e publica) e uma chave pre-compartilhada (PSK) de resistencia pos-quantica com wg(8)
umask 077
wg genkey | tee peer_a.key | wg pubkey > peer_a.pub
wg genpsk > peer_a_b.psk
ls -l peer_a.key peer_a.pub peer_a_b.psk
```

## Limites e trade-offs
Como o WireGuard opera exclusivamente sobre **UDP** e utiliza chaves públicas estáticas de 32 bytes codificadas em Base64 (44 caracteres), provisionar um peer no WireGuard é tão simples quanto adicionar uma chave pública SSH ao `~/.ssh/authorized_keys` — sem precisar gerenciar cadeias complexas de certificados X.509/ASN.1 no plano de dados!

## Como verificar
Use sempre `umask 077` antes de executar `wg genkey` ou `wg genpsk` para que os arquivos de chave privada nasçam com permissão `0600` (legíveis apenas pelo proprietário).

## Conexões
- [[wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers]] — Veja também: O Conceito Central do WireGuard — **Cryptokey Routing (`AllowedIPs`)**: Unificando Tabela de Roteamento IP e Lista de Controle de Acesso Criptográfica.
- [[wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico]] — Referência cruzada direta com wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico.
- [[wireguard-furtividade-silencio-udp-cookie-reply-mitigacao-dos]] — Referência cruzada direta com wireguard-furtividade-silencio-udp-cookie-reply-mitigacao-dos.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
