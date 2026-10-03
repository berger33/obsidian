---
id: software.seguranca.tranche06.000565
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

# Bettercap: Captura Seletiva e Inspeção de Tráfego com `net.sniff` (Filtros BPF, Expressões Regulares e Gravação PCAP)

## Em uma frase
O módulo **`net.sniff`** do Bettercap atua como um analisador de pacotes em tempo real e gravador PCAP integrado à sessão, capaz de aplicar simultaneamente um filtro **BPF** de kernel (`net.sniff.filter`) e uma expressão regular sobre o payload (`net.sniff.regexp`).

## Por que importa
Durante a avaliação de segurança de um equipamento industrial ou protocolo legado, permite capturar em um arquivo `.pcap` (`set net.sniff.output captura_lab.pcap`) apenas os pacotes que casam com determinados padrões de protocolo, além de identificar protocolos em texto claro (FTP, Telnet, HTTP Basic Auth, SNMP v1/v2c community strings, NTLMv1/v2).

## Como funciona
Quando `net.sniff.local` está em `false` (padrão), o sniffer ignora pacotes gerados pela própria máquina de auditoria para não poluir o console; ativá-lo (`set net.sniff.local true`) permite depurar o tráfego originado pela própria estação.

## Exemplo
```text
# Configurar captura seletiva no net.sniff filtrando com BPF e gravando pacotes relevantes em arquivo PCAP
set net.sniff.verbose false
set net.sniff.local false
set net.sniff.filter "tcp port 21 or tcp port 23 or udp port 161"
set net.sniff.output /cases/pcaps/legacy_protocols_audit.pcap
net.sniff on
```

## Limites e trade-offs
Deixar `set net.sniff.verbose true` ativo em uma interface de alto tráfego imprimirá cada pacote TCP/UDP no terminal, degradando a legibilidade dos eventos importantes; mantenha `net.sniff.verbose false` para exibir apenas eventos de aplicação parseados.

## Como verificar
Abra o arquivo gerado em `net.sniff.output` com `tshark -r /cases/pcaps/legacy_protocols_audit.pcap` para análise detalhada de cada fluxo.

## Conexões
- [[bettercap-auditoria-dns-spoof-proxies-http-https-packet-proxy]] — Veja também: Bettercap: Simulação de Redirecionamento DNS (`dns.spoof`) e Proxies Transparentes Scriptáveis (`http.proxy`, `https.proxy`, `tcp.proxy` e `packet.proxy`).
- [[bettercap-auditoria-wifi-80211-recon-wpa-pmkid-80211w-pmf]] — Veja também: Bettercap: Auditoria de Redes Sem Fio **WiFi 802.11** (`wifi.recon`, Descoberta de APs/Clientes, Captura EAPOL/PMKID e Validação de **802.11w PMF**).
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
