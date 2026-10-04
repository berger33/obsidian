---
id: software.seguranca.tranche15.001473
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

# Motor de **Detecção de Intrusão Sem Fio (WIDS)** do Kismet: Configurando Alertas **`apspoof` (Evil Twin / Rogue AP)**, **`DEAUTHFLOOD`**, **`CHANCONFLICT`** e **`CRYPTODROP`**

## Em uma frase
Como transformar o **Kismet** em um **WIDS Corporativo Ativo 24x7** que dispara um alerta imediato no SIEM (Wazuh / OpenSearch / Syslog) no exato segundo em que alguém liga um **Evil Twin (`apspoof`)** imitando o nome do Wi-Fi da sua empresa, tenta um ataque de **Deauthentication Flood (`DEAUTHFLOOD`)** ou quando um Access Point corporativo sofre downgrade de criptografia (**`CRYPTODROP`**)?

## Por que importa
O Kismet possui dezenas de assinaturas comportamentais e de estado de protocolo integradas (`kismet_alerts.conf`): **(1) `DEAUTHFLOOD` e `DISASSOCTRAFFIC`** — detectam injeção de quadros de desconexão (`aireplay-ng` / `mdk4`); **(2) `APSPOOF` (Plugin de Detecção de Rogue AP / Evil Twin)** — você declara na diretiva `apspoof=` o `SSID` da sua empresa e a lista exata de endereços MAC (`validmacs=`) dos seus Access Points legítimos.

## Como funciona
**(3) `CRYPTODROP`** — alerta se um BSSID que antes anunciava WPA2/WPA3 passar a anunciar rede aberta ou WEP!; **(4) `DHCPCONFLICT` / `ARPFLOOD`**; e **(5) `DOT11D` / `LONGSSID` / `BEACONRATE`** (anomalias e exploits de driver Wi-Fi)!

## Exemplo
```ini
# Configurar no /etc/kismet/kismet_site.conf a protecao WIDS apspoof para os SSIDs da empresa listando os OUIs/MACs oficiais dos APs legitimos
apspoof=CorpProd:ssid="Empresa-Corporativo",validmacs="aa:bb:cc:00:00:00/ff:ff:ff:00:00:00,11:22:33:44:55:66"
apspoof=CorpGuest:ssid="Empresa-Visitantes",validmacs="aa:bb:cc:00:00:00/ff:ff:ff:00:00:00"
alert=APSPOOF,10/min,1/sec
alert=DEAUTHFLOOD,10/min,2/sec
alert=CRYPTODROP,5/min,1/sec
```

## Limites e trade-offs
Olhe a precisão cirúrgica da diretiva **`apspoof=`** acima: assim que o sensor Kismet escuta no ar qualquer quadro Beacon ou Probe Response anunciando `ssid="Empresa-Corporativo"` cujo endereço MAC (`BSSID`) **não** pertença à lista `validmacs` dos seus APs reais, ele gera instantaneamente o alerta crítico **`APSPOOF`** informando o BSSID invasor, o canal exato e a intensidade de sinal RSSI em dBm para você localizar fisicamente o equipamento pirata!

## Como verificar
Você também pode usar a diretiva **`devicefound=`** (e `devicelost=`) no `kismet_site.conf` para disparar um alerta sempre que um endereço MAC específico entrar ou sair do perímetro físico de rádio do datacenter!

## Conexões
- [[kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio]] — Veja também: Configuração Resiliente com **`/etc/kismet/kismet_site.conf`** e Estratégia de **Channel Hopping Distribuído Multi-Rádio** no Kismet.
- [[kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls]] — Veja também: Arquitetura Distribuída de **Sensores Remotos (`kismet_cap_*`)** no Kismet: Monitorando Filiais, Andares e Datacenters a partir de um Único Servidor Central.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[aircrack-simulacao-rogue-ap-airbase-ng-evil-twin-karmetasploit-defesa]] — Referência cruzada direta com aircrack-simulacao-rogue-ap-airbase-ng-evil-twin-karmetasploit-defesa.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
