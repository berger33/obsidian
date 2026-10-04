---
id: software.seguranca.tranche14.001334
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

# Verificação Estrita de Certificados X.509 no Rustls com **` rustls-webpki`**: `RootCertStore`, `rustls-native-certs`, `webpki-roots` e Revogação **CRL / OCSP**

## Em uma frase
Por que a validação da cadeia de certificados X.509 no **Rustls** (realizada pela biblioteca **`rustls-webpki`**) é muito mais rigorosa e resistente a vulnerabilidades de falsificação de CA que implementações X.509 legadas?

## Por que importa
O **`rustls-webpki`** foi projetado especificamente em torno do perfil **WebPKI (`RFC 5280` + requisitos do CA/Browser Forum)**: **(1)** Ele separa estritamente **Certificados de Autoridade Certificadora (`BasicConstraints: CA=TRUE`)** de **Certificados de Entidade Final (`End-Entity`)** — conforme documentado em `features.rs`, o verificador padrão do Rustls **recusa usar uma âncora de confiança (`Trust Anchor`) simultaneamente como CA e como certificado de servidor autoassinado**, eliminando ambiguidades na construção de caminhos (`Path Building`)!; **(2)** Ele ignora o legado `Common Name (CN)` e exige validação estrita de `SubjectAlternativeName` (DNS ou IP); e **(3)** Valida restrições de subárvore **`NameConstraints`**!

## Como funciona
Para carregar as CAs confiáveis no `RootCertStore`, você pode escolher entre **`rustls-platform-verifier` / `rustls-native-certs`** (usa o Trust Store do sistema operacional, ideal para ambientes corporativos com PKI interna!) ou **`webpki-roots`** (embute as raízes do Mozilla Root Program diretamente no binário)!

## Exemplo
```rust
// Configurar um WebPkiServerVerifier no Rustls com suporte a verificacao de Listas de Certificados Revogados (CRLs)
use std::sync::Arc;
use rustls::client::WebPkiServerVerifier;
use rustls::RootCertStore;
use rustls_pki_types::CertificateRevocationListDer;

fn criar_verificador_com_crl(
    roots: Arc<RootCertStore>,
    crls: Vec<CertificateRevocationListDer<'static>>,
) -> Arc<WebPkiServerVerifier> {
    WebPkiServerVerifier::builder(roots)
        .with_crls(crls)
        .build()
        .expect("verificador X.509 com CRL")
}
```

## Limites e trade-offs
Usando o **`WebPkiServerVerifier::builder(roots).with_crls(crls)`** (e o equivalente **`WebPkiClientVerifier`** para mTLS no servidor!), você anexa Listas de Certificados Revogados (`CRLs` em formato DER) e controla se a checagem de revogação deve cobrir toda a cadeia ou apenas o certificado folha (`only_check_end_entity_revocation`) e como tratar status desconhecido (`enforce_revocation_expiry`)!

## Como verificar
Nunca implemente a trait `ServerCertVerifier` com um verificador vazio que ignora erros de certificado em código de produção!

## Conexões
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Veja também: Criptografia **Pós-Quântica Híbrida (`X25519MLKEM768`)** e Conformidade **FIPS 140-3** no Rustls com `aws-lc-rs`: Protegendo o Tráfego TLS Hoje.
- [[rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust]] — Veja também: Autenticação Mútua (**mTLS Zero-Trust**) e Seleção Dinâmica de Certificados via **SNI (`ResolvesServerCert`)** em Servidores Rustls.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Referência cruzada direta com openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
