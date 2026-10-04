---
id: software.seguranca.tranche15.001480
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

# Conformidade **PCI-DSS Requisito 11.2 (Auditoria Trimestral de Rogue Wireless)** e Mapeamento de Cobertura Física (`GPS` / `KML`) com Kismet

## Em uma frase
O padrão **PCI-DSS v4.0 (Requisito 11.2.1 e 11.2.2)** exige que toda organização que processa cartões de pagamento execute — **no mínimo a cada 3 meses (ou continuamente via WIDS automatizado)** — uma varredura de espectro sem fio em todas as lojas, escritórios e datacenters para identificar e remover qualquer ponto de acesso sem fio não autorizado (*Rogue AP*), mesmo em locais onde o Wi-Fi teoricamente "não existe"!

## Por que importa
Como o **Kismet** atende simultaneamente às duas modalidades exigidas pelo PCI-DSS: **(Modalidade A) WIDS Automatizado Contínuo** nos datacenters e **(Modalidade B) Varredura Física (*Site Survey / Walk-Through*) com GPS** nas filiais?

## Como funciona
Na Modalidade A, os sensores remotos `kismet_cap_*` + regras `apspoof=` / `devicefound=` monitoram o ar 24x7; na Modalidade B, o auditor caminha pelas instalações com um notebook/tablet rodando o Kismet + receptor GPS (`gps=gpsd:host=localhost,port=2947`) e ao final gera o inventário completo JSON/CSV e o mapa **`kismetdb_to_kml`** comprovando os locais auditados e os BSSIDs detectados!

## Exemplo
```bash
# Limpar logs sensiveis (kismetdb_strip_packets) e exportar relatorio KML georreferenciado e tabela de dispositivos para evidencia de auditoria PCI-DSS 11.2
kismetdb_strip_packets --in ./Auditoria-Trimestral-Q4.kismet --out ./Evidencia-PCI-Sem-Pacotes.kismet
kismetdb_to_kml --in ./Evidencia-PCI-Sem-Pacotes.kismet --out ./Mapa-Cobertura-Auditoria-Q4.kml
```

## Limites e trade-offs
Veja o utilitário **`kismetdb_strip_packets`** no exemplo acima: ele cria uma cópia limpa do arquivo `.kismet` **removendo 100% dos pacotes brutos capturados**, mas preservando intactos todos os dispositivos detectados, coordenadas GPS, timestamps e alertas WIDS — gerando o artefato de evidência perfeito e leve para anexar ao relatório de conformidade PCI-DSS sem reter tráfego de rede!

## Como verificar
Cruze a lista de endereços MAC (`BSSID`) encontrada no `kismetdb_dump_devices` com a tabela ARP/MAC Address Table dos switches cabeados (`bridge mdb` / `show mac address-table`) para descobrir instantaneamente se algum AP desconhecido visto no ar está fisicamente plugado em uma porta de rede interna da empresa!

## Conexões
- [[kismet-seguranca-execucao-suid-grupo-kismet-privsep-api-keys]] — Veja também: Arquitetura de **Privilege Separation (`privsep`)** do Kismet: Por Que o Servidor `kismet` Roda Sem Privilégios de `root` Usando Helpers SUID Restritos ao Grupo `kismet`?.
- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Referência cruzada direta com kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources.
- [[kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json]] — Referência cruzada direta com kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json.
- [[kismet-filtros-pacotes-privacidade-pcapng-mascaramento-compliance]] — Referência cruzada direta com kismet-filtros-pacotes-privacidade-pcapng-mascaramento-compliance.

## Fontes
- [Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)](https://raw.githubusercontent.com/kismetwireless/kismet/master/README.md) — repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets; consultado em 2026-10-03.
- [Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)](https://www.kismetwireless.net/docs/readme/intro/kismet/) — documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`; consultado em 2026-10-03.
