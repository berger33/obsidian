---
id: software.seguranca.tranche06.000552
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

# `tshark`: Diferença entre Filtros de Captura **BPF** (`-f`) e **Display Filters** (`-Y` / `-R`), e Análise em Duas Passagens (`-2`)

## Em uma frase
No **`tshark`** (o analisador CLI do Wireshark), existem duas linguagens de filtragem completamente distintas que atuam em camadas diferentes: **Capture Filters (`-f`)** usam a sintaxe **BPF** (*Berkeley Packet Filter* da `libpcap`, executada no kernel antes de gravar em disco) e **Display Filters (`-Y`)** usam o motor rico de dissecação de protocolos do Wireshark.

## Por que importa
Confundir `-f` com `-Y` é um erro frequente: `-f "tcp port 443 and not host 10.0.0.5"` descarta pacotes na placa de rede/kernel com custo mínimo de CPU, mas não entende campos de camada 7 complexos; já `-Y "tls.handshake.type == 1 and tls.handshake.extensions_server_name contains \"evil\""` entende milhares de protocolos, mas exige dissecar os pacotes.

## Como funciona
Quando um filtro de exibição depende de informações que só aparecem em pacotes futuros (como filtrar requisições HTTP que receberam resposta `http.response_in`, ou remontar fragmentos TCP/TLS multiframe), a flag **`-2` (*two-pass analysis*)** instrui o `tshark` a ler o arquivo PCAP duas vezes: na primeira passagem ele reconstrói todos os fluxos e dependências entre quadros, e na segunda passagem aplica o filtro `-R` / `-Y` com precisão total.

## Exemplo
```bash
# Analisar arquivo PCAPNG em duas passagens (-2) desativando resolucao DNS (-n) e filtrando ClientHello TLS
tshark -r /cases/pcaps/incident.pcapng -2 -n \
  -Y 'tls.handshake.type == 1 && !(tls.handshake.extensions_server_name contains ".internal.corp")'
```

## Limites e trade-offs
A análise em duas passagens (`-2`) requer um arquivo de captura buscável em disco (`-r`) e não pode ser usada simultaneamente com captura ao vivo em streaming contínuo sem buffer.

## Como verificar
Sempre passe a flag **`-n`** (desativa resolução reversa de DNS/portas) durante investigações forenses no `tshark` para evitar vazamento de OPSEC via consultas PTR para servidores DNS do atacante e acelerar a leitura do PCAP.

## Conexões
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Veja também: Wireshark & `dumpcap`: Arquitetura de Separação de Privilégios, Formato Nativo **`pcapng`** e Isolamento da Superfície de Ataque de Dissecadores.
- [[wireshark-extracao-campos-tshark-json-ek-fields-automacao-dfir]] — Veja também: `tshark`: Extração Estruturada de Campos (`-T fields -e ...`, `-T json`, `-T ek`) para Triagem Rápida em Linha de Comando.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
