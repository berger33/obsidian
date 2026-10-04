---
id: software.seguranca.tranche13.001296
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

# Integridade Criptográfica, **HMAC** e Derivação de Chaves (**KDF**) no OpenSSL 3.x: **`openssl dgst`**, **`openssl mac`** e **`openssl kdf` (`HKDF`, `PBKDF2`, `Scrypt`, `Argon2id`)**

## Em uma frase
No OpenSSL 3.x, além de calcular hashes criptográficos clássicos (`SHA-256`, `SHA-384`, `SHA-512`, `SHA3-256`, `BLAKE2b512`) e assinar/verificar arquivos com chaves assimétricas via **`openssl dgst`**, a linha de comando ganhou dois subcomandos dedicados muito poderosos que todo engenheiro de segurança deve conhecer: **`openssl mac`** e **`openssl kdf`**!

## Por que importa
Com **`openssl mac`**, você calcula códigos de autenticação de mensagem modernos — não apenas **`HMAC`** (`-macopt digest:SHA256`), mas também **`CMAC`** (baseado em AES), **`GMAC`**, **`Poly1305`** e **`KMAC128` / `KMAC256` (padrão SHA-3 NIST SP 800-185)**!

## Como funciona
E com **`openssl kdf`**, você deriva chaves criptográficas de alta entropia diretamente no terminal ou em scripts usando as **Key Derivation Functions (KDFs)** padronizadas: **`HKDF` (`RFC 5869`, usada no TLS 1.3 e no Noise/WireGuard!)**, **`PBKDF2`**, **`SCRYPT`** e **`ARGON2ID`** (no OpenSSL 3.2+)!

## Exemplo
```bash
# Calcular um HMAC-SHA256 com 'openssl mac' e derivar uma chave criptografica de 32 bytes (256 bits) usando HKDF-SHA256 com 'openssl kdf'
openssl mac -digest SHA256 -macopt hexkey:000102030405060708090a0b0c0d0e0f -in /etc/hostname HMAC
openssl kdf -keylen 32 -kdfopt digest:SHA256 -kdfopt key:segredo_mestre -kdfopt salt:sal_unico -kdfopt info:contexto_api HKDF
```

## Limites e trade-offs
Quando você precisa assinar digitalmente um arquivo binário de release (`release.tar.gz`) com uma chave privada ECDSA ou RSA e depois verificar essa assinatura em outro servidor usando apenas a chave pública, o comando também é o **`openssl dgst`**: **`openssl dgst -sha256 -sign privada.pem -out release.sig release.tar.gz`** e **`openssl dgst -sha256 -verify publica.pem -signature release.sig release.tar.gz`**!

## Como verificar
Nota para chaves **`Ed25519`** (*PureEdDSA*): como o algoritmo `Ed25519` já faz o hash `SHA-512` internamente sobre a mensagem inteira, use **`openssl pkeyutl -sign -inkey ed25519.pem -rawin -in arquivo -out arquivo.sig`** e **`openssl pkeyutl -verify -pubin -inkey ed25519_pub.pem -rawin -in arquivo -sigfile arquivo.sig`**!

## Conexões
- [[openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp]] — Veja também: Diagnóstico Profundo de **TLS 1.3 / 1.2 e mTLS** com **`openssl s_client`**: Inspecionando Cadeia de Certificados, **SNI**, **ALPN**, **OCSP Stapling** e Cipher Suites.
- [[openssl-criptografia-simetrica-enc-pbkdf2-iter-limitacoes-cms-age]] — Veja também: Criptografia de Arquivos com **`openssl enc`** vs. **`openssl cms`**: A Importância Obrigatória de **`-pbkdf2 -iter 600000`** e Limites de Cifras Sem MAC.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8]] — Referência cruzada direta com openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
