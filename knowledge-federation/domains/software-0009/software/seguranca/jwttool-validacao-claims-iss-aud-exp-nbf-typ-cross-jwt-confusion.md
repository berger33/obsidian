---
id: software.seguranca.tranche09.000888
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

# Segurança de Claims JWT conforme **IETF RFC 8725 (§3.8–3.12)**: Prevenção de **Cross-JWT Confusion (`aud`, `iss`, `typ`)** e Validação Temporal (`exp`, `nbf`)

## Em uma frase
Mesmo quando a assinatura criptográfica de um JWT é 100% válida e usa `ES256` ou `EdDSA` forte, a aplicação ainda pode ser completamente comprometida se não validar as **Claims Semânticas do Payload e do Header** exigidas pelas **Seções 3.8 a 3.12 do IETF RFC 8725 (JWT BCP)**!

## Por que importa
Considere o ataque de **Cross-JWT / Service Confusion**: uma organização usa o mesmo servidor de identidade (IdP / chave de assinatura) para emitir tokens para três serviços diferentes (`servico-chat`, `servico-faturamento` e `painel-admin`), ou usa a mesma chave para assinar um token de *"Confirmação de E-mail"* e um token de *"Sessão de Login"*.

## Como funciona
Se o `painel-admin` verificar apenas que a assinatura do IdP é válida, mas **não verificar que `"aud"` (*Audience*) é igual a `"https://admin.exemplo.com.br"` e que `"typ"` no Header é `"at+jwt"` (RFC 9068)**, um usuário comum pega o seu token legítimo do `servico-chat` e o envia para o `painel-admin`, sendo aceito como autenticado!

## Exemplo
```python
"""Validacao segura e completa de um JWT em Python (PyJWT) aplicando todas as exigencias do IETF RFC 8725."""
import jwt

def verify_access_token(token: str, public_key_pem: bytes) -> dict:
    return jwt.decode(
        token,
        key=public_key_pem,
        algorithms=["ES256"],  # Allowlist estrita (proibe 'none' e HS256 Key Confusion)
        issuer="https://idp.exemplo.com.br",
        audience="https://api-financeira.exemplo.com.br",
        leeway=30,
        options={
            "require": ["exp", "iat", "nbf", "iss", "aud", "sub", "jti"],
            "verify_signature": True,
            "verify_exp": True,
            "verify_nbf": True,
            "verify_iss": True,
            "verify_aud": True,
        },
    )
```

## Limites e trade-offs
Use o `jwt_tool -I` para testar em pentests: **(1)** enviar um token com `"exp"` no passado (para ver se o servidor esqueceu de validar expiração); **(2)** enviar um **Refresh Token** ou **ID Token** no lugar do **Access Token**; e **(3)** enviar um token emitido para o ambiente de `staging` ou para outro `client_id`/`aud` da mesma empresa!

## Como verificar
Garanta no código que a opção `require=["exp", "iss", "aud", "sub"]` esteja ativa (pois em muitas bibliotecas, se a claim `"exp"` for totalmente omitida do payload pelo atacante, a expiração só falha se `"exp"` estiver na lista `require`!).

## Conexões
- [[jwttool-adulteracao-claims-tampering-injecao-assinatura-customizada]] — Veja também: `jwt_tool` (`-T`, `-I`, `-S`): Adulteração Interativa e Não-Interativa de **Claims (`-pc` / `-pv`)**, Cabeçalhos (`-hc` / `-hv`) e Re-Assinatura (`hs256` / `rs256` / `es256`).
- [[jwttool-verificacao-chaves-publicas-jwks-reconstrucao-rsa-ecdsa]] — Veja também: `jwt_tool` (`-V -pk` / `-jw`): Verificação de Tokens contra **Chaves Públicas PEM e Arquivos JWKS**, Extração de Chaves e Reconstrução.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
