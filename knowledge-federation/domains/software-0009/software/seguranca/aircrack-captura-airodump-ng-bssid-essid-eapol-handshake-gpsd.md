---
id: software.seguranca.tranche15.001463
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

# Reconhecimento e Captura Seletiva 802.11 com **`airodump-ng`**: Bandas (`--band abg`), Filtros `--bssid` / `--essid-regex`, Quadros `PWR`/`Beacons` e `EAPOL`

## Em uma frase
Como usar o **`airodump-ng`** durante uma auditoria de segurança Wi-Fi corporativa para mapear todos os Access Points e clientes nas bandas de **2.4 GHz e 5 GHz (`--band abg`)**, identificar APs não autorizados (*Rogue APs*) e focar a captura em um canal e `BSSID` específicos para registrar o **4-Way Handshake EAPOL**?

## Por que importa
Na fase inicial de descoberta, você executa **`airodump-ng --band abg --wps --uptime wlan0mon`**: o `airodump-ng` salta continuamente entre todos os canais de 2.4 GHz (`b/g`) e 5 GHz (`a`) exibindo na metade superior da tela todos os Access Points (`BSSID`, potência `PWR` em dBm, `Beacons`, pacotes de dados `#Data`, canal `CH`, velocidade máxima `MB`, cifra `ENC: WPA2/WPA3`, `CIPHER: CCMP` e `AUTH: PSK/MGT/SAE`) e, na metade inferior, todas as estações clientes (`STATION`), a qual `BSSID` estão associadas e quais redes elas estão procurando (`Probes`)!

## Como funciona
Depois de identificar o AP alvo da auditoria, você **trava o `airodump-ng` no canal e BSSID exatos (`-c 36 --bssid AA:BB:CC:DD:EE:FF -w captura_alvo`)** para não perder nenhum quadro durante o salto de canais!

## Exemplo
```bash
# Mapear APs nas bandas 2.4GHz e 5GHz filtrando pelo padrao de nome da empresa (--essid-regex) e depois focar a captura em um BSSID e canal especificos
airodump-ng --band abg --essid-regex "^Corp-WiFi-.*" wlan0mon
airodump-ng -c 36 --bssid AA:BB:CC:DD:EE:FF -w ./auditoria_corp wlan0mon
```

## Limites e trade-offs
Quais são os 5 arquivos gerados automaticamente no disco pelo `-w ./auditoria_corp` do `airodump-ng` (controláveis também via `--output-format pcap,csv,netxml`)? **(1) `.cap` / `.pcap`** (os quadros 802.11 brutos); **(2) `.csv`** (planilha detalhada de todos os APs e clientes vistos com timestamps de primeira/última aparição); **(3) `.kismet.csv`**; **(4) `.kismet.netxml`** (estrutura XML completa de redes e clientes); e **(5) `.log.csv`** (coordenadas GPS + sinal quando integrado ao `gpsd`)!

## Como verificar
Como sabe se o `airodump-ng` conseguiu capturar o **4-Way Handshake WPA/WPA2** com sucesso? No canto superior direito da tela do terminal aparecerá imediatamente o aviso **`WPA handshake: AA:BB:CC:DD:EE:FF`**!

## Conexões
- [[aircrack-modo-monitor-airmon-ng-check-kill-mac80211-canais-5ghz-6ghz]] — Veja também: Gerenciamento de Modo Monitor (**Monitor Mode / `rfmon`**) com **`airmon-ng`**: `check kill`, Pilha Linux `mac80211` (`nl80211`) e Canais 2.4 GHz / 5 GHz.
- [[aircrack-injecao-pacotes-aireplay-ng-teste-driver-deauth-80211w-pmf]] — Veja também: Injeção de Quadros e Teste de Resiliência **IEEE 802.11w (`PMF` — *Protected Management Frames*)** com **`aireplay-ng`**: `--test` (`-9`) e `--deauth` (`-0`).
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Referência cruzada direta com aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
