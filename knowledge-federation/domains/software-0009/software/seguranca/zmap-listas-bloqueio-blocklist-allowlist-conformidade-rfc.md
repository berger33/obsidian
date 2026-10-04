---
id: software.seguranca.tranche08.000794
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

# ZMap: Governança de Escopo com **`/etc/zmap/blocklist.conf` (`-b`)**, **Allowlist (`-w`)** e **`--ignore-blocklist-errors`**

## Em uma frase
Por padrão, o ZMap carrega automaticamente o arquivo **`/etc/zmap/blocklist.conf`** (configurável com **`-b` / `--blocklist-file`**), que já bloqueia o envio de pacotes para sub-redes reservadas pelo IANA/IETF: endereços privados **RFC 1918 (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`)**, loopback (`127.0.0.0/8`), link-local (`169.254.0.0/16`), multicast (`224.0.0.0/4`) e redes governamentais/militares sensíveis.

## Por que importa
Isso explica um detalhe prático importantíssimo: **quando você tenta usar o ZMap para varrer uma rede interna corporativa (`10.0.0.0/8` ou `192.168.1.0/24`) sem alterar a blocklist padrão, o ZMap reporta `0 addresses allowed to be scanned` porque o `/etc/zmap/blocklist.conf` bloqueia o RFC 1918 por padrão!**

## Como funciona
Para varrer redes privadas internas autorizadas (`10.0.0.0/8`), passe um arquivo de blocklist customizado para redes internas (ex.: `-b /cases/easm/internal_blocklist.conf` contendo apenas loopback/multicast e as sub-redes OT/impressoras excluídas) combinado com uma **Allowlist (`-w /cases/easm/scope_allowlist.txt`)** contendo exatamente os blocos CIDR do escopo!

## Exemplo
```bash
# Criar uma blocklist e uma allowlist explicitas para varredura interna de sub-redes RFC 1918 autorizadas
cat << 'EOF' > /cases/easm/internal_blocklist.conf
127.0.0.0/8
224.0.0.0/4
10.250.0.0/16
EOF

sudo zmap -p 443 -B 10M \
  -b /cases/easm/internal_blocklist.conf \
  -w /cases/easm/authorized_cidrs.txt \
  -o /cases/easm/zmap_internal_443.txt
```

## Limites e trade-offs
Internamente, o ZMap compila a união da Allowlist (`-w`) menos a Blocklist (`-b`) em uma árvore binária radix (*Radix Tree / Constraint Tree*) em memória antes de iniciar o loop do grupo cíclico, garantindo que **nenhum IP contido na blocklist jamais seja gerado pelo iterador**!

## Como verificar
Verifique no log inicial do ZMap (`[INFO] constraint: ... addresses allowed`) a contagem exata de endereços IP que serão sondados.

## Conexões
- [[zmap-controle-banda-taxa-bandwidth-rate-cooldown-time-sender-threads]] — Veja também: ZMap: Controle de Largura de Banda (**`-B 10M` / `--bandwidth`**) vs Taxa de Pacotes (**`-r` / `--rate`**), `--sender-threads` e `--cooldown-time`.
- [[zmap-modulos-saida-output-modules-campos-output-filter-json-csv]] — Veja também: ZMap **Output Modules (`-O`)**, Seleção de Campos (**`-f` / `--output-fields`**) e Expressões Booleanas **`--output-filter`**.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.
- [[zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards]] — Referência cruzada direta com zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
