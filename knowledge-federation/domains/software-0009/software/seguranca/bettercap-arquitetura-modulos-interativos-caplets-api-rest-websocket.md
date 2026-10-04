---
id: software.seguranca.tranche06.000561
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

# Bettercap: Arquitetura em Go, Sessões Interativas, Automação Reprodutível com **Caplets (`.cap`)** e API REST / WebSocket (`api.rest`)

## Em uma frase
**Bettercap** (`bettercap/bettercap`, GPLv3, escrito em Go) é o framework modular unificado de reconhecimento e auditoria de segurança de redes que abrange redes **Ethernet IPv4/IPv6**, redes sem fio **WiFi (802.11)**, dispositivos **Bluetooth Low Energy (BLE)**, periféricos sem fio **2.4GHz HID** e barramentos automotivos/industriais **CAN-bus**.

## Por que importa
Em vez de encadear dezenas de scripts frágeis e incompatíveis para testar controles de camada 2/3, WiFi ou BLE durante um pentest interno ou exercício Red Team, o Bettercap consolida todos os módulos sobre um barramento interno de eventos em tempo real.

## Como funciona
As sessões do Bettercap podem ser operadas no console interativo (`active`, `help`, `set`, `get`), automatizadas de forma determinística através de arquivos de script chamados **Caplets (`.cap`)** (`bettercap/caplets`, executados com `-caplet arquivo.cap` ou `caplets.update`) ou controladas remotamente via **API REST + WebSocket** de eventos ao vivo (módulo `api.rest` consumido pela Web UI oficial).

## Exemplo
```bash
# Atualizar o repositorio oficial de caplets e iniciar o Bettercap executando comandos de reconhecimento passivo
sudo bettercap -eval "caplets.update; q"
sudo bettercap -iface eth0 -eval "net.recon on; events.stream on"
```

## Limites e trade-offs
Por expor controle total sobre interfaces de rede em modo promíscuo/monitor, quando habilitar o módulo `api.rest` sempre restrinja `api.rest.address` a `127.0.0.1`, defina credenciais fortes em `api.rest.username` / `api.rest.password` e utilize TLS (`api.rest.certificate` / `api.rest.key`).

## Como verificar
Execute `bettercap -version` e rode `help` dentro da sessão para listar o status (`running` / `not running`) de todos os módulos compilados.

## Conexões
- [[bettercap-reconhecimento-rede-net-recon-net-probe-syn-scan]] — Veja também: Bettercap: Reconhecimento de Host em Camada 2/3 (`net.recon`, `net.probe`, `net.show` e `syn.scan` Assíncrono).
- [[bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2]] — Referência cruzada direta com bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2.
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
