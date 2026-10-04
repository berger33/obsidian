---
id: software.seguranca.tranche15.001492
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

# Dominando as Primitivas de Filtro **BPF (`pcap-filter(7)`)** no `tcpdump`: Qualificadores de Tipo (`host`, `net`, `port`, `portrange`), Direção (`src`, `dst`) e Protocolo (`tcp`, `udp`, `icmp`, `ether`)

## Em uma frase
Como estruturar filtros **BPF (`pcap-filter`)** precisos no `tcpdump` combinando **Qualificadores de Tipo, Direção e Protocolo** com operadores booleanos (`and`/`&&`, `or`/`||`, `not`/`!`) e parênteses para isolar exatamente o tráfego suspeito em segundos?

## Por que importa
Toda primitiva BPF é formada por um identificador precedido por três categorias de qualificadores: **(1) `Type` (O que é o identificador)**: `host 10.0.0.5`, `net 192.168.0.0/16`, `port 443` ou `portrange 8000-8080`; **(2) `Dir` (Qual direção)**: `src`, `dst`, `src or dst` (padrão) ou `src and dst`; e **(3) `Proto` (Qual protocolo)**: `ether`, `arp`, `ip`, `ip6`, `icmp`, `tcp`, `udp`!

## Como funciona
Além dos filtros dentro da expressão BPF, a manpage `tcpdump(1)` destaca a flag de nível de socket **`-Q in|out|inout` (`--direction`)**: por exemplo, `-Q out` captura exclusivamente pacotes que **estão saindo da máquina local**, enquanto `-Q in` captura apenas pacotes que **estão entrando da rede**!

## Exemplo
```bash
# Filtrar conexoes de saida (-Q out) de uma sub-rede interna para qualquer IP externo nas portas 80, 443 ou 8080-8090 excluindo o jump host de gerencia
tcpdump -i eth0 -nn -Q out \
  'src net 10.20.0.0/16 and not dst net 10.0.0.0/8 and tcp and (dst port 80 or dst port 443 or dst portrange 8080-8090) and not host 10.20.0.5'
```

## Limites e trade-offs
Dica prática de sintaxe BPF: **SEMPRE coloque toda a expressão BPF entre aspas simples (`'...'`)** na linha de comando! Por quê? Porque sem aspas simples, o shell Bash interpreta os parênteses `( ... )` como abertura de subshell e o caractere `!` como expansão de histórico do Bash, quebrando o comando!

## Como verificar
E se a sua expressão BPF de exclusão de ruído tiver 20 linhas de sub-redes e portas conhecidas? Em vez de digitá-la na linha de comando, salve a expressão em um arquivo `filtro_caca.bpf` e passe **`tcpdump -nn -i eth0 -F ./filtro_caca.bpf`**!

## Conexões
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Veja também: Arquitetura do **`tcpdump` e `libpcap` (`the-tcpdump-group/tcpdump`)**: Filtragem **BPF (*Berkeley Packet Filter*) no Kernel**, `AF_PACKET` e Flags Essenciais (`-nn`, `-i`, `-s0`, `-v`).
- [[tcpdump-aritmetica-bytes-cabecalhos-tcpflags-offsets-filtros-cirurgicos]] — Veja também: Filtros BPF Cirúrgicos por **Offset de Bytes (`proto[expr:size]`)** e **Flags TCP (`tcp[tcpflags]`)** no `tcpdump`: Caçando `SYN` Puros, `RST`, Scans `Xmas`/`Null` e `HTTP GET/POST`.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
