---
id: software.seguranca.tranche14.001379
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
fontes: ["https://raw.githubusercontent.com/gravitational/teleport/master/README.md", "https://goteleport.com/docs/reference/architecture/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura de Alta Disponibilidade, **Armazenamento de Auditoria e Gravações (S3 / GCS / MinIO)** e Exportação de Eventos para **SIEM (`event-handler`)** no Teleport

## Em uma frase
Como implantar o **Plano de Controle do Teleport (`Auth Service` + `Proxy Service`)** em Alta Disponibilidade (HA) suportando milhares de servidores e garantindo que os logs de auditoria e as gravações de sessões SSH/K8s/RDP sejam armazenados de forma **imutável e à prova de adulteração**?

## Por que importa
Conforme a referência de arquitetura oficial do Teleport: **(1) O `Teleport Proxy Service` é 100% stateless** e escala horizontalmente atrás de um Load Balancer L4;

## Como funciona
Na camada complementar de operação e execução técnica: **(2) O `Teleport Auth Service`** escala em múltiplas réplicas quando conectado a um backend de estado transacional HA (**AWS DynamoDB, Google Cloud Firestore, CockroachDB ou PostgreSQL HA**) e um Object Storage (**Amazon S3, Google Cloud Storage ou MinIO**) para armazenar as gravações de sessão (`audit_sessions_uri: 's3://bucket-gravacoes-teleport'`)!; e **(3) Exportação para SIEM**: o plugin oficial **`teleport-event-handler`** consome o fluxo de eventos da API gRPC do Auth Service com mTLS e envia os logs JSON em tempo real para **OpenSearch, Elasticsearch, Splunk, Wazuh ou Fluentd**!

## Exemplo
```yaml
# Configurar na secao teleport.storage do /etc/teleport.yaml do Auth Service o backend HA e o armazenamento de gravacoes de sessao em S3
version: v3
teleport:
  nodename: auth-ha-01
  storage:
    type: dynamodb
    region: sa-east-1
    table_name: teleport-cluster-state
    audit_events_uri:
      - 'dynamodb://teleport-audit-events'
      - 'stdout://'
    audit_sessions_uri: 's3://empresa-teleport-session-recordings?region=sa-east-1'
```

## Limites e trade-offs
Habilite no bucket S3 / MinIO apontado por **`audit_sessions_uri`** o recurso **S3 Object Lock em modo `COMPLIANCE` (WORM — *Write Once, Read Many*)** com criptografia KMS: assim, uma vez que uma gravação de sessão SSH ou Kubernetes é enviada para o bucket, **nem mesmo um administrador root da conta AWS consegue apagar ou editar a gravação antes do prazo de retenção regulatório expirar**!

## Como verificar
Você também pode consultar os eventos de auditoria diretamente pela linha de comando administrativa com `tctl audit` ou reproduzir sessões gravadas com `tsh play <session-id>`.

## Conexões
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Veja também: Ingresso Seguro de Agentes (**Node Joining**) no Teleport: Eliminando Tokens Estáticos com **Cloud Auto-Joining (AWS IAM, GCP, Azure, Kubernetes)** e **TPM Joining**.
- [[teleport-federacao-trusted-clusters-leaf-root-isolamento-multi-tenant]] — Veja também: Federação Multi-Cluster e Multi-Cloud com **Trusted Clusters (`Root Cluster` e `Leaf Clusters`)** no Teleport.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Referência cruzada direta com teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf.
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Referência cruzada direta com arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
