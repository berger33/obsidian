---
id: software.seguranca.tranche09.000882
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

# `jwt_tool` (`-X a`, `-X n`, `-X b`, `-X p`): Auditoria de Bypass de Assinatura (**`alg: none` CVE-2015-2951**, **Null Signature**, **Blank Password** e **Psychic Signatures CVE-2022-21449**)

## Em uma frase
A seção 2.1 do **RFC 8725 (JWT BCP)** alerta sobre falhas catastróficas na verificação de assinatura onde um servidor aceita tokens forjados sem conhecer a chave secreta.

## Por que importa
O `jwt_tool` testa automaticamente quatro classes de bypass de assinatura através da flag **`-X` (*eXploit*)**: **(1) `-X a` (`alg: none`, CVE-2015-2951)** — altera o cabeçalho para `"alg": "none"`, `"None"`, `"NONE"`, `"nOnE"` e remove a assinatura (explorando bibliotecas que chamam `jwt.decode(token)` confiando no algoritmo declarado pelo próprio atacante!); **(2) `-X n` (*Null Signature*, CVE-2020-28042)** — mantém `"alg": "HS256"`/`"RS256"` mas trunca a assinatura após o segundo ponto; **(3) `-X b` (*Blank Password*, CVE-2019-20933)** — assina o token usando uma string vazia `""` como chave HMAC (quando a variável de ambiente `JWT_SECRET` não foi carregada no container!); e **(4) `-X p` (*Psychic Signatures*, CVE-2022-21449 no Java 15–18)** — preenche `r = 0, s = 0` em assinaturas **ECDSA (`ES256`/`ES384`/`ES512`)**!

## Como funciona
Combinar esses exploits com **`-T` (*Tamper*)** ou **`-I -pc role -pv admin`** permite testar se o backend aceita um token modificado com privilégio administrativo!

## Exemplo
```bash
# Gerar variantes de teste para bypass de assinatura alg=none (-X a) e Psychic Signature ECDSA (-X p) modificando a claim role=admin
jwt_tool "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -I -pc role -pv admin -X p
```

## Limites e trade-offs
Na engenharia defensiva do código backend (Python `PyJWT`, Node `jose`, Go `golang-jwt`, Java `nimbus-jose-jwt`): **SEMPRE passe uma allowlist explícita de algoritmos permitidos na função de verificação (ex.: `algorithms=["ES256"]` no PyJWT), nunca inclua `"none"`, e aborte a inicialização da aplicação (`fail-fast`) se a variável `JWT_SECRET` estiver vazia ou tiver menos de 32 bytes**!

## Como verificar
Teste todas as variantes geradas contra o endpoint de homologação usando o modo Playbook (`-M pb`).

## Conexões
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Veja também: **`jwt_tool` (`ticarpi/jwt_tool`) & Padrão JWT (RFC 7519 / RFC 8725 BCP)**: Anatomia de **JSON Web Tokens (`Header.Payload.Signature`)** e Decodificação.
- [[jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion]] — Veja também: `jwt_tool` (**`-X k` — *Key Confusion Attack*, CVE-2016-10555**): Confusão de Algoritmo Assimétrico (**`RS256`**) para Simétrico (**`HS256`**) e Defesa conforme **RFC 8725 §3.1**.
- [[jwttool-varredura-automatizada-playbook-scan-at-pb-er-canary]] — Referência cruzada direta com jwttool-varredura-automatizada-playbook-scan-at-pb-er-canary.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
