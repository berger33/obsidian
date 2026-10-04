---
id: software.seguranca.tranche14.001340
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

# Levando Segurança de Memória para Aplicações em C/C++ com **`rustls-ffi` (`crustls`)**: Integrando o Rustls no **`curl`**, **Apache `mod_tls`** e Daemons Legados

## Em uma frase
E se a sua organização mantém sistemas críticos escritos em **C ou C++** (ou utiliza ferramentas universais como **`curl`** e **Apache HTTP Server**) e quer substituir o parser TLS em C por uma implementação **Memory-Safe em Rust** sem precisar reescrever o sistema inteiro em Rust?

## Por que importa
A equipe oficial do Rustls mantém o projeto **`rustls-ffi` (`libcrustls` / pacote `librustls-dev`)**, uma biblioteca de bindings C estável e limpa (`#include <rustls.h>`) que expõe as estruturas seguras do Rustls (`rustls_client_config`, `rustls_server_config`, `rustls_connection`) para qualquer programa em C ou C++!

## Como funciona
Hoje, projetos de infraestrutura mundial já possuem backends oficiais baseados em `rustls-ffi`: **(1) O `curl` (`libcurl` compilado com `--with-rustls`)**, permitindo fazer requisições HTTPS em C com a segurança de memória do Rustls; e **(2) O módulo `mod_tls` do Apache HTTP Server** (desenvolvido em parceria com a ISRG / Let's Encrypt como alternativa moderna e *memory-safe* ao clássico `mod_ssl`)!

## Exemplo
```bash
# Verificar no terminal quais backends TLS (OpenSSL, Rustls, GnuTLS) estao compilados e ativos na sua instalacao do curl
curl --version | head -n 3
```

## Limites e trade-offs
Por que a API do **`rustls-ffi`** foi desenhada como uma API C nova e segura (onde toda função retorna códigos explícitos `rustls_result` e gerencia propriedade de ponteiros de forma estrita) em vez de tentar imitar a antiga API `SSL_*` do OpenSSL? Porque a própria API histórica em C do OpenSSL contém armadilhas de gerenciamento de memória e ponteiros compartilhados que impediriam garantir *Memory Safety* na fronteira FFI!

## Como verificar
Ao construir novas aplicações nativas na nuvem, proxies de borda, agentes de segurança ou CLIs, prefira diretamente o ecossistema **Rust + `rustls` + `rustls-aws-lc-rs`** para obter simultaneamente **Memory Safety**, **TLS 1.3**, **Pós-Quântico (`X25519MLKEM768`)** e **FIPS 140-3**.

## Conexões
- [[rustls-depuracao-segura-sslkeylogfile-keylog-wireshark-auditoria]] — Veja também: Depuração Controlada de Tráfego TLS 1.3 com **`KeyLogFile` (`SSLKEYLOGFILE`)** e **Session Exporters (`RFC 5705` / `RFC 8446`)** no Rustls.
- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Referência cruzada direta com rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring.
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Referência cruzada direta com rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [Rustls Official GitHub Repository (`rustls/rustls`)](https://raw.githubusercontent.com/rustls/rustls/main/README.md) — repositório oficial da biblioteca TLS memory-safe Rustls cobrindo `CryptoProvider` (`aws-lc-rs` e `ring`), pós-quântico, FIPS e integração `tokio-rustls`; consultado em 2026-10-03.
- [Rustls Official Manual — Features and Non-Features (`features.rs`)](https://raw.githubusercontent.com/rustls/rustls/main/rustls/src/manual/features.rs) — especificação oficial de recursos e *non-features* deliberadas do Rustls cobrindo TLS 1.2/1.3, cifras AEAD, `X25519MLKEM768`, `WebPkiServerVerifier`/`WebPkiClientVerifier` e Encrypted Client Hello (`RFC 9849`); consultado em 2026-10-03.
