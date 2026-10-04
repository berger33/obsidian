---
id: software.seguranca.tranche16.001556
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

# Operação e Diagnóstico em Tempo de Execução no Chisel: Sinais Unix (**`SIGUSR2` Stats**, **`SIGHUP` Reconnect**, **`SIGINT`/`SIGTERM`**) e Tuning de Backoff

## Em uma frase
Quando um túnel `chisel client` ou `chisel server` está rodando em background (ou como serviço systemd com `--pid`) há vários dias, como inspecionar as estatísticas de uso de memória/goroutines do processo ao vivo ou forçar o cliente a reconectar imediatamente sem precisar matar e reiniciar o processo?

## Por que importa
Conforme documentado diretamente na constante `signalsTemplate` em `main.go`, o processo `chisel` escuta três sinais Unix especiais em tempo de execução: **(1) `SIGUSR2`** — imprime no log as **estatísticas de processo em tempo real (`cos.GoStats()`: uso de memória RAM, número de Goroutines ativas e GC)**!.

## Como funciona
**(2) `SIGHUP`** — **curto-circuita imediatamente o temporizador de espera de reconexão (*reconnect backoff timer*)** do cliente, forçando uma tentativa de reconexão instantânea!; e **(3) `SIGINT` / `SIGTERM`** — inicia um **Graceful Shutdown** (enquanto um segundo sinal força a saída imediata)!

## Exemplo
```bash
# Enviar SIGUSR2 para imprimir estatisticas de memoria/goroutines em tempo real e SIGHUP para forcar reconexao imediata do chisel client
kill -USR2 "$(cat ./chisel.pid)"
kill -HUP "$(pidof chisel)"
```

## Limites e trade-offs
Veja também como ajustar os parâmetros de resiliência do `chisel client` para links instáveis (como conexões móveis 4G/5G ou satelitais): use **`--keepalive 20s`** (para enviar um ping SSH a cada 20 segundos evitando que firewalls estaduais derrubem a sessão TCP por ociosidade), **`--max-retry-count`** (padrão infinito) e **`--max-retry-interval 1m`** (para que o backoff exponencial nunca espere mais de 1 minuto entre tentativas)!

## Como verificar
O sinal `SIGHUP` é especialmente útil em scripts de `NetworkManager dispatcher` (ou hooks de VPN): assim que a interface Wi-Fi ou VPN do notebook volta a ficar online, um `pkill -HUP chisel` reconecta todos os túneis no mesmo segundo sem esperar o timer de 5 minutos do backoff exponencial!

## Conexões
- [[chisel-atravessando-proxies-corporativos-socks-http-connect-stdio-ssh]] — Veja também: Atravessando Proxies de Saída Corporativos (**`--proxy` HTTP CONNECT / SOCKS5**) e **SSH sobre HTTP (`stdio:` + `ssh -o ProxyCommand`)** com o Chisel.
- [[chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap]] — Veja também: Double Pivoting (Encadeamento Multi-Hop de Túneis Chisel) e Integração com **`proxychains4` (`proxychains-ng`)** para Segmentos Isolados.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Referência cruzada direta com chisel-encaminhamento-portas-forward-reverse-r-socks5-udp.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
