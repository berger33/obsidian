---
id: software.seguranca.tranche13.001299
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/openssl/openssl/master/README.md", "https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Hardening Sistêmico via **`/etc/ssl/openssl.cnf`**: Impondo **`MinProtocol = TLSv1.2`** e **`CipherString = DEFAULT@SECLEVEL=2`** para Todas as Aplicações do Servidor!

## Em uma frase
Imagine um servidor Linux onde rodam 15 aplicações diferentes (scripts Python `requests`/`urllib3`, serviços C++, agentes Ruby, clientes PostgreSQL, Postfix, curl). Em vez de depender de que cada desenvolvedor lembre de desabilitar o TLS 1.0/1.1 e cifras fracas no código de cada aplicação individual, como impor **uma política criptográfica mínima obrigatória no nível da própria biblioteca `libssl`** para todo o sistema operacional?

## Por que importa
Através da seção **`[system_default_sect]` (`ssl_conf`)** no arquivo global **`/etc/ssl/openssl.cnf`**, no OpenSSL 3.x você define duas diretivas que blindam instantaneamente todas as conexões TLS de cliente e servidor que usam a configuração padrão da `libssl`: **(1) `MinProtocol = TLSv1.2`** (ou `TLSv1.3` em ambientes internos modernos — bloqueando na raiz qualquer tentativa de negociar SSLv3, TLS 1.0 ou TLS 1.1!); e **(2) `CipherString = DEFAULT@SECLEVEL=2`** (ou `@SECLEVEL=3`)!

## Como funciona
O que significam os **Security Levels (`@SECLEVEL=0` a `5`)** do OpenSSL? **`@SECLEVEL=2`** exige no mínimo **112 bits de segurança equivalente** (bloqueando chaves RSA/DH menores que **2.048 bits**, curvas ECC menores que **224 bits** e qualquer assinatura `SHA-1` ou `MD5`!), enquanto **`@SECLEVEL=3`** eleva a exigência para **128 bits de segurança** (exigindo chaves RSA/DH de no mínimo **3.072 bits**, curvas ECC >= **256 bits** e **Perfect Forward Secrecy obrigatório** — proibindo RSA Key Transport estático!)!

## Exemplo
```bash
# Auditar quais Cipher Suites permanecem permitidas no OpenSSL 3.x sob o nivel de seguranca estrito @SECLEVEL=3 (128-bit security + PFS obrigatorio)
openssl ciphers -v 'DEFAULT@SECLEVEL=3' | head -n 20
```

## Limites e trade-offs
Ao investigar por que uma aplicação moderna no Ubuntu 22.04/24.04, Debian 12 ou RHEL 9 se recusa a conectar em um equipamento legado antigo que ainda usa um certificado RSA de 1.024 bits ou assinado com SHA-1 (`sslv3 alert handshake failure` / `ca md too weak`), lembre-se de que a causa é justamente a proteção **`@SECLEVEL=2`** ativa no `/etc/ssl/openssl.cnf`!

## Como verificar
Jamais reduza o `@SECLEVEL` global do `/etc/ssl/openssl.cnf` para `1` ou `0` em produção apenas por causa de um único sistema legado: em vez disso, atualize o certificado do sistema legado para **ECDSA P-256 / P-384** ou **RSA-3072 com SHA-256**!

## Conexões
- [[openssl-formatos-certificados-chaves-pem-der-pkcs12-conversao-segura]] — Veja também: Conversão Segura entre Formatos de Certificados e Chaves (**`PEM`, `DER`, `PKCS#12 / .pfx`, `PKCS#7`**) no OpenSSL 3.x: Criptografia Forte no **`openssl pkcs12`**.
- [[openssl-benchmarking-criptografico-speed-evp-aes-ni-avx512-pqc-ml-kem]] — Veja também: Benchmarking Criptográfico e Aceleração de Hardware com **`openssl speed -evp`**: Medindo **AES-NI / VAES**, **ChaCha20-Poly1305**, **Ed25519** e **ML-KEM / ML-DSA**.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp]] — Referência cruzada direta com openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
