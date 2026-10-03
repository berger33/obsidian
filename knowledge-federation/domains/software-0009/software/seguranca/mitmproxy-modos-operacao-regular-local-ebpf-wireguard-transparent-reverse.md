---
id: software.seguranca.tranche08.000742
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

# mitmproxy: Os 9 Modos de Operação (`regular`, **`local` via eBPF/OS**, **`wireguard`** User-Space, `reverse`, `transparent`, `tun`, `upstream`, `socks5` e `dns`)

## Em uma frase
Conforme detalhado na documentação oficial `Proxy Modes` (`docs.mitmproxy.org/stable/concepts/modes/`), o `mitmproxy` suporta nove modos de captura (selecionados com **`--mode <especificacao>`**, podendo inclusive rodar múltiplos modos simultaneamente na mesma instância!).

## Por que importa
Para aplicações que ignoram as variáveis `HTTP_PROXY`/`HTTPS_PROXY` do sistema operacional (como aplicativos Android em Flutter/React Native/Xamarin, binários Go/Rust ou malwares), dois modos modernos eliminam a necessidade de configurar regras complexas de `iptables`/`pf` manualmente: **(1) `--mode local` (*Local Capture*)** e **(2) `--mode wireguard`**.

## Como funciona
No modo **`--mode local:curl,meu_app`** (ou `--mode local:!navegador` para excluir um processo), o `mitmproxy_rs` usa instrumentação de baixo nível do sistema operacional (**eBPF** no Linux 6.8+, Network Extension no macOS e WinDivert no Windows) para interceptar transparentemente apenas os processos locais escolhidos pelo nome ou PID! Já no modo **`--mode wireguard`**, o `mitmproxy` sobe um **servidor VPN WireGuard 100% em user-space (sem precisar de `root`)** na porta `51820/UDP` e exibe um **QR Code** no terminal para conectar qualquer celular Android/iOS em 5 segundos!

## Exemplo
```bash
# Iniciar o mitmproxy em modo WireGuard user-space (para interceptar apps mobile sem root) ou em modo Local por processo
mitmweb --mode wireguard@51820 --web-host 127.0.0.1
mitmdump --mode local:curl -w /cases/pentest/curl_only.mitm
```

## Limites e trade-offs
No modo `--mode local` em Linux, lembre-se da limitação documentada oficialmente: o nome do processo é comparado contra os primeiros **16 caracteres** (`TASK_COMM_LEN` do kernel Linux) e captura conexões de saída (*egress*); para interceptar tráfego de entrada em um servidor, utilize **`--mode reverse:https://backend.internal:8443`**!

## Como verificar
Teste `mitmdump --mode wireguard` e verifique a geração automática das chaves WireGuard em `~/.mitmproxy/wireguard.conf` e da configuração de cliente com `AllowedIPs = 0.0.0.0/0`.

## Conexões
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Veja também: **`mitmproxy`**, **`mitmdump`** e **`mitmweb`**: Arquitetura do Proxy de Interceptação Programável para HTTP/1, HTTP/2, **HTTP/3 (QUIC)**, WebSockets, TCP/UDP e DNS.
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Veja também: mitmproxy: Gestão da CA Dinâmica (`~/.mitmproxy/`, Domínio Mágico **`mitm.it`**), Certificados de Cliente **mTLS** (`--certs` / `--client-certs`) e `SSLKEYLOGFILE`.
- [[frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning]] — Referência cruzada direta com frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
