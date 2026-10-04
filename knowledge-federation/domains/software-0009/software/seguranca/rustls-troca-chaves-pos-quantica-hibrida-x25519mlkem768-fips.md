---
id: software.seguranca.tranche14.001333
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

# Criptografia **Pós-Quântica Híbrida (`X25519MLKEM768`)** e Conformidade **FIPS 140-3** no Rustls com `aws-lc-rs`: Protegendo o Tráfego TLS Hoje

## Em uma frase
Como habilitar no **Rustls** a troca de chaves híbrida pós-quântica padronizada pelo IETF/NIST (**`X25519MLKEM768`**, que combina a curva elíptica `X25519` com o algoritmo de encapsulamento de chaves baseado em reticulados **NIST FIPS 203 `ML-KEM-768`**) e o modo **FIPS 140-3**?

## Por que importa
Com o provedor oficial **`rustls-aws-lc-rs`**, o suporte ao grupo de troca de chaves híbrido **`X25519MLKEM768`** já vem **integrado e negociado automaticamente no TLS 1.3**! Quando um cliente Rustls conecta a um servidor compatível (como Cloudflare, Chrome, servidores Rustls ou OpenSSL 3.5+), o `ClientHello` oferece `X25519MLKEM768` como grupo preferencial de *Key Share*, protegendo imediatamente a sessão TLS 1.3 contra ataques do tipo *"Harvest Now, Decrypt Later"*!

## Como funciona
E para ambientes regulados que exigem **FIPS 140-3**, basta ativar a feature Cargo `fips` no `rustls` / `aws-lc-rs`: o Rustls passa a usar o módulo criptográfico **AWS-LC FIPS validado pelo NIST CMVP**, restringindo automaticamente as Cipher Suites e curvas exclusivamente aos algoritmos aprovados pelo FIPS!

## Exemplo
```rust
// Verificar programaticamente no Rustls se o ClientConfig/ServerConfig esta operando com um CryptoProvider aprovado para FIPS 140-3
fn verificar_modo_fips(config: &rustls::ClientConfig) {
    assert!(
        config.fips(),
        "O CryptoProvider atual nao esta operando em modo validado FIPS 140-3!"
    );
}
```

## Limites e trade-offs
Veja o método **`config.fips()`** (disponível tanto em `ClientConfig` quanto em `ServerConfig`) no exemplo acima: você pode colocar um `assert!(config.fips())` na inicialização do seu binário em produção para garantir que o serviço jamais suba se alguém compilar a imagem sem o provedor FIPS ativo!

## Como verificar
Como o *Key Share* do `X25519MLKEM768` adiciona ~1.216 bytes ao `ClientHello`, o Rustls gerencia o buffering e a fragmentação dos registros TLS de forma transparente sobre o socket TCP.

## Conexões
- [[rustls-decisoes-seguranca-non-features-tls12-tls13-pfs-aead-obrigatorio]] — Veja também: Filosofia **"Secure by Default" e Non-Features Deliberadas** no Rustls: Por que o Rustls Proíbe Cifras Sem PFS, Modos CBC (`MAC-then-Encrypt`), Renegociação e TLS < 1.2?.
- [[rustls-validacao-certificados-webpki-root-store-pinning-crl]] — Veja também: Verificação Estrita de Certificados X.509 no Rustls com **` rustls-webpki`**: `RootCertStore`, `rustls-native-certs`, `webpki-roots` e Revogação **CRL / OCSP**.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[strongswan-criptografia-pos-quantica-pqc-ikev2-rfc9370-ml-kem-hibrido]] — Referência cruzada direta com strongswan-criptografia-pos-quantica-pqc-ikev2-rfc9370-ml-kem-hibrido.
- [[openssl-conformidade-fips-140-3-fipsmodule-cnf-fipsinstall-validacao]] — Referência cruzada direta com openssl-conformidade-fips-140-3-fipsmodule-cnf-fipsinstall-validacao.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
