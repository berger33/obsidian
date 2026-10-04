---
id: software.seguranca.tranche15.001497
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

# Captura Remota em Tempo Real via **SSH Pipe para o Wireshark** e Inspeção de **Network Namespaces de Containers (`nsenter -t <PID> -n tcpdump`)**

## Em uma frase
Como inspecionar visualmente no **Wireshark** (na sua estação de trabalho) o tráfego ao vivo de um servidor de produção remoto na nuvem ou de um **Container Kubernetes/Docker *Distroless*** (que não possui `tcpdump` nem shell instalados dentro da imagem do container!), **sem gravar nenhum arquivo `.pcap` no disco do servidor remoto**?

## Por que importa
Veja os dois padrões de engenharia mais elegantes do Linux: **(Padrão 1 — Captura Remota via Pipe SSH `-w -`)**: você roda via SSH `tcpdump -i eth0 -U -s0 -w - 'not port 22'` (onde `-w -` escreve o fluxo binário `.pcap` diretamente no `stdout` com flush por pacote `-U` e `'not port 22'` exclui a própria conexão SSH para não causar loop infinito!) e canaliza por pipe `|` direto para `wireshark -k -i -` (ou `tshark -r -`) na sua máquina local!

## Como funciona
E **(Padrão 2 — Captura no Namespace de Rede de um Container Distroless via `nsenter -n`)**: você descobre no host o PID do container (`inspect --format '{{.State.Pid}}'`) e executa no host **`nsenter -t <PID> -n tcpdump -i eth0 -nn`**!

## Exemplo
```bash
# Capturar o trafego de dentro do Network Namespace de um container Distroless usando o binario tcpdump do proprio host via nsenter -n
CONTAINER_PID="$(docker inspect -f '{{.State.Pid}}' meu-container-app 2>/dev/null || echo 1)"
nsenter -t "${CONTAINER_PID}" -n tcpdump -i any -nn -c 20 'not port 22'
```

## Limites e trade-offs
Entenda por que o **`nsenter -t ${CONTAINER_PID} -n tcpdump ...`** acima é uma técnica indispensável para DevSecOps e resposta a incidentes em Kubernetes/Docker: **(1)** Suas imagens de container de produção continuam **100% enxutas e seguras (sem `tcpdump`, sem `CAP_NET_RAW` e sem shell dentro do container!)**, e **(2)** O comando `nsenter -n` entra **apenas no Network Namespace (`netns`)** do container mantendo o Mount Namespace do host — usando o binário `/usr/sbin/tcpdump` já instalado no nó host para enxergar exclusivamente a interface `eth0` e `lo` daquele Pod/container!

## Como verificar
E no **Padrão 1 (SSH Pipe)**, lembre-se sempre de filtrar a porta exata do seu próprio túnel SSH (`'not port 22'` ou `'not (host $SSH_CLIENT and port 22)'`)!

## Conexões
- [[tcpdump-diagnostico-redes-modernas-any-vlan-vxlan-geneve-icmp-mtu]] — Veja também: Diagnóstico de Redes Cloud e Containers com `tcpdump`: Interface **`-i any` (`SLL2`)**, Tags **VLAN (`vlan`)**, Túneis Overlay (**`vxlan` / `geneve`**) e Problemas de **MTU (`icmp[0] == 3 and icmp[1] == 4`)**.
- [[tcpdump-otimizacao-alta-velocidade-snaplen-s-buffer-b-timestamps-nano]] — Veja também: Otimização de Captura em Alta Velocidade e Precisão de Tempo no `tcpdump`: **`snaplen` (`-s`)**, Buffer do Kernel (**`-B`**), Precisão **Nanossegundos (`--nano`)** e Bytecode **`-d`**.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.
- [[tcpdump-inspecao-payload-ascii-hex-a-x-xx-linhas-buffered-l-pipes]] — Referência cruzada direta com tcpdump-inspecao-payload-ascii-hex-a-x-xx-linhas-buffered-l-pipes.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
