---
id: software.seguranca.tranche09.000887
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

# `jwt_tool` (`-T`, `-I`, `-S`): Adulteração Interativa e Não-Interativa de **Claims (`-pc` / `-pv`)**, Cabeçalhos (`-hc` / `-hv`) e Re-Assinatura (`hs256` / `rs256` / `es256`)

## Em uma frase
Quando você descobre a chave secreta HMAC (via `-C`), obtém uma chave privada de teste ou quer testar se um microsserviço downstream valida apenas o formato do token sem verificar a assinatura (*Unverified Signature*), você precisa editar as claims do Payload (`sub`, `role`, `tenant_id`, `exp`) e re-assinar o token.

## Por que importa
O `jwt_tool` oferece dois modos para isso: **(1) Modo Interativo (`-T` — *Tamper*)**, que abre um menu passo a passo no terminal permitindo editar/adicionar/excluir qualquer campo do Header ou Payload; e **(2) Modo Não-Interativo de Injeção (`-I`)**, onde **`-hc` / `-hv`** injetam chaves/valores no Header e **`-pc` / `-pv`** injetam chaves/valores no Payload (ou `-pf payloads.txt` para fuzzing de valores)!

## Como funciona
Para assinar o token modificado, a flag **`-S <algoritmo>`** (`hs256`, `hs384`, `hs512`, `rs256`, `es256`, `ps256`) combinada com **`-p <segredo_hmac>`** (ou `-pk` / `-prk <chave_privada.pem>`) gera o token assinado pronto para uso!

## Exemplo
```bash
# Modificar nao-interativamente as claims sub e role de um JWT (-I -pc/-pv) e re-assina-lo com a chave HMAC descoberta (-S hs256 -p)
jwt_tool "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -I -pc sub -pv "1" -pc role -pv "admin" \
  -S hs256 -p "Segredo-De-Homologacao-Descoberto"
```

## Limites e trade-offs
Um erro grave e surpreendentemente comum em arquiteturas com **API Gateway**: o desenvolvedor pensa que o API Gateway na borda já validou a assinatura do JWT e, por isso, no microsserviço interno chama **`jwt.decode(token, options={"verify_signature": False})`** (ou faz `base64_decode` manual do segundo segmento)! Se qualquer atacante conseguir alcançar o microsserviço ou se uma rota do Gateway não tiver o plugin JWT ativo, qualquer token modificado com `jwt_tool -I` sem chave válida será aceito!

## Como verificar
Teste sempre enviar um token com claim `sub` alterada e assinatura original intacta (sem re-assinar) para verificar se o backend realmente valida a assinatura criptográfica em todas as rotas.

## Conexões
- [[jwttool-varredura-automatizada-playbook-scan-at-pb-er-canary]] — Veja também: `jwt_tool` Modos de Varredura Ativa (**`-M pb` Playbook**, **`-M at` All Tests**, **`-M er` Forced Errors** e **`-M cc` Claim Fuzzing**) com **Canary Value (`-cv`)**.
- [[jwttool-validacao-claims-iss-aud-exp-nbf-typ-cross-jwt-confusion]] — Veja também: Segurança de Claims JWT conforme **IETF RFC 8725 (§3.8–3.12)**: Prevenção de **Cross-JWT Confusion (`aud`, `iss`, `typ`)** e Validação Temporal (`exp`, `nbf`).
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
