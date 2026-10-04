---
id: software.seguranca.tranche16.001551
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

# Arquitetura do **Chisel (`jpillora/chisel`)**: Tunelamento Rápido **TCP e UDP** Encapsulado sobre **HTTP / WebSockets** e Criptografado via **SSH (`crypto/ssh`)**

## Em uma frase
Como o **Chisel (`jpillora/chisel`)** consegue transportar múltiplos túneis **TCP, UDP e SOCKS5** bidirecionais através de firewalls corporativos restritivos e proxies HTTP usando **um único executável portátil em Go** (que funciona tanto como `chisel server` quanto como `chisel client`)?

## Por que importa
Conforme detalhado no `README.md` e no código-fonte `main.go`, a arquitetura do Chisel empilha três camadas com perfeição: **(1) Transporte Externo HTTP -> Upgrade WebSocket (`ws://` ou `wss://`)** — a conexão inicial é uma requisição HTTP padrão (que atravessa firewalls de borda, balanceadores de carga L7, Cloudflare/CDNs e proxies corporativos!).

## Como funciona
**(2) Segurança e Multiplexação Interna via Protocolo SSH (`golang.org/x/crypto/ssh`)** — dentro do WebSocket, o Chisel estabelece uma sessão **SSH criptografada de ponta a ponta** com verificação de impressão digital (*Fingerprint*) da chave ECDSA do servidor e autenticação de cliente; e **(3) Canais SSH Multiplexados** — permitindo abrir dezenas de encaminhamentos de portas TCP, UDP (`/udp`) e SOCKS5 simultâneos sobre **uma única conexão TCP/HTTP**!

## Exemplo
```bash
# Verificar a versao do binario unico do Chisel e inspecionar os modos server e client integrados
chisel --version
chisel --help
chisel server --help
```

## Limites e trade-offs
Olhe que detalhe importante de engenharia: mesmo que você execute o Chisel sobre `http://` puro (sem TLS externo), **todo o tráfego dentro do túnel Chisel JÁ É 100% CRIPTOGRAFADO pelo protocolo SSH (`crypto/ssh`)**! E quando você coloca o `chisel server` atrás de um proxy HTTPS reverso (ou usa `--tls-key` / `--tls-cert` / `--tls-domain`), você ganha **dupla proteção**: TLS externo padrão na porta `443` + SSH interno com chave própria!

## Como verificar
Além disso, como destaca o `README.md`, o cliente Chisel possui **reconexão automática com *Exponential Backoff*** (`--min-retry-interval` / `--max-retry-interval`) e pings de `--keepalive` (padrão `25s` em `main.go`) que detectam conexões mortas por NAT e restabelecem o túnel automaticamente.

## Conexões
- [[chisel-autenticacao-seguranca-keygen-keyfile-fingerprint-authfile-regex]] — Veja também: Blindando o Chisel Contra MITM e Acesso Não Autorizado: **`--keygen` / `--keyfile`**, Pinning de **`--fingerprint`** e Controle de Acesso **`--authfile` (`users.json`)**.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Referência cruzada direta com chisel-encaminhamento-portas-forward-reverse-r-socks5-udp.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
