---
id: software.seguranca.tranche09.000886
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

# `jwt_tool` Modos de Varredura Ativa (**`-M pb` Playbook**, **`-M at` All Tests**, **`-M er` Forced Errors** e **`-M cc` Claim Fuzzing**) com **Canary Value (`-cv`)**

## Em uma frase
Em vez de gerar dezenas de tokens modificados na mão e testá-los um por um no navegador, o `jwt_tool` inclui um cliente HTTP integrado (compatível com proxies como Burp/ZAP/`mitmproxy`) que envia automaticamente uma bateria de tokens mutados para a aplicação alvo e identifica exatamente quais mutações foram aceitas!

## Por que importa
Para conectar o `jwt_tool` ao endpoint da aplicação, você informa quer a URL alvo (**`-t https://api.alvo/me`**) + cabeçalho/cookie contendo o token (**`-rh "Authorization: Bearer <JWT>"`** ou **`-rc "jwt=<JWT>"`**), quer um arquivo contendo a requisição HTTP bruta (**`-r request.raw`**), junto com um **Valor Canário (`-cv "Bem-vindo"` ou `-cv '"status":"ok"'`)** — uma string que só aparece na resposta quando o token é aceito como válido!

## Como funciona
Os quatro modos de scan (`-M`) são: **`-M pb` (*Playbook Scan*)** — executa os testes mais eficazes de misconfiguration em sequência; **`-M at` (*All Tests*)** — executa todos os ataques de assinatura, cabeçalhos e claims; **`-M er` (*Forced Errors*)** — força erros de parsing para vazar stack traces da biblioteca JWT usada pelo backend; e **`-M cc` (*Common Claims*)**!

## Exemplo
```bash
# Executar um Playbook Scan (-M pb) automatizado contra um endpoint de API verificando quais mutacoes mantem o Canary Value (-cv)
jwt_tool -t https://api.internal.corp/v1/profile \
  -rh "Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIn0.assinatura" \
  -cv '"authenticated":true' \
  -M pb
```

## Limites e trade-offs
Por que o modo **`-M er` (*Forced Errors*)** é tão útil no início de um pentest? Porque ao enviar tokens com JSON malformado, Base64 truncado ou tipos de dados inválidos em `exp`, servidores em modo debug frequentemente devolvem no erro `500` o stack trace revelando exatamente qual biblioteca e versão está rodando (`pyjwt 1.7.1`, `auth0/java-jwt`, `jsonwebtoken 8.5.1`)!

## Como verificar
Cada requisição enviada pelo `jwt_tool` recebe um ID de rastreamento único no log (`~/.jwt_tool/logs/`) e pode ser re-executada individualmente com **`-Q <ID>`**!

## Conexões
- [[jwttool-auditoria-forca-segredos-hmac-dicionario-c-hashcat]] — Veja também: `jwt_tool` (**`-C -d` Dictionary Attack**) & **Hashcat (`-m 16500`)**: Auditoria de Segredos Simétricos Fracos em **`HS256` / `HS384` / `HS512`**.
- [[jwttool-adulteracao-claims-tampering-injecao-assinatura-customizada]] — Veja também: `jwt_tool` (`-T`, `-I`, `-S`): Adulteração Interativa e Não-Interativa de **Claims (`-pc` / `-pv`)**, Cabeçalhos (`-hc` / `-hv`) e Re-Assinatura (`hs256` / `rs256` / `es256`).
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.
- [[jwttool-ataques-exclusao-assinatura-alg-none-null-blank-psychic-ecdsa]] — Referência cruzada direta com jwttool-ataques-exclusao-assinatura-alg-none-null-blank-psychic-ecdsa.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
