---
id: software.seguranca.tranche09.000884
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

# `jwt_tool` (`-X i`, `-X s`, `-I -hc kid`): Ataques de **Injeção de Chave no Cabeçalho (`jwk` CVE-2018-0114, `jku`, `x5u`)** e Manipulação de **`kid` (Path Traversal / SQLi)**

## Em uma frase
A especificação JWS (RFC 7515) define cabeçalhos opcionais para indicar ao destinatário qual chave pública usar na validação: **`"jwk"`** (embute uma chave pública JWK diretamente dentro do cabeçalho do token!), **`"jku"` (*JWK Set URL*)**, **`"x5u"` (*X.509 URL*)** e **`"kid"` (*Key ID*)**.

## Por que importa
Se o desenvolvedor do backend implementar o resolvedor de chaves confiando cegamente nesses cabeçalhos sem validá-los contra uma lista estática de chaves confiáveis, quatro ataques clássicos testados pelo `jwt_tool` tornam-se possíveis: **(1) `-X i` (*Inject Inline JWK*, CVE-2018-0114)** — o `jwt_tool` gera um novo par de chaves RSA próprio, assina o token forjado com a sua chave privada e coloca a sua própria chave pública dentro do cabeçalho `"jwk"` do token!; **(2) `-X s` (*Spoof JWKS URL*)** — aponta `"jku"` ou `"x5u"` para um servidor controlado pelo tester (ou explora SSRF/Open Redirect no domínio alvo); **(3) `kid` Path Traversal (`"kid": "../../../../dev/null"`)** — faz o servidor ler o arquivo vazio `/dev/null` como chave HMAC e assina o token com string vazia!; e **(4) `kid` SQL/Command Injection**!

## Como funciona
Conforme determina o **RFC 8725 Seção 3.10**, o servidor **jamais** deve buscar chaves em URLs `jku`/`x5u` arbitrárias nem confiar em chaves `"jwk"` auto-declaradas pelo cliente sem validação de cadeia PKI.

## Exemplo
```bash
# Testar CVE-2018-0114 (Inline JWK Injection: -X i) e Path Traversal no cabecalho kid apuntando para /dev/null
jwt_tool "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -I -pc role -pv admin -X i

jwt_tool "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDQyIiwicm9sZSI6InVzZXIifQ.assinatura" \
  -I -hc kid -hv "../../../../../dev/null" -pc role -pv admin -S hs256 -p ""
```

## Limites e trade-offs
No código do servidor que utiliza `"kid"` para selecionar chaves em um JWKS ou diretório, valide que o valor de `kid` corresponde estritamente a uma regex alfanumérica (`^[a-zA-Z0-9_-]{1,64}$`) e faça a busca como chave de dicionário em memória (nunca concatenando `kid` em caminhos de sistema de arquivos `open()` ou queries SQL!).

## Como verificar
Audite como os seus microsserviços resolvem o campo `kid` e certifique-se de que cabeçalhos `jku`, `x5u` e `jwk` desconhecidos são ignorados.

## Conexões
- [[jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion]] — Veja também: `jwt_tool` (**`-X k` — *Key Confusion Attack*, CVE-2016-10555**): Confusão de Algoritmo Assimétrico (**`RS256`**) para Simétrico (**`HS256`**) e Defesa conforme **RFC 8725 §3.1**.
- [[jwttool-auditoria-forca-segredos-hmac-dicionario-c-hashcat]] — Veja também: `jwt_tool` (**`-C -d` Dictionary Attack**) & **Hashcat (`-m 16500`)**: Auditoria de Segredos Simétricos Fracos em **`HS256` / `HS384` / `HS512`**.
- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — Referência cruzada direta com jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725.
- [[wapiti-deteccao-out-of-band-ssrf-xxe-log4shell-endpoint-customizado]] — Referência cruzada direta com wapiti-deteccao-out-of-band-ssrf-xxe-log4shell-endpoint-customizado.

## Fontes
- [jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs](https://raw.githubusercontent.com/ticarpi/jwt_tool/master/README.md) — documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking; consultado em 2026-10-03.
- [IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725) — padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens; consultado em 2026-10-03.
- [IETF RFC 7519 — JSON Web Token (JWT) Standard Specification](https://datatracker.ietf.org/doc/html/rfc7519) — especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens; consultado em 2026-10-03.
