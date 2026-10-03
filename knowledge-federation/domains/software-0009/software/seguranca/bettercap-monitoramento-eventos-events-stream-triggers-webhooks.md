---
id: software.seguranca.tranche06.000569
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

# Bettercap: Monitoramento de Eventos (`events.stream`), Filtros (`events.ignore`), Gatilhos Reativos (`events.on`) e Sensores de Honeypot L2

## Em uma frase
O módulo **`events.stream`** é o sistema nervoso central do Bettercap: todos os demais módulos emitem eventos tipados (`endpoint.new`, `endpoint.lost`, `wifi.client.probe`, `wifi.ap.new`, `ble.device.new`, `syn.scan`, `net.sniff.*`, `mod.started`) que podem ser filtrados, gravados em arquivo de log ou usados como gatilhos reativos.

## Por que importa
Permite transformar uma instância do Bettercap rodando em modo 100% passivo (`net.recon on` ou `wifi.recon on`) em um **sensor leve de monitoramento de Camada 2 / WIDS** que alerta o SOC imediatamente sempre que um novo endereço MAC desconhecido (`endpoint.new`) se conecta a uma VLAN restrita de servidores ou quando um cliente WiFi procura por um SSID sensível.

## Como funciona
Com `set events.stream.output /var/log/bettercap-events.log` e `events.stream.http.request.dump`, todos os eventos são persistidos em disco, enquanto `events.ignore <tipo>` silencia eventos ruidosos no terminal.

## Exemplo
```text
# Configurar o Bettercap como sensor passivo de Camada 2 que registra novos endpoints detectados na VLAN
events.ignore net.sniff.mdns
set events.stream.output /var/log/secops/vlan_l2_endpoints.log
net.recon on
events.stream on
```

## Limites e trade-offs
Combine o monitoramento passivo de `endpoint.new` com inspeção de tabelas ARP para detectar tentativas de *ARP Spoofing* ou conexão física de dispositivos não autorizados (*rogue devices*) em sub-redes de datacenter.

## Como verificar
Verifique a escrita de eventos no arquivo configurado em `events.stream.output` sempre que um novo host entrar na sub-rede.

## Conexões
- [[bettercap-auditoria-hid-24ghz-canbus-automotivo-dbc-industrial]] — Veja também: Bettercap: Auditoria de Periféricos Sem Fio **2.4GHz HID** (`hid.recon`) e Barramentos Automotivos/Industriais **CAN-bus** (`can.recon` / Arquivos **DBC**).
- [[bettercap-automacao-caplets-api-rest-tls-seguranca-operacional]] — Veja também: Bettercap: Desenvolvimento de **Caplets (`.cap`)** Auditáveis, Hardening do Módulo `api.rest` e Governança de Escopo em Pentests.
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[bettercap-reconhecimento-rede-net-recon-net-probe-syn-scan]] — Referência cruzada direta com bettercap-reconhecimento-rede-net-recon-net-probe-syn-scan.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
