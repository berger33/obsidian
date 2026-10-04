---
id: software.seguranca.tranche13.001275
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/netblue30/firejail/master/README.md", "https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Isolamento de Rede no Firejail: **`--net=none`**, Interfaces Virtuais **`veth` (`--net=eth0` / `br0`)**, Firewall Interno **`--netfilter`** e **`--protocol`**

## Em uma frase
Quantas ferramentas locais (leitores de PDF, editores de imagem como GIMP/Inkscape, reprodutores de vídeo, calculadoras, visualizadores de Markdown ou ferramentas de engenharia reversa como Ghidra/Radare2) **não têm nenhuma razão legítima para abrir conexões de rede com a Internet**?

## Por que importa
Para qualquer aplicação que deve operar 100% offline, o Firejail oferece duas barreiras instantâneas: **(1) `--net=none`** — cria um **Network Namespace** novo contendo **apenas uma interface de loopback (`lo`) desconectada do mundo externo**, tornando fisicamente impossível para a aplicação enviar ou receber qualquer pacote de rede!; e **(2) `protocol unix`** — restringe a syscall `socket(2)` via `seccomp-bpf` para permitir apenas sockets locais `AF_UNIX`, bloqueando a própria criação de sockets `AF_INET` (IPv4), `AF_INET6` (IPv6), `AF_PACKET` e `AF_NETLINK` no Kernel!

## Como funciona
E quando a aplicação **precisa** de rede (por exemplo, um daemon web de teste ou navegador), passar **`--net=eth0`** (ou `--net=br0`) cria um par de interfaces virtuais Ethernet (`veth` / `macvlan`) com sua própria pilha TCP/IP isolada, endereço IP próprio (`--ip=192.168.1.200` ou DHCP) e seu próprio firewall **`--netfilter=/etc/firejail/webserver.net`** exclusivo dentro da sandbox!

## Exemplo
```bash
# Executar uma ferramenta de analise ou leitor de documentos com Network Namespace 100% desconectado da rede (--net=none) e auditar estatisticas
firejail --net=none --private ./analisador_binario_local ./amostra.bin
firejail --netstats
```

## Limites e trade-offs
O comando **`firejail --netstats`** monitora em tempo real a taxa de transferência (`RX` / `TX` em KB/s) de todas as sandboxes que utilizam namespaces de rede (`--net=...`) no host!

## Como verificar
Ao analisar documentos suspeitos (PDFs, documentos Office no LibreOffice) ou testar scripts desconhecidos, rodar com **`firejail --net=none --private`** garante que nenhum *beacon*, *canary token* remoto ou exfiltração de dados consiga sair da máquina!

## Conexões
- [[firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs]] — Veja também: Redução de Superfície de Ataque do Kernel no Firejail: **`--seccomp`**, **`--caps.drop=all`**, **`--nonewprivs`** e **`--noroot` (User Namespace)**.
- [[firejail-isolamento-grafico-x11-xephyr-xvfb-xpra-wayland-dbus]] — Veja também: Protegendo o Servidor Gráfico e o Barramento IPC no Firejail: Isolamento de **X11 (`--x11=xephyr`/`xpra`)**, **Wayland** e Filtragem de **D-Bus (`--dbus-user`)**.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Referência cruzada direta com firejail-isolamento-filesystem-private-private-dev-private-etc-bin.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
