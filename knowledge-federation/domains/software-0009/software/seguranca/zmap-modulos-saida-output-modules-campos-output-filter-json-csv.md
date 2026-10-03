---
id: software.seguranca.tranche08.000795
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

# ZMap **Output Modules (`-O`)**, Seleção de Campos (**`-f` / `--output-fields`**) e Expressões Booleanas **`--output-filter`**

## Em uma frase
Por padrão, o ZMap utiliza o módulo de saída `csv` exportando apenas uma coluna (`saddr`, o endereço IP que respondeu com sucesso), o que permite canalizar `zmap -p 443 -q` diretamente via pipe para outra ferramenta.

## Por que importa
Porém, cada módulo de sondagem do ZMap disponibiliza dezenas de campos de telemetria de camada de rede e transporte (listados com **`zmap -M tcp_synscan --list-output-fields`**), incluindo `saddr`, `daddr`, `sport`, `dport`, `seqnum`, `acknum`, **`window`** (tamanho da janela TCP!), **`ttl`** (Time-To-Live do pacote IP para fingerprinting passivo de SO!), `classification` (`synack` vs `rst`), `success` e `timestamp_str`!

## Como funciona
Combinando **`-O json`** (ou **`-O csv`**) com **`-f "saddr,sport,ttl,window,classification"`** e a expressão booleana **`--output-filter="success = 1 && repeat = 0"`**, você exporta metadados ricos eliminando duplicatas!

## Exemplo
```bash
# Exportar resultados do ZMap em JSON Lines (-O json) incluindo TTL e TCP Window para fingerprinting passivo de SO
sudo zmap -p 443 -B 10M \
  -b /cases/easm/internal_blocklist.conf \
  -O json \
  -f "saddr,dport,ttl,window,classification,timestamp_str" \
  --output-filter="success = 1 && repeat = 0" \
  10.20.0.0/16 \
  -o /cases/easm/zmap_rich_443.jsonl
```

## Limites e trade-offs
Por que capturar os campos **`ttl`** e **`window`** no `-f` do ZMap é tão valioso? Porque sem enviar **nenhum** pacote adicional, o TTL inicial do `SYN-ACK` já diferencia instantaneamente se o servidor é **Linux/Unix (`TTL <= 64`)**, **Windows (`TTL <= 128`)** ou **Roteador/Equipamento de Rede Cisco/F5 (`TTL <= 255`)**!

## Como verificar
Execute `zmap -M tcp_synscan --list-output-fields` para ver todos os campos que podem ser passados em `-f` e filtrados em `--output-filter`.

## Conexões
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Veja também: ZMap: Governança de Escopo com **`/etc/zmap/blocklist.conf` (`-b`)**, **Allowlist (`-w`)** e **`--ignore-blocklist-errors`**.
- [[zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes]] — Veja também: Arquitetura **ZMap (L4) + ZGrab 2.0 (L7)**: Pipeline de Sondagem em Escala de Camada de Transporte para Transcrição Completa de Handshakes de Aplicação.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
