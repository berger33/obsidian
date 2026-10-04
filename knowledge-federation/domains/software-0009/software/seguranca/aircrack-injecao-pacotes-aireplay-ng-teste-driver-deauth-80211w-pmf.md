---
id: software.seguranca.tranche15.001464
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

# Injeção de Quadros e Teste de Resiliência **IEEE 802.11w (`PMF` — *Protected Management Frames*)** com **`aireplay-ng`**: `--test` (`-9`) e `--deauth` (`-0`)

## Em uma frase
Por que nas redes Wi-Fi antigas (WPA2 sem 802.11w) qualquer pessoa de fora da rede conseguia desconectar instantaneamente um cliente legítimo enviando apenas alguns pacotes falsos de desautenticação (`aireplay-ng -0`), e **como o padrão `IEEE 802.11w` (*Protected Management Frames — PMF*, obrigatório no WPA3!) derrota completamente esse ataque**?

## Por que importa
Porque no padrão 802.11 original, apenas os quadros de *Dados* eram criptografados, enquanto os **Quadros de Gerenciamento (*Management Frames*: `Deauthentication`, `Disassociation`, `Action`) viajavam em texto claro sem nenhuma assinatura criptográfica (`MIC`)**! Assim, bastava falsificar o endereço MAC do Access Point (`-a <BSSID>`) e enviar um quadro `Deauth` para o MAC do cliente (`-c <CLIENT_MAC>`) para forçá-lo a reconectar e capturar o *4-Way Handshake*!

## Como funciona
Com o **IEEE 802.11w (`PMF = Required` / `ieee80211w=2` no `hostapd`)**, os quadros de `Deauthentication` e `Disassociation` unicast são cifrados e autenticados pela chave de sessão e os quadros broadcast são assinados pelo protocolo **BIP (`Broadcast/Multicast Integrity Protocol` — `AES-CMAC`)**: quando você roda um teste autorizado de `aireplay-ng --deauth` contra uma rede com **802.11w PMF ativo**, o cliente valida o `MIC`, descarta os quadros falsos na hora e **a conexão Wi-Fi não cai**!

## Exemplo
```bash
# Testar se a placa Wi-Fi e o driver suportam injecao de pacotes 802.11 (--test) e validar se o AP alvo possui protecao 802.11w PMF contra Deauth
aireplay-ng --test wlan0mon
aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon
```

## Limites e trade-offs
Sempre execute **`aireplay-ng --test wlan0mon`** (atalho `-9`) antes de iniciar uma auditoria ativa: ele faz um * Injection Test* local verificando a qualidade da transmissão da placa e listando com quais APs próximos a injeção alcança 100% de resposta!

## Como verificar
Como recomendação imediata de defesa em qualquer auditoria de rede sem fio corporativa: configure todos os SSIDs nos controladores Wi-Fi (Cisco, Aruba, Ubiquiti UniFi, FortiAP, `hostapd`) com **802.11w Protected Management Frames (`PMF`) habilitado (`Required` em SSIDs WPA3/WPA2 modernos)**.

## Conexões
- [[aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd]] — Veja também: Reconhecimento e Captura Seletiva 802.11 com **`airodump-ng`**: Bandas (`--band abg`), Filtros `--bssid` / `--essid-regex`, Quadros `PWR`/`Beacons` e `EAPOL`.
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Veja também: Anatomia do **4-Way Handshake EAPOL** no WPA/WPA2-PSK e Auditoria com **`aircrack-ng -w`**: `PMK`, `PTK`, `ANonce`, `SNonce`, `MIC` e Pares de Mensagens (`2+3` ou `3+4`).
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Referência cruzada direta com kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
