---
id: software.seguranca.tranche14.001332
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/rustls/rustls/main/README.md", "https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Filosofia **"Secure by Default" e Non-Features Deliberadas** no Rustls: Por que o Rustls Proíbe Cifras Sem PFS, Modos CBC (`MAC-then-Encrypt`), Renegociação e TLS < 1.2?

## Em uma frase
Diferente de bibliotecas legadas que tentam implementar todas as extensões e cifras obsoletas criadas nos últimos 30 anos (exigindo que o desenvolvedor configure dezenas de flags para desativar opções inseguras), o **Rustls** segue um princípio radical de engenharia de segurança: **"Secure with Zero Configuration — No Obsolete Cryptography by Design"**!

## Por que importa
Consultando a especificação oficial de **`Non-features` (`features.rs`)** do Rustls, veja o que o Rustls **NÃO suporta e JAMAIS suportará deliberadamente**: **(1) Protocolos obsoletos**: sem SSLv1/v2/v3, sem TLS 1.0 e sem TLS 1.1 (apenas **TLS 1.3** e **TLS 1.2**!);

## Como funciona
Na camada complementar de implementação e execução técnica: **(2) Cifras quebradas ou sem AEAD**: sem RC4, sem DES/3DES, sem EXPORT e **sem nenhuma cifra CBC / `MAC-then-Encrypt`** (eliminando 100% da família de ataques *Lucky13*, *POODLE* e *Padding Oracle* — apenas cifras **AEAD**: `AES-128-GCM`, `AES-256-GCM` e `ChaCha20-Poly1305`!); **(3) Sem troca de chaves sem Forward Secrecy**: sem RSA Key Transport estático e sem Diffie-Hellman de logaritmo discreto lento (`FFDHE`) por padrão (apenas **ECDHE com `X25519`, `secp256r1` ou `secp384r1` e `X25519MLKEM768`**!); e **(4) Sem Renegociação TLS 1.2 e sem Compressão TLS (`CRIME`)**!

## Exemplo
```rust
// Auditar em tempo de execucao quais Cipher Suites AEAD e grupos de troca de chaves (KX) estao habilitados no provider padrao do Rustls
fn listar_suites_ativas() {
    let provider = rustls::crypto::aws_lc_rs::default_provider();
    for suite in &provider.cipher_suites {
        println!("CipherSuite ativa: {:?}", suite.suite());
    }
    for kx in &provider.kx_groups {
        println!("Grupo Key Exchange ativo: {:?}", kx.name());
    }
}
```

## Limites e trade-offs
Além disso, no **TLS 1.2**, o Rustls exige proteções modernas contra ataques de *Triple Handshake* e *Downgrade*: suporte a **Extended Master Secret (`RFC 7627` / `RFC 9846`)** e **Signaling Cipher Suite Value (`SCSV` / sentinelas de downgrade do TLS 1.3 no `ServerHello.random`)**!

## Como verificar
Essa superfície mínima de protocolo significa que qualquer aplicação compilada com `ClientConfig` / `ServerConfig` padrão do Rustls já nasce automaticamente com nota **A+** em auditorias de TLS sem precisar de tuning manual de strings de cifras!

## Conexões
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Veja também: Arquitetura do **Rustls (`rustls/rustls`)**: Biblioteca Moderna de **TLS 1.3 e TLS 1.2 Memory-Safe em Rust** e Modelo de **`CryptoProvider` (`aws-lc-rs` e `ring`)**.
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Veja também: Criptografia **Pós-Quântica Híbrida (`X25519MLKEM768`)** e Conformidade **FIPS 140-3** no Rustls com `aws-lc-rs`: Protegendo o Tráfego TLS Hoje.
- [[rustls-validacao-certificados-webpki-root-store-pinning-crl]] — Referência cruzada direta com rustls-validacao-certificados-webpki-root-store-pinning-crl.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
