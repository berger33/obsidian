---
id: software.seguranca.tranche06.000553
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

# `tshark`: Extração Estruturada de Campos (`-T fields -e ...`, `-T json`, `-T ek`) para Triagem Rápida em Linha de Comando

## Em uma frase
A opção **`-T`** do `tshark` transforma pacotes binários dissecados em dados tabulares ou JSON estruturado prontos para processamento com `jq`, `awk`, `sort | uniq -c` ou ingestão direta no OpenSearch/Timesketch.

## Por que importa
Em um arquivo PCAP de 5 GB de um incidente de exfiltração DNS ou beaconing HTTPS, extrair apenas os campos específicos (`-T fields -e frame.time_epoch -e ip.src -e ip.dst -e dns.qry.name`) permite identificar os domínios exfiltrados em poucos segundos.

## Como funciona
Os formatos suportados por `-T` incluem **`fields`** (exige uma ou mais flags `-e <campo>` e permite customizar separador `-E separator=,`, cabeçalho `-E header=y` e aspas `-E quote=d`), **`json`** (árvore completa dos protocolos dissecados), **`ek`** (JSON Lines newline-delimited para ingestão Bulk no Elasticsearch/OpenSearch), **`pdml`** e **`psml`**.

## Exemplo
```bash
# Extrair tabela CSV de conexoes TLS (IP origem, IP destino, SNI e huella JA3/JA4) de um PCAP forense
tshark -r /cases/pcaps/incident.pcapng -n \
  -Y "tls.handshake.type == 1" \
  -T fields \
  -E header=y -E separator=, -E quote=d \
  -e frame.time_utc -e ip.src -e ip.dst -e tls.handshake.extensions_server_name -e tls.handshake.ja3
```

## Limites e trade-offs
Se um mesmo pacote contiver múltiplas ocorrências do mesmo campo (ex.: pacotes com encapsulamento IP-in-IP/ICMP ou múltiplos registros DNS), use `-E occurrence=f` (primeiro), `l` (último) ou `a` (todos, separados por `-E aggregator=/`).

## Como verificar
Para descobrir o nome exato de qualquer campo de filtro ou extração `-e` de um protocolo no `tshark`, execute `tshark -G fields | grep -i <protocolo>` ou inspecione a barra de status inferior da GUI do Wireshark.

## Conexões
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Veja também: `tshark`: Diferença entre Filtros de Captura **BPF** (`-f`) e **Display Filters** (`-Y` / `-R`), e Análise em Duas Passagens (`-2`).
- [[wireshark-estatisticas-forenses-tshark-z-conversations-io-follow]] — Veja também: `tshark`: Estatísticas Forenses (`-q -z conv,tcp`, `-z io,phs`, `-z endpoints`, `-z dns,tree`, `-z http,tree`) e Reconstrução de Streams (`-z follow`).

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
