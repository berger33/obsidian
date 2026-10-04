---
id: software.seguranca.tranche15.001478
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
fontes: ["https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md", "https://www.kismetwireless.net/docs/readme/intro/kismet/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Filtros de Captura e Conformidade de Privacidade (**LGPD / GDPR / PCI-DSS**) em WIDS com Kismet: Gravando Apenas Quadros de Gerenciamento (Sem Dados de Usuários!)

## Em uma frase
Quando uma empresa implanta sensores **WIDS (Kismet)** permanentes nos escritórios para detectar Rogue APs (`APSPOOF`), ataques de Deauth e dispositivos invasores, o time Jurídico / DPO (LGPD/GDPR) frequentemente faz uma pergunta crucial: *"O sensor WIDS está gravando no disco o conteúdo dos pacotes de dados dos celulares pessoais dos funcionários e visitantes?"*

## Por que importa
E mais: gravar gigabytes de tráfego de vídeo e downloads dos usuários no `.kismet` encheria o disco do servidor em poucos dias sem agregar nada à detecção WIDS de Rogue APs!

## Como funciona
O Kismet resolve tanto a exigência jurídica de privacidade quanto o consumo de disco através do **Packet Filtering Engine (`kismet_filter.conf` / `log_types=`)**: você pode configurar o Kismet para **analisar 100% dos quadros em memória para alimentar o motor WIDS e o inventário de dispositivos**, mas no arquivo `.kismet` **descartar os quadros `DATA` (gravando apenas quadros `MANAGEMENT` / `BEACON` / `ALERT`) ou desabilitar completamente a tabela `packets` mantendo apenas `devices` e `alerts`**!

## Exemplo
```ini
# Configurar no /etc/kismet/kismet_site.conf a filtragem de pacotes no log .kismet para descartar pacotes de dados (DATA) preservando WIDS e inventario
kis_log_packets=false
kis_log_devices=true
kis_log_alerts=true
kis_log_datasources=true
```

## Limites e trade-offs
Olhe a simplicidade e o impacto das 4 linhas acima no `kismet_site.conf` (**`kis_log_packets=false`** mantendo `kis_log_devices=true` e `kis_log_alerts=true`): **(1)** O tamanho do arquivo `.kismet` diário cai de dezenas de Gigabytes para poucos Megabytes; **(2)** Zero pacotes de payload de usuários são gravados em disco (conformidade total com LGPD/GDPR!); e **(3) 100% dos alertas WIDS (`APSPOOF`, `DEAUTHFLOOD`, `CRYPTODROP`) e o inventário completo de BSSIDs, SSIDs, canais e sinais RSSI continuam funcionando normalmente**!

## Como verificar
E se você precisar gravar pacotes `.pcap`, mas quiser excluir o tráfego de determinados endereços MAC confiáveis de alto volume, use as regras `filter_Log=` por endereço MAC ou tipo de quadro (`management`, `phy`, `data`).

## Conexões
- [[kismet-automacao-api-rest-websockets-alertas-tempo-real-siem-soar]] — Veja também: Automação e Integração com SIEM/SOAR via **API REST e WebSockets (`.ekjson` / `.itjson`)** do Kismet: Consumindo Alertas WIDS e Handshakes em Tempo Real.
- [[kismet-seguranca-execucao-suid-grupo-kismet-privsep-api-keys]] — Veja também: Arquitetura de **Privilege Separation (`privsep`)** do Kismet: Por Que o Servidor `kismet` Roda Sem Privilégios de `root` Usando Helpers SUID Restritos ao Grupo `kismet`?.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio]] — Referência cruzada direta com kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio.
- [[kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json]] — Referência cruzada direta com kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
