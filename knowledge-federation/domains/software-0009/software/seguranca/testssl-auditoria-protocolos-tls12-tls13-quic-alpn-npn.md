---
id: software.seguranca.tranche07.000602
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://testssl.sh/doc/testssl.1.md", "https://github.com/drwetter/testssl.sh", "https://github.com/testssl/testssl.sh"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `testssl.sh`: Verificação de Versões de Protocolo (`-p` — SSLv2/SSLv3/TLS 1.0/1.1/1.2/1.3, QUIC/HTTP3 e ALPN)

## Em uma frase
A opção **`-p` (`--protocols`)** do `testssl.sh` testa individualmente se o servidor alvo aceita negociações nos protocolos **SSLv2**, **SSLv3**, **TLS 1.0**, **TLS 1.1**, **TLS 1.2**, **TLS 1.3** e **QUIC (HTTP/3)**, além de enumerar os protocolos de camada de aplicação anunciados via **ALPN** (*Application-Layer Protocol Negotiation*, ex.: `h2`, `http/1.1`, `h3`).

## Por que importa
Conformidades modernas (PCI-DSS v4.0, NIST SP 800-52r2, RFC 8996) exigem a desativação completa de SSLv2, SSLv3, TLS 1.0 e TLS 1.1, permitindo exclusivamente **TLS 1.2** (com cifras AEAD e PFS) e **TLS 1.3** (RFC 8446).

## Como funciona
Quando executado apenas com `-p`, o `testssl.sh` completa a auditoria de versões de protocolo e ALPN em poucos segundos sem precisar testar individualmente cada uma das 370 suítes de cifra.

## Exemplo
```bash
# Auditar exclusivamente as versoes de protocolo TLS/QUIC e negociacao ALPN em um gateway de API
testssl.sh -p --connect-timeout 5 --openssl-timeout 5 https://api.internal.corp:8443
```

## Limites e trade-offs
Sempre configure **`--connect-timeout 5`** e **`--openssl-timeout 5`** ao auditar servidores protegidos por firewalls corporativos ou *tarpits* que descartam pacotes (`DROP` silencioso) em vez de responder com `TCP RST`, evitando que o scan fique travado por 2 minutos por conexão.

## Como verificar
Verifique na saída de `testssl.sh -p` que `SSLv2`, `SSLv3`, `TLS 1` e `TLS 1.1` estão marcados como `not offered (OK)` e que `TLS 1.3` está ativo.

## Conexões
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Veja também: `testssl.sh`: Arquitetura de Auditoria de Servidores TLS/SSL via Sockets TCP Nativo e Binários OpenSSL Estáticos.
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Veja também: `testssl.sh`: Auditoria de Categorias de Cifras (`-s` / `-E`), **Forward Secrecy** (`-f`), Curvas Elípticas e Híbridas Pós-Quânticas (**ML-KEM**).
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
