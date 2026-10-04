---
id: software.seguranca.tranche16.001557
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

# Double Pivoting (Encadeamento Multi-Hop de Túneis Chisel) e Integração com **`proxychains4` (`proxychains-ng`)** para Segmentos Isolados

## Em uma frase
Durante um Pentest Interno em uma infraestrutura industrial ou bancária com múltiplas camadas de firewall (`Estação do Auditor -> Rede DMZ (10.10.0.0/24) -> Rede Interna (172.16.0.0/24) -> Rede de Bancos (192.168.50.0/24)`), como encadear o **Chisel** através de dois ou mais saltos (*Multi-Hop / Double Pivoting*) quando a Rede de Bancos só é acessível a partir da Rede Interna?

## Por que importa
Existem duas formas limpas no Chisel: **(Forma 1 — Encadeamento de Port Forward Reverso + SOCKS Reverso)**: no `Host 1 (DMZ)`, você já tem um túnel `R:127.0.0.1:1080:socks` conectado ao seu `chisel server` e abre também um encaminhamento reverso ou local que expõe a porta do `chisel server` dentro do `Host 1`; o `Host 2 (Rede Interna)` conecta seu `chisel client` na porta do `Host 1` abrindo um segundo SOCKS **`R:127.0.0.1:1081:socks`** direto na máquina do auditor!

## Como funciona
Ou **(Forma 2 — `dynamic_chain` / `strict_chain` no `/etc/proxychains4.conf`)**, empilhando `socks5 127.0.0.1 1080` e `socks5 127.0.0.1 1081`!

## Exemplo
```bash
# Executar o NetExec (nxc) ou Nmap (-sT -Pn) atraves de um tunel SOCKS5 reverso do Chisel usando proxychains4 (-q modo silencioso)
proxychains4 -q nxc smb 192.168.50.10 -u auditor -p "${SENHA_TESTE}" --shares
proxychains4 -q nmap -sT -Pn -n -p 22,80,443,445,3389 192.168.50.10
```

## Limites e trade-offs
Por que ao rodar o **`nmap`** através de um proxy SOCKS5 do Chisel com `proxychains4` você **SEMPRE deve passar as flags `-sT` (*TCP Connect Scan*) e `-Pn` (*Skip Ping Discovery*)**? Porque o protocolo SOCKS5 opera na Camada 5 (Sessão) transportando fluxos TCP completos (`connect()`) e UDP — ele **não transporta pacotes `ICMP Echo` brutos nem `Raw Sockets` de meio-handshake `SYN` (`-sS`)**! Sem `-sT -Pn`, o Nmap tentará mandar um ping ICMP fora do proxy, achará que o host está desligado e abortará!

## Como verificar
E como veremos no próximo grupo desta Tranche (`1561–1570`), quando você quiser rodar o `nmap` direto na tabela de roteamento da sua máquina **sem precisar de `proxychains4` e suportando ICMP**, a alternativa moderna de Camada 3 é o **Ligolo-ng (`TUN` + `Gvisor`)**!

## Conexões
- [[chisel-operacao-sinais-unix-sigusr2-sighup-sigint-tuning-keepalive]] — Veja também: Operação e Diagnóstico em Tempo de Execução no Chisel: Sinais Unix (**`SIGUSR2` Stats**, **`SIGHUP` Reconnect**, **`SIGINT`/`SIGTERM`**) e Tuning de Backoff.
- [[chisel-uso-defensivo-acesso-remoto-zero-trust-containers-k8s-dev]] — Veja também: Uso Legítimo de Engenharia e DevSecOps do Chisel: Túneis Seguros de Diagnóstico em **Containers (`ghcr.io/jpillora/chisel`)** e Ambientes Cloud.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Referência cruzada direta com chisel-encaminhamento-portas-forward-reverse-r-socks5-udp.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
