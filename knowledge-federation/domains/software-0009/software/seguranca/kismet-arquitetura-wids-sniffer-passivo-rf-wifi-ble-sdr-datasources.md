---
id: software.seguranca.tranche15.001471
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

# Arquitetura do **Kismet (`kismetwireless/kismet`)**: Sistema de **Detecção de Intrusão Sem Fio (WIDS)** e Sniffer RF Passivo Multi-Protocolo (**Wi-Fi, Bluetooth/BLE, Zigbee e SDR**)

## Em uma frase
Qual é a diferença fundamental entre uma ferramenta de auditoria pontual e o **Kismet (`kismetwireless/kismet`)** — o motor open-source padrão mundial de **Wireless Intrusion Detection System (WIDS)**, monitoramento contínuo de espectro e captura de pacotes sem fio?

## Por que importa
Três características tornam o Kismet único na defesa cibernética: **(1) Operação 100% Passiva (*Zero-Emission Passive Sniffing*)** — o Kismet jamais transmite um único quadro de rádio para descobrir redes; ele reconstrói inclusive **SSIDs Ocultos (*Hidden SSIDs*) e clientes silenciosos** apenas observando passivamente os quadros de dados e associação no ar!.

## Como funciona
**(2) Arquitetura Multi-Física (*Multi-PHY RF*)** — muito além do Wi-Fi (`IEEE 802.11a/b/g/n/ac/ax`), o Kismet monitora simultaneamente **Bluetooth / Bluetooth Low Energy (BLE)**, **Zigbee / 802.15.4**, **Sensores RF 433/915 MHz (`RTL-SDR`: termômetros, medidores inteligentes `rtl_433`, TPMS)** e **Aviação ADS-B (`rtladsb`)**!; e **(3) Motor WIDS 24x7 com Sensores Remotos Distribuídos** e Web UI moderna (`:2501`)!

## Exemplo
```bash
# Iniciar o servidor Kismet especificando uma fonte de captura Wi-Fi (-c) em modo daemon/headless e verificar a porta da Web UI/API REST (:2501)
kismet --version
kismet -c wlan0 --daemonize --no-ncurses-wrapper
ss -tulnp | grep 2501 || true
```

## Limites e trade-offs
No modelo de configuração moderno do Kismet, você nunca precisa colocar a placa Wi-Fi em modo monitor manualmente antes de rodar o programa: basta passar **`-c wlan0`** (ou declarar `source=wlan0:name=SensorMatriz` no `/etc/kismet/kismet_site.conf`), e o binário auxiliar de captura **`kismet_cap_linux_wifi`** gerencia sozinho a criação da interface monitor `wlan0mon`, o controle de `rfkill` e o salto rápido de canais (*Channel Hopping*)!

## Como verificar
Na primeira vez que o Kismet inicia, ele gera automaticamente um usuário e senha administrativos em **`~/.kismet/kismet_httpd.conf`** e escuta por padrão apenas em `127.0.0.1:2501`.

## Conexões
- [[kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio]] — Veja também: Configuração Resiliente com **`/etc/kismet/kismet_site.conf`** e Estratégia de **Channel Hopping Distribuído Multi-Rádio** no Kismet.
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Referência cruzada direta com kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
