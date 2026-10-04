---
id: software.seguranca.tranche14.001335
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

# Autenticação Mútua (**mTLS Zero-Trust**) e Seleção Dinâmica de Certificados via **SNI (`ResolvesServerCert`)** em Servidores Rustls

## Em uma frase
Como construir em Rust (usando `rustls` + `tokio-rustls` / `axum` / `tonic` gRPC) um servidor de microsserviço ou API Gateway Zero-Trust que **exige Certificado de Cliente X.509 válido (`mTLS`)**, valida revogação contra uma CRL interna e ainda seleciona dinamicamente o certificado de servidor correto com base no **SNI (`Server Name Indication`)** enviado pelo cliente?

## Por que importa
No lado do servidor (`ServerConfig`), o Rustls oferece o **`WebPkiClientVerifier::builder(client_roots)`**! Diferente de configurações antigas onde mTLS era "tudo ou nada" sem granularidade, o `WebPkiClientVerifier` permite: **(1) Exigir certificado de cliente obrigatório** (rejeitando no handshake qualquer conexão sem certificado assinado pela CA interna `.build()`); **(2) Permitir certificado opcional (`.allow_unauthenticated()`)** para rotas mistas; e **(3) Anexar CRLs de clientes revogados (`.with_crls(...)`)**!

## Como funciona
E quando o mesmo servidor atende múltiplos domínios (`api.empresa.br`, `auth.empresa.br`) ou rotaciona certificados em tempo real sem reiniciar o processo, você utiliza **`ResolvesServerCertUsingSni`** ou implementa a trait **`ResolvesServerCert`**!

## Exemplo
```rust
// Configurar um ServerConfig no Rustls exigindo Autenticacao Mutua (mTLS) obrigatoria de clientes assinados pela CA interna
use std::sync::Arc;
use rustls::{RootCertStore, ServerConfig};
use rustls::server::WebPkiClientVerifier;
use rustls_pki_types::{CertificateDer, PrivateKeyDer};

fn criar_servidor_mtls(
    ca_clientes: Arc<RootCertStore>,
    cert_cadeia: Vec<CertificateDer<'static>>,
    chave_privada: PrivateKeyDer<'static>,
) -> Arc<ServerConfig> {
    let client_verifier = WebPkiClientVerifier::builder(ca_clientes)
        .build()
        .expect("verificador mTLS de clientes");

    let config = ServerConfig::builder()
        .with_client_cert_verifier(client_verifier)
        .with_single_cert(cert_cadeia, chave_privada)
        .expect("certificado e chave privada validos");
    Arc::new(config)
}
```

## Limites e trade-offs
Após o handshake mTLS concluir, a aplicação pode inspecionar a cadeia exata de certificados apresentada pelo cliente chamando **`connection.peer_certificates()`** sobre a sessão Rustls — permitindo extrair o `SPIFFE ID` (URI SAN, usado no Istio/SPIRE) ou o `Subject` do cliente para decisões de autorização em nível de rota!

## Como verificar
Para recarregar certificados TLS renovados pelo Certbot/Step-CA em memória com zero downtime, implemente a trait `ResolvesServerCert` lendo um `ArcSwap<CertifiedKey>` atualizado por um watcher de arquivo ou sinal `SIGHUP`.

## Conexões
- [[rustls-validacao-certificados-webpki-root-store-pinning-crl]] — Veja também: Verificação Estrita de Certificados X.509 no Rustls com **` rustls-webpki`**: `RootCertStore`, `rustls-native-certs`, `webpki-roots` e Revogação **CRL / OCSP**.
- [[rustls-privacidade-encrypted-client-hello-ech-rfc9849-sni-alpn]] — Veja também: Privacidade no Handshake TLS 1.3 com **Encrypted Client Hello (`ECH` — `RFC 9849`)**, Compressão de Certificados (**`RFC 8879`**) e **Raw Public Keys (`RFC 7250`)** no Rustls.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
