---
id: software.seguranca.tranche08.000750
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

# mitmproxy: Uso Defensivo como **Reverse Proxy de Diagnóstico (`--mode reverse`)**, Honeypot de API de Alta Interação e **Upstream Proxy Chaining**

## Em uma frase
Além do uso ofensivo/auditoria no lado do cliente, o modo **`--mode reverse:https://backend.internal:8443`** posiciona o `mitmproxy` na frente de um servidor web ou API como um proxy reverso transparente com terminação TLS.

## Por que importa
Para equipes de **Resposta a Incidentes (DFIR)** e **Engenharia de Decepção (Honeypots)**, colocar o `mitmdump --mode reverse` na frente de um serviço vulnerável sob investigação ou de um Honeypot de API permite gravar 100% dos exploits enviados pelos atacantes em arquivos `.mitm` completos (com chaves TLS decifradas) e aplicar *virtual patching* instantâneo em Python (`flow.response = http.Response.make(403, b"Forbidden")`) enquanto a equipe de engenharia corrige o código da aplicação!

## Como funciona
E em pentests onde o tráfego precisa sair através de um proxy corporativo ou túnel SOCKS5/HTTP secundário (ou ser encadeado do `mitmproxy` para o **OWASP ZAP**), o modo **`--mode upstream:http://127.0.0.1:8090`** encadeia os dois proxies perfeitamente.

## Exemplo
```bash
# Posicionar o mitmdump como Reverse Proxy TLS na porta 443 gravando todo o trafego de entrada para analise forense
mitmdump --mode reverse:http://127.0.0.1:8000 \
  --listen-host 0.0.0.0 --listen-port 443 \
  --certs "api.honeypot.corp=/etc/letsencrypt/live/api.honeypot.corp/fullchain_and_key.pem" \
  -w /cases/dfir/inbound_attacks.mitm
```

## Limites e trade-offs
Note o formato da flag **`--certs "[dominio=]caminho.pem"`**: no `mitmproxy`, o arquivo `.pem` passado para `--certs` deve conter tanto a **chave privada sem senha** quanto a **cadeia completa de certificados X.509** concatenados no mesmo arquivo.

## Como verificar
Verifique que o tráfego recebido na porta 443 apresenta o certificado oficial configurado em `--certs` e grava os fluxos completos em `/cases/dfir/inbound_attacks.mitm`.

## Conexões
- [[mitmproxy-interceptacao-http3-quic-websockets-grpc-protobuf-dns]] — Veja também: mitmproxy: Interceptação de Protocolos Modernos — **HTTP/3 (QUIC sobre UDP)**, **gRPC / Protocol Buffers**, **WebSockets** e Servidor **DNS** Scriptável.
- [[mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse]] — Referência cruzada direta com mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse.
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Referência cruzada direta com mitmproxy-automacao-addons-python-request-response-websocket-hooks.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
