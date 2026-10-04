---
id: software.seguranca.tranche08.000775
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

# Masscan: Gravação em Formato Binário Nativo (**`-oB`**) e Conversão Offline Instantânea (**`--readscan`**) para XML Nmap (`-oX`), JSON (`-oJ`), Grepable (`-oG`) e List (`-oL`)

## Em uma frase
Conforme documentado em `doc/masscan.8.markdown`, o Masscan suporta cinco formatos de arquivo de saída: **Binário nativo (`-oB scan.bin`)**, **XML compatível com Nmap (`-oX scan.xml`)**, **JSON (`-oJ scan.json`)**, **Grepable Nmap (`-oG scan.gnmap`)** e **Lista simples (`-oL scan.txt`)**.

## Por que importa
A melhor prática de engenharia para varreduras grandes no Masscan é gravar a captura primária sempre no formato **Binário compacto (`-oB scan.bin`)**: além de ser muito menor em disco e mais rápido de gravar em alta taxa de pacotes, o arquivo `.bin` preserva todos os metadados brutos e pode ser convertido **offline em milissegundos** para qualquer outro formato quantas vezes você quiser usando **`masscan --readscan scan.bin`**!

## Como funciona
Ainda mais útil: ao executar `masscan --readscan scan.bin`, você pode passar filtros de IP/CIDR e portas na linha de comando para extrair de um arquivo `.bin` gigante apenas os resultados de uma sub-rede ou porta específica!

## Exemplo
```bash
# Ler um arquivo binario de varredura (-oB) offline com --readscan, filtrar apenas a porta 443 da sub-rede 10.20.0.0/16 e converter para JSON e XML!
masscan --readscan /cases/easm/internal_scan.bin 10.20.0.0/16 -p443 -oJ /cases/easm/subnet20_https.json
masscan --readscan /cases/easm/internal_scan.bin -oX /cases/easm/full_scan_nmap_compatible.xml
```

## Limites e trade-offs
Note que você pode usar `--readscan` sem privilégios de `root` (pois nenhuma placa de rede é aberta na leitura offline do arquivo `.bin`) e alimentar o XML ou JSON resultante diretamente em ferramentas de gestão de vulnerabilidades, DefectDojo ou scripts de segunda fase do Nmap.

## Como verificar
Teste converter um arquivo `.bin` para `-oL` (`status protocol port ip timestamp`) e `-oJ` usando `masscan --readscan`.

## Conexões
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Veja também: Masscan: Arquivos de Configuração (`-c`), Pausa e Retomada Exata (**`paused.conf` / `--resume`**) e Distribuição em Cluster (**`--shards`**).
- [[masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados]] — Veja também: Masscan: Varredura de Portas **UDP (`-pU:53,123,161,500`)**, Uso de **`--nmap-payloads`** e Injeção de Payloads UDP Customizados (`--pcap-payloads`).
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Referência cruzada direta com masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
