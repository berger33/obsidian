---
id: software.seguranca.tranche15.001462
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
fontes: ["https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md", "https://www.aircrack-ng.org/doku.php?id=aircrack-ng"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gerenciamento de Modo Monitor (**Monitor Mode / `rfmon`**) com **`airmon-ng`**: `check kill`, Pilha Linux `mac80211` (`nl80211`) e Canais 2.4 GHz / 5 GHz

## Em uma frase
Qual é a diferença fundamental entre o **Modo Promíscuo (*Promiscuous Mode*)** de uma placa Ethernet comum e o **Modo Monitor (*Monitor Mode / `rfmon`*)** habilitado pelo **`airmon-ng start wlan0`** em uma placa Wi-Fi 802.11, e por que esquecer de rodar **`airmon-ng check kill`** antes da auditoria faz a captura perder o 4-Way Handshake?

## Por que importa
Em uma placa Wi-Fi normal (*Managed Mode*), o firmware do rádio só entrega ao sistema operacional pacotes depois de associado a um único Access Point e já convertidos em quadros Ethernet 802.3 falsos. Já no **Modo Monitor (`wlan0mon`)**, a placa não precisa se associar a nenhum AP e entrega ao kernel **100% dos quadros brutos de rádio IEEE 802.11 (Management, Control e Data) precedidos pelo cabeçalho `Radiotap`** (que traz a potência de sinal RSSI em dBm, canal/frequência e taxa de modulação)!

## Como funciona
E por que rodar **`airmon-ng check kill`** antes de `airmon-ng start` é obrigatório? Porque gerenciadores de rede de desktop (`NetworkManager`, `wpa_supplicant`, `avahi-daemon`) ficam tentando reconectar a placa ou varrer canais em background — se o `wpa_supplicant` mudar a placa para o canal 1 no exato segundo em que você estava capturando um Handshake no canal 36, você perde os pacotes EAPOL!

## Exemplo
```bash
# Identificar e encerrar processos interferentes (NetworkManager/wpa_supplicant) e habilitar uma interface virtual em Modo Monitor no canal 36 (5 GHz)
airmon-ng check
airmon-ng check kill
airmon-ng start wlan0 36
iw dev
```

## Limites e trade-offs
Como o **`airmon-ng`** conversa com o Kernel Linux moderno? Através das bibliotecas **`libnl-3` / `libnl-genl-3` (Netlink `nl80211`)**, além de `ethtool`, `usbutils` e `pciutils` para identificar com precisão o barramento (`USB`, `PCIe`, `SDIO`), o driver (`ath9k_htc`, `mt76x2u`, `rtl88XXau`, `iwlwifi`) e o chipset exato da placa de rede!

## Como verificar
Ao finalizar o teste autorizado, basta rodar **`airmon-ng stop wlan0mon && systemctl start NetworkManager`** para destruir a interface monitor e devolver a estação à operação normal.

## Conexões
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Veja também: Arquitetura da Suíte **Aircrack-ng (`aircrack-ng/aircrack-ng`)**: Os 4 Pilares da Auditoria de Redes Sem Fio **IEEE 802.11** (Monitoramento, Injeção, Testes de Driver e Cracking SIMD).
- [[aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd]] — Veja também: Reconhecimento e Captura Seletiva 802.11 com **`airodump-ng`**: Bandas (`--band abg`), Filtros `--bssid` / `--essid-regex`, Quadros `PWR`/`Beacons` e `EAPOL`.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
