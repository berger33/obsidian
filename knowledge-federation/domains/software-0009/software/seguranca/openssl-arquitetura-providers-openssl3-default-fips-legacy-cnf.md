---
id: software.seguranca.tranche13.001291
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

# Arquitetura do **OpenSSL 3.x (`openssl/openssl`)**: `libssl`, `libcrypto` e o Novo Modelo de **Providers (`default`, `fips`, `legacy`, `base`, `null`)**

## Em uma frase
O **OpenSSL (`openssl/openssl`)** é o alicerce criptográfico da Internet moderna: suas duas bibliotecas centrais — **`libssl`** (implementação de **TLS 1.3 `RFC 8446`**, **TLS 1.2**, **DTLS 1.2** e **QUIC v1 `RFC 9000`**) e **`libcrypto`** (algoritmos simétricos, assimétricos, hashes, KDFs e infraestrutura X.509/PKI) — sustentam desde servidores Nginx, Apache, Postfix, OpenSSH e strongSwan até runtimes Python, Node.js, PostgreSQL e o próprio Kernel/usuário Linux!

## Por que importa
Na série **OpenSSL 3.x**, a antiga API de `ENGINE` foi depreciada e substituída por uma arquitetura modular revolucionária chamada **Providers (`OSSL_PROVIDER`)**: um *Provider* é uma unidade plugável que fornece implementações de operações criptográficas (cifragem, assinatura, digest, troca de chaves, KEM) selecionadas por *Property Query Strings* (ex.: `"fips=yes"`).

## Como funciona
O OpenSSL 3.x vem com **5 Providers nativos**: **(1) `default`** (todos os algoritmos modernos seguros padrão: AES-GCM, ChaCha20-Poly1305, SHA-2/SHA-3, RSA, ECDSA, Ed25519, X25519, Argon2, ML-KEM/ML-DSA no 3.5+); **(2) `fips`** (módulo validado **FIPS 140-3**!); **(3) `legacy`** (algoritmos obsoletos desativados por padrão: MD4, RC4, DES, Blowfish, RIPEMD160 — isolados para nunca serem usados por acidente!); **(4) `base`** (codificadores PEM/DER/ASN.1 sem criptografia, usado junto com o `fips`); e **(5) `null`**!

## Exemplo
```bash
# Verificar a versao do OpenSSL 3.x, os Providers atualmente carregados e os algoritmos fornecidos pelo provider 'default'
openssl version -a
openssl list -providers
openssl list -cipher-algorithms -provider default | head -n 20
```

## Limites e trade-offs
Por que separar algoritmos obsoletos (`MD4`, `RC4`, `DES`, `3DES`, `CAST5`) em um **`legacy` provider desabilitado por padrão** no OpenSSL 3.x foi um marco de engenharia de segurança? Porque garante que nenhuma aplicação linkada à `libcrypto` use acidentalmente uma cifra quebrada dos anos 1990, a menos que o administrador carregue explicitamente `-provider legacy -provider default`!

## Como verificar
A ativação global de providers e políticas de algoritmos para todo o sistema operacional é controlada no arquivo **`/etc/ssl/openssl.cnf`** na seção `[provider_sect]`.

## Conexões
- [[openssl-conformidade-fips-140-3-fipsmodule-cnf-fipsinstall-validacao]] — Veja também: Conformidade **FIPS 140-3** no OpenSSL 3.x: Ativando o **`fips` Provider (`fips.so`)**, Auto-Testes **`openssl fipsinstall`** e `default_properties = fips=yes`.
- [[openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8]] — Referência cruzada direta com openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8.
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Referência cruzada direta com strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
