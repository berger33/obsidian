---
id: software.seguranca.tranche15.001491
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

# Arquitetura do **`tcpdump` e `libpcap` (`the-tcpdump-group/tcpdump`)**: Filtragem **BPF (*Berkeley Packet Filter*) no Kernel**, `AF_PACKET` e Flags Essenciais (`-nn`, `-i`, `-s0`, `-v`)

## Em uma frase
Presente em praticamente todo servidor Linux, BSD, macOS e appliance de segurança do planeta, como o **`tcpdump`** (em conjunto com a biblioteca **`libpcap`**) consegue filtrar um link de 10 Gbps procurando os pacotes de um único IP sem consumir quase nada de CPU em espaço de usuário?

## Por que importa
Porque a expressão de filtro passada ao `tcpdump` (ex.: `'host 192.0.2.10 and tcp port 443'`) **NÃO é avaliada em espaço de usuário pelo processo `tcpdump`**! A biblioteca `libpcap` compila a expressão em **Bytecode BPF (*Berkeley Packet Filter*)** e o injeta diretamente no **Kernel do sistema operacional (`SO_ATTACH_FILTER` no socket `AF_PACKET` / `TPACKET_V3`)**!

## Como funciona
Assim, o Kernel avalia o filtro BPF logo na chegada do pacote no buffer da placa de rede (muitas vezes compilado para instruções nativas da CPU pelo **BPF JIT Compiler** do Kernel!) e **descarta 99,99% dos pacotes que não batem com o filtro antes mesmo de copiá-los para a memória de espaço de usuário do `tcpdump`**!

## Exemplo
```bash
# Capturar pacotes na interface eth0 sem resolver DNS/portas (-nn), mostrando enderecos MAC (-e), tamanho completo (-s0) e estatisticas detalhadas (-v)
tcpdump --version
tcpdump -i eth0 -nn -e -s0 -v -c 10 'tcp port 443'
```

## Limites e trade-offs
Por que todo engenheiro de redes e de resposta a incidentes **SEMPRE inclui a flag `-nn` (duplo `-n`)** ao rodar o `tcpdump` em produção ou durante um incidente de segurança? Porque sem `-n`, o `tcpdump` tenta fazer uma consulta **DNS Reversa (`PTR`)** para cada endereço IP visto no pacote: **(1)** Isso trava a saída na tela se o DNS estiver lento, **(2)** Polui a própria captura de pacotes com centenas de consultas DNS geradas pelo próprio `tcpdump` e **(3) Em uma investigação de malware/C2, fazer uma consulta PTR pode alertar o servidor DNS autoritativo do atacante de que um analista está investigando o IP dele (falha grave de OPSEC)**!

## Como verificar
Ao encerrar o `tcpdump` (ou ao enviar o sinal `SIGUSR1` no Linux / `SIGINFO` `Ctrl+T` no BSD/macOS sem parar a captura!), observe sempre as 3 métricas finais documentadas na manpage oficial: `packets captured`, `packets received by filter` e **`packets dropped by kernel`** (se `dropped by kernel > 0`, aumente o buffer do kernel com **`-B 16384`**!).

## Conexões
- [[tcpdump-primitivas-filtros-bpf-host-net-port-portrange-proto-logica]] — Veja também: Dominando as Primitivas de Filtro **BPF (`pcap-filter(7)`)** no `tcpdump`: Qualificadores de Tipo (`host`, `net`, `port`, `portrange`), Direção (`src`, `dst`) e Protocolo (`tcp`, `udp`, `icmp`, `ether`).
- [[tcpdump-aritmetica-bytes-cabecalhos-tcpflags-offsets-filtros-cirurgicos]] — Referência cruzada direta com tcpdump-aritmetica-bytes-cabecalhos-tcpflags-offsets-filtros-cirurgicos.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
