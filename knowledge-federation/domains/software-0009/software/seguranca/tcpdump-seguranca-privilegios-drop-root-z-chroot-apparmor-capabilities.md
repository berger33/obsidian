---
id: software.seguranca.tranche15.001499
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

# Segurança Operacional do Próprio `tcpdump`: Abandono de Privilégios (**`-Z user`**), Linux Capabilities (**`cap_net_raw,cap_net_admin`**), Perfis **AppArmor** e Flag **`-n` ao Ler PCAPs**

## Em uma frase
Por que a própria manpage oficial `tcpdump(1)` alerta que **ler um arquivo `.pcap` capturado por terceiros não requer privilégios de `root` e JAMAIS deve ser executado com `sudo tcpdump -r suspeito.pcap`**?

## Por que importa
Porque quando o `tcpdump` imprime os pacotes na tela (sem `-w`), ele aciona dezenas de **dissecadores de protocolo escritos em C** para interpretar os campos do pacote! Embora o `tcpdump` moderno use abandono automático de privilégios (`-Z tcpdump` + `chroot` ao capturar de uma interface e filtros `seccomp`/AppArmor nas distribuições Linux), **ao analisar um arquivo `.pcap` offline com `-r`, você deve sempre rodar o `tcpdump` como um usuário comum sem privilégios (ou dentro de um sandbox `firejail --net=none` / `bwrap`) e usando `-w` durante a captura**!

## Como funciona
Além disso, para permitir que um analista de SOC ou engenheiro de redes capture pacotes em um servidor de diagnóstico sem precisar conceder acesso `sudo` completo à máquina, você pode usar **Linux Capabilities (`cap_net_raw,cap_net_admin=eip`)** restrito ao grupo `pcap`!

## Exemplo
```bash
# Analisar um arquivo .pcap suspeito offline sem privilegios de root, sem resolucao DNS (-nn), contando pacotes (--count) e lendo com seguranca
tcpdump --count -r ./captura_incidente.pcap 'tcp[tcpflags] & tcp-rst != 0'
tcpdump -nn -tttt -r ./captura_incidente.pcap | head -n 25
```

## Limites e trade-offs
Veja a flag **`--count`** na primeira linha acima (documentada na manpage `tcpdump(1)`): quando combinada com `-r arquivo.pcap` e uma expressão BPF, o `tcpdump --count` **não executa os dissecadores de impressão de protocolos em C** — ele apenas avalia o filtro BPF sobre o arquivo e imprime o número total de pacotes que casaram com a expressão em frações de segundo!

## Como verificar
No Ubuntu/Debian e SUSE, o pacote `tcpdump` já instala o perfil de confinamento **`/etc/apparmor.d/usr.sbin.tcpdump`** do **AppArmor**: verifique com `aa-status | grep tcpdump` que ele está ativo em modo `enforce`!

## Conexões
- [[tcpdump-otimizacao-alta-velocidade-snaplen-s-buffer-b-timestamps-nano]] — Veja também: Otimização de Captura em Alta Velocidade e Precisão de Tempo no `tcpdump`: **`snaplen` (`-s`)**, Buffer do Kernel (**`-B`**), Precisão **Nanossegundos (`--nano`)** e Bytecode **`-d`**.
- [[tcpdump-descriptografia-ipsec-esp-assinatura-tcp-md5-forense-tcpslice]] — Veja também: Recursos Forenses Avançados do `tcpdump`: Descriptografia de **IPsec ESP (`-E spi@ip algo:secret`)**, Verificação **TCP-MD5 (`-M`)**, Lista de Arquivos (**`-V`**) e **`tcpslice`**.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.

## Fontes
- [The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/README.md) — repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança; consultado em 2026-10-03.
- [Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)](https://www.tcpdump.org/manpages/tcpdump.1.html) — manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF; consultado em 2026-10-03.
