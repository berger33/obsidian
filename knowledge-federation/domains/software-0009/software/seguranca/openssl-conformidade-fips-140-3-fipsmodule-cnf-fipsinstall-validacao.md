---
id: software.seguranca.tranche13.001292
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

# Conformidade **FIPS 140-3** no OpenSSL 3.x: Ativando o **`fips` Provider (`fips.so`)**, Auto-Testes **`openssl fipsinstall`** e `default_properties = fips=yes`

## Em uma frase
Em ambientes governamentais, financeiros, de defesa, saúde e nuvem regulamentada (FedRAMP, PCI-DSS, BACEN), os sistemas devem operar utilizando exclusivamente módulos criptográficos validados segundo a norma **FIPS 140-3 (*Federal Information Processing Standards*)** — que exige que apenas algoritmos aprovados pelo NIST sejam permitidos e que o módulo criptográfico execute auto-testes de integridade (**KATs — *Known Answer Tests*** e verificação `HMAC-SHA256` do próprio binário `fips.so`!) antes de processar qualquer dado.

## Por que importa
No **OpenSSL 3.x**, como funciona a ativação e verificação do **FIPS Provider (`fips.so`)**?

## Como funciona
Primeiro, o utilitário **`openssl fipsinstall`** executa todos os auto-testes criptográficos sobre o módulo `fips.so`, calcula o MAC de integridade do binário e gera o arquivo **`fipsmodule.cnf`**. Segundo, no `/etc/ssl/openssl.cnf`, você inclui `.include /caminho/fipsmodule.cnf`, ativa os providers **`fips`** e **`base`** (para serialização PEM/DER) e define na seção `[algorithm_sect]` a propriedade global **`default_properties = fips=yes`**! Com `fips=yes` ativo, qualquer tentativa de uma aplicação chamar um algoritmo não aprovado pelo FIPS (como `MD5` ou `RC4`) é **bloqueada automaticamente dentro da `libcrypto`**!

## Exemplo
```bash
# Testar se uma operacao de hash aprovada (SHA-256) funciona e verificar como propriedades de provider controlam a selecao de algoritmos
openssl dgst -sha256 /etc/hostname
openssl list -digest-algorithms -propquery "fips=yes" | head -n 20
```

## Limites e trade-offs
Graças à arquitetura de *Property Queries* (`-propquery "fips=yes"` ou `default_properties = fips=yes`) do OpenSSL 3.x, você pode inclusive manter os providers `default` e `fips` carregados no mesmo processo e restringir o motor de busca de algoritmos para aceitar exclusivamente implementações com o atributo `fips=yes`!

## Como verificar
Se um único byte do arquivo binário `fips.so` for modificado em disco (por corrupção ou adulteração), a verificação do `module-mac` no `fipsmodule.cnf` falha na inicialização e o OpenSSL entra imediatamente em estado de erro seguro (*Fail-Closed*).

## Conexões
- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Veja também: Arquitetura do **OpenSSL 3.x (`openssl/openssl`)**: `libssl`, `libcrypto` e o Novo Modelo de **Providers (`default`, `fips`, `legacy`, `base`, `null`)**.
- [[openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8]] — Veja também: Geração Moderna de Chaves Assimétricas com **`openssl genpkey`**: Preferindo **`Ed25519` / `X25519` / `ECDSA P-384`** e Proteção **PKCS#8 (`-aes-256-cbc`)**.

## Fontes
- [OpenSSL 3.x Official Repository README (`openssl/openssl`)](https://raw.githubusercontent.com/openssl/openssl/master/README.md) — repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando; consultado em 2026-10-03.
- [OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)](https://raw.githubusercontent.com/openssl/openssl/master/README-PROVIDERS.md) — documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`); consultado em 2026-10-03.
