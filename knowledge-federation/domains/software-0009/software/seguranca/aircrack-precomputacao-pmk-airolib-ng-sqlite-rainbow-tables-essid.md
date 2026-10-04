---
id: software.seguranca.tranche15.001466
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

# Pré-Computação de **Pairwise Master Keys (`PMK`)** com **`airolib-ng`** e `aircrack-ng -r`: Acelerando Auditorias em `1.000x` sobre SSIDs Padronizados

## Em uma frase
Por que o cálculo da **PMK (`PBKDF2-HMAC-SHA1` com 4.096 iterações)** consome 99,9% do tempo de CPU ao auditar uma senha WPA/WPA2-PSK, e por que o padrão Wi-Fi usa o **nome da rede (`ESSID`)** como o *Salt* dessa função `PBKDF2`?

## Por que importa
Ao usar o `ESSID` como *Salt*, os criadores do 802.11i quiseram impedir que uma única tabela pré-computada global funcionasse para qualquer nome de rede. Porém, se uma organização usa um `ESSID` comum ou padronizado em 50 filiais (ex.: `Corporativo`, `Visitantes`, `Matriz-WiFi`), o *Salt* (`ESSID`) é exatamente o mesmo em todas as 50 filiais!

## Como funciona
A suíte Aircrack-ng inclui o utilitário **`airolib-ng`** (baseado em **SQLite3**): ele permite pré-computar uma vez as `PMKs` para os seus `ESSIDs` e dicionários de auditoria (`airolib-ng banco_pmk.sqlite --batch`), e depois passar **`aircrack-ng -r banco_pmk.sqlite captura.cap`** para testar **milhões de chaves por segundo quase instantaneamente**, pois a etapa cara do `PBKDF2` já está pronta no banco!

## Exemplo
```bash
# Criar um banco SQLite3 no airolib-ng, importar o ESSID alvo e a lista de senhas, pre-computar as PMKs (--batch) e auditar com aircrack-ng -r
echo "Matriz-WiFi" > ./essid_alvo.txt
airolib-ng ./pmk_db.sqlite --import essid ./essid_alvo.txt
airolib-ng ./pmk_db.sqlite --import passwd ./dicionario_auditoria.txt
airolib-ng ./pmk_db.sqlite --batch
airolib-ng ./pmk_db.sqlite --stats
aircrack-ng -r ./pmk_db.sqlite ./auditoria_corp-01.cap
```

## Limites e trade-offs
Qual é a lição de defesa imediata que o **`airolib-ng`** ensina aos arquitetos de redes sem fio? **JAMAIS utilize nomes de rede (`ESSID`) genéricos ou padrão de fabricante (como `default`, `linksys`, `dlink`, `corporate`, `wifi`)**, pois já existem tabelas públicas de `PMKs` pré-computadas para os 1.000 `ESSIDs` mais comuns do mundo! Use sempre um `ESSID` exclusivo da sua organização combinado com uma senha longa (> 20 caracteres aleatórios) ou, melhor ainda, migre a rede corporativa para **WPA2/WPA3-Enterprise (`802.1X EAP-TLS`)**!

## Como verificar
Use `airolib-ng ./pmk_db.sqlite --clean all` para remover entradas inválidas e executar `VACUUM` otimizando o banco SQLite.

## Conexões
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Veja também: Anatomia do **4-Way Handshake EAPOL** no WPA/WPA2-PSK e Auditoria com **`aircrack-ng -w`**: `PMK`, `PTK`, `ANonce`, `SNonce`, `MIC` e Pares de Mensagens (`2+3` ou `3+4`).
- [[aircrack-descriptografia-trafego-pcap-airdecap-ng-wpa2-wep-wireshark]] — Veja também: Descriptografia de Capturas 802.11 (`.cap` / `.pcap`) com **`airdecap-ng`**: Removendo Cabeçalhos 802.11 e Decifrando Tráfego WPA/WPA2 (`CCMP`/`TKIP`) para Análise Forense.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[aircrack-evolucao-wpa3-sae-dragonfly-wpa2-enterprise-8021x-mitigacao]] — Referência cruzada direta com aircrack-evolucao-wpa3-sae-dragonfly-wpa2-enterprise-8021x-mitigacao.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
