---
id: software.seguranca.tranche08.000741
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

# **`mitmproxy`**, **`mitmdump`** e **`mitmweb`**: Arquitetura do Proxy de Interceptação Programável para HTTP/1, HTTP/2, **HTTP/3 (QUIC)**, WebSockets, TCP/UDP e DNS

## Em uma frase
**`mitmproxy`** (`mitmproxy/mitmproxy`, licença MIT, escrito em Python e Rust via `mitmproxy_rs`) é a suíte open-source de proxy de interceptação TLS/SSL para análise de segurança de aplicações web/APIs, pentests mobile e engenharia reversa de protocolos.

## Por que importa
Conforme documentado no `README.md` oficial, o projeto fornece três frontends sobre o mesmo motor de proxy e sistema de addons: **(1) `mitmproxy`** (interface interativa TUI de console em terminal com atalhos estilo Vim), **(2) `mitmdump`** (o equivalente ao `tcpdump` para HTTP/TLS: ferramenta de linha de comando sem interface visual para gravação, replay e execução de scripts Python em alta velocidade) e **(3) `mitmweb`** (interface gráfica web no navegador para inspeção visual de fluxos).

## Como funciona
Diferente de proxies antigos restritos a HTTP/1.1 sobre TCP, a arquitetura moderna do `mitmproxy` intercepta e disseca nativamente **HTTP/1.x**, **HTTP/2**, **HTTP/3 sobre QUIC (UDP)**, **WebSockets**, fluxos **TCP e UDP brutos** e consultas **DNS**.

## Exemplo
```bash
# Verificar a versao do mitmproxy/mitmdump, a versao do OpenSSL e iniciar captura silenciosa em arquivo de fluxo (-w)
mitmdump --version
mitmdump --listen-host 127.0.0.1 --listen-port 8080 -w /cases/pentest/api_session.mitm
```

## Limites e trade-offs
Sempre vincule a porta de escuta ao loopback (`--listen-host 127.0.0.1` no modo local/regular) ou a uma interface de laboratório isolada, pois deixar a porta do proxy aberta em `0.0.0.0` em uma rede compartilhada permite que terceiros usem sua estação como proxy de saída.

## Como verificar
Abra um arquivo `.mitm` gravado pelo `mitmdump` no `mitmproxy -r /cases/pentest/api_session.mitm` para navegar interativamente por todas as requisições e respostas capturadas.

## Conexões
- [[mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse]] — Veja também: mitmproxy: Os 9 Modos de Operação (`regular`, **`local` via eBPF/OS**, **`wireguard`** User-Space, `reverse`, `transparent`, `tun`, `upstream`, `socks5` e `dns`).
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Referência cruzada direta com mitmproxy-automacao-addons-python-request-response-websocket-hooks.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
