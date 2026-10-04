---
id: software.seguranca.tranche16.001555
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/jpillora/chisel/master/README.md", "https://raw.githubusercontent.com/jpillora/chisel/master/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Atravessando Proxies de Saída Corporativos (**`--proxy` HTTP CONNECT / SOCKS5**) e **SSH sobre HTTP (`stdio:` + `ssh -o ProxyCommand`)** com o Chisel

## Em uma frase
Em redes corporativas seguras, as estações de trabalho e servidores internos **não têm rota direta para a internet (NAT)** — a única forma de sair para a internet é passando por um **Proxy Corporativo (`HTTP CONNECT` na porta `3128`/`8080` ou `SOCKS5` na porta `1080`)**, muitas vezes exigindo usuário e senha! Como o `chisel client` atravessa esse proxy de saída, e como usar o modo especial **`stdio:`** para encapsular uma sessão `OpenSSH` real dentro do Chisel?

## Por que importa
Para atravessar um proxy de saída, basta passar ao `chisel client` a flag **`--proxy http://usuario:senha@proxy.interno:8080`** (ou `socks5://proxy.interno:1080`)!

## Como funciona
E para conectar o seu cliente **`ssh` (`OpenSSH`)** diretamente a um servidor SSH remoto passando por um firewall HTTP que bloqueia a porta 22, o Chisel inclui o destino especial **`stdio:<host>:<port>`** (documentado em `remotesTemplate` no `main.go`), projetado especificamente para a diretiva **`ProxyCommand`** do OpenSSH!

## Exemplo
```bash
# Usar o modo stdio do chisel client dentro do ProxyCommand do OpenSSH para fazer SSH real encapsulado sobre HTTPS/WebSocket na porta 443
ssh -o ProxyCommand='chisel client --fingerprint '"${SERVER_FP}"' https://tunel.exemplo.br:443 stdio:%h:%p' \
  admin@127.0.0.1
```

## Limites e trade-offs
Olhe que integração limpa na linha de comando acima: quando você roda `ssh -o ProxyCommand='chisel client ... stdio:%h:%p' admin@127.0.0.1`, o cliente `ssh` não abre uma conexão TCP na porta 22 — ele conversa via `stdin`/`stdout` (`stdio`) com o processo `chisel client`, que encapsula o fluxo sobre HTTPS/WebSocket até o `chisel server` na porta `443` e entrega na porta `22` (`%p`) do servidor!

## Como verificar
Isso permite usar todos os recursos nativos do OpenSSH (`scp`, `sftp`, `rsync`, `JumpHost -J`, encaminhamento de agente FIDO2) através de redes que só permitem tráfego HTTPS na porta 443!

## Conexões
- [[chisel-camuflagem-reverse-proxy-backend-tls-letsencrypt-headers]] — Veja também: Camuflagem HTTP (**`--backend` Reverse Proxy**), TLS Nativo (**`--tls-domain` Let's Encrypt / `--tls-cert`**) e Customização de **`--header` / `Host`** no Chisel.
- [[chisel-operacao-sinais-unix-sigusr2-sighup-sigint-tuning-keepalive]] — Veja também: Operação e Diagnóstico em Tempo de Execução no Chisel: Sinais Unix (**`SIGUSR2` Stats**, **`SIGHUP` Reconnect**, **`SIGINT`/`SIGTERM`**) e Tuning de Backoff.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
