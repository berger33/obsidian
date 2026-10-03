---
id: software.seguranca.tranche09.000881
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

# **`jwt_tool` (`ticarpi/jwt_tool`) & Padrão JWT (RFC 7519 / RFC 8725 BCP)**: Anatomia de **JSON Web Tokens (`Header.Payload.Signature`)** e Decodificação

## Em uma frase
Um **JSON Web Token (JWT, IETF RFC 7519)** assinado no formato **JWS (*JSON Web Signature*, RFC 7515)** consiste em três segmentos codificados em `Base64URL` separados por ponto (`.`): **`Header`** (metadados criptográficos como `"alg"`, `"typ"`, `"kid"`, `"jku"`, `"x5u"`), **`Payload`** (*Claims* de identidade e autorização como `"iss"`, `"sub"`, `"aud"`, `"exp"`, `"nbf"`, `"iat"`, `"jti"` e roles) e **`Signature`**; enquanto o formato **JWE (RFC 7516)** possui cinco segmentos cifrados.

## Por que importa
A ferramenta open-source **`jwt_tool.py`** (`ticarpi/jwt_tool`, escrita em Python 3) é o toolkit de referência para decodificar, validar, adulterar (*tamper*), fazer fuzzing de claims, testar vulnerabilidades criptográficas conhecidas (mapeadas no **IETF RFC 8725 — *JSON Web Token Best Current Practices***) e auditar a força de segredos HMAC.

## Como funciona
Na primeira execução, o `jwt_tool` gera em **`~/.jwt_tool/`** seu arquivo de configuração **`jwtconf.ini`** junto com pares de chaves RSA/ECDSA e arquivos **JWKS (`JSON Web Key Set`, RFC 7517)** prontos para testes de segurança.

## Exemplo
```bash
# Decodificar e inspecionar todos os campos do Header, Payload (com conversao de timestamps exp/iat) e Signature de um JWT
jwt_tool "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIiLCJleHAiOjE5MjA0OTkyMDB9.x8X_assinatura_exemplo"
```

## Limites e trade-offs
Lembre-se do erro conceitual mais comum de desenvolvedores juniores: **um JWT padrão (JWS de 3 partes) NÃO é criptografado — ele é apenas codificado em Base64URL e assinado**! Qualquer pessoa ou script que veja o token consegue ler 100% do Payload sem precisar de nenhuma chave; portanto, **jamais coloque senhas, segredos ou dados sensíveis não-públicos dentro do Payload de um JWS** (se precisar de confidencialidade, use **JWE**, RFC 7516)!

## Como verificar
Execute `jwt_tool <TOKEN>` em qualquer token capturado no `mitmproxy` para auditar se o payload expõe dados pessoais (PII) ou segredos internos.

## Conexões
- [[jwttool-ataques-exclusao-assinatura-alg-none-null-blank-psychic-ecdsa]] — Veja também: `jwt_tool` (`-X a`, `-X n`, `-X b`, `-X p`): Auditoria de Bypass de Assinatura (**`alg: none` CVE-2015-2951**, **Null Signature**, **Blank Password** e **Psychic Signatures CVE-2022-21449**).
- [[jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion]] — Referência cruzada direta com jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
