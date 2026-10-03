---
id: software.seguranca.tranche09.000883
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

# `jwt_tool` (**`-X k` — *Key Confusion Attack*, CVE-2016-10555**): Confusão de Algoritmo Assimétrico (**`RS256`**) para Simétrico (**`HS256`**) e Defesa conforme **RFC 8725 §3.1**

## Em uma frase
Uma das vulnerabilidades criptográficas mais elegantes e perigosas documentadas na **Seção 3.1 do IETF RFC 8725 (*Algorithm Verification*)** é o ataque de **Confusão de Algoritmo / Key Confusion (`RS256` -> `HS256`, CVE-2016-10555)**.

## Por que importa
Entenda exatamente como a falha acontece no código do servidor: a aplicação foi projetada para usar criptografia assimétrica **`RS256`** (o servidor de autenticação assina o JWT com sua **Chave Privada RSA**, e os microsserviços validam o JWT passando a **Chave Pública RSA `public.pem`** para `jwt.verify(token, public_key_pem)`). Porém, a chave pública RSA é pública (exposta em `/jwks.json`, `/certs` ou extraída de dois tokens)!

## Como funciona
Se um atacante alterar o cabeçalho do JWT de `"alg": "RS256"` para **`"alg": "HS256"` (HMAC-SHA256 simétrico)** e assinar o token usando **os bytes exatos do arquivo `public.pem` como se fossem o segredo simétrico HMAC** (`jwt_tool <JWT> -X k -pk public.pem`), uma biblioteca mal configurada que não restringe `algorithms=["RS256"]` lerá `"alg": "HS256"` e calculará o HMAC usando a string `public.pem` que ela própria tem em memória — validando o token forjado pelo atacante!

## Exemplo
```bash
# Testar vulnerabilidade de Key Confusion (RS256 -> HS256) assinando o token com a chave publica RSA do servidor (-X k -pk)
jwt_tool "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -I -pc role -pv admin \
  -X k -pk /cases/pentest/server_public_key.pem
```

## Limites e trade-offs
Como o **RFC 8725 Seção 3.1 e 3.2** erradica 100% o ataque de *Key Confusion*? Através de duas regras obrigatórias: **(1)** toda chamada `verify()` deve fixar o algoritmo esperado (`algorithms=["RS256"]`) ignorando algoritmos simétricos quando a chave for pública; e **(2)** usar objetos de chave fortemente tipados (`RSAPublicKey` / JWK com `"kty": "RSA"` e `"alg": "RS256"`), que lançam exceção de tipo se passados para uma função HMAC `HS256`!

## Como verificar
Verifique no código-fonte de todos os microsserviços que validam JWT se o parâmetro `algorithms` está explicitamente travado apenas no algoritmo assimétrico emitido pelo IdP.

## Conexões
- [[jwttool-ataques-exclusao-assinatura-alg-none-null-blank-psychic-ecdsa]] — Veja também: `jwt_tool` (`-X a`, `-X n`, `-X b`, `-X p`): Auditoria de Bypass de Assinatura (**`alg: none` CVE-2015-2951**, **Null Signature**, **Blank Password** e **Psychic Signatures CVE-2022-21449**).
- [[jwttool-injecao-cabecalhos-jwk-jku-x5u-kid-path-traversal-sqli]] — Veja também: `jwt_tool` (`-X i`, `-X s`, `-I -hc kid`): Ataques de **Injeção de Chave no Cabeçalho (`jwk` CVE-2018-0114, `jku`, `x5u`)** e Manipulação de **`kid` (Path Traversal / SQLi)**.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
