---
id: software.devops.tranche20.001961
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://documentation.wazuh.com/current/getting-started/components/index.html", "https://raw.githubusercontent.com/wazuh/wazuh/master/README.md", "https://github.com/wazuh/wazuh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Wazuh: arquitetura da plataforma open-source de XDR e SIEM (`Wazuh Server`, `Wazuh Indexer`, `Wazuh Dashboard` e `Wazuh Agent`)

## Em uma frase
O **Wazuh** é uma plataforma gratuita e open-source de **XDR (*Extended Detection and Response*)** e **SIEM (*Security Information and Event Management*)** para proteção de cargas on-premises, virtualizadas, em containers e em nuvem, baseada no **`Wazuh Agent`** instalado nos endpoints e em três componentes centrais: **`Wazuh Server`**, **`Wazuh Indexer`** e **`Wazuh Dashboard`**.

## Por que importa
Operar ferramentas isoladas para análise de logs (syslog), monitoramento de integridade de arquivos (FIM), detecção de rootkits, varredura de vulnerabilidades (CVEs) e auditoria de conformidade (PCI-DSS/CIS) impede correlacionar eventos de um mesmo ataque em uma única linha do tempo.

## Como funciona
Na arquitetura oficial do Wazuh: 1) os **Wazuh Agents** (Linux, Windows, macOS, Solaris, AIX, HP-UX) coletam telemetria de sistema, logs, inventário e integridade de arquivos e enviam criptografados ao servidor; 2) o **Wazuh Server** processa os dados através de *decoders* e *rules* buscando indicadores de comprometimento (IOCs) e gerencia/atualiza os agentes remotamente; 3) o **Wazuh Indexer** (motor de busca full-text e analytics distribuído) indexa e armazena os alertas; e 4) o **Wazuh Dashboard** fornece a interface web de threat hunting e compliance.

## Exemplo
```bash
# Verificando o status dos serviços centrais do Wazuh Manager e listando agentes conectados:
systemctl status wazuh-manager
/var/ossec/bin/agent_control -l
```

## Limites e trade-offs
Além do monitoramento baseado em agentes, o Wazuh Server também monitora dispositivos *agentless* (firewalls, switches, roteadores, appliances de rede) recebendo logs via **Syslog** ou sondando configurações periodicamente via SSH/API.

## Como verificar
Execute `/var/ossec/bin/agent_control -l` no Wazuh Server para listar todos os agentes registrados e seu status (`Active` / `Disconnected`).

## Conexões
- [[wazuh-file-integrity-monitoring-fim-syscheck-who-data-auditd]] — Veja também: Wazuh File Integrity Monitoring (`FIM` / `syscheck`): detecção em tempo real de alterações em arquivos e atribuição `whodata`.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://documentation.wazuh.com/current/getting-started/components/index.html) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
