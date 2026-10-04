---
id: software.seguranca.tranche14.001355
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

# Enriquecimento em Tempo Real com **`wiseService` (*With Intelligence See Everything*)**, **YARA** em Fluxo (`yara.ini`) e **`arkime.rules`**

## Em uma frase
Como fazer com que cada pacote/sessão capturado pelo Arkime já seja rotulado automaticamente em tempo real na captura se o IP, domínio, hash MD5/SHA256 ou JA3 constar no seu **MISP / OpenCTI / AlienVault OTX / Abuse.ch**, ou se o conteúdo do fluxo casar com uma regra **YARA**?

## Por que importa
O Arkime possui três motores nativos de enriquecimento e detecção em tempo de captura: **(1) `wiseService` (*With Intelligence See Everything*)** — um microserviço do ecossistema Arkime que agrega fontes externas de Threat Intelligence (MISP, VirusTotal, OTX, listas CSV/JSON locais de ativos do CMDB, mapeamento de IP -> Usuário do Active Directory/VPN) e enriquece os metadados SPI das sessões em tempo real com cache em memória/Redis!;

## Como funciona
Na camada complementar de operação e execução técnica: **(2) Integração Nativa com `YARA` (`yara=ARKIME_INSTALL_DIR/etc/yara.ini`)** — o binário `capture` avalia regras YARA compiladas diretamente sobre os fluxos TCP remontados e adiciona o campo `yara` com o nome da regra disparada na sessão!; e **(3) `rulesFiles` (`arkime.rules`)**!

## Exemplo
```yaml
# Exemplo de regra em /opt/arkime/etc/arkime.rules: adiciona tag de alerta ou ignora gravacao de PCAP com base em campos SPI ou BPF
version: 1
rules:
  - name: "Rotular conexoes SSH originadas de fora da VPN de gerencia"
    when: "fieldSet"
    fields:
      protocols: "ssh"
    ops:
      "_tags": "alerta:ssh-fora-padrao"
```

## Limites e trade-offs
Combinar o **`wiseService`** com o seu inventário interno (CMDB / IPAM / DHCP) transforma a experiência do analista no Arkime: em vez de ver apenas `ip.src == 10.20.4.88`, a sessão passa a mostrar os campos customizados `asset.owner == "Financeiro"`, `asset.hostname == "NOT-FIN-042"` e `user == "carlos.mendes"` diretamente na tela de busca!

## Como verificar
No `arkime.rules`, você pode usar `when: "everyPacket"`, `when: "sessionSetup"`, `when: "afterClassify"` ou `when: "fieldSet"` para executar ações como adicionar `_tags` ou acionar `dontSaveSPI` / `maxPacketsToSave`.

## Conexões
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Veja também: Caça a Ameaças (**Threat Hunting**) no Arkime: Linguagem de Expressões de Busca, **Sessions**, **SPI View**, **SPI Graph** e **Connections Graph**.
- [[arkime-ecossistema-parliament-cont3xt-esproxy-federacao-multi-cluster]] — Veja também: O Ecossistema Completo do Arkime: **`Parliament`** (Multi-Cluster Dashboard), **`Cont3xt`** (Agregador de CTI/OSINT) e **`esProxy`**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
