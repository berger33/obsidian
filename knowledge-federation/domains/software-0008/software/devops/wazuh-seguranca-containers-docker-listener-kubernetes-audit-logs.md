---
id: software.devops.tranche20.001967
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

# Wazuh para Containers e Kubernetes: integração nativa com Docker Engine (`docker-listener`) e Kubernetes Audit Webhook

## Em uma frase
O Wazuh oferece visibilidade profunda de segurança para ambientes containerizados por meio da integração nativa do agente com a API do **Docker Engine** (`wodle name="docker-listener"`) e da ingestão dos **Audit Logs do Kubernetes** (`kube-apiserver`) no Wazuh Server.

## Por que importa
Em hosts que rodam containers, monitorar apenas o sistema operacional host sem visibilidade sobre eventos do daemon Docker ou chamadas à API do Kubernetes não detecta a criação de um container `--privileged`, a execução de um shell interativo `docker exec` / `kubectl exec` ou alterações em volumes persistentes.

## Como funciona
O módulo `docker-listener` no Wazuh Agent escuta em tempo real os eventos do daemon Docker, gerando alertas imediatos quando containers iniciam em modo privilegiado, montam caminhos sensíveis do host, abrem shells interativos ou sofrem falhas de healthcheck.

## Exemplo
```xml
<wodle name="docker-listener">
  <interval>10m</interval>
  <attempts>5</attempts>
  <run_on_start>yes</run_on_start>
  <disabled>no</disabled>
</wodle>
```

## Limites e trade-offs
Para que o `docker-listener` funcione nos nós de containers, o ambiente Python do host (ou container do agente) precisa do pacote `docker` (`python3-docker`) e permissão de leitura no socket `/var/run/docker.sock`.

## Como verificar
Inicie um container de teste com `--privileged` e verifique a geração imediata do alerta de container privilegiado no painel *Docker / Containers* do Wazuh Dashboard.

## Conexões
- [[wazuh-active-response-bloqueio-automatico-ameacas-firewall-drop]] — Veja também: Wazuh Active Response: execução automatizada de contramedidas (`firewall-drop`, bloqueio de IP e isolamento) sob ataque.
- [[wazuh-cloud-security-monitoring-aws-cloudtrail-gcp-pubsub-azure]] — Veja também: Wazuh Cloud Security Monitoring: ingestão em nível de API de AWS (CloudTrail/GuardDuty), Google Cloud Pub/Sub e Microsoft Azure.

## Fontes
- [Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)](https://raw.githubusercontent.com/wazuh/wazuh/master/README.md) — README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem; consultado em 2026-10-03.
- [Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)](https://documentation.wazuh.com/current/getting-started/components/index.html) — Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador; consultado em 2026-10-03.
- [Wazuh — Official GitHub Repository](https://github.com/wazuh/wazuh) — Repositório oficial GPLv2 do Wazuh; consultado em 2026-10-03.
