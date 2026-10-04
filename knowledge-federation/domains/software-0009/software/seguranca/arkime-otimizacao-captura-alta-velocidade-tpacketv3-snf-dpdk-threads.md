---
id: software.seguranca.tranche14.001353
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

# Captura Sem Perda de Pacotes em Links de **10 Gbps a 100 Gbps** no Arkime: `packetThreads`, **`tpacketv3` (`AF_PACKET`)**, **`pcapWriteMethod=simple-nodirect`** e **Criptografia de PCAP em Repouso**

## Em uma frase
Quando o tráfego da rede ultrapassa 1 Gbps rumo a 10 Gbps, 40 Gbps ou 100 Gbps, uma captura `libpcap` padrão com 1 thread não dá conta de copiar os pacotes da placa de rede e gravá-los no disco sem sofrer **Packet Drops**. Como configurar o `capture` do Arkime no `config.ini` para atingir **Zero Packet Loss** em alta velocidade e ainda **criptografar os arquivos `.pcap` gravados no disco**?

## Por que importa
No plano de captura e processamento, você ajusta: **(1) `pcapReadMethod=tpacketv3`** (usa os anéis de memória compartilhados *Zero-Copy* `TPACKET_V3` do Kernel Linux `AF_PACKET`, ou drivers de hardware como `snf`, `nt`, `pfring`, `dpdk`); **(2) `packetThreads=6`** (ou até `24` threads que parseiam os pacotes e montam os metadados SPI em paralelo, alimentadas pela fila `maxPacketsInQueue`); e **(3) `synOnly=false`** / filtros **`bpf`** ou **`dontSaveBPFs`** (ex.: para gravar apenas os primeiros `N` pacotes de streams de vídeo pesados ou fluxos TLS já inspecionados, economizando 70% do disco!)!

## Como funciona
E no plano de escrita em disco (`pcapWriteMethod`), o Arkime suporta **Criptografia Nativa em Tempo Real dos Arquivos `.pcap` (`simple-aes-256-ctr` ou `simple-xor-2048`)** integrada ao KMS/chave local — garantindo que se um disco físico for roubado do datacenter, os arquivos `.pcap` estarão cifrados com **AES-256-CTR**!

## Exemplo
```ini
# Tuning de alta performance (10Gbps+) e criptografia em repouso AES-256-CTR dos arquivos PCAP no /opt/arkime/etc/config.ini
pcapReadMethod=tpacketv3
tpacketv3BlockSize=8388608
tpacketv3NumThreads=4
packetThreads=8
pcapWriteMethod=simple
pcapWriteSize=262144
simpleEncoding=aes-256-ctr
simpleKEKId=chave-kek-sensores-2026
```

## Limites e trade-offs
Olhe que recurso prático de economia de disco no `config.ini`: a diretiva **`dontSaveBPFs`** permite definir filtros BPF com um número limite de pacotes por sessão (por exemplo, `dontSaveBPFs=port 443:20` grava no disco `.pcap` **apenas os primeiros 20 pacotes de cada conexão HTTPS `:443`** — preservando 100% do handshake TLS, certificados, JA3/JA4 e metadados SPI, mas descartando os gigabytes de carga útil cifrada que não poderiam ser lidos sem a chave!).

## Como verificar
Monitore sempre na aba **Stats -> Capture Graphs** do Arkime a métrica **`Dropped Packets / Overload Drops`** para confirmar que `tpacketv3` e `packetThreads` estão dimensionados com folga.

## Conexões
- [[arkime-configuracao-config-ini-tiered-pcapdir-freespaceg-rotacao]] — Veja também: Configuração Hierárquica (**`/opt/arkime/etc/config.ini`**), Retenção Automática de Disco (**`freeSpaceG`**) e Timeouts de Fluxo no Arkime.
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Veja também: Caça a Ameaças (**Threat Hunting**) no Arkime: Linguagem de Expressões de Busca, **Sessions**, **SPI View**, **SPI Graph** e **Connections Graph**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[snort-modos-operacao-libdaq-afpacket-nfq-inline-ips-drop-reject]] — Referência cruzada direta com snort-modos-operacao-libdaq-afpacket-nfq-inline-ips-drop-reject.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
