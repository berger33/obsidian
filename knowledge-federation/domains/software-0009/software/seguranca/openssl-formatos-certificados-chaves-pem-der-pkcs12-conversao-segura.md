---
id: software.seguranca.tranche13.001298
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

# Conversão Segura entre Formatos de Certificados e Chaves (**`PEM`, `DER`, `PKCS#12 / .pfx`, `PKCS#7`**) no OpenSSL 3.x: Criptografia Forte no **`openssl pkcs12`**

## Em uma frase
Na vida real de operações de segurança e infraestrutura, diferentes plataformas exigem formatos diferentes para o mesmo certificado e chave privada: servidores Linux (**Nginx, Apache, strongSwan, Envoy, Kubernetes Secrets**) usam arquivos texto Base64 **PEM (`.pem`, `.crt`, `.key`)**; aplicações Java/Android e Windows às vezes usam binário **DER (`.der`, `.cer`)**; e servidores Windows IIS, Balanceadores F5/Citrix, clientes VPN móveis e navegadores exigem um único arquivo empacotado **PKCS#12 (`.p12` / `.pfx`)**!

## Por que importa
Como converter entre esses formatos com segurança máxima no **OpenSSL 3.x**?

## Como funciona
No **OpenSSL 3.x**, o subcomando **`openssl pkcs12 -export`** deu um salto enorme de segurança: enquanto o OpenSSL 1.1.1 antigo cifrava arquivos `.p12`/`.pfx` por padrão usando algoritmos legados (`3DES` e `SHA1` com 2.048 iterações!), **o OpenSSL 3.x usa por padrão `PBKDF2` com `AES-256-CBC` e `HMAC-SHA256`!** (E se você precisar gerar um `.pfx` para importar em um sistema legado antigo que ainda não entende PBKDF2/AES-256 no PKCS#12, o OpenSSL 3.x exige que você passe explicitamente a flag `-legacy`!).

## Exemplo
```bash
# Empacotar certificado + chave privada + cadeia de CA em um container PKCS#12 (.p12/.pfx) protegido com AES-256-CBC e PBKDF2 no OpenSSL 3.x
openssl pkcs12 -export \
  -in ./api.crt \
  -inkey ./api.key \
  -out ./api_bundle.p12 \
  -name "certificado-api-prod" \
  -passout pass:SenhaDeTransporteForte2026

# Inspecionar os algoritmos criptograficos (PBES2, PBKDF2, AES-256-CBC, SHA256) aplicados ao arquivo PKCS#12 gerado
openssl pkcs12 -info -in ./api_bundle.p12 -noout -passin pass:SenhaDeTransporteForte2026
```

## Limites e trade-offs
Olhe o comando de auditoria **`openssl pkcs12 -info -in api_bundle.p12 -noout`** acima: ele mostra exatamente o `MAC: sha256, Iteration 2048` e o `PKCS7 Encrypted data: PBES2, PBKDF2, AES-256-CBC` sem extrair nem imprimir a chave privada na tela!

## Como verificar
Para converter um certificado de **PEM para DER** (binário ASN.1 bruto), basta rodar **`openssl x509 -in api.crt -outform der -out api.der`** (e o inverso com `-inform der -outform pem`).

## Conexões
- [[openssl-criptografia-simetrica-enc-pbkdf2-iter-limitacoes-cms-age]] — Veja também: Criptografia de Arquivos com **`openssl enc`** vs. **`openssl cms`**: A Importância Obrigatória de **`-pbkdf2 -iter 600000`** e Limites de Cifras Sem MAC.
- [[openssl-politicas-seguranca-openssl-cnf-cipherstring-seclevel-minprotocol]] — Veja também: Hardening Sistêmico via **`/etc/ssl/openssl.cnf`**: Impondo **`MinProtocol = TLSv1.2`** e **`CipherString = DEFAULT@SECLEVEL=2`** para Todas as Aplicações do Servidor!.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Referência cruzada direta com openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao.
- [[strongswan-roadwarrior-virtual-ip-pools-eap-tls-eap-mschapv2]] — Referência cruzada direta com strongswan-roadwarrior-virtual-ip-pools-eap-tls-eap-mschapv2.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
