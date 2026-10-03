---
id: software.seguranca.tranche09.000885
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md", "https://datatracker.ietf.org/doc/html/rfc8725", "https://datatracker.ietf.org/doc/html/rfc7519"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `jwt_tool` (**`-C -d` Dictionary Attack**) & **Hashcat (`-m 16500`)**: Auditoria de Segredos Simétricos Fracos em **`HS256` / `HS384` / `HS512`**

## Em uma frase
Quando uma aplicação assina tokens JWT com algoritmos simétricos **HMAC (`HS256`, `HS384`, `HS512`)**, a segurança inteira do sistema de autenticação depende da **entropia do segredo compartilhado (`JWT_SECRET`)** — e como a assinatura de qualquer JWT capturado é calculada localmente sobre a string `Base64URL(Header) + "." + Base64URL(Payload)`, **um atacante consegue testar milhões de senhas por segundo OFFLINE (sem enviar um único pacote para o servidor!)** até encontrar a chave que produz aquela mesma assinatura!

## Por que importa
No `jwt_tool`, passar as flags **`-C -d <wordlist.txt>`** (*Crack mode*) executa um teste rápido de dicionário em CPU contra o token para detectar segredos fracos deixados por desenvolvedores (`secret`, `changeme`, `jwt_secret_key`, `123456`, nome da empresa ou chaves padrão de frameworks).

## Como funciona
E quando o teste em CPU com `jwt_tool -C` não encontra a senha nas primeiras milhares de palavras, basta copiar a string do JWT para um arquivo e usar o **Hashcat em GPU no modo `-m 16500` (JWT HS256/HS384/HS512)** a dezenas de milhões de hashes por segundo!

## Exemplo
```bash
# Auditar offline se o segredo HMAC (HS256) de um JWT consta em uma wordlist de segredos padrao (-C -d) e verificar com -V -p
jwt_tool "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -C -d /usr/share/seclists/Passwords/scraped-JWT-secrets.txt
```

## Limites e trade-offs
Conforme exige o **IETF RFC 7518 (JWA Seção 3.2)** e o **RFC 8725**, uma chave simétrica para `HS256` **DEVE ter no mínimo 256 bits (32 bytes) de entropia criptograficamente aleatória** (`openssl rand -base64 32`), e para `HS512` no mínimo 512 bits (64 bytes) — tornando a quebra offline por dicionário ou força bruta matematicamente impossível!

## Como verificar
Mais seguro ainda em arquiteturas de microsserviços: substitua `HS256` simétrico por **`EdDSA` (`Ed25519`) ou `ES256` (`ECDSA P-256`) assimétrico**, onde apenas o servidor de identidade possui a chave privada de assinatura e os microsserviços possuem apenas a chave pública!

## Conexões
- [[jwttool-injecao-cabecalhos-jwk-jku-x5u-kid-path-traversal-sqli]] — Veja também: `jwt_tool` (`-X i`, `-X s`, `-I -hc kid`): Ataques de **Injeção de Chave no Cabeçalho (`jwk` CVE-2018-0114, `jku`, `x5u`)** e Manipulação de **`kid` (Path Traversal / SQLi)**.
- [[jwttool-varredura-automatizada-playbook-scan-at-pb-er-canary]] — Veja também: `jwt_tool` Modos de Varredura Ativa (**`-M pb` Playbook**, **`-M at` All Tests**, **`-M er` Forced Errors** e **`-M cc` Claim Fuzzing**) com **Canary Value (`-cv`)**.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
