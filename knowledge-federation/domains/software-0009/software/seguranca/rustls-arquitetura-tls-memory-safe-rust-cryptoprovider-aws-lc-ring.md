---
id: software.seguranca.tranche14.001331
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

# Arquitetura do **Rustls (`rustls/rustls`)**: Biblioteca Moderna de **TLS 1.3 e TLS 1.2 Memory-Safe em Rust** e Modelo de **`CryptoProvider` (`aws-lc-rs` e `ring`)**

## Em uma frase
Por que projetos críticos de infraestrutura da Internet (como clientes e servidores HTTP em Rust `reqwest`/`hyper`/`axum`, proxies Envoy/Pingora/Linkerd, resolvedores DNS `ickory-dns` e até módulos C via `rustls-ffi` como Apache `mod_tls` e `curl`) estão adotando o **Rustls** como implementação de **TLS 1.3 e TLS 1.2**?

## Por que importa
Historicamente, bibliotecas TLS escritas em C (com centenas de milhares de linhas de parsing manual de buffers ASN.1, X.509 e pacotes de rede) sofreram vulnerabilidades graves de corrupção de memória como o *Heartbleed (`CVE-2014-0160`)*! Escrito em **Rust seguro de memória (*memory-safe*)** e auditado independentemente (com selo OpenSSF Best Practices), o **Rustls** elimina na compilação classes inteiras de bugs de *buffer over-read*, *use-after-free* e *null pointer dereference* na máquina de estados do protocolo TLS!

## Como funciona
Além disso, desde o Rustls 0.22/0.24+, toda primitiva criptográfica é plugável através da trait/struct **`crypto::CryptoProvider`**, mantendo dois provedores oficiais de primeira linha: **(1) `rustls-aws-lc-rs`** (baseado no **AWS-LC** da Amazon: altíssima performance, suporte a **FIPS 140-3** e troca de chaves pós-quântica **`X25519MLKEM768`**!) e **(2) `rustls-ring`** (portabilidade enxuta baseada no `ring`)!

## Exemplo
```rust
// Inicializar explicitamente o CryptoProvider recomendado (aws-lc-rs) e construir um ClientConfig seguro no Rustls
use std::sync::Arc;
use rustls::{ClientConfig, RootCertStore};

fn criar_config_tls(roots: RootCertStore) -> Arc<ClientConfig> {
    let provider = Arc::new(rustls::crypto::aws_lc_rs::default_provider());
    let config = ClientConfig::builder_with_provider(provider)
        .with_safe_default_protocol_versions()
        .expect("versoes TLS seguras")
        .with_root_certificates(roots)
        .with_no_client_auth();
    Arc::new(config)
}
```

## Limites e trade-offs
Por que o Rustls recomenda o provedor **`rustls-aws-lc-rs`** como escolha principal em servidores e aplicações modernas? Porque além de entregar performance de criptografia simétrica e assimétrica altamente otimizada em assembly para x86_64 e ARM64, ele já inclui suporte nativo à troca de chaves híbrida pós-quântica **`X25519MLKEM768`** e modo validado **FIPS 140-3**!

## Como verificar
Para ambientes restritos ou microcontroladores/IoT, a arquitetura `CryptoProvider` também permite plugar provedores comunitários como `rustls-symcrypt` (Microsoft SymCrypt), `rustls-graviola`, `rustls-mbedtls-provider` ou `rustls-rustcrypto`.

## Conexões
- [[rustls-decisoes-seguranca-non-features-tls12-tls13-pfs-aead-obrigatorio]] — Veja também: Filosofia **"Secure by Default" e Non-Features Deliberadas** no Rustls: Por que o Rustls Proíbe Cifras Sem PFS, Modos CBC (`MAC-then-Encrypt`), Renegociação e TLS < 1.2?.
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Referência cruzada direta com rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
