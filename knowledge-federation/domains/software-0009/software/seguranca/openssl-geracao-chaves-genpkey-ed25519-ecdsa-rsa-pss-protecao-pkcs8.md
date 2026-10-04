---
id: software.seguranca.tranche13.001293
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

# Geração Moderna de Chaves Assimétricas com **`openssl genpkey`**: Preferindo **`Ed25519` / `X25519` / `ECDSA P-384`** e Proteção **PKCS#8 (`-aes-256-cbc`)**

## Em uma frase
Por que você deve aposentar imediatamente os comandos antigos da era OpenSSL 0.9.8/1.0 (`openssl genrsa`, `openssl ecparam -genkey`, `openssl dsaparam`) e padronizar 100% da geração de chaves privadas no subcomando unificado **`openssl genpkey`**?

## Por que importa
Os comandos legados eram específicos de algoritmo e produziam formatos antigos de envelope PEM, enquanto `genpkey` opera sobre a API unificada `EVP_PKEY`.

## Como funciona
Porque **`openssl genpkey`** é a interface moderna baseada na arquitetura `EVP_PKEY` e nos *Providers* do OpenSSL 3.x: **(1)** Ele suporta de forma uniforme todos os algoritmos modernos — curvas de Edwards **`ED25519`** e **`ED448`** (para assinatura digital), curvas de Montgomery **`X25519`** e **`X448`** (para troca de chaves Diffie-Hellman), curvas NIST **`EC` (`P-256` / `P-384` / `P-521`)**, **`RSA` / `RSA-PSS`** e até algoritmos pós-quânticos **`ML-KEM` / `ML-DSA`** (no OpenSSL 3.5+)!; e **(2)** Ele salva a chave privada diretamente no padrão moderno **PKCS#8 (`-----BEGIN ENCRYPTED PRIVATE KEY-----`)** usando derivação de chave baseada em senha **PBKDF2 com `AES-256-CBC`**!

## Exemplo
```bash
# Gerar chaves privadas modernas Ed25519, ECDSA P-384 e RSA-4096 usando o comando unificado 'openssl genpkey' e extrair a chave publica
openssl genpkey -algorithm ED25519 -out ./chave_ed25519.pem
openssl pkey -in ./chave_ed25519.pem -pubout -out ./chave_ed25519_pub.pem
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-384 -out ./chave_p384.pem
chmod 600 ./chave_ed25519.pem ./chave_p384.pem
```

## Limites e trade-offs
Sempre que gerar uma chave privada que ficará armazenada em disco para uso humano ou de Autoridade Certificadora (CA), adicione a flag **`-aes-256-cbc`** ao `openssl genpkey` para cifrar o envelope PKCS#8 com uma passphrase forte guardada no seu **KeePassXC**!

## Como verificar
Para inspecionar os parâmetros matemáticos internos e o tamanho em bits de qualquer chave privada ou pública gerada, execute **`openssl pkey -in chave.pem -text -noout`**.

## Conexões
- [[openssl-conformidade-fips-140-3-fipsmodule-cnf-fipsinstall-validacao]] — Veja também: Conformidade **FIPS 140-3** no OpenSSL 3.x: Ativando o **`fips` Provider (`fips.so`)**, Auto-Testes **`openssl fipsinstall`** e `default_properties = fips=yes`.
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Veja também: Operações de **PKI e Certificados X.509** no OpenSSL 3.x: Gerando **CSRs e Certificados com `SAN` (`-addext subjectAltName`)** em Uma Única Linha!.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
