---
id: software.seguranca.tranche16.001553
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

# Sintaxe Completa de `<remote>` no Chisel: Tunelamento **Local (Forward)**, **Reverso (`R:`)**, **Proxy Dinâmico `SOCKS5` (`--socks5` / `R:socks`)** e **Túneis `UDP` (`/udp`)**

## Em uma frase
Como funciona a gramática de especificação de túneis **`<local-host>:<local-port>:<remote-host>:<remote-port>/<protocol>`** do `chisel client` (definida em `remotesTemplate` no `main.go`), e qual é a diferença entre abrir um túnel normal vs. um túnel reverso prefixado por **`R:`**?

## Por que importa
Veja como a sintaxe é concisa e poderosa: **(1) Forward Tunnel (sem `R:`)**: compartilha um serviço da rede do **Servidor** para a máquina do **Cliente** (ex.: `chisel client https://srv:8443 5432:10.0.0.50:5432` faz a porta `127.0.0.1:5432` do cliente acessar o banco `10.0.0.50:5432` lá na rede do servidor!).

## Como funciona
**(2) Reverse Tunnel (prefixo `R:`)**: compartilha um serviço da rede do **Cliente** (que está atrás de NAT/Firewall!) para o **Servidor** (ex.: `R:127.0.0.1:2222:10.10.10.5:22` ou **`R:127.0.0.1:1080:socks`**); e **(3) Suporte a `UDP` (`/udp`)**: basta acrescentar **`/udp`** ao final de qualquer especificação (ex.: `5353:1.1.1.1:53/udp`) para tunelar pacotes UDP (como DNS, SNMP ou WireGuard) sobre a conexão TCP/WebSocket do Chisel!

## Exemplo
```bash
# Iniciar o chisel server habilitando tuneis reversos (--reverse) e conectar o chisel client expondo um proxy SOCKS5 reverso apenas no loopback do servidor
chisel server --host 127.0.0.1 --port 8080 --keyfile ./server.key --authfile ./users.json --reverse &
chisel client --fingerprint "${SERVER_FP}" --auth "${CHISEL_AUTH}" \
  http://127.0.0.1:8080 \
  R:127.0.0.1:1080:socks \
  R:127.0.0.1:8445:192.168.10.20:445
```

## Limites e trade-offs
Olhe o cuidado essencial de segurança ao usar **`R:` (Reverse Port Forwarding)** em um servidor de auditoria na nuvem (VPS): se você escrever apenas `R:1080:socks` (sem especificar `127.0.0.1`), como `local-interface` tem como padrão `0.0.0.0`, o `chisel server` abrirá a porta `1080` do SOCKS5 **para toda a internet pública (`0.0.0.0:1080`) sem senha**! Especifique **SEMPRE `R:127.0.0.1:1080:socks`** para que o proxy reverso escute exclusivamente em `localhost` no servidor!

## Como verificar
Note também que você pode passar **quantos `<remote>` quiser em um único comando `chisel client`** (como no exemplo acima, que abre simultaneamente o `R:127.0.0.1:1080:socks` e o port forward SMB `R:127.0.0.1:8445:192.168.10.20:445` dentro da mesma conexão WebSocket!).

## Conexões
- [[chisel-autenticacao-seguranca-keygen-keyfile-fingerprint-authfile-regex]] — Veja também: Blindando o Chisel Contra MITM e Acesso Não Autorizado: **`--keygen` / `--keyfile`**, Pinning de **`--fingerprint`** e Controle de Acesso **`--authfile` (`users.json`)**.
- [[chisel-camuflagem-reverse-proxy-backend-tls-letsencrypt-headers]] — Veja também: Camuflagem HTTP (**`--backend` Reverse Proxy**), TLS Nativo (**`--tls-domain` Let's Encrypt / `--tls-cert`**) e Customização de **`--header` / `Host`** no Chisel.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.
- [[sliver-pivoting-portfwd-socks5-pivots-named-pipes-tcp-interno]] — Referência cruzada direta com sliver-pivoting-portfwd-socks5-pivots-named-pipes-tcp-interno.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
