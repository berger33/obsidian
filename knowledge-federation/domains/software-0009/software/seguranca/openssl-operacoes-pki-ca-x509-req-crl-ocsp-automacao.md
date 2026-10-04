---
id: software.seguranca.tranche13.001294
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

# Operações de **PKI e Certificados X.509** no OpenSSL 3.x: Gerando **CSRs e Certificados com `SAN` (`-addext subjectAltName`)** em Uma Única Linha!

## Em uma frase
Quem trabalhava com versões antigas do OpenSSL lembra como era trabalhoso gerar uma **CSR (*Certificate Signing Request*)** ou um certificado X.509 contendo a extensão obrigatória **Subject Alternative Name (`SAN` — `subjectAltName`)**: era preciso criar um arquivo `.cnf` temporário separado no disco apenas para passar `v3_req`!

## Por que importa
No **OpenSSL 3.x (`openssl req` e `openssl x509`)**, isso foi completamente modernizado com a flag **`-addext`** e com as flags diretas **`-copy_extensions copyall`**! Com um único comando de linha sem nenhum arquivo auxiliar temporário, você gera a chave privada, define o `Subject` (`-subj`) e injeta todas as extensões X.509 v3 críticas: **`-addext "subjectAltName=DNS:api.exemplo.br,DNS:*.api.exemplo.br,IP:10.1.2.3"`**, **`-addext "keyUsage=critical,digitalSignature,keyEncipherment"`** e **`-addext "extendedKeyUsage=serverAuth,clientAuth"`**!

## Como funciona
Por que a extensão **`subjectAltName` (`SAN`)** é 100% obrigatória hoje? Porque desde a **RFC 2818 / CAB Forum Baseline Requirements**, todos os navegadores modernos (Chrome, Firefox, Safari) e bibliotecas TLS/HTTPS **ignoram completamente o campo legado `Common Name (CN)`** para validação de hostname e exigem que todos os FQDNs e IPs constem dentro de **`X509v3 Subject Alternative Name`**!

## Exemplo
```bash
# Gerar uma chave ECDSA P-256 e um Certificado X.509 / CSR com extensoes Subject Alternative Name (SAN) completas em um unico comando
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-256 -nodes \
  -days 365 -sha256 \
  -subj "/C=BR/O=Seguranca/CN=api.interna.exemplo.br" \
  -addext "subjectAltName=DNS:api.interna.exemplo.br,IP:10.10.20.30" \
  -addext "keyUsage=critical,digitalSignature" \
  -addext "extendedKeyUsage=serverAuth,clientAuth" \
  -keyout ./api.key -out ./api.crt
openssl x509 -in ./api.crt -noout -subject -issuer -dates -ext subjectAltName
```

## Limites e trade-offs
O comando de verificação na última linha do exemplo (**`openssl x509 -in api.crt -noout -subject -issuer -dates -ext subjectAltName`**) deve fazer parte do seu checklist diário de SRE e Segurança: ele mostra em 4 linhas limpas o titular, o emissor, as datas de início/expiração (`notBefore` / `notAfter`) e exatamente quais domínios/IPs estão autorizados no `SAN`!

## Como verificar
Para verificar criptograficamente se um certificado folha (`api.crt`) foi assinado por uma cadeia de Autoridade Certificadora (`ca-chain.pem`), use **`openssl verify -CAfile ca-chain.pem api.crt`**!

## Conexões
- [[openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8]] — Veja também: Geração Moderna de Chaves Assimétricas com **`openssl genpkey`**: Preferindo **`Ed25519` / `X25519` / `ECDSA P-384`** e Proteção **PKCS#8 (`-aes-256-cbc`)**.
- [[openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp]] — Veja também: Diagnóstico Profundo de **TLS 1.3 / 1.2 e mTLS** com **`openssl s_client`**: Inspecionando Cadeia de Certificados, **SNI**, **ALPN**, **OCSP Stapling** e Cipher Suites.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Referência cruzada direta com strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
