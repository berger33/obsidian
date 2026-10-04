---
id: software.seguranca.tranche15.001472
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

# Configuração Resiliente com **`/etc/kismet/kismet_site.conf`** e Estratégia de **Channel Hopping Distribuído Multi-Rádio** no Kismet

## Em uma frase
Se um sensor WIDS tiver apenas 1 rádio Wi-Fi tentando saltar entre os 13 canais de 2.4 GHz e os 25+ canais de 5 GHz (a uma taxa padrão de 5 canais por segundo, `channel_hop_speed=5/sec`), ele passará apenas ~2% do tempo em cada canal — podendo perder um ataque rápido que aconteça em outro canal! Como o **Kismet** resolve esse problema usando **Divisão Automática de Canais entre Múltiplos Rádios (`split_source_hopping`)** e o arquivo de sobrescrita **`kismet_site.conf`**?

## Por que importa
Primeiro, regra de ouro da documentação do Kismet: **nunca edite os arquivos base `/etc/kismet/kismet.conf` ou `kismet_alerts.conf` diretamente** (pois eles são sobrescritos nas atualizações de pacotes!). Coloque todas as suas fontes (`source=`), alertas WIDS e configurações customizadas dentro de **`/etc/kismet/kismet_site.conf`**, que tem precedência automática sobre todos os outros arquivos!

## Como funciona
Segundo, quando você conecta 2 ou 3 adaptadores Wi-Fi no mesmo sensor (ex.: `wlan0` dedicado a 2.4 GHz `channels="1,6,11"` e `wlan1` + `wlan2` dedicados a 5 GHz), o Kismet habilita por padrão **`split_source_hopping=true`**: ele embaralha e divide os canais entre as interfaces para que duas placas nunca desperdicem tempo escutando o mesmo canal simultaneamente!

## Exemplo
```ini
# Exemplo de /etc/kismet/kismet_site.conf dedicando um radio aos canais principais de 2.4GHz (1,6,11) e dois radios para varredura completa de 5GHz + BLE
server_name=Sensor-WIDS-Datacenter-SP
log_prefix=/var/log/kismet/
source=wlan0:name=Radio_24GHz,hop=true,channels="1,6,11",channel_hop_speed=5/sec
source=wlan1:name=Radio_5GHz_A,hop=true,band5ghz=true,channel_hop_speed=10/sec
source=hci0:name=Bluetooth_BLE_Sensor
```

## Limites e trade-offs
Veja na configuração do `Radio_24GHz` acima o parâmetro **`channels="1,6,11"`**: como na banda de 2.4 GHz os canais 1, 6 e 11 são os únicos três canais que não se sobrepõem (e onde 98% dos APs operam), restringir o rádio de 2.4 GHz a saltar apenas entre `1, 6 e 11` aumenta em **400% o tempo de escuta útil** em comparação a varrer os 14 canais!

## Como verificar
E se você quiser travar um rádio extra permanentemente no canal exato do seu SSID corporativo principal para ter **100% de captura em tempo real sem nenhum salto**, basta definir `source=wlan2:name=Fixo_Canal36,hop=false,channel=36`!

## Conexões
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Veja também: Arquitetura do **Kismet (`kismetwireless/kismet`)**: Sistema de **Detecção de Intrusão Sem Fio (WIDS)** e Sniffer RF Passivo Multi-Protocolo (**Wi-Fi, Bluetooth/BLE, Zigbee e SDR**).
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Veja também: Motor de **Detecção de Intrusão Sem Fio (WIDS)** do Kismet: Configurando Alertas **`apspoof` (Evil Twin / Rogue AP)**, **`DEAUTHFLOOD`**, **`CHANCONFLICT`** e **`CRYPTODROP`**.
- [[kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls]] — Referência cruzada direta com kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls.
- [[aircrack-modo-monitor-airmon-ng-check-kill-mac80211-canais-5ghz-6ghz]] — Referência cruzada direta com aircrack-modo-monitor-airmon-ng-check-kill-mac80211-canais-5ghz-6ghz.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
