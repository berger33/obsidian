---
id: software.seguranca.tranche08.000749
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

# mitmproxy: Interceptação de Protocolos Modernos — **HTTP/3 (QUIC sobre UDP)**, **gRPC / Protocol Buffers**, **WebSockets** e Servidor **DNS** Scriptável

## Em uma frase
Aplicações mobile e microsserviços modernos utilizam cada vez mais **HTTP/3 sobre QUIC (porta 443/UDP)**, chamadas binárias **gRPC (`application/grpc` com Protocol Buffers sobre HTTP/2)** e conexões persistentes **WebSockets**: ferramentas de proxy antigas que só entendem TCP forçam o aplicativo a fazer fallback para HTTP/1.1 ou falham completamente quando o cliente exige QUIC.

## Por que importa
O `mitmproxy` suporta nativamente a interceptação de **HTTP/3 / QUIC**, a visualização automática de mensagens **Protocol Buffers / gRPC** (decodificando a estrutura de campos numéricos Protobuf mesmo sem o arquivo `.proto`, ou usando definições `.proto` quando fornecidas) e a edição em tempo real de frames **WebSocket** (`websocket_message`).

## Como funciona
Além disso, o modo **`--mode dns@53`** transforma o `mitmproxy` em um servidor DNS completo onde o hook `dns_request(flow)` / `dns_response(flow)` pode responder ou redirecionar registros `A`, `AAAA`, `CNAME`, `TXT` e `HTTPS/SVCB` programaticamente.

## Exemplo
```python
"""Addon mitmproxy para inspecionar e registrar todas as mensagens WebSocket bidirecionais."""
from mitmproxy import http, ctx

def websocket_message(flow: http.HTTPFlow) -> None:
    assert flow.websocket is not None
    msg = flow.websocket.messages[-1]
    direction = "Client -> Server" if msg.from_client else "Server -> Client"
    ctx.log.info(f"[WS {direction}] ({len(msg.content)} bytes): {msg.content[:120]!r}")
```

## Limites e trade-offs
Dentro de `websocket_message(flow)`, você pode modificar o payload em trânsito (`msg.content = b'{"action":"ping"}'`) ou descartar completamente um frame WebSocket específico chamando **`msg.drop()`**!

## Como verificar
Teste interceptar uma conexão WebSocket ou gRPC no `mitmproxy` e alterne os modos de visualização de corpo (`m` -> `Protobuf`, `Hex`, `Raw`, `JSON`) na aba de detalhes.

## Conexões
- [[mitmproxy-leitura-programatica-arquivos-fluxo-flowreader-har-export]] — Veja também: mitmproxy (`mitmproxy.io.FlowReader` & `save_har`): Análise Forense Offline de Arquivos `.mitm`, Extração de Segredos e Exportação **HAR / cURL / OpenAPI**.
- [[mitmproxy-proxy-reverso-waf-leve-decepcao-honeypot-upstream-chaining]] — Veja também: mitmproxy: Uso Defensivo como **Reverse Proxy de Diagnóstico (`--mode reverse`)**, Honeypot de API de Alta Interação e **Upstream Proxy Chaining**.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse]] — Referência cruzada direta com mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
