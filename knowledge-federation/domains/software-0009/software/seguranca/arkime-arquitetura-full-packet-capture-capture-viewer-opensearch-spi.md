---
id: software.seguranca.tranche14.001351
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

# Arquitetura do **Arkime (`arkime/arkime`, ex-Moloch)**: Sistema de **Full Packet Capture (FPC)** e Indexação de Metadados **SPI** em Escala Multi-Gigabit

## Em uma frase
Quando o seu NIDS (**Snort 3 / Suricata**) ou EDR dispara um alerta de possível intrusão ou exfiltração de dados, os logs resumidos dizem que houve uma conexão, mas **não mostram o conteúdo byte a byte real do que trafegou na rede**. Como gravar **100% dos pacotes brutos (`.pcap`) de links de 10 Gbps a 100 Gbps** e conseguir pesquisar e baixar qualquer conversa de dias ou semanas atrás em menos de 2 segundos?

## Por que importa
Criado originalmente na AOL em 2012 com o nome *Moloch* e mantido hoje como **Arkime (`arkime/arkime`, certificado OpenSSF Best Practices)**, o Arkime é a plataforma open-source padrão mundial de **Full Packet Capture (FPC) e Network Forensics em larga escala**!

## Como funciona
Sua arquitetura é formada por **3 componentes principais** que rodam de forma distribuída em quantos sensores você precisar: **(1) `capture`** — um binário multithreaded escrito em **C** que captura o tráfego da placa de rede, grava os pacotes brutos em arquivos `.pcap` padrão diretamente nos discos locais do sensor (com offsets exatos de byte) e faz o *parse* profundo de protocolos enviando **Metadados de Sessão (`SPI — Session Profile Information`)** para o banco de busca; **(2) `OpenSearch / Elasticsearch`** — indexa apenas os metadados SPI e os ponteiros para os arquivos `.pcap` locais de cada sensor; e **(3) `viewer`** — uma aplicação **Node.js** que roda em cada sensor (e centralizadamente) para servir a interface web, buscar sessões e transmitir apenas os pacotes solicitados pelo analista!

## Exemplo
```bash
# Verificar o status dos servicos arkimecapture e arkimeviewer em um sensor de rede Linux e inspecionar a configuracao principal
systemctl status arkimecapture arkimeviewer
head -n 35 /opt/arkime/etc/config.ini
```

## Limites e trade-offs
Entenda por que essa arquitetura **Descentralizada de Armazenamento de PCAP + Indexação Central de SPI** do Arkime escala para dezenas de Gigabits por segundo com custo mínimo: **os arquivos `.pcap` pesados nunca são enviados pela rede para o cluster OpenSearch**! Eles ficam gravados sequencialmente nos discos locais de cada sensor (`pcapDir`); quando você clica em uma sessão no navegador, o `viewer` central pede ao `viewer` daquele sensor específico para ler via `pread(2)` exatamente o offset de bytes daquela sessão no `.pcap` local!

## Como verificar
Como o Arkime grava arquivos `.pcap` padrão na pasta `pcapDir`, você também pode exportá-los com 1 clique para abrir diretamente no **Wireshark** ou analisar com **Snort 3 / Suricata / Zeek**!

## Conexões
- [[arkime-configuracao-config-ini-tiered-pcapdir-freespaceg-rotacao]] — Veja também: Configuração Hierárquica (**`/opt/arkime/etc/config.ini`**), Retenção Automática de Disco (**`freeSpaceG`**) e Timeouts de Fluxo no Arkime.
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Referência cruzada direta com arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
