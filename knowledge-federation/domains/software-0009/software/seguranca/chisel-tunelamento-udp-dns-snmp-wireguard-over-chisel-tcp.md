---
id: software.seguranca.tranche16.001559
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

# Tunelamento de Protocolos **UDP (`<remote>/udp`)** no Chisel: Encapsulando Consultas **DNS (`53/udp`)**, **SNMP (`161/udp`)** ou **WireGuard** sobre HTTP/WebSockets

## Em uma frase
Um desafio clássico em redes corporativas e auditorias de segurança: ferramentas de proxy tradicionais (como `ssh -D` SOCKS ou encaminhamentos TCP `-L`/`-R` do OpenSSH) transportam **apenas pacotes TCP**! Como auditar um servidor **DNS interno (`53/udp`)**, consultar **SNMP (`161/udp`)** ou até mesmo passar um túnel **WireGuard (`51820/udp`)** quando você só tem um túnel HTTP/WebSocket disponível?

## Por que importa
Usando o sufixo **`/udp`** do Chisel (ex.: `1053:10.20.30.53:53/udp` ou reverso `R:127.0.0.1:1053:10.20.30.53:53/udp`)!

## Como funciona
Quando você especifica `/udp` no final de um `<remote>`, o Chisel abre um socket `UDP` local na ponta de entrada, empacota cada datagrama UDP recebido com seu tamanho exato, transmite pelo canal SSH multiplexado dentro do WebSocket TCP até a outra ponta, dispara o datagrama UDP na rede remota e devolve a resposta UDP pelo mesmo canal!

## Exemplo
```bash
# Tunelar a porta UDP 53 de um servidor DNS interno (10.20.30.53:53/udp) para a porta local 1053/udp via Chisel e consultar com dig
chisel client --fingerprint "${SERVER_FP}" --auth "${CHISEL_AUTH}" \
  https://tunel.exemplo.br:443 \
  127.0.0.1:1053:10.20.30.53:53/udp &
dig @127.0.0.1 -p 1053 _ldap._tcp.dc._msdcs.corp.interno SRV +short
```

## Limites e trade-offs
Olhe que solução cirúrgica no comando acima: ao tunelar `10.20.30.53:53/udp` para `127.0.0.1:1053` no seu host local, você pode usar `dig`, `nslookup`, **`dnsx`** ou o resolvedor DNS do sistema diretamente em `127.0.0.1:1053` para enumerar registros `SRV`, `SOA` e zonas do Active Directory interno sobre UDP!

## Como verificar
Lembre-se apenas de que, ao encapsular protocolos de VPN UDP em tempo real (como WireGuard) dentro de um túnel TCP/WebSocket, se houver perda de pacotes na rede externa pode ocorrer o fenômeno conhecido como *TCP-over-TCP / Retransmission Meltdown*; para consultas pontuais como DNS, SNMP, NTP e TFTP sobre `/udp`, o funcionamento é imediato e impecável!

## Conexões
- [[chisel-uso-defensivo-acesso-remoto-zero-trust-containers-k8s-dev]] — Veja também: Uso Legítimo de Engenharia e DevSecOps do Chisel: Túneis Seguros de Diagnóstico em **Containers (`ghcr.io/jpillora/chisel`)** e Ambientes Cloud.
- [[chisel-deteccao-forense-blue-team-websocket-ssh-banner-rita-suricata]] — Veja também: Engenharia de Detecção (**Blue Team / SOC / NIDS**) Contra Túneis **Chisel**: Handshake **WebSocket (`Sec-WebSocket-Protocol: chisel-v3`)**, Banner SSH Interno e **Long Connections**.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Referência cruzada direta com chisel-encaminhamento-portas-forward-reverse-r-socks5-udp.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
