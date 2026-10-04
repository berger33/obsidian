---
id: software.seguranca.tranche06.000554
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

# `tshark`: Estatísticas Forenses (`-q -z conv,tcp`, `-z io,phs`, `-z endpoints`, `-z dns,tree`, `-z http,tree`) e Reconstrução de Streams (`-z follow`)

## Em uma frase
Combinar **`-q`** (suprime a impressão linha a linha de cada pacote) com **`-z <estatistica>`** transforma o `tshark` em um gerador instantâneo de matrizes de conversação, hierarquias de protocolos e reconstrutor de sessões TCP/TLS/HTTP completas.

## Por que importa
Antes de inspecionar pacotes individuais em um PCAP desconhecido, rodar `-q -z io,phs` (*Protocol Hierarchy Statistics*) e `-q -z conv,tcp` (*TCP Conversations* ordenadas por bytes transferidos) mostra imediatamente se houve transferência massiva de dados por um protocolo incomum (como SSH na porta 443, ICMP volumoso ou SMB para fora da sub-rede).

## Como funciona
E uma vez identificado o fluxo suspeito (`tcp.stream eq N`), o comando **`-q -z "follow,tcp,ascii,N"`** (ou `follow,tls,ascii,N` / `follow,http,ascii,N`) reconstrói na saída padrão todo o diálogo cliente-servidor remontado na ordem exata dos números de sequência TCP.

## Exemplo
```bash
# Gerar hierarquia de protocolos, top conversacoes TCP e reconstruir o payload completo do stream TCP #12
tshark -r /cases/pcaps/incident.pcapng -n -q -z io,phs
tshark -r /cases/pcaps/incident.pcapng -n -q -z conv,tcp | head -n 25
tshark -r /cases/pcaps/incident.pcapng -n -q -z "follow,tcp,ascii,12"
```

## Limites e trade-offs
Para fluxos binários (como protocolos C2 proprietários ou transferências de arquivos brutos), troque `ascii` por **`raw`** ou **`hexdump`** em `-z "follow,tcp,raw,12"` para evitar corrupção de bytes não-imprimíveis.

## Como verificar
Verifique na saída de `-q -z io,phs` a porcentagem de pacotes e bytes de cada protocolo de camada de aplicação presente na captura.

## Conexões
- [[wireshark-extracao-campos-tshark-json-ek-fields-automacao-dfir]] — Veja também: `tshark`: Extração Estruturada de Campos (`-T fields -e ...`, `-T json`, `-T ek`) para Triagem Rápida em Linha de Comando.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Veja também: Wireshark & `tshark`: Decriptação Passiva de Tráfego **TLS 1.2/1.3** (`SSLKEYLOGFILE` e `editcap --inject-secrets`) e **Kerberos** (`keytab`).
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Referência cruzada direta com wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
