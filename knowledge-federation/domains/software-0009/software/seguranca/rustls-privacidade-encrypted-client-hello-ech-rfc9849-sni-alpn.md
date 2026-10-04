---
id: software.seguranca.tranche14.001336
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

# Privacidade no Handshake TLS 1.3 com **Encrypted Client Hello (`ECH` — `RFC 9849`)**, Compressão de Certificados (**`RFC 8879`**) e **Raw Public Keys (`RFC 7250`)** no Rustls

## Em uma frase
Em uma conexão TLS 1.3 padrão, embora todo o tráfego HTTP e até o certificado do servidor já viajem criptografados, um único campo crítico no primeiro pacote (`ClientHello`) ainda viajava em texto claro visível para qualquer provedor de internet (ISP) ou sniffer passivo no caminho: a extensão **`SNI` (*Server Name Indication*)**, que revela o nome do domínio exato que o usuário está acessando!

## Por que importa
Como o **Rustls** resolve esse último vazamento de metadados do TLS 1.3 e acelera handshakes modernos?

## Como funciona
O Rustls implementa nativamente no cliente o padrão **Encrypted Client Hello (`ECH`, `RFC 9849`)**! Com o **ECH** habilitado (obtendo a `EchConfigList` publicada pelo domínio em registros DNS `HTTPS` / `SVCB` via DoH/DoT), o cliente Rustls divide o `ClientHello` em dois: um **`ClientHelloOuter`** público (que mostra apenas o nome genérico do provedor de borda/CDN, ex.: `cloudflare-ech.com`) e um **`ClientHelloInner` 100% criptografado via HPKE (`RFC 9180`)** que contém o **SNI verdadeiro, o ALPN privado e as extensões sensíveis**!

## Exemplo
```rust
// Configurar o modo Encrypted Client Hello (ECH - RFC 9849) no Rustls usando os parametros ECH publicados no registro DNS HTTPS
use rustls::client::{EchConfig, EchMode};
use rustls::crypto::aws_lc_rs::hpke::ALL_SUPPORTED_SUITES;
use rustls_pki_types::EchConfigListBytes;

fn criar_modo_ech(ech_dns_bytes: EchConfigListBytes<'static>) -> EchMode {
    let ech_config = EchConfig::new(ech_dns_bytes, ALL_SUPPORTED_SUITES)
        .expect("EchConfig HPKE suportada");
    EchMode::from(ech_config)
}
```

## Limites e trade-offs
E o que acontece se você também habilitar a **Compressão de Certificados (`RFC 8879`)** suportada pelo Rustls (via Brotli/Zlib)? Cadeias de certificados X.509 (especialmente importantes com certificados futuros pós-quânticos maiores!) são comprimidas e cacheadas em memória, reduzindo o tamanho das mensagens `Certificate` em até **70%** e evitando que o handshake TLS exceda a janela inicial de congestionamento TCP (`initcwnd`)!

## Como verificar
Para comunicações Machine-to-Machine (M2M) / IoT onde os pares já conhecem os hashes das chaves públicas um do outro sem precisar da sobrecarga ASN.1 de certificados X.509 completos, o Rustls também suporta **Raw Public Keys (`RFC 7250`)** no TLS 1.3!

## Conexões
- [[rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust]] — Veja também: Autenticação Mútua (**mTLS Zero-Trust**) e Seleção Dinâmica de Certificados via **SNI (`ResolvesServerCert`)** em Servidores Rustls.
- [[rustls-retomada-sessao-tickets-0rtt-anti-replay-seguranca]] — Veja também: Retomada de Sessão (**Session Resumption**), Rotação de **Session Tickets** e Riscos de **Replay em Dados `0-RTT` (`EarlyData`)** no Rustls.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Referência cruzada direta com rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
