---
id: software.devops.tranche20.001968
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

# Wazuh Cloud Security Monitoring: ingestão em nível de API de AWS (CloudTrail/GuardDuty), Google Cloud Pub/Sub e Microsoft Azure

## Em uma frase
Além de monitorar instâncias individuais com agentes, o Wazuh monitora a infraestrutura de nuvem pública diretamente em **nível de API** através de módulos de integração nativos para **Amazon AWS** (`wodle name="aws-s3"`, cobrindo CloudTrail, GuardDuty, VPC Flow Logs, Config e WAF), **Google Cloud Platform** (`gcp-pubsub` / `gcp-bucket`) e **Microsoft Azure** (`azure-logs`).

## Por que importa
Se um invasor roubar credenciais de console da AWS e criar uma nova chave IAM ou abrir um Security Group na porta 22, nenhum agente instalado dentro de uma VM EC2 verá essa chamada de API da conta cloud.

## Como funciona
O Wazuh Server busca periodicamente os logs de auditoria da nuvem (como eventos do AWS CloudTrail em S3 ou mensagens de Audit Logs no GCP Pub/Sub), aplica regras específicas de postura de nuvem e correlaciona eventos de API cloud com alertas vindos dos agentes nas VMs.

## Exemplo
```xml
<wodle name="aws-s3">
  <disabled>no</disabled>
  <interval>10m</interval>
  <run_on_start>yes</run_on_start>
  <bucket type="cloudtrail">
    <name>corp-prod-cloudtrail-logs</name>
    <aws_profile>wazuh-readonly</aws_profile>
  </bucket>
</wodle>
```

## Limites e trade-offs
Em implantações em EKS/EC2 ou GKE, autentique os módulos cloud do Wazuh usando *IAM Roles for Service Accounts (IRSA)* / *Instance Profiles* com permissão somente-leitura mínima sobre o bucket/tópico de auditoria.

## Como verificar
Verifique nos logs do `wazuh-modulesd` (`/var/ossec/logs/ossec.log`) a conclusão sem erros do ciclo de coleta do `aws-s3` ou `gcp-pubsub`.

## Conexões
- [[wazuh-seguranca-containers-docker-listener-kubernetes-audit-logs]] — Veja também: Wazuh para Containers e Kubernetes: integração nativa com Docker Engine (`docker-listener`) e Kubernetes Audit Webhook.
- [[wazuh-clustering-alta-disponibilidade-master-workers-filebeat-indexer]] — Veja também: Wazuh Clustering e Escalabilidade: topologia `master`/`worker` do Wazuh Server, Filebeat e cluster `Wazuh Indexer`.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
