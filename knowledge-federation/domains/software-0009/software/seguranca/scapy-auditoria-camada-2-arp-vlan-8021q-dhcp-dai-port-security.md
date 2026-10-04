---
id: software.seguranca.tranche15.001486
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
fontes: ["https://raw.githubusercontent.com/secdev/scapy/master/README.md", "https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Testes de Segurança de **Camada 2 (Data Link)** com Scapy: Auditoria de **Dynamic ARP Inspection (DAI)**, **802.1Q VLAN Hopping (Double Tagging)** e **DHCP Snooping**

## Em uma frase
Como usar o **Scapy** durante um Pentest Interno autorizado ou validação de arquitetura de rede para testar se os switches corporativos estão com **Dynamic ARP Inspection (`DAI`)**, **DHCP Snooping** e bloqueio de **VLAN Hopping (`802.1Q Double Tagging` / `DTP`)** devidamente configurados?

## Por que importa
Como o Scapy constrói o quadro Ethernet byte a byte na Camada 2 (`sendp` / `srp`), você pode montar exatamente os quadros de teste de cada controle L2: **(1) ARP Discovery & Validação DAI**: construir quadros `Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="10.10.10.0/24")` com `srp()` (`arping()`) ou testar se a porta do switch bloqueia respostas ARP `is-at` (`op=2`) com IP que não consta na tabela de *DHCP Snooping Binding*.

## Como funciona
**(2) Teste de `802.1Q Double Tagging`**: empilhar **duas tags VLAN `Dot1Q` seguidas (`Ether() / Dot1Q(vlan=1) / Dot1Q(vlan=20) / IP(...)`)** para verificar se o switch remove a VLAN nativa externa e encaminha o pacote indevidamente para a VLAN interna `20`!

## Exemplo
```python
# Executar descoberta ARP ultra-rapida em uma sub-rede local (srp na Camada 2) e construir um quadro de teste 802.1Q VLAN Tagging no Scapy
from scapy.all import ARP, Dot1Q, Ether, ICMP, IP, srp

ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.0.2.0/24"), timeout=2, verbose=0)
for _, rcv in ans:
    print(rcv.sprintf(r"%Ether.src% -> %ARP.psrc%"))

quadro_vlan = Ether() / Dot1Q(vlan=10) / Dot1Q(vlan=20) / IP(dst="192.0.2.99") / ICMP()
```

## Limites e trade-offs
Olhe o método **`rcv.sprintf(r"%Ether.src% -> %ARP.psrc%")`** no exemplo acima (documentado na tabela de métodos do `usage.rst`): o método `.sprintf()` do Scapy permite extrair e formatar campos de qualquer camada do pacote usando placeholders `%Camada.campo%` sem precisar encadear `if pkt.haslayer(...)`!

## Como verificar
Como impedir **100% dos ataques de `802.1Q Double Tagging`, `ARP Spoofing` e `Rogue DHCP`** nos switches de acesso corporativos? **(1)** Desative negociação dinâmica de trunk (`switchport mode access` + `switchport nonegotiate`); **(2)** Nunca use a `VLAN 1` (ou qualquer VLAN de usuários) como `Native VLAN` nos links de trunk; e **(3)** Habilite **`ip dhcp snooping`** + **`ip arp inspection vlan ...`**!

## Conexões
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Veja também: Fuzzing Inteligente de Protocolos de Rede com **`fuzz()`** e `VolatileValue` no Scapy: Testando a Robustez de Parsers, Firewalls e Regras IDS/IPS.
- [[scapy-teste-evasao-fragmentacao-ip-overlap-idps-snort-suricata]] — Veja também: Testando Motores de Reassemblagem de **NIDS/NIPS (Snort 3 / Suricata / Firewalls)** com **`fragment()`** e Fragmentação IP/TCP Customizada no Scapy.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas]] — Referência cruzada direta com scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
