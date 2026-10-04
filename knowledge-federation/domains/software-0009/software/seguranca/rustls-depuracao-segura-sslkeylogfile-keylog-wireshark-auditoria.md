---
id: software.seguranca.tranche14.001339
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

# Depuração Controlada de Tráfego TLS 1.3 com **`KeyLogFile` (`SSLKEYLOGFILE`)** e **Session Exporters (`RFC 5705` / `RFC 8446`)** no Rustls

## Em uma frase
Como o TLS 1.3 usa **Perfect Forward Secrecy (ECDHE / ML-KEM)** em 100% das conexões, possuir a chave privada do certificado do servidor **não serve mais para descriptografar um arquivo `.pcap`** capturado no Wireshark/Arkime! Então, como um engenheiro de segurança ou desenvolvedor depura um problema de protocolo dentro de um túnel TLS do Rustls em ambiente de laboratório ou extrai segredos de canal (**Channel Binding `RFC 5705` / `RFC 9266` `tls-exporter`**)?

## Por que importa
Para depuração controlada em laboratório, o Rustls oferece a struct **`rustls::KeyLogFile`** (implementação da trait `KeyLog`): quando explicitamente habilitada no `ClientConfig` ou `ServerConfig` (`config.key_log = Arc::new(KeyLogFile::new())`), ela verifica se a variável de ambiente **`SSLKEYLOGFILE`** está definida e grava ali os segredos efêmeros da sessão (`CLIENT_HANDSHAKE_TRAFFIC_SECRET`, `CLIENT_traffic_secret_0`) no formato NSS Key Log que o **Wireshark** e o **`tshark`** leem instantaneamente!

## Como funciona
E para protocolos que exigem **Channel Binding criptográfico** (como `SCRAM-SHA-256-PLUS` no PostgreSQL ou autenticação de token vinculada ao canal TLS para impedir *Token Replay*), o Rustls implementa **`connection.export_keying_material(...)` (`RFC 5705` / `RFC 8446 Section 7.5`)**!

## Exemplo
```bash
# Em ambiente de laboratorio local, passar SSLKEYLOGFILE para uma aplicacao com KeyLogFile habilitado e descriptografar o PCAP no tshark
export SSLKEYLOGFILE="./tls_debug_keys.log"
tshark -r ./captura_lab.pcap -o "tls.keylog_file:./tls_debug_keys.log" -Y "http"
```

## Limites e trade-offs
Por segurança padrão (**Secure by Default**), o `ClientConfig` e o `ServerConfig` do Rustls vêm com **`NoKeyLog`** configurado de fábrica — o que significa que, diferentemente de outras bibliotecas onde basta um malware definir `SSLKEYLOGFILE` no ambiente do usuário para vazar todas as chaves TLS, **uma aplicação Rustls de produção ignora `SSLKEYLOGFILE` a menos que o desenvolvedor tenha optado explicitamente por injetar `KeyLogFile::new()`**!

## Como verificar
Mesmo quando habilitar `KeyLogFile` para diagnóstico, proteja essa opção atrás de uma flag de compilação de debug (`#[cfg(debug_assertions)]`) ou flag explícita de CLI.

## Conexões
- [[rustls-otimizacao-performance-vectored-io-fragment-size-tokio-rustls]] — Veja também: Performance de Alta Vazão no Rustls: **Vectored I/O (`write_vectored`)**, **`max_fragment_size`**, Zero-Copy Unbuffering e Integração **`tokio-rustls`**.
- [[rustls-integracao-c-ffi-rustls-ffi-curl-apache-mod-tls-migracao]] — Veja também: Levando Segurança de Memória para Aplicações em C/C++ com **`rustls-ffi` (`crustls`)**: Integrando o Rustls no **`curl`**, **Apache `mod_tls`** e Daemons Legados.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
