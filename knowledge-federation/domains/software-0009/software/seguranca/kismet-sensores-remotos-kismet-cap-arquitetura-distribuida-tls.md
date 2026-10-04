---
id: software.seguranca.tranche15.001474
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

# Arquitetura Distribuída de **Sensores Remotos (`kismet_cap_*`)** no Kismet: Monitorando Filiais, Andares e Datacenters a partir de um Único Servidor Central

## Em uma frase
Uma grande empresa tem 10 andares no prédio principal e 5 datacenters/filiais. Como os sinais de rádio Wi-Fi e Bluetooth de 2.4 GHz / 5 GHz não atravessam vários andares de concreto, como monitorar o espectro de RF de todos os andares e filiais **concentrando tudo em um único servidor central do Kismet** sem precisar instalar o servidor completo em cada andar?

## Por que importa
Através da arquitetura de **Remote Capture Datasources (`kismet_cap_*`)** do Kismet!

## Como funciona
Os binários de captura do Kismet (**`kismet_cap_linux_wifi`**, **`kismet_cap_linux_bluetooth`**, **`kismet_cap_pcapfile`**, **`kismet_cap_sdr_rtl433`**) são programas em C ultraleves e independentes que podem rodar em qualquer pequeno dispositivo de borda (como um Raspberry Pi, roteador OpenWrt ou mini-PC de US$ 30 instalado no forro de cada andar!) e conectar de saída via **TCP/TLS ou WebSockets (`--connect` + `--apikey` + `--ssl`)** ao servidor Kismet central!

## Exemplo
```bash
# Executar em uma sonda remota leve (ex.: Raspberry Pi no 5o andar) o coletor kismet_cap_linux_wifi enviando os quadros via TLS/WebSocket ao servidor central
kismet_cap_linux_wifi \
  --connect https://kismet-central.exemplo.br:2501 \
  --ssl \
  --apikey "${KISMET_SENSOR_APIKEY}" \
  --source=wlan0:name=Sensor_Andar_05,uuid=550e8400-e29b-41d4-a716-446655440005
```

## Limites e trade-offs
Veja as três vantagens arquiteturais de usar sondas remotas **`kismet_cap_linux_wifi`** conectadas ao servidor central: **(1) Segurança da Sonda**: a sonda remota no forro do prédio **não armazena nenhum log ou banco de dados local** e se autentica no servidor central usando uma **API Key restrita exclusivamente ao papel `datasource`**!; **(2) Fixação de UUID (`uuid=...`)**: ao atribuir um UUID determinístico a cada sonda de andar, o Kismet central sabe exatamente qual andar viu um Rogue AP com sinal `-40 dBm` (muito perto!) versus `-85 dBm` (longe), permitindo **triangular a sala física do dispositivo invasor**!; e **(3) Gerenciamento Centralizado de Canais**!

## Como verificar
No servidor Kismet central, habilite `remote_capture_listen=0.0.0.0` (ou interface da VLAN de gerência) protegido por TLS/Proxy Reverso e gere uma API Key individual por sonda na Web UI (`Settings -> API Keys -> role: datasource`).

## Conexões
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Veja também: Motor de **Detecção de Intrusão Sem Fio (WIDS)** do Kismet: Configurando Alertas **`apspoof` (Evil Twin / Rogue AP)**, **`DEAUTHFLOOD`**, **`CHANCONFLICT`** e **`CRYPTODROP`**.
- [[kismet-monitoramento-bluetooth-ble-zigbee-sdr-iot-seguranca-fisica]] — Veja também: Além do Wi-Fi: Monitoramento de **Bluetooth / BLE (`kismet_cap_linux_bluetooth`)**, **Zigbee (`802.15.4`)** e **Rádio Definido por Software (`RTL-SDR`)** no Kismet.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio]] — Referência cruzada direta com kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio.
- [[kismet-seguranca-execucao-suid-grupo-kismet-privsep-api-keys]] — Referência cruzada direta com kismet-seguranca-execucao-suid-grupo-kismet-privsep-api-keys.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
