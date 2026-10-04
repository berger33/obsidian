---
id: software.seguranca.tranche16.001561
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

# Arquitetura do **Ligolo-ng (`nicocha30/ligolo-ng`)**: Tunelamento de **Camada 3 (VPN-like)** com Interface **`TUN`** no Proxy e Pilha TCP/IP Userland (**Google `gVisor`**) no Agente

## Em uma frase
Por que o **Ligolo-ng (`nicocha30/ligolo-ng`)** revolucionou o *Pivoting* em exercícios de Red Team e testes de intrusão em redes internas, superando a lentidão e as limitações de proxies **SOCKS5 (`proxychains4`)** a ponto de atingir mais de **100 Mbits/s** no `iperf3`?

## Por que importa
Conforme explicado na seção *How is this different from Ligolo/Chisel/Meterpreter...* do `README.md` oficial, o Ligolo-ng **NÃO usa SOCKS nem encaminhamento porta-a-porta**: **(1) No Servidor Proxy (`proxy`, a máquina do auditor)**, ele cria uma placa de rede virtual de Camada 3 (**Interface `TUN`**, ex.: `ligolo` ou `utun4` no macOS / `wintun.dll` no Windows), de modo que o Kernel do auditor roteia pacotes IP nativamente pela tabela de rotas (`ip route`) sem precisar de `proxychains`!

## Como funciona
**(2) No Agente (`agent`, rodando na máquina alvo comprometida SEM privilégios de root/Admin!)**, o Ligolo-ng embarca a pilha de rede em espaço de usuário **Google `gVisor` (`netstack`)**: quando um pacote IP/TCP/UDP/ICMP chega pelo túnel TLS multiplexado, o `gVisor` dentro do `agent` traduz o pacote IP em chamadas de sistema de usuário (`connect()`, `sendto()`, ping) na rede interna do alvo!

## Exemplo
```bash
# Criar a interface TUN e rota diretamente pelo console do Ligolo-ng (>= v0.6+) ou via iproute2 no Linux do servidor Proxy
ip tuntap add user "$(whoami)" mode tun ligolo
ip link set ligolo up
ip route add 192.168.20.0/24 dev ligolo
```

## Limites e trade-offs
Entenda a mágica de o **`agent` NÃO exigir privilégios de `root` ou `Administrator`** na máquina alvo enquanto oferece uma interface `TUN` completa na máquina do auditor: como no alvo o `agent` usa o **`gVisor`** para converter o pacote `SYN` recebido da `TUN` em uma syscall normal `connect()` de espaço de usuário (devolvendo `SYN-ACK` na `TUN` se o `connect()` funcionar, `RST` se receber `ECONNREFUSED`, ou silêncio se der timeout), **qualquer conta de usuário restrita (`www-data`, `iis apppool`, usuário comum do AD) consegue abrir um túnel de sub-rede inteira**!

## Como verificar
Além disso, como a sua estação de trabalho enxerga a sub-rede remota como uma rota IP normal (`192.168.20.0/24 dev ligolo`), ferramentas que não funcionam bem com `proxychains` (como scanners UDP, **Nmap**, **NetExec**, **Impacket**, **Certipy**, **BloodHound**, `rdesktop`/`xfreerdp` e scripts Go/Python) funcionam **nativamente na velocidade da placa de rede**!

## Conexões
- [[ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning]] — Veja também: Segurança Criptográfica do Túnel Ligolo-ng: **Let's Encrypt (`-autocert`)**, Certificados Próprios (`-certfile`) e Pinning de **SHA-256 Fingerprint (`-selfcert` + `-accept-fingerprint`)**.
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Referência cruzada direta com ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
