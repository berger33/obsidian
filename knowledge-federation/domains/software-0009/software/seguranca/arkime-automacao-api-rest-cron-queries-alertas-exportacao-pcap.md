---
id: software.seguranca.tranche14.001359
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

# Automação no Arkime: **Periodic Queries (*Cron Queries*)**, **Hunt Jobs (Busca de Bytes/Regex nos PCAPs Brutos)** e Extração de PCAP via **API REST**

## Em uma frase
E quando o indicador que você está procurando (por exemplo, uma string específica dentro do corpo de um protocolo binário customizado ou um shellcode/comando enviado dentro de uma sessão TCP) **não faz parte dos metadados SPI indexados no OpenSearch**, mas está gravado dentro dos pacotes brutos `.pcap` nos discos dos sensores?

## Por que importa
O Arkime possui duas ferramentas extraordinárias para automação e caça profunda: **(1) Packet Search / `Hunt` (aba *Hunt*)** — você seleciona uma janela de tempo e uma expressão de filtro inicial (ex.: `port.dst == 4444`) e digita uma string ASCII, Hexadecimal ou **Expressão Regular**; o Arkime despacha um *Hunt Job* em background que abre os arquivos `.pcap` brutos nos sensores e varre **o payload byte a byte de todos os pacotes daquelas sessões**, listando exatamente quais sessões contêm os bytes procurados!; e **(2) Periodic Queries (*Cron Queries*)**!

## Como funciona
Com **Cron Queries** (`cronQueries=true` em um único nó `viewer`), o Arkime executa consultas agendadas a cada poucos minutos sobre as novas sessões que entram e pode rotular sessões, enviar alertas para Webhook/SIEM ou encaminhar pacotes!

## Exemplo
```bash
# Baixar via API REST do Arkime (autenticacao Digest) um arquivo .pcap filtrado por uma expressao de busca e janela temporal
curl -sk --anyauth -u "${ARKIME_USER}:${ARKIME_PASS}" \
  -G "https://127.0.0.1:8005/api/sessions.pcap" \
  --data-urlencode "date=24" \
  --data-urlencode "expression=ip.src == 10.1.2.15 && port.dst == 4444" \
  -o ./sessoes_suspeitas_10_1_2_15.pcap
```

## Limites e trade-offs
A **API REST do Arkime (`/api/sessions.pcap`, `/api/sessions.json`, `/api/sessions.csv`, `/api/spiview`)** permite integrar o Full Packet Capture diretamente ao seu **SOAR**: quando o **Snort 3**, **Suricata** ou **Wazuh** gera um alerta com `{src_ip, src_port, dst_ip, dst_port, timestamp}`, o playbook do SOAR faz um `GET /api/sessions.pcap` no Arkime passando a 5-tupla e a janela de 5 minutos ao redor do alerta e **anexa automaticamente o arquivo `.pcap` completo da conversa ao chamado do TheHive**!

## Como verificar
Lembre-se da regra documentada no `config.ini.sample`: descomente **`cronQueries=true` em APENAS UM nó `viewer` do cluster** para evitar que múltiplos nós executem os mesmos Cron Queries e Hunt Jobs em duplicidade.

## Conexões
- [[arkime-ingestao-pcap-offline-dfir-capture-r-analise-forense]] — Veja também: Uso do Arkime em **Laboratórios de DFIR Offline (`capture -r`)**: Importando Diretórios de Arquivos `.pcap` de Incidentes para Investigação Visual e Grafo.
- [[arkime-integracao-zeek-suricata-snort-malcolm-correlacao-community-id]] — Veja também: Tríade da Visibilidade de Rede (**NSM**): Correlacionando **Arkime (FPC) + Zeek (Logs de Transação) + Suricata / Snort 3 (Alertas IDS)** via **`communityId`**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Referência cruzada direta com arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
