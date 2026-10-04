---
id: software.seguranca.tranche14.001360
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/arkime/arkime/main/README.md", "https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tríade da Visibilidade de Rede (**NSM**): Correlacionando **Arkime (FPC) + Zeek (Logs de Transação) + Suricata / Snort 3 (Alertas IDS)** via **`communityId`**

## Em uma frase
Como arquitetar uma plataforma de **Network Security Monitoring (NSM)** de nível mundial onde um alerta disparado pelo **Suricata / Snort 3** leva o analista instantaneamente aos logs ricos de protocolo do **Zeek** (e às análises de beaconing do **RITA**) e, com mais um clique, abre os pacotes `.pcap` completos daquela exata conexão no **Arkime**?

## Por que importa
O elo mágico que une **Suricata / Snort 3 + Zeek + Arkime** chama-se **`Community ID Flow Hashing`**!

## Como funciona
O **Community ID** é um algoritmo padronizado aberto (`v1:` + Base64 do hash `SHA-1` da tupla normalizada `{Protocolo, IP_Origem, IP_Destino, Porta_Origem, Porta_Destino, Seed}`) calculado de forma idêntica pelo **Arkime** (campo SPI **`communityId`**), pelo **Zeek** (plugin `CommunityID`, campo `community_id`) e pelo **Suricata / Snort 3** (campo `community_id` no `eve.json` / `alert_json`)! Assim, mesmo que as três ferramentas rodem em processos separados, **toda conexão TCP/UDP recebe exatamente a mesma string `communityId` (ex.: `1:LQU9qZlK+B5F3KDmev6m5PMibrg=`) nas três ferramentas**!

## Exemplo
```text
# Buscar no Arkime todas as sessoes e pacotes PCAP correspondentes ao exato Community ID de um alerta do Suricata/Snort ou log do Zeek
communityId == "1:LQU9qZlK+B5F3KDmev6m5PMibrg="
```

## Limites e trade-offs
Projetos integrados de defesa cibernética como o **Malcolm (`idaholab/Malcolm`, desenvolvido pelo Idaho National Laboratory / CISA)** e o **Security Onion** são construídos exatamente sobre essa tríade (**Arkime + Zeek + Suricata + OpenSearch** conectada por `communityId`): você vê o alerta no dashboard, clica no `communityId` e já está diante do stream TCP reconstituído e do `.pcap` pronto para download no Arkime!

## Como verificar
Garanta que todos os sensores (Zeek, Suricata/Snort e Arkime) usem exatamente a mesma `seed` padrão (`0`) no cálculo do `Community ID` e estejam sincronizados via `chrony` (NTP).

## Conexões
- [[arkime-automacao-api-rest-cron-queries-alertas-exportacao-pcap]] — Veja também: Automação no Arkime: **Periodic Queries (*Cron Queries*)**, **Hunt Jobs (Busca de Bytes/Regex nos PCAPs Brutos)** e Extração de PCAP via **API REST**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[snort-saidas-logs-alert-json-unified2-integracao-siem-opensearch]] — Referência cruzada direta com snort-saidas-logs-alert-json-unified2-integracao-siem-opensearch.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
