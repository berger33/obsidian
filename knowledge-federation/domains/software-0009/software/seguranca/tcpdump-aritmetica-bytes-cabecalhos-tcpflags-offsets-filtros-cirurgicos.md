---
id: software.seguranca.tranche15.001493
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

# Filtros BPF Cirúrgicos por **Offset de Bytes (`proto[expr:size]`)** e **Flags TCP (`tcp[tcpflags]`)** no `tcpdump`: Caçando `SYN` Puros, `RST`, Scans `Xmas`/`Null` e `HTTP GET/POST`

## Em uma frase
Como o motor BPF do `tcpdump` permite inspecionar **qualquer byte ou bit exato dentro do cabeçalho IP, TCP, UDP ou ICMP** em velocidade de Kernel usando a sintaxe **`proto[offset : tamanho]`**?

## Por que importa
No cabeçalho TCP (RFC 793), o byte de deslocamento **`13` (`tcp[13]` ou constante simbólica `tcp[tcpflags]`)** contém as **Flags de Controle TCP** (`CWR | ECE | URG | ACK | PSH | RST | SYN | FIN`). O `pcap-filter` já fornece as constantes simbólicas prontas: **`tcp-fin` (`0x01`)**, **`tcp-syn` (`0x02`)**, **`tcp-rst` (`0x04`)**, **`tcp-push` (`0x08`)**, **`tcp-ack` (`0x10`)** e **`tcp-urg` (`0x20`)**!

## Como funciona
Veja a diferença crucial ao usar máscaras de bits (`&`): **(1) `'tcp[tcpflags] == tcp-syn'`** captura pacotes que têm **APENAS o bit `SYN` ligado e nenhum outro bit** (início de nova conexão ou SYN Scan, excluindo respostas `SYN+ACK`!); já **(2) `'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'`** captura qualquer pacote que tenha `SYN` **OU** `FIN` ligado (mesmo que `ACK` também esteja ligado)!

## Exemplo
```bash
# Capturar apenas pacotes de inicio de conexao (SYN puro sem ACK), pacotes de anomalia/scan (SYN+FIN simultaneo) ou requisicoes HTTP 'GET ' no payload
tcpdump -i eth0 -nn 'tcp[tcpflags] == tcp-syn'
tcpdump -i eth0 -nn 'tcp[tcpflags] & (tcp-syn|tcp-fin) == (tcp-syn|tcp-fin)'
tcpdump -i eth0 -nn -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'
```

## Limites e trade-offs
Entenda a aritmética genial da terceira linha acima (**`'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'`**): como o cabeçalho TCP tem tamanho variável (20 bytes sem opções, ou 32/40 bytes com opções Timestamp/SACK), onde começa o payload HTTP? Os 4 bits superiores do byte 12 do TCP (`tcp[12:1] & 0xf0`) contêm o *Data Offset* em palavras de 32 bits (4 bytes); deslocar 2 bits para a direita (`>> 2`) equivale a dividir por 16 e multiplicar por 4, dando o **offset exato onde começa o payload HTTP**, e `0x47455420` é `"GET "` em ASCII hexadecimal!

## Como verificar
Veja também como detectar instantaneamente em BPF scans furtivos do Nmap: **Null Scan (`'tcp[tcpflags] == 0'`)** e **Xmas Scan (`'tcp[tcpflags] & (tcp-fin|tcp-push|tcp-urg) == (tcp-fin|tcp-push|tcp-urg)'`)**!

## Conexões
- [[tcpdump-primitivas-filtros-bpf-host-net-port-portrange-proto-logica]] — Veja também: Dominando as Primitivas de Filtro **BPF (`pcap-filter(7)`)** no `tcpdump`: Qualificadores de Tipo (`host`, `net`, `port`, `portrange`), Direção (`src`, `dst`) e Protocolo (`tcp`, `udp`, `icmp`, `ether`).
- [[tcpdump-gravacao-rotacao-ring-buffer-pcap-c-g-w-z-pos-processamento]] — Veja também: Gravação Contínua de Pacotes em Disco (**Ring Buffer de Rotação**: `-w`, `-C`, `-G`, `-W`, `-z`) e Flush Imediato (`-U` / `SIGUSR2`) no `tcpdump`.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.
- [[scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas]] — Referência cruzada direta com scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
