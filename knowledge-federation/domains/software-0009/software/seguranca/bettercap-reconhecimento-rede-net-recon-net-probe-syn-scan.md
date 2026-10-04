---
id: software.seguranca.tranche06.000562
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

# Bettercap: Reconhecimento de Host em Camada 2/3 (`net.recon`, `net.probe`, `net.show` e `syn.scan` Assíncrono)

## Em uma frase
Os módulos **`net.recon`**, **`net.probe`** e **`syn.scan`** do Bettercap mapeiam os ativos vivos em uma sub-rede local monitorando a tabela ARP/NDP e enviando sondas leves de descoberta.

## Por que importa
Em uma auditoria de rede interna autorizada, o módulo `net.recon` começa operando **100% passivamente**: ele escuta o tráfego de broadcast/multicast local e lê periodicamente a tabela ARP do sistema para listar endereços IP, endereços MAC, fabricantes da placa de rede (OUI) e nomes de host sem enviar pacotes.

## Como funciona
Quando a descoberta ativa é autorizada no escopo, ativar **`net.probe on`** faz o Bettercap enviar pacotes UDP/mDNS/NBNS/UPnP/WSD de descoberta para todos os IPs da sub-rede para forçar o preenchimento da tabela ARP e descobrir nomes NetBIOS/Bonjour, enquanto **`syn.scan <IP/CIDR> <portas>`** executa um scanner TCP SYN assíncrono e extrai banners de serviços.

## Exemplo
```text
# Comandos interativos (ou de arquivo .cap) para reconhecimento de sub-rede e scan SYN nas portas administrativas
set net.probe.mdns true
set net.probe.nbns true
set net.probe.throttle 10
net.recon on
net.probe on
syn.scan 10.10.20.0/24 22,80,443,445,3389
net.show
```

## Limites e trade-offs
Em redes corporativas protegidas por NAC (*Network Access Control* 802.1X) ou switches com detecção de varredura ARP, reduza a agressividade configurando `set net.probe.throttle 50` (atraso em milissegundos entre sondas) ou mantenha apenas `net.recon on` (passivo).

## Como verificar
Use `set net.show.meta true` antes de rodar `net.show` para visualizar todas as portas abertas, banners e nomes mDNS/NetBIOS coletados de cada host.

## Conexões
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Veja também: Bettercap: Arquitetura em Go, Sessões Interativas, Automação Reprodutível com **Caplets (`.cap`)** e API REST / WebSocket (`api.rest`).
- [[bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2]] — Veja também: Bettercap: Auditoria de Resiliência de Camada 2 contra Spoofing (`arp.spoof`, `ndp.spoof`, `dhcp6.spoof`) e Validação de **DAI / RA Guard**.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
