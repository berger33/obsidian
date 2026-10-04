---
id: software.seguranca.tranche14.001356
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

# O Ecossistema Completo do Arkime: **`Parliament`** (Multi-Cluster Dashboard), **`Cont3xt`** (Agregador de CTI/OSINT) e **`esProxy`**

## Em uma frase
Quando uma grande corporação ou MSSP opera múltiplos clusters Arkime independentes (por exemplo: Cluster Datacenter SP, Cluster AWS us-east-1, Cluster Rede Industrial OT) e uma equipe de analistas de SOC/CTI precisa investigar indicadores externos rapidamente, como as aplicações complementares oficiais do Arkime se encaixam?

## Por que importa
O projeto Arkime inclui três aplicações dedicadas prontas para produção: **(1) `Parliament`** — o painel de monitoramento e portal unificado para múltiplos clusters Arkime, que verifica em tempo real se algum sensor parou de capturar pacotes, se o espaço em disco (`freeSpaceG`) está crítico ou se a taxa de pacotes por segundo caiu abruptamente (enviando alertas imediatos!);

## Como funciona
Na camada complementar de operação e execução técnica: **(2) `Cont3xt` (*Context*)** — uma ferramenta de **Contextual Threat Intelligence / OSINT** para analistas de SOC: você cola um IP, domínio, URL, hash, e-mail ou telefone (ou clica nele dentro do Arkime Viewer!) e o `Cont3xt` consulta simultaneamente dezenas de APIs (Shodan, VirusTotal, Spur, GreyNoise, Whois, DNS, Censys, AbuseIPDB, MISP) exibindo um relatório consolidado em árvore com *Link Buttons* customizáveis!; e **(3) `esProxy`** — um proxy de segurança que fica entre os sensores `capture` remotos e o cluster OpenSearch/Elasticsearch!

## Exemplo
```bash
# Verificar o status dos servicos opcionais do ecossistema Arkime (Parliament, Cont3xt e Wise) no servidor central
systemctl status arkimeparliament arkimecont3xt arkimewise || true
```

## Limites e trade-offs
Por que o **`Cont3xt`** (que pode inclusive ser rodado de forma standalone por qualquer equipe de SOC/DFIR mesmo sem captura de pacotes!) economiza tanto tempo na triagem de incidentes? Porque em vez de o analista abrir 15 abas diferentes no navegador para checar um IP suspeito no VirusTotal, AbuseIPDB, Shodan, GreyNoise e Whois, uma única busca no `Cont3xt` dispara todas as integrações em paralelo e permite baixar o dossiê completo da investigação!

## Como verificar
No **`Parliament`**, configure os alertas de **`No Packets`** (sensor sem receber tráfego da TAP/SPAN) e **`Out of Date`** (sensor com relógio NTP dessincronizado, o que arruinaria a correlação cronológica de PCAPs!).

## Conexões
- [[arkime-enriquecimento-wiseservice-threat-intel-regras-yara-tagger]] — Veja também: Enriquecimento em Tempo Real com **`wiseService` (*With Intelligence See Everything*)**, **YARA** em Fluxo (`yara.ini`) e **`arkime.rules`**.
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Veja também: Segurança e Autenticação do **Arkime Viewer**: `passwordSecret`, `serverSecret`, TLS Mútuo entre Sensores e Integração **SSO (`authMode=header-jwt` / OIDC)**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
