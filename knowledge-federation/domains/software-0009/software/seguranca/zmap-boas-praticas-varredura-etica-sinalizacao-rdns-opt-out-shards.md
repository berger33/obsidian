---
id: software.seguranca.tranche08.000799
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

# ZMap: Boas Práticas de **Varredura Ética (*Ethical Scanning*)**, Reprodutibilidade Científica (**`--seed`**), Distribuição (**`--shards`**) e Metadados (`--notes`)

## Em uma frase
Os autores do ZMap estabeleceram no artigo original e na Wiki oficial as diretrizes internacionais de **Varredura Ética de Rede (*Ethical Internet Scanning*)**, que devem ser seguidas por qualquer equipe de pesquisa ou EASM externo.

## Por que importa
As práticas recomendadas incluem: **(1)** configurar **DNS Reverso (`PTR`)** e uma página web explicativa na porta `80` dos IPs de origem da varredura informando quem é a organização responsável e como solicitar exclusão imediata (*opt-out*); **(2)** monitorar a caixa de e-mail de `abuse@` e atualizar o **`/etc/zmap/blocklist.conf`** imediatamente; **(3)** usar múltiplos IPs de origem (**`-S 203.0.113.10-203.0.113.20`**) se autorizado; e **(4)** registrar metadados de auditoria com **`--metadata-file=/cases/easm/scan_meta.json`** e **`--notes="Ticket-SecOps-2026"`**!

## Como funciona
Para **reprodutibilidade determinística** e divisão de trabalho entre vários coletores, fixar **`--seed <uint64>`** combinado com **`--shards <N>`** e **`--shard <id>`** garante que cada coletor varra uma fatia matematicamente disjunta do grupo cíclico $\mathbb{Z}_p^*$!

## Exemplo
```bash
# Executar o shard 0 de 4 coletores distribuidos compartilhando a mesma semente (--seed) e gravando metadados completos de auditoria
sudo zmap -p 443 -B 20M \
  --seed=987654321 \
  --shards=4 --shard=0 \
  --notes="Auditoria Mensal de Superficie Externa - Ticket SEC-4092" \
  --metadata-file=/cases/easm/zmap_shard0_metadata.json \
  -w /cases/easm/authorized_cidrs.txt \
  -o /cases/easm/zmap_shard0_results.txt
```

## Limites e trade-offs
Atenção: na sintaxe do ZMap, a numeração de **`--shard`** começa em **`0`** (portanto, para `--shards=4`, os quatro coletores usam `--shard=0`, `--shard=1`, `--shard=2` e `--shard=3`), e é obrigatório que todos os 4 coletores recebam exatamente o mesmo valor em **`--seed`**!

## Como verificar
Inspecione o arquivo JSON gerado por `--metadata-file` para auditar o horário exato de início/fim, a versão do ZMap, a taxa de pacotes efetiva e o hash SHA-256 da blocklist utilizada.

## Conexões
- [[zmap-auditoria-protocolos-industriais-ot-ics-scada-zgrab2-modbus-siemens-dnp3]] — Veja também: ZGrab 2.0 em Auditoria de Redes **OT / ICS / SCADA** e Bancos de Dados: Módulos `modbus`, `siemens` (S7), `dnp3`, `bacnet`, `fox` e `mongodb`/`redis`.
- [[zmap-deteccao-defensiva-assinatura-ip-id-54321-suricata-zeek]] — Veja também: Engenharia de Detecção (Blue Team): Identificação da Assinatura Clássica do **ZMap (`IP ID = 54321` / `0xd431`)** no **Suricata**, **Zeek** e **`tcpdump`**.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Referência cruzada direta com zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc.
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Referência cruzada direta com masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
