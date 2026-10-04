---
id: software.seguranca.tranche08.000744
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://docs.mitmproxy.org/stable/concepts/modes/", "https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md", "https://docs.mitmproxy.org/stable/addons-overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# mitmproxy: Linguagem de **Expressões de Filtro de Fluxo (*Flow Filter Expressions*)** para Visualização (`v`), Interceptação (`i`) e Exportação

## Em uma frase
Em uma aplicação moderna que dispara centenas de requisições de telemetria, fontes, imagens e scripts de terceiros por minuto, o analista precisa filtrar cirurgicamente os fluxos usando a linguagem de **Expressões de Filtro** do `mitmproxy` (usada tanto na TUI/Web quanto na CLI do `mitmdump`).

## Por que importa
Os operadores de filtro permitem combinar condições com **`&` (AND)**, **`|` (OR)**, **`!` (NOT)** e parênteses: **`~d <regex>`** (domínio), **`~u <regex>`** (URL), **`~m <regex>`** (método HTTP, ex.: `~m "(POST|PUT|DELETE)"`), **`~c <codigo>`** (status HTTP, ex.: `~c 500`), **`~hq <regex>`** / **`~hs <regex>`** (cabeçalhos de requisição/resposta), **`~bq <regex>`** / **`~bs <regex>`** (corpo de requisição/resposta), **`~a`** (fluxos de assets estáticos JS/CSS/imagens) e **`~websocket`**.

## Como funciona
No `mitmdump -r sessao_completa.mitm -w apenas_api_erros.mitm "<filtro>"`, você pode filtrar gigabytes de tráfego gravado e extrair em segundos apenas as requisições `POST`/`PUT` do domínio alvo que retornaram erro ou contiveram um token específico.

## Exemplo
```bash
# Filtrar um arquivo de captura (.mitm) extraindo apenas chamadas POST/PUT/PATCH para /api/ que nao sejam assets estaticos
mitmdump -nr /cases/pentest/api_session.mitm \
  -w /cases/pentest/filtered_mutations.mitm \
  "~d api\\.exemplo\\.com\\.br & ~u /v[12]/ & ~m (POST|PUT|PATCH|DELETE) & !~a"
```

## Limites e trade-offs
Quando você está auditando um aplicativo que faz *Certificate Pinning* apenas para domínios de terceiros (ou inversamente, quando você só quer interceptar o TLS de `api.exemplo.com.br` sem tocar no tráfego bancário/Google Play do aparelho), use **`--ignore-hosts '^(.+\.)?google\.com:443$'`** ou **`--allow-hosts '^api\.exemplo\.com\.br:443$'`** para que o `mitmproxy` faça *passthrough TCP* transparente dos demais domínios sem quebrar o TLS deles!

## Como verificar
Teste a expressão de filtro ao vivo no `mitmproxy` pressionando `f` (*Set view filter*) antes de aplicá-la em lote no `mitmdump`.

## Conexões
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Veja também: mitmproxy: Gestão da CA Dinâmica (`~/.mitmproxy/`, Domínio Mágico **`mitm.it`**), Certificados de Cliente **mTLS** (`--certs` / `--client-certs`) e `SSLKEYLOGFILE`.
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Veja também: mitmproxy: Desenvolvimento de **Addons em Python (`-s script.py`)** — Hooks de Ciclo de Vida (`request`, `response`, `websocket_message`, `tcp_message`, `dns_request`).
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[mitmproxy-modificacao-trafego-modify-body-modify-headers-map-local]] — Referência cruzada direta com mitmproxy-modificacao-trafego-modify-body-modify-headers-map-local.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
