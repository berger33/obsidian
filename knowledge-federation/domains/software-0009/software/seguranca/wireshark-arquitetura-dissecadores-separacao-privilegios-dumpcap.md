---
id: software.seguranca.tranche06.000551
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/wireshark/wireshark/master/README.md", "https://www.wireshark.org/docs/man-pages/tshark.html", "https://www.wireshark.org/docs/wsug_html_chunked/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Wireshark & `dumpcap`: Arquitetura de Separação de Privilégios, Formato Nativo **`pcapng`** e Isolamento da Superfície de Ataque de Dissecadores

## Em uma frase
**Wireshark** (`wireshark/wireshark`, GPLv2) é o analisador de protocolos de rede padrão da indústria, projetado com uma arquitetura estrita de **separação de privilégios** onde a captura bruta de pacotes no kernel é isolada no binário mínimo **`dumpcap`**, enquanto os mais de 3.000 dissecadores complexos de protocolos (`libwireshark` / `wireshark` / `tshark`) rodam sempre como usuário comum sem privilégios.

## Por que importa
Dissecadores de protocolos de rede fazem parsing em C de pacotes arbitrários vindos da rede hostil; conforme alerta enfaticamente o `README.md` oficial do Wireshark, **jamais se deve executar `wireshark` ou `tshark` como `root`**, pois uma vulnerabilidade de corrupção de memória em um dissecador daria execução de código como `root` ao atacante que enviasse um pacote malformado pela rede.

## Como funciona
Para capturar pacotes sem `root`, o administrador atribui capacidades POSIX (`cap_net_raw,cap_net_admin=eip`) exclusivamente ao binário `/usr/bin/dumpcap` e restringe sua execução ao grupo `wireshark`. O formato nativo padrão do Wireshark e TShark é o **PCAPNG** (*PCAP Next Generation*), que armazena múltiplas interfaces, estatísticas de descarte de pacotes, comentários de analistas por pacote, resolução de nomes local e blocos de segredos de decriptação TLS (**DSB** — *Decryption Secrets Block*).

## Exemplo
```bash
# Verificar capacidades POSIX do dumpcap e capturar em ring-buffer de 10 arquivos de 100 MB como usuario comum
getcap /usr/bin/dumpcap
dumpcap -i eth0 -b filesize:102400 -b files:10 -w /cases/pcaps/ring_capture.pcapng
```

## Limites e trade-offs
Para capturas contínuas de alta velocidade em servidores de produção (10 Gbps+), invoque diretamente o **`dumpcap`** (sem carregar a engine de dissecação `libwireshark` na memória) com `-b filesize:... -b files:...` para zero processamento de protocolo durante a gravação.

## Como verificar
Confirme que `ps aux | grep -E 'wireshark|tshark'` nunca exibe UID `0` (`root`) e que `dumpcap` grava arquivos `.pcapng` nativos.

## Conexões
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Veja também: `tshark`: Diferença entre Filtros de Captura **BPF** (`-f`) e **Display Filters** (`-Y` / `-R`), e Análise em Duas Passagens (`-2`).
- [[wireshark-extracao-campos-tshark-json-ek-fields-automacao-dfir]] — Referência cruzada direta com wireshark-extracao-campos-tshark-json-ek-fields-automacao-dfir.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
