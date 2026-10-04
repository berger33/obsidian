---
id: software.seguranca.tranche15.001498
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

# Otimização de Captura em Alta Velocidade e Precisão de Tempo no `tcpdump`: **`snaplen` (`-s`)**, Buffer do Kernel (**`-B`**), Precisão **Nanossegundos (`--nano`)** e Bytecode **`-d`**

## Em uma frase
Quando você precisa capturar pacotes em uma interface de 10 Gbps / 25 Gbps sob tráfego intenso sem sofrer **`packets dropped by kernel`** e sem encher o disco em 30 segundos, ou quando precisa medir latência de rede com precisão de **nanossegundos (`--nano`)**, quais parâmetros da manpage `tcpdump(1)` fazem toda a diferença?

## Por que importa
Quatro ajustes técnicos resolvem o problema: **(1) Redução de `snaplen` (`-s 96` ou `-s 128`)** — por padrão (`-s 0` / `262144`), o `tcpdump` copia o pacote inteiro de 1.500 bytes (ou Jumbo Frames de 9.000 bytes!). Se você só precisa analisar os cabeçalhos Ethernet + IP + TCP/UDP (sem o payload da aplicação), passar **`-s 96`** corta cada pacote nos primeiros 96 bytes, **reduzindo em até 93% o volume de escrita em disco e a cópia de memória no kernel** (além de proteger dados sensíveis do payload!); **(2) Aumento do Ring Buffer do Kernel (`-B 32768`, 32 MiB)**.

## Como funciona
**(3) `--nano` e `-j adapter_unsynced`** (timestamps de hardware da placa de rede com precisão de nanossegundos!); e **(4) `-w arquivo.pcap` silencioso** (sem formatar texto na tela durante a captura)!

## Exemplo
```bash
# Inspecionar o bytecode BPF gerado pelo compilador (-d) e capturar cabecalhos (-s 96) com buffer de kernel de 32 MiB (-B 32768) e precisao de nanossegundos
tcpdump -d 'tcp port 443 and (tcp[tcpflags] & tcp-syn != 0)'
tcpdump -i eth0 -nn -s 96 -B 32768 --nano -c 100 -w /var/tmp/cabecalhos_rapidos.pcap
```

## Limites e trade-offs
Veja na primeira linha acima a flag **`-d`** (ou `-dd` para array C e `-ddd` para decimal usado no módulo `xt_bpf` do `iptables`/`nftables`!): ela imprime na tela as instruções assembly exatas da **Máquina Virtual BPF (`ldh`, `jeq`, `ldb`, `jset`, `ret`)** compiladas para a sua expressão — permitindo verificar se o otimizador BPF (`-O`, ativo por padrão) gerou o filtro mais enxuto possível!

## Como verificar
Ao analisar um arquivo `.pcap` já capturado usando `-r`, explore também as flags de formatação de timestamp: **`-tttt`** (imprime a data completa `YYYY-MM-DD HH:MM:SS.frac` em cada linha — essencial para relatórios forenses!), **`-ttt`** (mostra o delta de tempo entre a linha atual e a linha anterior!) e **`-S`** (imprime números de sequência TCP absolutos em vez de relativos)!

## Conexões
- [[tcpdump-captura-remota-ssh-pipes-wireshark-containers-netns-nsenter]] — Veja também: Captura Remota em Tempo Real via **SSH Pipe para o Wireshark** e Inspeção de **Network Namespaces de Containers (`nsenter -t <PID> -n tcpdump`)**.
- [[tcpdump-seguranca-privilegios-drop-root-z-chroot-apparmor-capabilities]] — Veja também: Segurança Operacional do Próprio `tcpdump`: Abandono de Privilégios (**`-Z user`**), Linux Capabilities (**`cap_net_raw,cap_net_admin`**), Perfis **AppArmor** e Flag **`-n` ao Ler PCAPs**.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.
- [[tcpdump-gravacao-rotacao-ring-buffer-pcap-c-g-w-z-pos-processamento]] — Referência cruzada direta com tcpdump-gravacao-rotacao-ring-buffer-pcap-c-g-w-z-pos-processamento.
- [[arkime-otimizacao-captura-alta-velocidade-tpacketv3-snf-dpdk-threads]] — Referência cruzada direta com arkime-otimizacao-captura-alta-velocidade-tpacketv3-snf-dpdk-threads.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
