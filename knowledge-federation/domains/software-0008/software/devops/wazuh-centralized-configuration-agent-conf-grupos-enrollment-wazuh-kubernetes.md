---
id: software.devops.tranche20.001970
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

# Wazuh Gerenciamento Centralizado (`agent.conf`) e Orquestração (`wazuh-kubernetes` / Ansible): grupos de agentes e rollout

## Em uma frase
O Wazuh Server permite gerenciar e atualizar remotamente a configuração de milhares de agentes sem tocar em cada máquina individualmente por meio de **Agent Groups** e do arquivo centralizado **`/var/ossec/etc/shared/<group>/agent.conf`**, além de fornecer manifestos oficiais para **Kubernetes (`wazuh/wazuh-kubernetes`)**, Docker, Ansible e Terraform.

## Por que importa
Editar `/var/ossec/etc/ossec.conf` manualmente em 500 servidores Linux e 200 servidores Windows toda vez que um novo arquivo de log precisa ser monitorado é lento e inconsistente.

## Como funciona
Um mesmo agente pode pertencer a múltiplos grupos simultaneamente (por exemplo `linux`, `nginx` e `pci-dss`). O Wazuh Server mescla os arquivos `agent.conf` desses grupos, calcula o hash MD5 (`merged.mg`), distribui a configuração automaticamente pelo canal criptografado do agente e reinicia o agente remotamente quando necessário.

## Exemplo
```bash
# Criando um grupo de agentes, atribuindo o agente 001 ao grupo e verificando a sincronização:
/var/ossec/bin/agent_groups -a -g k8s-nodes -q
/var/ossec/bin/agent_groups -a -i 001 -g k8s-nodes -q
/var/ossec/bin/agent_groups -s -i 001
```

## Limites e trade-offs
Antes de salvar alterações em um `agent.conf` compartilhado que será distribuído para centenas de máquinas, valide sempre sua sintaxe com **`/var/ossec/bin/verify-agent-conf`**.

## Como verificar
Execute `/var/ossec/bin/verify-agent-conf` no Wazuh Server e confirme que zero erros são reportados antes da distribuição aos agentes.

## Conexões
- [[wazuh-clustering-alta-disponibilidade-master-workers-filebeat-indexer]] — Veja também: Wazuh Clustering e Escalabilidade: topologia `master`/`worker` do Wazuh Server, Filebeat e cluster `Wazuh Indexer`.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://documentation.wazuh.com/current/getting-started/components/index.html) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
