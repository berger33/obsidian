---
id: software.seguranca.tranche08.000779
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Masscan: Ajustes de Camada de Enlace (**`--interface`**, **`--adapter-ip`**, **`--adapter-mac`**, **`--router-mac`**), Tags **802.1Q VLAN** e Diagnóstico `--packet-trace`

## Em uma frase
Como o Masscan constrói seus próprios quadros Ethernet brutos (Camada 2) em user-space antes de injetá-los no driver da placa de rede (`libpcap` / `PF_RING` / `AF_PACKET`), ele precisa descobrir na inicialização qual placa de rede usar (`-e` / `--interface`), qual é o endereço IP/MAC de origem (`--adapter-ip`, `--adapter-mac`) e qual é o endereço MAC do gateway padrão (`--router-mac`) via resolução ARP.

## Por que importa
Em ambientes especiais — como interfaces VPN Point-to-Point (`tun0` de OpenVPN/WireGuard que não têm cabeçalho Ethernet de 14 bytes), trunks **VLAN IEEE 802.1Q (`--adapter-vlan <id>`)** ou redes estáticas sem ARP — o Masscan pode falhar ao resolver o gateway se essas opções não forem informadas ou se a interface incorreta for escolhida.

## Como funciona
Para diagnosticar problemas de roteamento ou enlace em segundos, a flag **`--packet-trace`** (combinada com `--rate 1`) imprime no terminal cada quadro Ethernet/IP/TCP enviado pela thread de transmissão e recebido pela thread de captura!

## Exemplo
```bash
# Diagnosticar o envio e recebimento de quadros de rede do Masscan em uma interface especifica com --packet-trace
sudo masscan 10.30.10.10 -p80,443 \
  --interface eth0 \
  --rate 2 \
  --packet-trace
```

## Limites e trade-offs
Você também pode salvar 100% dos pacotes brutos recebidos pelo Masscan diretamente em um arquivo `.pcap` padrão do Wireshark passando a flag **`--pcap /cases/pcaps/masscan_responses.pcap`** durante a varredura!

## Como verificar
Se o Masscan exibir aviso de falha ao resolver o endereço MAC do roteador em uma rede segmentada, verifique o MAC do gateway com `ip neigh show` e passe `--router-mac <aa:bb:cc:dd:ee:ff>`.

## Conexões
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Veja também: Arquitetura de Varredura em **Dois Estágios**: Descoberta Rápida de Portas (`0-65535`) com **Masscan** + Fingerprinting Profundo (`-sV -sC`) com **Nmap**.
- [[masscan-deteccao-defensiva-syn-cookies-suricata-zeek-conntrack-tuning]] — Veja também: Defesa e Detecção contra Varreduras **Masscan**: Proteção da Tabela **`nf_conntrack`** em Firewalls e Detecção de Varreduras Espalhadas no **Suricata / Zeek**.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables]] — Referência cruzada direta com masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
