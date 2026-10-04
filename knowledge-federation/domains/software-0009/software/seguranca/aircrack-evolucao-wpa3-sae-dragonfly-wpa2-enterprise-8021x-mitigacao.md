---
id: software.seguranca.tranche15.001470
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

# Do WEP (`PTW`/`KoreK`) e WPA2-PSK ao **WPA3-SAE (*Simultaneous Authentication of Equals* / Dragonfly)** e **OWE**: Por que o WPA3 Elimina o Cracking Offline de Handshakes?

## Em uma frase
Conforme detalhado na documentação oficial do **`aircrack-ng`**, por que protocolos antigos como o **WEP** (quebrado estatisticamente pelo ataque **PTW** de *Pyshkin, Tews e Weinmann* sobre pacotes ARP e pelo método **FMS/KoreK** devido ao IV curto de 24 bits no RC4) e o **WPA2-PSK** (vulnerável a auditoria de dicionário offline se a senha for fraca, via captura do 4-Way Handshake ou do `PMKID` no primeiro quadro EAPOL) estão sendo substituídos pelo **WPA3 (`WPA3-Personal SAE` e `WPA3-Enterprise 192-bit`)**?

## Por que importa
No **WPA2-PSK**, qualquer pessoa passiva no ar que capturar apenas 1 handshake EAPOL (ou 1 `PMKID`) pode levar o arquivo `.cap` para casa e testar bilhões de senhas offline em GPUs sem nunca mais falar com o Access Point!

## Como funciona
O **WPA3-Personal** substitui o PSK estático pelo protocolo **SAE (*Simultaneous Authentication of Equals*, handshake *Dragonfly* baseado em *Password-Authenticated Key Exchange — PAKE* sobre curvas elípticas / grupos finitos)**: **(1) Imunidade a Dicionário Offline**: capturar o handshake SAE no ar **não permite testar senhas offline**, pois cada tentativa de adivinhar a senha exige interagir ativamente ao vivo com o AP!; **(2) Perfect Forward Secrecy (PFS)**: mesmo que alguém descubra a senha do Wi-Fi amanhã, **não conseguirá descriptografar com `airdecap-ng` os arquivos `.pcap` capturados ontem**!; e **(3) `IEEE 802.11w (PMF)` obrigatório**!

## Exemplo
```bash
# Inspecionar nos arquivos .csv gerados pelo airodump-ng quais Access Points ainda operam com WEP/WPA1/WPA2-PSK puro versus WPA3 (SAE / OWE / MGT)
awk -F',' 'NR>2 && NF>10 {print $1, $4, $6, $7, $8, $14}' ./auditoria_corp-01.csv | head -n 20
```

## Limites e trade-offs
Cuidado com uma armadilha comum ao configurar roteadores e controladores em **Modo de Transição WPA2/WPA3 (`WPA3-SAE Transition Mode`)**: enquanto o modo misto `WPA2-PSK + WPA3-SAE` estiver habilitado no mesmo SSID para suportar dispositivos antigos, um atacante ainda pode forçar ou capturar um handshake **WPA2-PSK** usando a mesma senha compartilhada do SSID!

## Como verificar
A arquitetura ideal para redes sem fio modernas é: **(1) SSID Corporativo**: **WPA3-Enterprise (`802.1X EAP-TLS`)**; **(2) SSID de IoT/Dispositivos sem suporte a 802.1X**: **WPA3-SAE puro em 5 GHz / 6 GHz (`Wi-Fi 6E/7`)** (ou WPA2 com *Unique Pre-Shared Keys por dispositivo — PPSK/MPSK* em VLAN isolada); e **(3) SSID de Visitantes Aberto**: **WPA3-OWE (*Opportunistic Wireless Encryption — Enhanced Open*)**, que cifra o tráfego aéreo individualmente com Diffie-Hellman mesmo sem exigir senha!

## Conexões
- [[aircrack-simulacao-rogue-ap-airbase-ng-evil-twin-karmetasploit-defesa]] — Veja também: Simulação de **Rogue Access Point / Evil Twin** com **`airbase-ng`** e Detecção de Ataques de Associação Automática em Auditorias Red Team.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Referência cruzada direta com aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
