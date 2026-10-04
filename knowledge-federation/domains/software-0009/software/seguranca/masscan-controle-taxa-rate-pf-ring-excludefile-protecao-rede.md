---
id: software.seguranca.tranche08.000773
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

# Masscan: Dimensionamento de Taxa (`--rate`), Exclusão Obrigatória de Sub-redes Críticas (**`--excludefile`**) e Aceleração **`PF_RING` DNA**

## Em uma frase
Quando você varre grandes blocos de rede (como `10.0.0.0/8` internamente ou blocos públicos de um cliente), certas sub-redes e endereços **jamais** devem receber pacotes de varredura: impressoras industriais antigas (porta `9100`), CLPs SCADA/ICS, equipamentos médicos e blocos de terceiros fora do escopo contratual.

## Por que importa
O Masscan resolve isso de forma determinística na matemática da cifra BlackRock através da flag **`--excludefile <arquivo.txt>`** (ou `--exclude <ip/cidr>`): qualquer IP ou CIDR listado no `excludefile` é ignorado em tempo constante sem afetar a velocidade de transmissão!

## Como funciona
Ao dimensionar **`--rate <pacotes_por_segundo>`**, lembre-se de que cada pacote TCP `SYN` mínimo em Ethernet tem ~64 bytes + framing (~672 bits no fio), portanto: `--rate 10000` consome ~6,7 Mbps; `--rate 100000` consome ~67 Mbps; e `--rate 1488095` satura completamente uma placa de rede Gigabit Ethernet (1 Gbps) a 100% da capacidade física!

## Exemplo
```bash
# Executar varredura Masscan sobre 10.0.0.0/8 excluindo sub-redes OT/SCADA e impressoras via --excludefile
cat << 'EOF' > /cases/easm/exclude_critical.txt
# Sub-redes de Automacao Industrial (OT/SCADA) e Gerencia de Loopback
10.250.0.0/16
10.255.0.0/16
EOF

sudo masscan 10.0.0.0/8 -p22,80,443,445,3389,8080,8443 \
  --excludefile /cases/easm/exclude_critical.txt \
  --rate 5000 \
  --wait 10 \
  -oB /cases/easm/internal_scan.bin
```

## Limites e trade-offs
Observe a flag **`--wait <segundos>`** (padrão `10` segundos): como o Masscan é assíncrono, depois que o último pacote `SYN` é transmitido pela placa de rede, os pacotes `SYN-ACK` e banners dos servidores mais lentos ainda estão voltando pela rede; jamais reduza `--wait 0` se estiver capturando `--banners`!

## Como verificar
Confirme na saída inicial do Masscan a contagem de endereços excluídos após o carregamento do `--excludefile`.

## Conexões
- [[masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables]] — Veja também: Masscan **`--banners`**: Como Resolver o Conflito de **Pacotes `RST` do Kernel Linux** usando **`--source-ip` Dedicado** ou **`--adapter-port` + `iptables`/`nftables`**.
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Veja também: Masscan: Arquivos de Configuração (`-c`), Pausa e Retomada Exata (**`paused.conf` / `--resume`**) e Distribuição em Cluster (**`--shards`**).
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Referência cruzada direta com zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
