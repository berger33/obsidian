---
id: software.seguranca.tranche14.001338
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

# Performance de Alta Vazão no Rustls: **Vectored I/O (`write_vectored`)**, **`max_fragment_size`**, Zero-Copy Unbuffering e Integração **`tokio-rustls`**

## Em uma frase
Como o **Rustls** atinge vazão multi-gigabit e latência de handshake inferior a bibliotecas legadas em C quando integrado a servidores assíncronos em Rust (**`tokio-rustls`**, **`hyper`**, **`tonic`**, **`quinn` QUIC**)?

## Por que importa
Através de quatro otimizações arquiteturais na camada de I/O do Rustls: **(1) Vectored I/O (`writev` syscall via `write_vectored`)** — em vez de copiar múltiplos registros TLS para um único buffer intermediário na memória antes de chamar o kernel, o Rustls entrega fatias de memória diretamente para a chamada de sistema `writev(2)`, minimizando cópias de memória e transições usuário-kernel!;

## Como funciona
Na camada complementar de implementação e execução técnica: **(2) Ajuste de Tamanho de Fragmento (`max_fragment_size`)** — permite alinhar o tamanho dos registros TLS com o MTU da interface de rede subjacente para evitar que um registro TLS de 16 KB fique bloqueado esperando o último pacote TCP chegar (*Head-of-Line Blocking* de registro!); **(3) API `UnbufferedConnection`** para motores de alto desempenho (`io_uring`); e **(4) Integração com Kernel TLS (`ktls`)**!

## Exemplo
```rust
// Exemplo de aceite de conexao assincrona TLS 1.3 com tokio-rustls aplicando timeout rigoroso no handshake contra Slowloris TLS
use std::sync::Arc;
use std::time::Duration;
use tokio::net::TcpStream;
use tokio::time::timeout;
use tokio_rustls::TlsAcceptor;

async fn aceitar_conexao_segura(
    acceptor: &TlsAcceptor,
    tcp_stream: TcpStream,
) -> std::io::Result<tokio_rustls::server::TlsStream<TcpStream>> {
    timeout(Duration::from_secs(5), acceptor.accept(tcp_stream))
        .await
        .map_err(|_| std::io::Error::new(std::io::ErrorKind::TimedOut, "Handshake TLS expirou"))?
}
```

## Limites e trade-offs
Regra obrigatória de engenharia defensiva mostrada no código acima: **SEMPRE envolva `acceptor.accept(tcp_stream)` em um `tokio::time::timeout` curto (ex.: `5` segundos)**! Por quê? Porque sem um timeout no handshake TLS, um atacante pode abrir milhares de conexões TCP e nunca enviar o `ClientHello` (ataque de exaustão de sockets *TLS Slowloris*), prendendo tasks assíncronas indefinidamente!

## Como verificar
Reutilize sempre a mesma instância `Arc<ServerConfig>` e `Arc<ClientConfig>` entre todas as conexões do processo (nunca reconstrua `ServerConfig` ou `RootCertStore` a cada requisição, pois é dentro do `Arc<ServerConfig>` que reside o cache de retomada de sessões TLS!).

## Conexões
- [[rustls-retomada-sessao-tickets-0rtt-anti-replay-seguranca]] — Veja também: Retomada de Sessão (**Session Resumption**), Rotação de **Session Tickets** e Riscos de **Replay em Dados `0-RTT` (`EarlyData`)** no Rustls.
- [[rustls-depuracao-segura-sslkeylogfile-keylog-wireshark-auditoria]] — Veja também: Depuração Controlada de Tráfego TLS 1.3 com **`KeyLogFile` (`SSLKEYLOGFILE`)** e **Session Exporters (`RFC 5705` / `RFC 8446`)** no Rustls.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[openssl-benchmarking-criptografico-speed-evp-aes-ni-avx512-pqc-ml-kem]] — Referência cruzada direta com openssl-benchmarking-criptografico-speed-evp-aes-ni-avx512-pqc-ml-kem.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
