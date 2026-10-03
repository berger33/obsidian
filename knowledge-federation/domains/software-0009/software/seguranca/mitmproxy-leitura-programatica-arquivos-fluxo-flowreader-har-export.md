---
id: software.seguranca.tranche08.000748
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

# mitmproxy (`mitmproxy.io.FlowReader` & `save_har`): Análise Forense Offline de Arquivos `.mitm`, Extração de Segredos e Exportação **HAR / cURL / OpenAPI**

## Em uma frase
Como os arquivos de captura gerados por `-w sessao.mitm` são streams binários estruturados do `mitmproxy`, o módulo Python **`mitmproxy.io.FlowReader`** permite processar esses arquivos em scripts externos de ciência de dados, auditoria de privacidade (LGPD/GDPR) ou geração de especificações OpenAPI sem precisar subir o proxy.

## Por que importa
Com apenas 10 linhas de Python usando `FlowReader`, uma equipe de AppSec varre horas de tráfego capturado em testes de homologação para encontrar vazamento de dados pessoais (CPFs, cartões, tokens JWT em query strings), listar todos os endpoints e parâmetros descobertos ou exportar para o formato padrão **HAR (*HTTP Archive*)** via `--set hardump=saida.har`.

## Como funciona
Dentro do `mitmproxy` interativo, o comando `:export.file curl @focus /tmp/cmd.sh` (ou `:export.clip httpie @focus`) converte instantaneamente qualquer requisição capturada para um comando `curl` ou `httpie` completo pronto para reprodução.

## Exemplo
```python
"""Ler programaticamente um arquivo .mitm com FlowReader para auditar tokens expostos em query strings."""
from mitmproxy import io, http

with open("/cases/pentest/api_session.mitm", "rb") as logfile:
    reader = io.FlowReader(logfile)
    for flow in reader.stream():
        if isinstance(flow, http.HTTPFlow):
            for k in flow.request.query.keys():
                if any(s in k.lower() for s in ("token", "key", "secret", "password", "jwt")):
                    print(f"[Secret in URL Query] {flow.request.method} {flow.request.pretty_url}")
```

## Limites e trade-offs
Para converter diretamente um arquivo `.mitm` existente para um arquivo `.har` padrão pela linha de comando sem abrir interface, execute: **`mitmdump -nr sessao.mitm --set hardump=sessao.har`**!

## Como verificar
Execute o script `FlowReader` sobre suas capturas de pentest para auditar automaticamente cabeçalhos de segurança ausentes, cookies sem `HttpOnly`/`Secure` e segredos em URLs.

## Conexões
- [[mitmproxy-replay-cliente-servidor-testes-regressao-idor-bola]] — Veja também: mitmproxy: **Client-Side Replay (`-C`)** e **Server-Side Replay (`-S`)** para Testes de Regressão de Autorização (**IDOR / BOLA**) e Simulação Offline.
- [[mitmproxy-interceptacao-http3-quic-websockets-grpc-protobuf-dns]] — Veja também: mitmproxy: Interceptação de Protocolos Modernos — **HTTP/3 (QUIC sobre UDP)**, **gRPC / Protocol Buffers**, **WebSockets** e Servidor **DNS** Scriptável.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Referência cruzada direta com mitmproxy-automacao-addons-python-request-response-websocket-hooks.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
