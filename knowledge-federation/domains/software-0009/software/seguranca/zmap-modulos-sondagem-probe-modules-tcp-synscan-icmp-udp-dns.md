---
id: software.seguranca.tranche08.000792
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ZMap **Probe Modules (`-M`)**: Sondagem `tcp_synscan` (padrão), `icmp_echoscan`, `udp`, `dns` e `upnp` com **`--probe-args`**

## Em uma frase
A arquitetura do ZMap separa completamente o motor de permutação de endereços e transmissão Ethernet dos **Módulos de Sondagem (*Probe Modules*, selecionados com `-M` / `--probe-module`)**, que definem como construir o pacote de saída e como validar se um pacote recebido é uma resposta legítima.

## Por que importa
O módulo padrão é o **`-M tcp_synscan`** (que exige `-p <porta_destino>` e classifica respostas `SYN-ACK` como `success=1` e `RST` como `success=0`); para descoberta de hosts ativos via ICMP Ping em larga escala, usa-se **`-M icmp_echoscan`**; e para protocolos UDP, usa-se **`-M udp`**, **`-M dns`** ou **`-M upnp`**!

## Como funciona
No módulo **`-M udp`**, a flag **`--probe-args`** permite passar payloads estáticos em texto/hex (`text:...` ou `hex:...`), carregar um arquivo binário (`file:/caminho/payload.bin`) ou usar um **Template Dinâmico (`template:/caminho/pkt.tpl`)** que injeta campos aleatórios de transação/porta em cada pacote UDP enviado!

## Exemplo
```bash
# Sondar servidores DNS autoritativos ou recursivos na porta 53/UDP usando o modulo nativo -M dns do ZMap
sudo zmap -M dns -p 53 \
  --probe-args="A,exemplo.com.br" \
  -B 10M \
  10.0.0.0/8 \
  -o /cases/easm/internal_dns_servers.txt
```

## Limites e trade-offs
Quando usar **`-M icmp_echoscan`** para mapear quais endereços IP respondem a ping dentro dos blocos `/8` e `/16` internos de uma grande empresa, nenhuma porta (`-p`) precisa ser informada, pois o módulo constrói pacotes `ICMP Echo Request (Type 8)` e valida os `Echo Reply (Type 0)`.

## Como verificar
Execute `zmap -M udp --help` ou `zmap -M dns --help` para consultar a documentação embutida de `--probe-args` daquele módulo específico.

## Conexões
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Veja também: **ZMap (`zmap/zmap`)**: Arquitetura de Varredura *Stateless* de Pacote Único via Permutação em **Grupos Cíclicos Multiplicativos ($\mathbb{Z}_p^*$)**.
- [[zmap-controle-banda-taxa-bandwidth-rate-cooldown-time-sender-threads]] — Veja também: ZMap: Controle de Largura de Banda (**`-B 10M` / `--bandwidth`**) vs Taxa de Pacotes (**`-r` / `--rate`**), `--sender-threads` e `--cooldown-time`.
- [[zmap-modulos-saida-output-modules-campos-output-filter-json-csv]] — Referência cruzada direta com zmap-modulos-saida-output-modules-campos-output-filter-json-csv.
- [[masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados]] — Referência cruzada direta com masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
