---
id: software.seguranca.tranche15.001467
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

# Descriptografia de Capturas 802.11 (`.cap` / `.pcap`) com **`airdecap-ng`**: Removendo Cabeçalhos 802.11 e Decifrando Tráfego WPA/WPA2 (`CCMP`/`TKIP`) para Análise Forense

## Em uma frase
Imagine este cenário de **DFIR / Perícia Forense de Rede**: você capturou um arquivo `.pcap` em Modo Monitor (`airodump-ng`) da rede Wi-Fi do seu próprio laboratório ou de um segmento IoT onde **você já conhece a senha WPA2-PSK (`-p`) ou a PMK (`-k`)**, mas ao abrir o arquivo no `tcpdump` ou no `Zeek` / `Snort 3`, os pacotes aparecem apenas como quadros `802.11 Data` criptografados com `AES-CCMP`!

## Por que importa
Como decifrar todos os pacotes de uma captura Wi-Fi 802.11 e convertê-los em um arquivo `.pcap` padrão com quadros Ethernet desencapsulados pronto para o **Zeek**, **Suricata**, **Snort 3**, **Arkime** ou **Wireshark**?

## Como funciona
Usando o utilitário oficial **`airdecap-ng`** da suíte Aircrack-ng! Quando você executa **`airdecap-ng -e "NomeDoSSID" -p "SenhaDaRede" captura.cap`**, o `airdecap-ng` localiza na captura o **4-Way Handshake EAPOL** de cada estação cliente que conectou, deriva a **PTK (*Pairwise Transient Key*)** específica de cada sessão a partir dos nonces (`ANonce` + `SNonce`), descriptografa todos os pacotes `AES-CCMP`/`TKIP` daquela sessão e grava o arquivo **`captura-dec.cap`**!

## Exemplo
```bash
# Descriptografar um arquivo .cap WPA2-PSK (contendo o 4-way handshake das sessoes) usando airdecap-ng e inspecionar o trafego decifrado no tcpdump
airdecap-ng -b AA:BB:CC:DD:EE:FF -e "IoT-Lab-WiFi" -p "SenhaLabIoT#2026" ./captura_iot-01.cap
tcpdump -n -r ./captura_iot-01-dec.cap | head -n 20
```

## Limites e trade-offs
Por que o **`airdecap-ng`** precisa que o **4-Way Handshake EAPOL** da sessão do cliente esteja presente dentro do arquivo `.cap` mesmo quando você já informa a senha `-p` correta da rede WPA2-PSK? Porque no WPA2-PSK, o tráfego de dados não é cifrado diretamente pela senha (`PMK`): cada vez que um cliente conecta ao AP, um novo par de nonces aleatórios (`ANonce` e `SNonce`) é gerado no 4-Way Handshake para derivar uma **`PTK` efêmera exclusiva daquela conexão**! Sem o 4-Way Handshake daquela conexão no `.cap`, não há os nonces para calcular a `PTK`!

## Como verificar
E se a captura for de uma rede aberta (Open Wi-Fi sem criptografia), mas você quiser remover os cabeçalhos 802.11/Radiotap e convertê-la em pacotes Ethernet padrão para ferramentas que não entendem quadros 802.11? Basta rodar **`airdecap-ng -b AA:BB:CC:DD:EE:FF captura_aberta.cap`** sem `-p`/`-w`!

## Conexões
- [[aircrack-precomputacao-pmk-airolib-ng-sqlite-rainbow-tables-essid]] — Veja também: Pré-Computação de **Pairwise Master Keys (`PMK`)** com **`airolib-ng`** e `aircrack-ng -r`: Acelerando Auditorias em `1.000x` sobre SSIDs Padronizados.
- [[aircrack-analise-grafos-airgraph-ng-relacoes-capr-cpg-clientes-probes]] — Veja também: Mapeamento Visual de Relações Sem Fio com **`airgraph-ng`**: Grafos **`CAPR` (*Client to AP Relationship*)** e **`CPG` (*Common Probe Graph*)** a partir do CSV do `airodump-ng`.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Referência cruzada direta com aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
