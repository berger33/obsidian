---
id: software.seguranca.tranche15.001477
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md", "https://www.kismetwireless.net/docs/readme/intro/kismet/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Automação e Integração com SIEM/SOAR via **API REST e WebSockets (`.ekjson` / `.itjson`)** do Kismet: Consumindo Alertas WIDS e Handshakes em Tempo Real

## Em uma frase
Como conectar o **Kismet** ao seu pipeline de **SIEM (Wazuh, OpenSearch, Elastic, Splunk)** ou a um bot de alerta no Slack/TheHive para receber em tempo real cada alerta WIDS (`APSPOOF`, `DEAUTHFLOOD`) ou monitorar os dispositivos presentes no perímetro sem precisar olhar para a interface web?

## Por que importa
Todo o motor interno do Kismet é construído como um servidor **REST API + WebSockets Event Stream** na porta `:2501`!

## Como funciona
Autenticando-se com um cabeçalho/parâmetro de **API Key (`KISMET` cookie ou `?KISMET=<apikey>`)**, você pode consultar endpoints JSON (`.json`), JSON Lines para streaming (**`.itjson`** — *Iterative JSON* que não consome RAM ao exportar 100.000 dispositivos!) ou formato pronto para **Elasticsearch/OpenSearch (`.ekjson`)** — além de conectar nos endpoints **WebSocket (`/alerts/alerts.ws`, `/devices/monitor.ws`)** para receber eventos no exato milissegundo em que ocorrem!

## Exemplo
```bash
# Consultar via API REST do Kismet todos os alertas WIDS recentes em JSON e listar os Access Points detectados nos ultimos 60 segundos
curl -sk -H "Cookie: KISMET=${KISMET_APIKEY}" \
  "http://127.0.0.1:2501/alerts/all_alerts.json" | jq .
curl -sk -H "Cookie: KISMET=${KISMET_APIKEY}" \
  "http://127.0.0.1:2501/devices/last-time/-60/devices.json" | jq 'length'
```

## Limites e trade-offs
Sabia que o Kismet também possui um endpoint de API REST dedicado que extrai em tempo real **apenas os pacotes EAPOL de 4-Way Handshakes WPA/WPA2 capturados para um BSSID específico**? Basta fazer um `GET` autenticado em `/phy/phy80211/by-key/<KEY>/pcap/handshake.pcap` para baixar instantaneamente o `.pcap` enxuto contendo apenas o handshake daquele AP!

## Como verificar
Ao criar uma API Key para o seu coletor de SIEM no Kismet, aplique o **Princípio do Privilégio Mínimo**: crie uma chave com permissão **`readonly`** em vez de `admin`!

## Conexões
- [[kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json]] — Veja também: O Formato Unificado **`kismetdb` (`.kismet` SQLite3)** e os Utilitários de Extração Forense (`kismetdb_to_pcap`, `kismetdb_to_kml`, `kismetdb_dump_devices`).
- [[kismet-filtros-pacotes-privacidade-pcapng-mascaramento-compliance]] — Veja também: Filtros de Captura e Conformidade de Privacidade (**LGPD / GDPR / PCI-DSS**) em WIDS com Kismet: Gravando Apenas Quadros de Gerenciamento (Sem Dados de Usuários!).
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Referência cruzada direta com kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
