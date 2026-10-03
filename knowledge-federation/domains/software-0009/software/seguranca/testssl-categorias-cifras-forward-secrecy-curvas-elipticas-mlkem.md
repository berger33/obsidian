---
id: software.seguranca.tranche07.000603
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

# `testssl.sh`: Auditoria de Categorias de Cifras (`-s` / `-E`), **Forward Secrecy** (`-f`), Curvas Elípticas e Híbridas Pós-Quânticas (**ML-KEM**)

## Em uma frase
As opções **`-s` (`--std`)**, **`-E` (`--each-cipher`)** e **`-f` (`--fs`)** avaliam a força das suítes de cifra oferecidas pelo servidor, a ordem de preferência do servidor e os parâmetros de **Perfect Forward Secrecy (PFS)** (grupos Diffie-Hellman `FFDHE`, curvas elípticas `X25519`, `secp256r1`/`P-256`, `secp384r1`/`P-384` e grupos híbridos pós-quânticos **ML-KEM** como `X25519MLKEM768` e `SecP256r1MLKEM512`).

## Por que importa
Se um servidor TLS 1.2 permitir suítes de troca de chaves **RSA estático** (`TLS_RSA_WITH_AES_...`, sem `ECDHE` ou `DHE`), qualquer adversário que capture o tráfego cifrado hoje e consiga comprometer a chave privada do servidor no futuro decifrará retroativamente todas as sessões passadas.

## Como funciona
O teste `-s` agrupa as cifras em categorias de risco (*NULL*, *Anonymous*, *EXPORT*, *LOW/DES/3DES/RC4*, *CBC*, *AEAD GCM/ChaCha20-Poly1305*), enquanto `-f` verifica se o servidor prioriza `ECDHE` e quais grupos de troca de chaves (incluindo grupos pós-quânticos NIST FIPS 203 ML-KEM no TLS 1.3) são suportados.

## Exemplo
```bash
# Auditar categorias de cifras (-s) e suporte a Forward Secrecy / curvas elipticas / ML-KEM (-f)
testssl.sh -s -f --wide https://api.internal.corp:443
```

## Limites e trade-offs
No TLS 1.2, além de exigir `ECDHE`, desative todas as suítes em modo **CBC** (vulneráveis a variantes de oráculo de padding *Lucky13* / *GOLDENDOODLE* / *Zombie POODLE*), mantendo apenas cifras **AEAD** (`ECDHE-ECDSA-AES128-GCM-SHA256`, `ECDHE-RSA-AES128-GCM-SHA256`, `AES256-GCM-SHA384` e `CHACHA20-POLY1305`).

## Como verificar
Confirme na seção `Forward Secrecy` que o servidor oferece apenas cifras AEAD com `ECDHE` e suporta a curva `X25519` e `secp256r1`.

## Conexões
- [[testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn]] — Veja também: `testssl.sh`: Verificação de Versões de Protocolo (`-p` — SSLv2/SSLv3/TLS 1.0/1.1/1.2/1.3, QUIC/HTTP3 e ALPN).
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Veja também: `testssl.sh`: Auditoria de Certificados X.509 (`-S`), Cadeia de Confiança, **OCSP Stapling**, *Certificate Transparency* e Registros **DNS CAA**.
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.
- [[testssl-vulnerabilidades-criptograficas-heartbleed-robot-drown-poodle-logjam]] — Referência cruzada direta com testssl-vulnerabilidades-criptograficas-heartbleed-robot-drown-poodle-logjam.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
