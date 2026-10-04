---
id: software.devops.tranche20.001969
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

# Wazuh Clustering e Escalabilidade: topologia `master`/`worker` do Wazuh Server, Filebeat e cluster `Wazuh Indexer`

## Em uma frase
Para suportar dezenas de milhares de agentes com alta disponibilidade, tanto o **Wazuh Server** (configurado em cluster `master` + múltiplos nós `worker` sincronizados na porta TCP `1516`) quanto o **Wazuh Indexer** (cluster OpenSearch multi-nó alimentado via **Filebeat** com TLS mútuo) escalam horizontalmente.

## Por que importa
Um único nó Wazuh Server analisa dados de centenas a poucos milhares de agentes; acima disso, concentrar o registro (`1515`) e a recepção contínua de eventos (`1514`) em uma única máquina cria gargalo de CPU e ponto único de falha.

## Como funciona
Em um cluster Wazuh Server: 1) o nó **`master`** centraliza a configuração (arquivos `agent.conf`, decoders, rules e grupos) e a replica automaticamente para todos os nós **`worker`**; 2) os agentes conectam-se através de um balanceador de carga aos nós `worker` (porta `1514/TCP`), que processam os eventos em paralelo; e 3) o **Filebeat** em cada nó do Wazuh Server lê `/var/ossec/logs/alerts/alerts.json` e envia com segurança para o cluster **Wazuh Indexer**.

## Exemplo
```bash
# Inspecionando os nós ativos e o estado de sincronização de um cluster Wazuh Server:
/var/ossec/bin/cluster_control -l
/var/ossec/bin/cluster_control -i
```

## Limites e trade-offs
Mantenha a chave simétrica `<key>` do bloco `<cluster>` no `ossec.conf` com exatamente 32 caracteres hexadecimais idênticos entre o `master` e todos os `workers`, e proteja a porta `1516` restrita à rede privada interna dos servidores Wazuh.

## Como verificar
Execute `/var/ossec/bin/cluster_control -l` e `filebeat test output` em cada nó do servidor para confirmar a saúde do cluster e a conexão com o Wazuh Indexer.

## Conexões
- [[wazuh-cloud-security-monitoring-aws-cloudtrail-gcp-pubsub-azure]] — Veja também: Wazuh Cloud Security Monitoring: ingestão em nível de API de AWS (CloudTrail/GuardDuty), Google Cloud Pub/Sub e Microsoft Azure.
- [[wazuh-centralized-configuration-agent-conf-grupos-enrollment-wazuh-kubernetes]] — Veja também: Wazuh Gerenciamento Centralizado (`agent.conf`) e Orquestração (`wazuh-kubernetes` / Ansible): grupos de agentes e rollout.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://documentation.wazuh.com/current/getting-started/components/index.html) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
