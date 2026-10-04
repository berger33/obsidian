---
id: software.seguranca.tranche15.001494
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

# Gravação Contínua de Pacotes em Disco (**Ring Buffer de Rotação**: `-w`, `-C`, `-G`, `-W`, `-z`) e Flush Imediato (`-U` / `SIGUSR2`) no `tcpdump`

## Em uma frase
Se você executar simplesmente `tcpdump -i eth0 -w captura.pcap` em um servidor de produção para tentar capturar um bug ou ataque intermitente que acontece uma vez por dia, o arquivo `captura.pcap` crescerá sem parar até **encher 100% da partição do disco e derrubar o servidor**!

## Por que importa
Como configurar o `tcpdump` para operar como um **Gravador de Caixa-Preta Contínuo (*Ring Buffer de Disco*)** que nunca consome mais do que um limite fixo de Gigabytes?

## Como funciona
Combinando as flags **`-w`** (arquivo de saída), **`-C <tamanho>`** (rotaciona o arquivo a cada N milhões de bytes, ou sufixos `k`/`m`/`g` nas versões modernas: `-C 100m`), **`-W <quantidade>`** (mantém no máximo `W` arquivos numerados em disco, **sobrescrevendo o mais antigo em anel circular FIFO**!), **`-G <segundos>`** (rotaciona por tempo com strftime `%Y%m%d-%H%M%S.pcap`) e **`-z <comando>`** (executa `gzip`, `zstd` ou um script em background assim que cada arquivo fecha)!

## Exemplo
```bash
# Gravar um Ring Buffer continuo de no maximo 10 arquivos de 100 MB cada (teto maximo de 1 GB em disco) com flush imediato por pacote (-U)
tcpdump -i eth0 -nn -s0 -U \
  -C 100 -W 10 \
  -w /var/tmp/ring_captura.pcap \
  'not port 22'
```

## Limites e trade-offs
Preste muita atenção a um problema clássico de permissão de segurança (`AppArmor` / `SELinux` / `-Z user`) quando você usa **`-C` / `-G` / `-W`** no `tcpdump`: após abrir a placa de rede, o `tcpdump` abandona os privilégios de `root` mudando para o usuário não-privilegiado **`tcpdump` (`-Z tcpdump`)** ANTES de criar o primeiro arquivo! Portanto, **o diretório de destino (`/var/tmp/` ou uma pasta `/data/pcap/` com `chown tcpdump:tcpdump`) DEVE ter permissão de escrita para o usuário `tcpdump`**, caso contrário o `tcpdump` falhará com `Permission denied` ao tentar criar o arquivo ou rotacionar para o arquivo `ring_captura.pcap1`!

## Como verificar
E para scripts ou análises em tempo real onde você quer ler o `.pcap` enquanto ele ainda está sendo gravado, passe **`-U`** (*packet-buffered output*, que faz flush no arquivo a cada pacote) ou envie **`kill -USR2 $(pidof tcpdump)`** para forçar o flush do buffer!

## Conexões
- [[tcpdump-aritmetica-bytes-cabecalhos-tcpflags-offsets-filtros-cirurgicos]] — Veja também: Filtros BPF Cirúrgicos por **Offset de Bytes (`proto[expr:size]`)** e **Flags TCP (`tcp[tcpflags]`)** no `tcpdump`: Caçando `SYN` Puros, `RST`, Scans `Xmas`/`Null` e `HTTP GET/POST`.
- [[tcpdump-inspecao-payload-ascii-hex-a-x-xx-linhas-buffered-l-pipes]] — Veja também: Inspeção de Payload em Tempo Real (**`-A` ASCII**, **`-X` / `-XX` Hex+ASCII**) e Streaming Line-Buffered (**`-l` / `--immediate-mode`**) para Pipes Unix no `tcpdump`.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.
- [[tcpdump-seguranca-privilegios-drop-root-z-chroot-apparmor-capabilities]] — Referência cruzada direta com tcpdump-seguranca-privilegios-drop-root-z-chroot-apparmor-capabilities.
- [[arkime-configuracao-config-ini-tiered-pcapdir-freespaceg-rotacao]] — Referência cruzada direta com arkime-configuracao-config-ini-tiered-pcapdir-freespaceg-rotacao.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
