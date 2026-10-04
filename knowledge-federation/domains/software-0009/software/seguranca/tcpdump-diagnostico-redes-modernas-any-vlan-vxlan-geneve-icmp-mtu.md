---
id: software.seguranca.tranche15.001496
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md", "https://www.tcpdump.org/manpages/tcpdump.1.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Diagnóstico de Redes Cloud e Containers com `tcpdump`: Interface **`-i any` (`SLL2`)**, Tags **VLAN (`vlan`)**, Túneis Overlay (**`vxlan` / `geneve`**) e Problemas de **MTU (`icmp[0] == 3 and icmp[1] == 4`)**

## Em uma frase
Em servidores Linux que hospedam múltiplos containers (**Docker / Podman**), nós **Kubernetes (Cilium / Calico VXLAN / Geneve)** ou múltiplas VLANs e túneis VPN (**WireGuard `wg0` / strongSwan XFRM**), você muitas vezes não sabe por qual das 20 interfaces virtuais (`veth*`, `cni0`, `eth0`, `wg0`) um pacote está entrando ou sendo descartado!

## Por que importa
Como descobrir por qual interface exatamente o pacote passa e como filtrar tráfego encapsulado em **VLAN 802.1Q** ou **VXLAN** no `tcpdump`?

## Como funciona
Primeiro: nas versões modernas (`tcpdump 4.99+` com `libpcap 1.10+`), quando você captura na pseudo-interface **`tcpdump -i any -nn`**, o Linux usa o cabeçalho **`LINUX_SLL2`** que **imprime o nome exato da interface de rede (`eth0 In`, `veth4a2b Out`, `wg0 Out`) em cada linha de pacote**, permitindo seguir um pacote entrando pela `eth0`, passando pelo roteamento/NAT e saindo pela `veth` do container em uma única tela! Segundo: cuidado com a primitiva **`vlan`** no BPF — quando você escreve `'vlan 100 and host 10.0.0.5'`, a palavra `vlan` **desloca o ponteiro de offsets BPF em 4 bytes para todas as expressões que vêm à direita dela**!

## Exemplo
```bash
# Rastrear um pacote atravessando multiplas interfaces do host/containers (-i any), filtrar dentro de uma VLAN 802.1Q e detectar bloqueio de Path MTU Discovery
tcpdump -i any -nn 'icmp or port 8080'
tcpdump -i eth0 -nn -e 'vlan 100 and host 10.20.30.40'
tcpdump -i any -nn 'icmp and icmp[0] == 3 and icmp[1] == 4'
```

## Limites e trade-offs
Olhe a terceira linha de diagnóstico acima (**`tcpdump -i any -nn 'icmp and icmp[0] == 3 and icmp[1] == 4'`** — ou para IPv6 `'icmp6 and ip6[40] == 2'` *Packet Too Big*): ela captura pacotes **ICMP Destination Unreachable — Fragmentation Needed and DF Set (`Type 3, Code 4`)**! Quando conexões TLS ou transferências grandes sobre túneis VPN/VXLAN travam misteriosamente após o `ClientHello`, 90% das vezes é um problema de **Path MTU Discovery Blackhole**, diagnosticado em segundos com esse filtro!

## Como verificar
Para decodificar pacotes dentro de túneis **VXLAN (UDP porta 4789)** ou forçar a interpretação de uma porta não-padrão como um protocolo conhecido (ex.: `vxlan`, `radius`, `snmp`, `rpc`), use a flag **`-T <tipo>`** do `tcpdump`!

## Conexões
- [[tcpdump-inspecao-payload-ascii-hex-a-x-xx-linhas-buffered-l-pipes]] — Veja também: Inspeção de Payload em Tempo Real (**`-A` ASCII**, **`-X` / `-XX` Hex+ASCII**) e Streaming Line-Buffered (**`-l` / `--immediate-mode`**) para Pipes Unix no `tcpdump`.
- [[tcpdump-captura-remota-ssh-pipes-wireshark-containers-netns-nsenter]] — Veja também: Captura Remota em Tempo Real via **SSH Pipe para o Wireshark** e Inspeção de **Network Namespaces de Containers (`nsenter -t <PID> -n tcpdump`)**.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.
- [[tcpdump-primitivas-filtros-bpf-host-net-port-portrange-proto-logica]] — Referência cruzada direta com tcpdump-primitivas-filtros-bpf-host-net-port-portrange-proto-logica.
- [[strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump]] — Referência cruzada direta com strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
