---
id: software.seguranca.tranche15.001468
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

# Mapeamento Visual de Relações Sem Fio com **`airgraph-ng`**: Grafos **`CAPR` (*Client to AP Relationship*)** e **`CPG` (*Common Probe Graph*)** a partir do CSV do `airodump-ng`

## Em uma frase
Durante uma auditoria física ou investigação de segurança em um grande prédio comercial com dezenas de Access Points e centenas de notebooks/smartphones, ler manualmente milhares de linhas do arquivo `.csv` gerado pelo `airodump-ng` é exaustivo. Como transformar o `.csv` do `airodump-ng` em **diagramas visuais de grafos (PNG/DOT Graphviz)** que mostram instantaneamente quem está conectado onde e quais dispositivos pertencem à mesma organização?

## Por que importa
Com o utilitário oficial **`airgraph-ng`** da suíte Aircrack-ng!

## Como funciona
O `airgraph-ng` lê o arquivo `-01.csv` gerado pelo `airodump-ng` e produz **dois tipos de grafos analíticos (`-g`)**: **(1) `CAPR` (*Client to AP Relationship*)** — desenha cada Access Point (colorido pelo tipo de criptografia: verde para WPA2/WPA3, amarelo para WEP, vermelho para Open!) e liga por setas todos os clientes (`STATION`) associados a cada AP; e **(2) `CPG` (*Common Probe Graph*)** — agrupa todos os dispositivos clientes que enviaram *Probe Requests* procurando pelos mesmos nomes de redes salvas (`Probed ESSIDs`)!

## Exemplo
```bash
# Gerar a partir do arquivo CSV do airodump-ng o grafo de associacoes Cliente-AP (CAPR) e o grafo de Probes em comum (CPG) usando airgraph-ng
airgraph-ng -i ./auditoria_corp-01.csv -o ./grafo_clientes_ap.png -g CAPR
airgraph-ng -i ./auditoria_corp-01.csv -o ./grafo_probes_comuns.png -g CPG
```

## Limites e trade-offs
Por que o grafo **`CPG` (*Common Probe Graph*)** e a coluna `Probes` do `airodump-ng` representam um alerta importante de privacidade e OPSEC para dispositivos corporativos? Porque quando um notebook ou celular com Wi-Fi ligado fora do escritório envia *Directed Probe Requests* perguntando `"A rede Corp-Interna-Secreta está por perto?"`, ele revela para qualquer sensor passivo o histórico de redes onde aquele dispositivo já conectou!

## Como verificar
Em sistemas operacionais modernos (Linux NetworkManager `wifi.scan-rand-mac-address=yes`, iOS, Android, Windows 11), mantenha sempre ativa a **Randomização de Endereço MAC durante Scans de Probe (`MAC Address Randomization`)** e desative a opção *"Connect automatically / Send directed probes"* para SSIDs corporativos que não estejam ocultos.

## Conexões
- [[aircrack-descriptografia-trafego-pcap-airdecap-ng-wpa2-wep-wireshark]] — Veja também: Descriptografia de Capturas 802.11 (`.cap` / `.pcap`) com **`airdecap-ng`**: Removendo Cabeçalhos 802.11 e Decifrando Tráfego WPA/WPA2 (`CCMP`/`TKIP`) para Análise Forense.
- [[aircrack-simulacao-rogue-ap-airbase-ng-evil-twin-karmetasploit-defesa]] — Veja também: Simulação de **Rogue Access Point / Evil Twin** com **`airbase-ng`** e Detecção de Ataques de Associação Automática em Auditorias Red Team.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd]] — Referência cruzada direta com aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
