---
id: software.seguranca.tranche08.000745
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

# mitmproxy: Desenvolvimento de **Addons em Python (`-s script.py`)** — Hooks de Ciclo de Vida (`request`, `response`, `websocket_message`, `tcp_message`, `dns_request`)

## Em uma frase
A arquitetura inteira do `mitmproxy` é construída sobre um motor de **Addons em Python 3 orientados a eventos**: passar **`-s meu_addon.py`** ao `mitmproxy`, `mitmdump` ou `mitmweb` permite inspecionar, modificar, assinar criptograficamente, bloquear ou repetir qualquer pacote HTTP, WebSocket, TCP, UDP ou DNS em tempo real com poucas linhas de Python!

## Por que importa
O objeto `flow: http.HTTPFlow` entregue aos hooks **`request(flow)`** e **`response(flow)`** expõe diretamente `flow.request.method`, `flow.request.pretty_url`, `flow.request.headers`, `flow.request.content` / `.text` / `.json()` e `flow.response.status_code`.

## Como funciona
Para protocolos não-HTTP, o mesmo script pode implementar **`websocket_message(flow: http.HTTPFlow)`** (acessando `flow.websocket.messages[-1]`), **`tcp_message(flow: tcp.TCPFlow)`**, **`udp_message(flow: udp.UDPFlow)`** e **`dns_request(flow: dns.DNSFlow)`**!

## Exemplo
```python
"""Addon mitmproxy (audit_security_headers.py): audita respostas da API e recalcula assinatura HMAC de requisicoes."""
from mitmproxy import http, ctx
import hmac, hashlib

SECRET_KEY = b"chave-hmac-homologacao-2026"

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "api.internal.corp" and flow.request.content:
        sig = hmac.new(SECRET_KEY, flow.request.raw_content, hashlib.sha256).hexdigest()
        flow.request.headers["X-Signature-SHA256"] = sig

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "api.internal.corp":
        if "strict-transport-security" not in flow.response.headers:
            ctx.log.warn(f"[Missing HSTS] {flow.request.pretty_url}")
```

## Limites e trade-offs
Quando encadear uma ferramenta de fuzzing/DAST (como `ffuf`, `Nuclei` ou `sqlmap` com `--proxy http://127.0.0.1:8080`) através de um addon do `mitmdump -s audit_security_headers.py`, o addon recalcula automaticamente o cabeçalho `X-Signature-SHA256` (ou chama um método `rpc.exports` do **Frida**!) para cada payload mutado pela ferramenta de teste!

## Como verificar
Execute o addon em modo headless com **`mitmdump -q -s audit_security_headers.py -r input.mitm`** para testar sua lógica contra tráfego gravado antes de rodar ao vivo.

## Conexões
- [[mitmproxy-expressoes-filtro-flow-filters-interceptacao-seletiva]] — Veja também: mitmproxy: Linguagem de **Expressões de Filtro de Fluxo (*Flow Filter Expressions*)** para Visualização (`v`), Interceptação (`i`) e Exportação.
- [[mitmproxy-modificacao-trafego-modify-body-modify-headers-map-local]] — Veja também: mitmproxy: Reescrita Declarativa sem Código (`--modify-headers`, `--modify-body`, `--map-local` e `--map-remote`).
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[frida-comunicacao-bidirecional-rpc-exports-send-recv-python-host]] — Referência cruzada direta com frida-comunicacao-bidirecional-rpc-exports-send-recv-python-host.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
