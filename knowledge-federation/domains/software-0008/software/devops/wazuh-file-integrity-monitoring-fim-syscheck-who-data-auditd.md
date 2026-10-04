---
id: software.devops.tranche20.001962
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
fontes: ["https://raw.githubusercontent.com/wazuh/wazuh/master/README.md", "https://documentation.wazuh.com/current/getting-started/components/index.html", "https://github.com/wazuh/wazuh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Wazuh File Integrity Monitoring (`FIM` / `syscheck`): detecção em tempo real de alterações em arquivos e atribuição `whodata`

## Em uma frase
O módulo **File Integrity Monitoring (FIM / `syscheck`)** do Wazuh monitora diretórios e arquivos críticos do sistema operacional (como `/etc`, `/bin`, `/usr/sbin`), detectando alterações de conteúdo (hashes criptográficos SHA-256), permissões, propriedade e atributos, e identificando nativamente **qual usuário e qual processo (`whodata`)** realizou a modificação.

## Por que importa
Saber apenas que o arquivo `/etc/passwd` ou `/etc/ssh/sshd_config` foi modificado às 03:14 da manhã não basta para uma investigação forense ou requisito do PCI-DSS 11.5: o analista de SOC precisa saber qual conta de usuário e qual binário executou a escrita.

## Como funciona
Configurado no bloco `<syscheck>` do `/var/ossec/etc/ossec.conf` (ou centralmente via `agent.conf`), o FIM opera em três modos: 1) **Scheduled** (varredura periódica); 2) **`realtime="yes"`** (notificação instantânea via `inotify` do kernel Linux); e 3) **`whodata="yes"`** (integração com o subsistema Linux Audit `auditd` ou SACLs do Windows para registrar o `user_id`, `process_name` e `process_id` exatos da alteração).

## Exemplo
```xml
<syscheck>
  <disabled>no</disabled>
  <frequency>43200</frequency>
  <directories check_all="yes" realtime="yes" report_changes="yes">/etc,/usr/bin,/usr/sbin</directories>
  <directories check_all="yes" whodata="yes">/etc/ssh,/etc/sudoers.d</directories>
</syscheck>
```

## Limites e trade-offs
A opção `report_changes="yes"` calcula e exibe o `diff` linha por linha das alterações em arquivos de texto, mas **não** deve ser habilitada em arquivos que contenham chaves privadas ou senhas em texto claro para não enviar o segredo para os logs de alerta.

## Como verificar
Verifique nos logs do agente (`/var/ossec/logs/ossec.log`) a ativação do monitoramento `realtime`/`whodata` após reiniciar o `wazuh-agent`.

## Conexões
- [[wazuh-arquitetura-open-source-xdr-siem-server-indexer-dashboard-agent]] — Veja também: Wazuh: arquitetura da plataforma open-source de XDR e SIEM (`Wazuh Server`, `Wazuh Indexer`, `Wazuh Dashboard` e `Wazuh Agent`).
- [[wazuh-vulnerability-detection-syscollector-inventario-correlacao-cve]] — Veja também: Wazuh Vulnerability Detection e `syscollector`: inventário contínuo de pacotes e correlação automatizada com bancos de CVEs.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
