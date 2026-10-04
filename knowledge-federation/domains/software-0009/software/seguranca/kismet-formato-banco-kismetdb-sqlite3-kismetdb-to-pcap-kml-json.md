---
id: software.seguranca.tranche15.001476
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

# O Formato Unificado **`kismetdb` (`.kismet` SQLite3)** e os Utilitários de Extração Forense (`kismetdb_to_pcap`, `kismetdb_to_kml`, `kismetdb_dump_devices`)

## Em uma frase
Onde o **Kismet** moderno grava tudo o que captura e por que ele substituiu a dezena de arquivos separados das versões antigas pelo formato unificado **`.kismet` (`kismetdb`)**?

## Por que importa
Um arquivo **`.kismet` (`kismetdb`)** gerado em `/var/log/kismet/` é na verdade um **Banco de Dados Transacional `SQLite3` Autocontido**! Dentro desse único arquivo `.kismet`, o Kismet grava em tabelas indexadas: **(1) A tabela `packets`** — todos os pacotes brutos 802.11/BLE com cabeçalhos Radiotap, coordenadas GPS e sinal RSSI; **(2) A tabela `devices`** — o objeto JSON completo de cada Access Point, estação cliente, dispositivo BLE ou sensor visto; **(3) A tabela `alerts`** — todos os alertas WIDS disparados; **(4) A tabela `datasources`**; e **(5) A tabela `snapshots` / `messages`**!

## Como funciona
E para exportar esses dados para outras ferramentas de análise forense, o Kismet inclui a suíte de utilitários **`kismetdb_*`**: **`kismetdb_to_pcap`** (converte para `.pcapng` multi-interface para abrir no **Wireshark / Arkime / Aircrack-ng**!), **`kismetdb_to_wiglecsv`**, **`kismetdb_to_kml`** (gera mapas 3D para o Google Earth!) e **`kismetdb_dump_devices`** (exporta todos os dispositivos em JSON)!

## Exemplo
```bash
# Extrair de um arquivo de log .kismet (SQLite3) um arquivo PCAP-NG padrao para o Wireshark/Aircrack e um dump JSON de todos os dispositivos vistos
kismetdb_statistics --in ./Sensor-WIDS-20261003.kismet
kismetdb_to_pcap --in ./Sensor-WIDS-20261003.kismet --out ./captura_extraida.pcapng
kismetdb_dump_devices --in ./Sensor-WIDS-20261003.kismet --out ./inventario_dispositivos_rf.json
```

## Limites e trade-offs
Como o arquivo `.kismet` é um banco **SQLite3 padrão**, você também pode fazer consultas SQL ad-hoc diretamente nele usando o comando `sqlite3`: por exemplo, **`sqlite3 Sensor.kismet "SELECT devmac, type, first_time, last_time, strongest_signal FROM devices WHERE type='Wi-Fi AP' ORDER BY strongest_signal DESC LIMIT 10;"`**!

## Como verificar
Quando converter um `.kismet` que possui múltiplos sensores remotos (`Sensor_Andar_01`, `Sensor_Andar_02`) usando **`kismetdb_to_pcap`**, o formato `.pcapng` gerado preserva no cabeçalho de cada pacote o `Interface ID` do sensor exato que capturou aquele quadro!

## Conexões
- [[kismet-monitoramento-bluetooth-ble-zigbee-sdr-iot-seguranca-fisica]] — Veja também: Além do Wi-Fi: Monitoramento de **Bluetooth / BLE (`kismet_cap_linux_bluetooth`)**, **Zigbee (`802.15.4`)** e **Rádio Definido por Software (`RTL-SDR`)** no Kismet.
- [[kismet-automacao-api-rest-websockets-alertas-tempo-real-siem-soar]] — Veja também: Automação e Integração com SIEM/SOAR via **API REST e WebSockets (`.ekjson` / `.itjson`)** do Kismet: Consumindo Alertas WIDS e Handshakes em Tempo Real.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Referência cruzada direta com aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario.
- [[arkime-ingestao-pcap-offline-dfir-capture-r-analise-forense]] — Referência cruzada direta com arkime-ingestao-pcap-offline-dfir-capture-r-analise-forense.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
