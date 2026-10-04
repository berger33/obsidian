---
id: software.seguranca.tranche14.001337
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

# Retomada de Sessão (**Session Resumption**), Rotação de **Session Tickets** e Riscos de **Replay em Dados `0-RTT` (`EarlyData`)** no Rustls

## Em uma frase
Para reduzir a latência de reconexão de clientes recorrentes, o TLS 1.3 oferece **Retomada de Sessão via PSK / Tickets (`1-RTT Resumption`)** e envio imediato de dados no primeiro pacote (**`0-RTT Early Data`**). Quais são os cuidados de segurança que o **Rustls** aplica na retomada de sessão e por que você deve ter extremo cuidado antes de habilitar `0-RTT` (`enable_early_data`)?

## Por que importa
Primeiro, na retomada normal **`1-RTT`**: o `ServerConfig` do Rustls inclui por padrão um gerenciador de tickets em memória (**`Ticketer`**) que cifra os tickets de sessão com uma chave simétrica efêmera gerada na RAM e **rotaciona essa chave automaticamente a cada poucas horas** — garantindo que os tickets nunca fiquem gravados em disco e preservando o *Forward Secrecy* mesmo para sessões retomadas!

## Como funciona
Segundo, o perigo do **`0-RTT Early Data`**: dados enviados pelo cliente no `0-RTT` (junto com o primeiro pacote `ClientHello`, antes do servidor responder com um `ServerHello` fresco!) **NÃO possuem proteção contra Replay Attacks no nível do protocolo TLS**! Se um invasor na rede capturar o pacote TCP do `0-RTT` e reenviá-lo 10 vezes para o servidor, uma requisição não-idempotente (como `POST /api/transferir-dinheiro`) seria executada 10 vezes!

## Exemplo
```rust
// Por padrao, o Rustls mantem enable_early_data = false; verifique sempre essa propriedade ao auditar configuracoes de alta seguranca
fn auditar_config_segura(server_config: &rustls::ServerConfig) {
    assert!(
        !server_config.max_early_data_size.gt(&0),
        "0-RTT Early Data deve permanecer desabilitado para APIs mutaveis (risco de Replay Attack)!"
    );
}
```

## Limites e trade-offs
Por esse motivo de segurança, o **Rustls mantém `0-RTT` (`enable_early_data` / `max_early_data_size`) DESABILITADO por padrão** tanto no `ClientConfig` quanto no `ServerConfig`!

## Como verificar
Se você habilitar `0-RTT` em um proxy de borda para acelerar o carregamento inicial, aceite em `EarlyData` **exclusivamente requisições HTTP `GET` / `HEAD` estritamente idempotentes** e rejeite qualquer requisição com efeitos colaterais com o código HTTP **`425 Too Early` (`RFC 8470`)** forçando o cliente a reenviar após concluir o handshake `1-RTT` completo!

## Conexões
- [[rustls-privacidade-encrypted-client-hello-ech-rfc9849-sni-alpn]] — Veja também: Privacidade no Handshake TLS 1.3 com **Encrypted Client Hello (`ECH` — `RFC 9849`)**, Compressão de Certificados (**`RFC 8879`**) e **Raw Public Keys (`RFC 7250`)** no Rustls.
- [[rustls-otimizacao-performance-vectored-io-fragment-size-tokio-rustls]] — Veja também: Performance de Alta Vazão no Rustls: **Vectored I/O (`write_vectored`)**, **`max_fragment_size`**, Zero-Copy Unbuffering e Integração **`tokio-rustls`**.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[rustls-decisoes-seguranca-non-features-tls12-tls13-pfs-aead-obrigatorio]] — Referência cruzada direta com rustls-decisoes-seguranca-non-features-tls12-tls13-pfs-aead-obrigatorio.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
