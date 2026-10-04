---
id: software.seguranca.tranche06.000566
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/bettercap/bettercap/master/README.md", "https://raw.githubusercontent.com/bettercap/caplets/master/README.md", "https://www.bettercap.org/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bettercap: Auditoria de Redes Sem Fio **WiFi 802.11** (`wifi.recon`, Descoberta de APs/Clientes, Captura EAPOL/PMKID e Validação de **802.11w PMF**)

## Em uma frase
O módulo **`wifi`** do Bettercap transforma uma interface sem fio compatível com modo monitor e injeção de quadros em um analisador completo do espectro **IEEE 802.11 (2.4 GHz / 5 GHz / 6 GHz)**.

## Por que importa
Permite mapear todos os Access Points (BSSID, ESSID, canal, largura de banda, RSSI, cifra WPA2/WPA3-PSK ou 802.1X Enterprise e clientes associados via `wifi.show`), detectar *Rogue APs* / *Evil Twins* no perímetro físico da empresa e auditar se a rede corporativa está protegida contra ataques de desautenticação e captura *clientless* de **RSN PMKID**.

## Como funciona
Ao auditar um SSID de homologação da própria empresa, se o Access Point **não** estiver com **IEEE 802.11w (*Protected Management Frames — PMF*)** obrigatório (ou WPA3-SAE), quadros de gerência `Deauthentication` não-autenticados derrubarão clientes ou o AP exporá o hash `PMKID` no primeiro quadro EAPOL; já com **802.11w PMF (`MFP Required`) + WPA3/802.1X**, quadros de desautenticação forjados são ignorados pelos clientes.

## Exemplo
```text
# Reconhecimento passivo de espectro WiFi 802.11 filtrando canais de 5 GHz e salvando quadros EAPOL em PCAP
set wifi.interface wlan0mon
set wifi.handshakes.file /cases/pcaps/wifi_audit_eapol.pcap
wifi.recon on
wifi.recon.channel 36,40,44,48,149,153,157,161
wifi.show
```

## Limites e trade-offs
Em ambientes corporativos de produção, o padrão de segurança obrigatório é **WPA2/WPA3-Enterprise (802.1X EAP-TLS)** com validação estrita do certificado do servidor RADIUS no supplicant e **802.11w Protected Management Frames (PMF)** habilitado.

## Como verificar
Inspecione os beacons capturados no Wireshark (`wlan.rsn.capabilities.mfpr == 1`) para confirmar que a flag *Management Frame Protection Required* está ativa no SSID corporativo.

## Conexões
- [[bettercap-sniffer-rede-net-sniff-filtros-bpf-expressao-regular]] — Veja também: Bettercap: Captura Seletiva e Inspeção de Tráfego com `net.sniff` (Filtros BPF, Expressões Regulares e Gravação PCAP).
- [[bettercap-auditoria-bluetooth-low-energy-ble-recon-enum-gatt]] — Veja também: Bettercap: Auditoria de Dispositivos **Bluetooth Low Energy (BLE)** (`ble.recon`, `ble.show`, `ble.enum` e Inspeção de Características **GATT**).
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
