---
id: software.seguranca.tranche15.001461
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

# Arquitetura da Suíte **Aircrack-ng (`aircrack-ng/aircrack-ng`)**: Os 4 Pilares da Auditoria de Redes Sem Fio **IEEE 802.11** (Monitoramento, Injeção, Testes de Driver e Cracking SIMD)

## Em uma frase
Como funciona a suíte open-source **Aircrack-ng** — o padrão mundial de avaliação de segurança de redes Wi-Fi (`IEEE 802.11a/b/g/n/ac/ax`) em Linux, BSD, macOS e Windows — e como seus utilitários de linha de comando se dividem nas **4 áreas descritas no `README.md` oficial**?

## Por que importa
Diferente de um programa monolítico, o Aircrack-ng é um conjunto de ferramentas Unix especializadas que trabalham em pipeline: **(1) `Monitoring` (`airmon-ng` + `airodump-ng`)** — coloca a placa de rede sem fio em **Monitor Mode (`rfmon`)** e captura todos os quadros 802.11 brutos (Beacons, Probe Requests, Data, EAPOL Handshakes) gravando em arquivos `.cap`/`.pcap`, `.csv` e `.kismet.netxml`; **(2) `Testing` (`aireplay-ng --test`)** — verifica se o chipset e o driver (`mac80211` / `libnl`) suportam captura e **Injeção de Quadros 802.11** em cada canal.

## Como funciona
**(3) `Attacking` (`aireplay-ng`, `airbase-ng`)** — testa resiliência contra replay, desautenticação (validando se **802.11w PMF** está ativo!) e Rogue APs; e **(4) `Cracking` (`aircrack-ng`, `airolib-ng`)** — auditoria criptográfica de chaves acelerada por **SIMD (`SSE2`, `AVX`, `AVX2`, `AVX-512` e ARM NEON)**!

## Exemplo
```bash
# Verificar a versao e as instrucoes SIMD (AVX2/AVX-512) suportadas pela CPU no aircrack-ng e listar as interfaces Wi-Fi disponiveis com airmon-ng
aircrack-ng -u
airmon-ng
```

## Limites e trade-offs
Veja o comando **`aircrack-ng -u`** (*CPU detection*) acima: ele informa exatamente quais conjuntos de instruções vetoriais SIMD (`AVX-512`, `AVX2`, `AVX`, `SSE2`, `ASIMD`) e quantos núcleos físicos/lógicos via biblioteca **`hwloc`** o `aircrack-ng` selecionou automaticamente na sua máquina para maximizar a taxa de cálculo de `PBKDF2-HMAC-SHA1`!

## Como verificar
Para uso em laboratório de treinamento ou pipelines de CI/CD no Linux sem precisar de adaptadores Wi-Fi USB físicos, você pode carregar o módulo nativo do Kernel Linux **`mac80211_hwsim`** (`modprobe mac80211_hwsim radios=2`), que cria interfaces de rádio 802.11 virtuais perfeitas para testar toda a suíte `aircrack-ng`, `hostapd` e `wpa_supplicant`!

## Conexões
- [[aircrack-modo-monitor-airmon-ng-check-kill-mac80211-canais-5ghz-6ghz]] — Veja também: Gerenciamento de Modo Monitor (**Monitor Mode / `rfmon`**) com **`airmon-ng`**: `check kill`, Pilha Linux `mac80211` (`nl80211`) e Canais 2.4 GHz / 5 GHz.
- [[aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd]] — Referência cruzada direta com aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
