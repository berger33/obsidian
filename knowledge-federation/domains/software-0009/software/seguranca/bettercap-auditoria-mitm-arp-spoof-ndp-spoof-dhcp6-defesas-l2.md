---
id: software.seguranca.tranche06.000563
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

# Bettercap: Auditoria de Resiliência de Camada 2 contra Spoofing (`arp.spoof`, `ndp.spoof`, `dhcp6.spoof`) e Validação de **DAI / RA Guard**

## Em uma frase
Os módulos **`arp.spoof`** (IPv4 ARP cache poisoning), **`ndp.spoof`** (IPv6 Neighbor Discovery Protocol spoofing) e **`dhcp6.spoof`** do Bettercap permitem testar na prática se os switches de acesso corporativos estão aplicando corretamente os controles de segurança de Camada 2 (**Dynamic ARP Inspection — DAI**, **DHCP Snooping**, **IPv6 RA Guard** e **DHCPv6 Shield**).

## Por que importa
Muitas redes corporativas implementam segmentação rigorosa em firewalls de Camada 3, mas esquecem de configurar *DHCP Snooping + DAI* nas portas de acesso das VLANs de usuários ou deixam o IPv6 habilitado por padrão no Windows sem *RA Guard* no switch.

## Como funciona
Durante um teste autorizado contra uma estação de laboratório específica (`set arp.spoof.targets 10.10.20.55`), se o switch de acesso **não** possuir *Dynamic ARP Inspection* ativo, o host alvo atualizará sua tabela ARP associando o IP do gateway ao MAC da máquina de auditoria; se o switch **possuir** DAI apoiado na tabela de *DHCP Snooping Binding*, o switch descartará os pacotes ARP forjados e incrementará os contadores de violação DAI.

## Exemplo
```text
# Testar se o switch da VLAN bloqueia ARP Spoofing (DAI) contra um unico host de homologacao (10.10.20.55)
net.recon on
set arp.spoof.fullduplex true
set arp.spoof.targets 10.10.20.55
set arp.spoof.internal false
arp.spoof on
```

## Limites e trade-offs
Jamais execute `arp.spoof on` sem antes restringir **`set arp.spoof.targets <IP_UNICO_DE_TESTE>`**: omitir `arp.spoof.targets` tenta interceptar a sub-rede inteira simultaneamente, causando negação de serviço (DoS) severa na VLAN.

## Como verificar
Verifique nos switches de acesso (`show ip arp inspection statistics` / `show ipv6 snooping counters`) que os pacotes forjados são bloqueados por **DAI** e **RA Guard / ND Inspection**.

## Conexões
- [[bettercap-reconhecimento-rede-net-recon-net-probe-syn-scan]] — Veja também: Bettercap: Reconhecimento de Host em Camada 2/3 (`net.recon`, `net.probe`, `net.show` e `syn.scan` Assíncrono).
- [[bettercap-auditoria-dns-spoof-proxies-http-https-packet-proxy]] — Veja também: Bettercap: Simulação de Redirecionamento DNS (`dns.spoof`) e Proxies Transparentes Scriptáveis (`http.proxy`, `https.proxy`, `tcp.proxy` e `packet.proxy`).
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[responder-envenenamento-ipv6-dhcpv6-dns-takeover-wpad-mitigacao]] — Referência cruzada direta com responder-envenenamento-ipv6-dhcpv6-dns-takeover-wpad-mitigacao.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
