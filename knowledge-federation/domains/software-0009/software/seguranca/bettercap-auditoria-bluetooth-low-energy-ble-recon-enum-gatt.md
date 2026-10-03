---
id: software.seguranca.tranche06.000567
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/bettercap/bettercap/master/README.md", "https://raw.githubusercontent.com/bettercap/caplets/master/README.md", "https://www.bettercap.org/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bettercap: Auditoria de Dispositivos **Bluetooth Low Energy (BLE)** (`ble.recon`, `ble.show`, `ble.enum` e Inspeção de Características **GATT**)

## Em uma frase
O módulo **`ble`** do Bettercap realiza a descoberta de periféricos **Bluetooth Low Energy (BLE)** próximos (`ble.recon on` / `ble.show`) e enumera todos os serviços e características **GATT** (*Generic Attribute Profile*) expostos por um dispositivo (`ble.enum <MAC>`).

## Por que importa
Fechaduras inteligentes (*smart locks*), sensores médicos/industriais, coletores logísticos e beacons IoT frequentemente usam BLE assumindo erroneamente que o protocolo é invisível ou autenticado por padrão, deixando características GATT com permissão `WRITE` aberta sem pareamento/bonding LE Secure Connections.

## Como funciona
O comando `ble.enum <MAC>` conecta ao periférico BLE de teste e lista cada **Service UUID**, **Characteristic UUID**, suas propriedades de acesso (`READ`, `NOTIFY`, `INDICATE`, `WRITE`, `WRITE WITHOUT RESPONSE`) e os bytes atualmente armazenados em cada atributo.

## Exemplo
```text
# Descobrir dispositivos BLE no laboratorio IoT e enumerar a tabela GATT de um sensor especifico
ble.recon on
ble.show
ble.enum AA:BB:CC:11:22:33
```

## Limites e trade-offs
Durante a fabricação e auditoria de firmware de dispositivos BLE corporativos, exija **LE Secure Connections (Numeric Comparison / Out-of-Band)** e autenticação/criptografia no nível da característica GATT antes de permitir qualquer operação `READ` de dados sensíveis ou `WRITE` de comandos.

## Como verificar
Verifique na tabela retornada por `ble.enum` se alguma característica crítica de controle aceita `WRITE` sem exigir vínculo criptográfico (*Bonding / MITM Protection*).

## Conexões
- [[bettercap-auditoria-wifi-80211-recon-wpa-pmkid-80211w-pmf]] — Veja também: Bettercap: Auditoria de Redes Sem Fio **WiFi 802.11** (`wifi.recon`, Descoberta de APs/Clientes, Captura EAPOL/PMKID e Validação de **802.11w PMF**).
- [[bettercap-auditoria-hid-24ghz-canbus-automotivo-dbc-industrial]] — Veja também: Bettercap: Auditoria de Periféricos Sem Fio **2.4GHz HID** (`hid.recon`) e Barramentos Automotivos/Industriais **CAN-bus** (`can.recon` / Arquivos **DBC**).
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
