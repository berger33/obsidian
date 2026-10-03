---
id: software.seguranca.tranche08.000776
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

# Masscan: Varredura de Portas **UDP (`-pU:53,123,161,500`)**, Uso de **`--nmap-payloads`** e Injeção de Payloads UDP Customizados (`--pcap-payloads`)

## Em uma frase
Diferente do TCP (onde qualquer porta aberta responde com `SYN-ACK` a um pacote `SYN` vazio), um serviço **UDP** (como DNS na `53`, NTP na `123`, SNMP na `161`, NetBIOS na `137` ou IKE VPN na `500`) **ignora pacotes UDP vazios de 0 bytes e só responde se receber um datagrama UDP formatado de acordo com o protocolo esperado naquela porta**!

## Por que importa
O Masscan resolve a varredura UDP em alta velocidade permitindo especificar portas UDP com o prefixo **`U:`** (ex.: `-p80,443,U:53,U:123,U:161`) — e já traz embutidos probes para os protocolos UDP mais comuns (DNS, NTP, SNMPv2 `public`, NetBIOS, Memcached, Quake).

## Como funciona
Para estender a cobertura para dezenas de outros protocolos UDP, o Masscan suporta **`--nmap-payloads <caminho/nmap-payloads>`** (lendo diretamente o arquivo oficial de payloads UDP do Nmap!) ou **`--pcap-payloads <arquivo.pcap>`** (extraindo datagramas UDP reais de uma captura Wireshark/tcpdump para enviá-los nas portas correspondentes!).

## Exemplo
```bash
# Varrer portas UDP criticas (DNS, NTP, SNMP, SSDP) em alta velocidade usando o dicionario oficial de payloads UDP do Nmap
sudo masscan 10.10.0.0/16 -pU:53,U:123,U:161,U:1900 \
  --nmap-payloads /usr/share/nmap/nmap-payloads \
  --banners \
  --rate 2000 \
  -oJ /cases/easm/udp_services.json
```

## Limites e trade-offs
Na auditoria defensiva da borda externa da empresa, rodar o Masscan nas portas UDP conhecidas por ataques de **Amplificação e Reflexão DDoS** (`U:53` DNS aberto, `U:123` NTP `monlist`, `U:161` SNMP, `U:1900` SSDP, `U:11211` Memcached, `U:389` CLDAP) permite encontrar e fechar serviços mal configurados em minutos.

## Como verificar
Verifique no JSON de saída se algum host respondeu nas portas `U:161` ou `U:11211` em interfaces expostas.

## Conexões
- [[masscan-formatos-saida-binaria-ob-readscan-conversao-ox-oj-ol-og]] — Veja também: Masscan: Gravação em Formato Binário Nativo (**`-oB`**) e Conversão Offline Instantânea (**`--readscan`**) para XML Nmap (`-oX`), JSON (`-oJ`), Grepable (`-oG`) e List (`-oL`).
- [[masscan-customizacao-http-sni-vhost-payloads-heartbleed-poodle]] — Veja também: Masscan: Customização de Requisições HTTP (`--http-user-agent`, `--http-header`, `--http-method`), Captura de **Certificados TLS X.509** e Checagens **SMB / VULN**.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns]] — Referência cruzada direta com zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
