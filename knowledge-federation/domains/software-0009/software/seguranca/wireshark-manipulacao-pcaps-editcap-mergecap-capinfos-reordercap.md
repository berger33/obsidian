---
id: software.seguranca.tranche06.000558
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

# Utilitários de Manipulação Forense de PCAPs do Wireshark: `capinfos`, `editcap`, `mergecap` e `reordercap`

## Em uma frase
A suíte Wireshark instala quatro ferramentas de linha de comando ultrarrápidas que manipulam arquivos de captura sem precisar invocar os dissecadores pesados de protocolo: **`capinfos`**, **`editcap`**, **`mergecap`** e **`reordercap`**.

## Por que importa
Tentar abrir um arquivo PCAP único de 40 GB diretamente na GUI do Wireshark esgotará a memória RAM da estação do perito; recortar a janela exata do incidente com `editcap` ou inspecionar os metadados e o hash criptográfico com `capinfos` é instantâneo e consome poucos megabytes de RAM.

## Como funciona
O **`capinfos`** gera o laudo de metadados da evidência (número de pacotes, data do primeiro e último pacote, taxa média de bits, tipo de encapsulamento e hash SHA-256); o **`editcap`** fatia PCAPs por janela temporal (`-A "YYYY-MM-DD HH:MM:SS" -B ...`), divide em blocos de N pacotes (`-c 100000`) ou remove pacotes duplicados (`-d` / `-D <window>` causados por SPAN ports mal configuradas); o **`mergecap`** funde capturas de múltiplos sensores em ordem cronológica; e o **`reordercap`** corrige pacotes fora de ordem.

## Exemplo
```bash
# Gerar metadados forenses com SHA-256 (capinfos), remover duplicatas de SPAN port (-d) e recortar janela do incidente
capinfos -H /cases/pcaps/full_day_sensor.pcapng
editcap -d -A "2026-10-03 14:00:00" -B "2026-10-03 14:15:00" \
  /cases/pcaps/full_day_sensor.pcapng \
  /cases/pcaps/incident_15min_dedup.pcapng
```

## Limites e trade-offs
Ao capturar tráfego em *SPAN / Mirror Ports* de switches que espelham tanto ingress quanto egress de VLANs roteadas, até 50% dos pacotes podem vir duplicados (o que quebra alertas de retransmissão TCP no Wireshark); sempre rode **`editcap -d`** antes de analisar.

## Como verificar
Verifique com `capinfos /cases/pcaps/incident_15min_dedup.pcapng` a janela temporal resultante e a redução de pacotes duplicados.

## Conexões
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Veja também: Wireshark & `tshark`: Filtros de Detecção de Ataques em Active Directory (Kerberos Roasting, `DCSync` `DRSUAPI`, NTLM Relay e `psexec`).
- [[wireshark-dissecadores-customizados-lua-protocolos-c2-proprietarios]] — Veja também: Wireshark & `tshark`: Desenvolvimento de Dissecadores Customizados em **Lua** (`Proto`, `ProtoField`, `DissectorTable`) para Protocolos C2 Proprietários.
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
