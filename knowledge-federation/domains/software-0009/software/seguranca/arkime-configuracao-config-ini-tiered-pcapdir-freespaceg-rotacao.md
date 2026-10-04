---
id: software.seguranca.tranche14.001352
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/arkime/arkime/main/README.md", "https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Configuração Hierárquica (**`/opt/arkime/etc/config.ini`**), Retenção Automática de Disco (**`freeSpaceG`**) e Timeouts de Fluxo no Arkime

## Em uma frase
Como gerenciar dezenas de sensores Arkime espalhados por vários datacenters e filiais usando **um único arquivo `/opt/arkime/etc/config.ini` versionado no Git**, e como garantir que a gravação contínua de pacotes `.pcap` **nunca encha 100% do disco do servidor**?

## Por que importa
O Arkime utiliza no `config.ini` um **Sistema de Configuração em 3 Camadas (*Tiered Configuration System*)**: quando um sensor lê uma variável (como `interface`, `pcapDir` ou `bpf`), ele procura na seguinte ordem de prioridade: **(1º) Na seção `[nome_do_hostname_do_sensor]`**; **(2º) Na seção `[nome_da_nodeClass]`** (permitindo agrupar sensores por perfil, ex.: `[sensores-dmz]` — além de rotular todas as sessões automaticamente com a tag `class:sensores-dmz`!); e **(3º) Na seção global `[default]`**!

## Como funciona
E para proteger o armazenamento local de cada sensor, o processo `capture` gerencia a rotação e a limpeza dos arquivos `.pcap` automaticamente através de três diretivas em `config.ini`: **`pcapDir`** (aceita múltiplos diretórios separados por `;` para distribuir a escrita em vários discos JBOD/RAID0!), **`maxFileSizeG=12`** (tamanho de cada arquivo `.pcap`, até `36G`) e **`freeSpaceG=5%`**!

## Exemplo
```ini
# Exemplo de /opt/arkime/etc/config.ini com heranca em camadas ([default] + [sensor-borda-01]) e expurgo automatico por espaco livre (freeSpaceG=7%)
[default]
elasticsearch=https://opensearch-interno.exemplo.br:9200
rotateIndex=daily
pcapDir=/data/pcap_disk1;/data/pcap_disk2
maxFileSizeG=12
freeSpaceG=7%
tcpTimeout=600
tcpSaveTimeout=720
udpTimeout=30
icmpTimeout=10
dropUser=nobody
dropGroup=daemon

[sensor-borda-01]
interface=eth1;eth2
```

## Limites e trade-offs
Como funciona a proteção **`freeSpaceG=7%`**? O próprio binário `capture` monitora continuamente o espaço livre das partições listadas em `pcapDir`: sempre que o espaço livre cai abaixo de `7%` (ou de um valor em Gigabytes, ex.: `100G`), ele **apaga automaticamente os arquivos `.pcap` mais antigos em modelo FIFO (*Ring Buffer de Disco*)**, mantendo o sensor gravando 24x7 sem intervenção humana! (Enquanto a expiração dos metadados antigos no OpenSearch é feita pelo script `/opt/arkime/db/db.pl`!).

## Como verificar
Mantenha sempre `dropUser=nobody` e `dropGroup=daemon` (ou uma conta dedicada `arkime`) para que o binário `capture` abandone imediatamente os privilégios de `root` após abrir os sockets de captura na placa de rede!

## Conexões
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Veja também: Arquitetura do **Arkime (`arkime/arkime`, ex-Moloch)**: Sistema de **Full Packet Capture (FPC)** e Indexação de Metadados **SPI** em Escala Multi-Gigabit.
- [[arkime-otimizacao-captura-alta-velocidade-tpacketv3-snf-dpdk-threads]] — Veja também: Captura Sem Perda de Pacotes em Links de **10 Gbps a 100 Gbps** no Arkime: `packetThreads`, **`tpacketv3` (`AF_PACKET`)**, **`pcapWriteMethod=simple-nodirect`** e **Criptografia de PCAP em Repouso**.
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Referência cruzada direta com arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
