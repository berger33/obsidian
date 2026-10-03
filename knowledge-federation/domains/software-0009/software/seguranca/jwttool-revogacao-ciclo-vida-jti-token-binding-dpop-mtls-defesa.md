---
id: software.seguranca.tranche09.000890
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

# Arquitetura Defensiva de Sessões JWT: **Curta Duração (`exp`)**, Revogação via **`jti` Allowlist/Blocklist**, Cookies `HttpOnly` e **Sender-Constrained Tokens (`mTLS` RFC 8705 / `DPoP` RFC 9449)**

## Em uma frase
O maior *trade-off* arquitetural dos JSON Web Tokens *stateless* é a **Revogação e o Roubo de Token (Token Replay)**: se uma aplicação emite um JWT com validade de `30 dias` (`exp`) e o armazena no `localStorage` do navegador (acessível por qualquer script JavaScript em caso de XSS!), um atacante que roube esse JWT pode usá-lo de qualquer lugar do mundo durante 30 dias — mesmo depois que o usuário clicar em "Logout" ou trocar a senha!

## Por que importa
Para construir uma arquitetura de sessão JWT resiliente contra roubo e replay, combine quatro controles de engenharia: **(1) Access Tokens de Curtíssima Duração (`exp` de 5 a 15 minutos)** renovados via Refresh Token rotativo opaco; **(2) Armazenamento em Cookie `__Host-session` com `HttpOnly; Secure; SameSite=Strict`** (nunca em `localStorage`!); **(3) Identificador Único de Token (`"jti"`, RFC 7519 §4.1.7)** verificado em uma blocklist rápida em memória (Redis com TTL igual ao tempo restante até o `exp`) para permitir revogação imediata no Logout; e **(4) Sender-Constrained Tokens**!

## Como funciona
Com **OAuth 2.0 mTLS Certificate-Bound Access Tokens (RFC 8705, claim `"cnf": {"x5t#S256": "..."}`)** ou **DPoP (*Demonstrating Proof of Possession*, RFC 9449)**, o JWT fica vinculado criptograficamente à chave privada do cliente: mesmo que o JWT seja vazado, ele é inútil sem a chave privada correspondente!

## Exemplo
```json
{
  "iss": "https://idp.exemplo.com.br",
  "sub": "usr_948102",
  "aud": "https://api.exemplo.com.br",
  "exp": 1791034500,
  "iat": 1791033600,
  "jti": "d9b2d63d-a233-4123-847a-76382910abc1",
  "cnf": {
    "x5t#S256": "bwcK0esc3ACC3DB2Y5_lESsXE8o9ltc05O89jdN-dg2"
  }
}
```

## Limites e trade-offs
Durante um pentest, sempre faça este teste de validação de ciclo de vida: copie o JWT da sessão atual, clique em **"Sair / Logout"** na aplicação web, e tente reutilizar o JWT antigo no `jwt_tool` / `curl`! Se a API continuar aceitando o JWT após o Logout, reporte a falha de *Missing Server-Side Token Invalidation on Logout*!

## Como verificar
Verifique que o TTL do Access Token (`exp - iat`) não excede 900 segundos (15 minutos) em aplicações críticas.

## Conexões
- [[jwttool-verificacao-chaves-publicas-jwks-reconstrucao-rsa-ecdsa]] — Veja também: `jwt_tool` (`-V -pk` / `-jw`): Verificação de Tokens contra **Chaves Públicas PEM e Arquivos JWKS**, Extração de Chaves e Reconstrução.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.
- [[jwttool-validacao-claims-iss-aud-exp-nbf-typ-cross-jwt-confusion]] — Referência cruzada direta com jwttool-validacao-claims-iss-aud-exp-nbf-typ-cross-jwt-confusion.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
