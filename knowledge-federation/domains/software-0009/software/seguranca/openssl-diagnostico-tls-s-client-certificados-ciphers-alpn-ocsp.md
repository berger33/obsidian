---
id: software.seguranca.tranche13.001295
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

# Diagnóstico Profundo de **TLS 1.3 / 1.2 e mTLS** com **`openssl s_client`**: Inspecionando Cadeia de Certificados, **SNI**, **ALPN**, **OCSP Stapling** e Cipher Suites

## Em uma frase
Quando uma chamada HTTPS, gRPC, LDAPS, SMTPS ou banco de dados TLS falha com erro de handshake (`certificate verify failed`, `alert handshake failure`, `tlsv1 alert unknown ca`), o comando **`curl`** muitas vezes esconde os detalhes internos do protocolo TLS. Qual é o "bisturi cirúrgico" para depurar qualquer servidor TLS ou mTLS no nível de pacotes de handshake?

## Por que importa
O utilitário **`openssl s_client`** expõe de forma transparente cada mensagem negociada no handshake criptográfico, permitindo isolar falhas de cadeia X.509, SNI, ALPN ou mTLS em segundos.

## Como funciona
Com o **`openssl s_client`**, você abre uma conexão TLS direta com qualquer porta TCP (HTTPS `:443`, LDAPS `:636`, PostgreSQL/SMTP com `-starttls postgres` / `-starttls smtp`), envia o **SNI (`-servername host.exemplo.br`, habilitado por padrão no OpenSSL 3.x quando `-connect host:porta` recebe um nome DNS!)** e inspeciona em detalhes: **(1) A cadeia completa de certificados enviada pelo servidor (`-showcerts`)**; **(2) A versão exata do protocolo negociada (`-tls1_3` / `-tls1_2`) e a Cipher Suite (`TLS_AES_256_GCM_SHA384`)**; **(3) A curva de troca de chaves efêmera (`Server Temp Key: X25519, 253 bits` ou `X25519MLKEM768`)**; **(4) O protocolo de aplicação negociado via ALPN (`-alpn h2,http/1.1`)**; e **(5) A resposta de OCSP Stapling (`-status`)**!

## Exemplo
```bash
# Auditar a data de expiracao, cadeia de certificados e parametros TLS 1.3 de um endpoint HTTPS ou testar autenticacao mutua (mTLS)
echo | openssl s_client -connect localhost:443 -servername api.exemplo.br -tls1_3 -status 2>/dev/null | openssl x509 -noout -dates -subject -issuer
```

## Limites e trade-offs
Para testar **Autenticação Mútua TLS (mTLS / Zero Trust)** contra um gateway de API ou Ingress Controller, basta adicionar ao `openssl s_client` as flags do certificado e da chave privada do cliente: **`openssl s_client -connect api.interna:443 -cert cliente.crt -key cliente.key -CAfile ca-interna.pem`**!

## Como verificar
Dica prática: coloque sempre **`echo |`** (ou **`</dev/null`**) antes do `openssl s_client` em scripts automatizados para que ele encerre a conexão TCP limpa imediatamente após concluir o handshake TLS, sem ficar aguardando entrada interativa no terminal!

## Conexões
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Veja também: Operações de **PKI e Certificados X.509** no OpenSSL 3.x: Gerando **CSRs e Certificados com `SAN` (`-addext subjectAltName`)** em Uma Única Linha!.
- [[openssl-hashes-hmac-kdf-dgst-mac-kdf-hkdf-pbkdf2-scrypt-argon2]] — Veja também: Integridade Criptográfica, **HMAC** e Derivação de Chaves (**KDF**) no OpenSSL 3.x: **`openssl dgst`**, **`openssl mac`** e **`openssl kdf` (`HKDF`, `PBKDF2`, `Scrypt`, `Argon2id`)**.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
