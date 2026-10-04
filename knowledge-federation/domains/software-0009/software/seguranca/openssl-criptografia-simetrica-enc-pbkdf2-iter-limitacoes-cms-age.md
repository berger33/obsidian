---
id: software.seguranca.tranche13.001297
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

# Criptografia de Arquivos com **`openssl enc`** vs. **`openssl cms`**: A Importância Obrigatória de **`-pbkdf2 -iter 600000`** e Limites de Cifras Sem MAC

## Em uma frase
Muitos scripts de backup e tutoriais antigos na internet usam o comando `openssl enc -aes-256-cbc -in backup.tar -out backup.tar.enc` sem parâmetros adicionais. Como engenheiro de segurança, você precisa conhecer **duas armadilhas críticas** do `openssl enc` e como usá-lo (ou substituí-lo!) corretamente!

## Por que importa
Primeira armadilha: **Derivação de Senha**. Sem flags adicionais, versões antigas do `openssl enc` usavam uma derivação fraca de 1 única iteração; no OpenSSL moderno, ao usar senha no `openssl enc`, você **DEVE SEMPRE passar explicitamente `-pbkdf2 -iter 600000`** (recomendação OWASP para PBKDF2-HMAC-SHA256)!

## Como funciona
Segunda armadilha (ainda mais importante!): **Falta de Autenticação de Integridade (AEAD)**. O comando `openssl enc` suporta modos de cifra de fluxo/bloco como `-aes-256-cbc` ou `-chacha20`, mas **não anexa tag de autenticação AEAD (`AES-GCM` não é suportado no `openssl enc` CLI por design!)**. Isso significa que um arquivo cifrado apenas com `openssl enc -aes-256-cbc` sem um HMAC externo (ou sem usar **`openssl cms -encrypt -aes-256-gcm`**!) não detecta se um atacante alterou bits do *ciphertext*!

## Exemplo
```bash
# Cifrar um arquivo com openssl enc usando PBKDF2 com 600.000 iteracoes + gerar HMAC-SHA256 (Encrypt-then-MAC), ou usar 'openssl cms' com AES-256-GCM
openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -in ./segredo.txt -out ./segredo.txt.enc -pass pass:SenhaForteExemplo2026
```

## Limites e trade-offs
E qual é a alternativa nativa dentro do próprio OpenSSL que suporta **Criptografia Autenticada (`AES-256-GCM`)** e criptografia híbrida com certificados X.509 (`RSA-OAEP` / `ECDH`)? O subcomando **`openssl cms`** (*Cryptographic Message Syntax*, `RFC 5652` / `RFC 5083` `AuthEnvelopedData`): **`openssl cms -encrypt -aes-256-gcm -in segredo.txt -out segredo.cms -recip cert_destinatario.crt`**!

## Como verificar
Com o `openssl cms -encrypt -aes-256-gcm`, qualquer pessoa que possui apenas o certificado público `cert_destinatario.crt` pode cifrar o arquivo com integridade `AES-GCM` garantida, e apenas o detentor da chave privada (ex.: guardada no cofre ou HSM) consegue descriptografar (`openssl cms -decrypt`)!

## Conexões
- [[openssl-hashes-hmac-kdf-dgst-mac-kdf-hkdf-pbkdf2-scrypt-argon2]] — Veja também: Integridade Criptográfica, **HMAC** e Derivação de Chaves (**KDF**) no OpenSSL 3.x: **`openssl dgst`**, **`openssl mac`** e **`openssl kdf` (`HKDF`, `PBKDF2`, `Scrypt`, `Argon2id`)**.
- [[openssl-formatos-certificados-chaves-pem-der-pkcs12-conversao-segura]] — Veja também: Conversão Segura entre Formatos de Certificados e Chaves (**`PEM`, `DER`, `PKCS#12 / .pfx`, `PKCS#7`**) no OpenSSL 3.x: Criptografia Forte no **`openssl pkcs12`**.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
