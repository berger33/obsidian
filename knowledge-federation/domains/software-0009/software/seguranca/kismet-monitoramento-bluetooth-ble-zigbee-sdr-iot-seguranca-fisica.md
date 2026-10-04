---
id: software.seguranca.tranche15.001475
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

# Além do Wi-Fi: Monitoramento de **Bluetooth / BLE (`kismet_cap_linux_bluetooth`)**, **Zigbee (`802.15.4`)** e **Rádio Definido por Software (`RTL-SDR`)** no Kismet

## Em uma frase
Em salas de servidores seguras (SCIFs / Datacenters PCI-DSS) onde dispositivos sem fio não autorizados são proibidos, um atacante ou visitante mal-intencionado pode não usar Wi-Fi: ele pode entrar com um **teclado sem fio pirata, um rastreador BLE (AirTag / Flipper Zero / Skimmer Bluetooth), um dispositivo Zigbee ou um transmissor RF de 433/915 MHz**! Como usar o **Kismet** para detectar dispositivos **Bluetooth/BLE, Zigbee e Sub-GHz SDR** no perímetro físico?

## Por que importa
Porque o Kismet trata qualquer protocolo de rádio através da sua abstração **Multi-PHY**!

## Como funciona
Com qualquer adaptador Bluetooth padrão do Linux (**`source=hci0`** via `kismet_cap_linux_bluetooth`), o Kismet descobre todos os anúncios **Bluetooth Low Energy (BLE Advertisements)**, UUIDs de serviços GATT e dispositivos Bluetooth pareáveis; com um adaptador **TI CC2531 / KillerBee / NRF52840**, ele monitora redes **Zigbee / IEEE 802.15.4**; e com um dongle **RTL-SDR de US$ 25 (`source=rtl433-0`)**, ele decodifica transmissões de sensores industriais e IoT nas faixas de `315 MHz`, `433.92 MHz`, `868 MHz` e `915 MHz`!

## Exemplo
```bash
# Listar todas as interfaces e fontes de captura Multi-PHY (Wi-Fi, Bluetooth HCI, RTL-SDR, Zigbee) detectadas localmente pelo Kismet
kismet_cap_linux_bluetooth --list || true
kismet_cap_linux_wifi --list || true
```

## Limites e trade-offs
Para caçar dispositivos **Bluetooth Classic** que não estão em modo de descoberta pública (*Non-Discoverable Bluetooth*) usando hardware dedicado no Kismet, o ecossistema Kismet também suporta de primeira classe o hardware open-source **Ubertooth One (`kismet_cap_ubertooth_one`)**, que captura os *Lower Address Parts (`LAP`)* dos pacotes Bluetooth diretamente na camada física de 2.4 GHz!

## Como verificar
Combinar `source=wlan0` + `source=hci0` + `source=rtl433-0` em cada sonda Raspberry Pi instalada nos datacenters entrega visibilidade completa do espectro eletromagnético do ambiente físico em um único dashboard!

## Conexões
- [[kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls]] — Veja também: Arquitetura Distribuída de **Sensores Remotos (`kismet_cap_*`)** no Kismet: Monitorando Filiais, Andares e Datacenters a partir de um Único Servidor Central.
- [[kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json]] — Veja também: O Formato Unificado **`kismetdb` (`.kismet` SQLite3)** e os Utilitários de Extração Forense (`kismetdb_to_pcap`, `kismetdb_to_kml`, `kismetdb_dump_devices`).
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
