---
id: software.seguranca.tranche14.001358
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

# Uso do Arkime em **Laboratórios de DFIR Offline (`capture -r`)**: Importando Diretórios de Arquivos `.pcap` de Incidentes para Investigação Visual e Grafo

## Em uma frase
Você sabia que o **Arkime** não serve apenas para monitorar interfaces de rede ao vivo 24x7, mas também é uma das melhores ferramentas do mundo para **analisar offline dezenas de gigabytes de arquivos `.pcap` coletados durante um incidente de segurança ou exercício de CTF/Red Team**?

## Por que importa
Quando uma equipe de DFIR recebe 50 arquivos `.pcap` somando 80 GB capturados pelo `tcpdump` ou por um firewall em uma rede comprometida, abrir 80 GB no Wireshark desktop trava a memória RAM da estação!

## Como funciona
Com o comando **`/opt/arkime/bin/capture -r /caminho/evidencias.pcap -t tag-caso-incidente01`** (ou **`-R /caminho/pasta_pcaps/`** para importar recursivamente uma pasta inteira!), o motor em C do Arkime indexa os 80 GB de PCAPs em poucos minutos e disponibiliza todas as conversas, certificados TLS, DNS, HTTP, SMB, *SPI View*, *Connections Graph* e *CyberChef* no navegador para toda a equipe de resposta a incidentes investigar simultaneamente!

## Exemplo
```bash
# Importar recursivamente (-R) um diretorio de arquivos PCAP de um incidente forense no Arkime sem copiar os arquivos (--scheme) e rotulando com tag
/opt/arkime/bin/capture \
  -c /opt/arkime/etc/config.ini \
  -R /evidencias/caso_2026_10/pcaps/ \
  --tag incidente-2026-10 \
  --skip
```

## Limites e trade-offs
Dica de ouro nos argumentos do `capture -R` acima: a flag **`--skip`** ignora arquivos `.pcap` que já foram indexados anteriormente naquela pasta (permitindo rodar o comando repetidamente conforme novos PCAPs chegam da coleta!), e no modo padrão de leitura offline (`-r` / `-R`), o Arkime **apenas indexa os offsets apontando para os arquivos `.pcap` originais onde eles já estão**, sem duplicar os 80 GB no disco!

## Como verificar
Ao indexar PCAPs de múltiplos hosts diferentes do mesmo incidente, passe **`--tag host-web01`** / **`--tag host-db01`** em cada importação para filtrar facilmente por host na barra de busca (`tags == "host-web01"`).

## Conexões
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Veja também: Segurança e Autenticação do **Arkime Viewer**: `passwordSecret`, `serverSecret`, TLS Mútuo entre Sensores e Integração **SSO (`authMode=header-jwt` / OIDC)**.
- [[arkime-automacao-api-rest-cron-queries-alertas-exportacao-pcap]] — Veja também: Automação no Arkime: **Periodic Queries (*Cron Queries*)**, **Hunt Jobs (Busca de Bytes/Regex nos PCAPs Brutos)** e Extração de PCAP via **API REST**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Referência cruzada direta com arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
