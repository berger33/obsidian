---
id: software.seguranca.tranche06.000568
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

# Bettercap: Auditoria de Periféricos Sem Fio **2.4GHz HID** (`hid.recon`) e Barramentos Automotivos/Industriais **CAN-bus** (`can.recon` / Arquivos **DBC**)

## Em uma frase
O Bettercap inclui dois módulos especializados para auditoria de sistemas embarcados e hardware físico: **`hid`** (para dongles USB sem fio proprietários de 2.4 GHz baseados em transceptores Nordic Semiconductor nRF24L01+) e **`can`** (para redes **CAN-bus** automotivas e industriais via interfaces SocketCAN `can0` ou adaptadores seriais SLCAN).

## Por que importa
Periféricos sem fio antigos (teclados e mouses não-Bluetooth de 2.4 GHz vulneráveis a *MouseJacking*) aceitam quadros de teclado não-criptografados pelo ar; já em veículos e máquinas industriais, o barramento **CAN** (*Controller Area Network*) transmite quadros de controle sem autenticação de origem por padrão.

## Como funciona
No módulo **`can`**, carregar um banco de dados **DBC** (*CAN Database*, via `set can.dbc.file veiculo.dbc`) permite que o `can.recon on` e o `can.show` decodifiquem automaticamente os IDs de quadros CAN e os bits do payload em sinais de engenharia legíveis (ex.: velocidade da roda, rotação do motor, estado das travas).

## Exemplo
```text
# Monitorar e decodificar mensagens de um barramento CAN de bancada usando um arquivo de definicoes DBC
set can.device can0
set can.transport socketcan
set can.dbc.file /opt/secops/can/powertrain_bench.dbc
can.recon on
can.show
```

## Limites e trade-offs
Testes em barramentos **CAN-bus** (`can.write` / `can.fuzz`) devem ser executados **exclusivamente em bancadas de laboratório isoladas (*bench setups* / simuladores HIL)** e jamais em veículos em movimento ou plantas industriais operacionais, pois quadros CAN arbitrários afetam atuadores físicos críticos.

## Como verificar
Utilize `can.recon on` com `can.dbc.file` na bancada de teste para validar se os gateways automotivos filtram mensagens entre a rede de infotainment e o barramento de powertrain.

## Conexões
- [[bettercap-auditoria-bluetooth-low-energy-ble-recon-enum-gatt]] — Veja também: Bettercap: Auditoria de Dispositivos **Bluetooth Low Energy (BLE)** (`ble.recon`, `ble.show`, `ble.enum` e Inspeção de Características **GATT**).
- [[bettercap-monitoramento-eventos-events-stream-triggers-webhooks]] — Veja também: Bettercap: Monitoramento de Eventos (`events.stream`), Filtros (`events.ignore`), Gatilhos Reativos (`events.on`) e Sensores de Honeypot L2.
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[wireshark-dissecadores-customizados-lua-protocolos-c2-proprietarios]] — Referência cruzada direta com wireshark-dissecadores-customizados-lua-protocolos-c2-proprietarios.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
