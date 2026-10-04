---
id: software.seguranca.tranche13.001300
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

# Benchmarking Criptográfico e Aceleração de Hardware com **`openssl speed -evp`**: Medindo **AES-NI / VAES**, **ChaCha20-Poly1305**, **Ed25519** e **ML-KEM / ML-DSA**

## Em uma frase
Ao escolher quais algoritmos criptográficos configurar no seu gateway VPN (**strongSwan** / **WireGuard**), no seu Ingress Controller (**Nginx / Envoy**), no seu **OpenSSH** ou no seu banco de dados, como medir **empiricamente no seu próprio hardware de produção** quantos Gigabytes por segundo cada cifra simétrica (`AES-256-GCM` vs. `ChaCha20-Poly1305`) consegue processar e quantas milhares de assinaturas/trocas de chaves por segundo sua CPU faz com `Ed25519` vs. `ECDSA P-256` vs. `RSA-4096` vs. `ML-KEM-768`?

## Por que importa
Usando a ferramenta oficial de benchmark embutida no OpenSSL: **`openssl speed`**!

## Como funciona
Segredo técnico fundamental ao rodar benchmarks de cifras simétricas e hashes no OpenSSL: **SEMPRE passe a flag `-evp <algoritmo>`** (ex.: **`openssl speed -evp aes-256-gcm`** ou **`openssl speed -evp chacha20-poly1305`**)! Por quê? Porque é a camada **`EVP` (*Envelope*)** dos Providers do OpenSSL 3.x que aciona automaticamente as instruções de aceleração de hardware do processador (**Intel/AMD `AES-NI`, `VAES`, `PCLMULQDQ`, `AVX2`/`AVX-512` e ARMv8 Cryptography Extensions**)!

## Exemplo
```bash
# Medir por 3 segundos (-seconds 3) a vazao real em bytes/s com aceleracao de hardware (EVP) entre AES-256-GCM e ChaCha20-Poly1305 e assinaturas Ed25519
openssl speed -seconds 3 -evp aes-256-gcm
openssl speed -seconds 3 -evp chacha20-poly1305
openssl speed -seconds 3 ed25519
```

## Limites e trade-offs
Em processadores modernos x86_64 com instruções **AES-NI + VAES (AVX-512)**, você verá o `openssl speed -evp aes-256-gcm` atingir velocidades impressionantes de **5 GB/s a mais de 15 GB/s em um único núcleo de CPU** (`-multi $(nproc)` testa todos os núcleos em paralelo!) — provando que criptografia TLS 1.3 / IPsec moderna em hardware atual tem sobrecarga de CPU próxima de zero!

## Como verificar
Já na comparação de chaves assimétricas (`openssl speed rsa2048 rsa4096 ecdsap256 ed25519`), o benchmark mostra por que **`Ed25519`** e **`ECDSA P-256`** dominam a engenharia moderna: eles assinam dezenas de vezes mais rápido que o `RSA-4096` com chaves 10x menores!

## Conexões
- [[openssl-politicas-seguranca-openssl-cnf-cipherstring-seclevel-minprotocol]] — Veja também: Hardening Sistêmico via **`/etc/ssl/openssl.cnf`**: Impondo **`MinProtocol = TLSv1.2`** e **`CipherString = DEFAULT@SECLEVEL=2`** para Todas as Aplicações do Servidor!.
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Referência cruzada direta com openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf.
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Referência cruzada direta com strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
