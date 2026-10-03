---
id: software.seguranca.tranche09.000889
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

# `jwt_tool` (`-V -pk` / `-jw`): Verificação de Tokens contra **Chaves Públicas PEM e Arquivos JWKS**, Extração de Chaves e Reconstrução

## Em uma frase
Durante uma auditoria de segurança de APIs e provedores OpenID Connect (OIDC), frequentemente você encontra um endpoint público **`/.well-known/jwks.json`** (ou certificados TLS do servidor) e quer verificar matematicamente qual daquelas chaves públicas assinou o JWT que você tem em mãos.

## Por que importa
O modo Verify (**`-V`**) do `jwt_tool` valida a assinatura de qualquer token contra uma chave pública em formato PEM (**`-V -pk public.pem`**) ou diretamente contra um arquivo **JSON Web Key Set (**`-V -jw jwks.json`**)**, identificando imediatamente qual chave do conjunto valida o token!

## Como funciona
Além disso, o `jwt_tool` permite exportar chaves públicas no formato JWKS e auxiliar na reconstrução/conversão entre formatos JWK (`n`, `e` em Base64URL) e PEM (`-----BEGIN PUBLIC KEY-----`) para alimentar o ataque de *Key Confusion* (`-X k`).

## Exemplo
```bash
# Baixar o conjunto de chaves publicas JWKS do provedor OIDC e verificar matematicamente um JWT contra o arquivo JWKS (-V -jw)
curl -sS https://idp.internal.corp/.well-known/jwks.json -o /cases/pentest/idp_jwks.json
jwt_tool "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIn0.assinatura" \
  -V -jw /cases/pentest/idp_jwks.json
```

## Limites e trade-offs
Atenção ao auditar endpoints `/.well-known/jwks.json` gerados manualmente por desenvolvedores: verifique se por um erro grave de serialização o JSON exposto em `/jwks.json` inclui os parâmetros de **Chave Privada RSA (`"d"`, `"p"`, `"q"`, `"dp"`, `"dq"`, `"qi"`) ou ECC (`"d"`)**! Se o campo `"d"` estiver presente no JWKS público, a chave privada inteira do servidor vazou!

## Como verificar
Execute `jq '.keys[] | has("d")' /cases/pentest/idp_jwks.json` em todo endpoint JWKS auditado para confirmar que retorna apenas `false`.

## Conexões
- [[jwttool-validacao-claims-iss-aud-exp-nbf-typ-cross-jwt-confusion]] — Veja também: Segurança de Claims JWT conforme **IETF RFC 8725 (§3.8–3.12)**: Prevenção de **Cross-JWT Confusion (`aud`, `iss`, `typ`)** e Validação Temporal (`exp`, `nbf`).
- [[jwttool-revogacao-ciclo-vida-jti-token-binding-dpop-mtls-defesa]] — Veja também: Arquitetura Defensiva de Sessões JWT: **Curta Duração (`exp`)**, Revogação via **`jti` Allowlist/Blocklist**, Cookies `HttpOnly` e **Sender-Constrained Tokens (`mTLS` RFC 8705 / `DPoP` RFC 9449)**.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.
- [[jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion]] — Referência cruzada direta com jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
