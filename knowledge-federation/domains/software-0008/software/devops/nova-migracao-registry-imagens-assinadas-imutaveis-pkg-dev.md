---
id: software.devops.tranche12.001146
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md", "https://nova.docs.fairwinds.com/quickstart/", "https://nova.docs.fairwinds.com/usage/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Migração de Registry (us-docker.pkg.dev) e Imagens Assinadas e Imutáveis

## Em uma frase
A partir da versão `v3.12.0` do Fairwinds Nova, as imagens oficiais de container migraram do registro depreciado `quay.io/fairwinds/nova` para `us-docker.pkg.dev/fairwinds-ops/oss/nova`, adotando imagens criptograficamente assinadas e tags estritamente imutáveis.

## Por que importa
CronJobs Kubernetes e pipelines de CI que ainda referenciam `quay.io/fairwinds/nova` ou tags flutuantes como `latest`, `v3` ou `v3.11` deixam de receber atualizações ou falham ao puxar versões novas após a desativação das tags mutáveis.

## Como funciona
Para executar o Nova dentro do cluster Kubernetes (como um `CronJob` de auditoria ou via Helm chart), a especificação do Pod deve referenciar a versão completa `us-docker.pkg.dev/fairwinds-ops/oss/nova:v<major>.<minor>.<patch>` ou fixar a imagem por digest imutável `@sha256:<digest>`, garantindo integridade de supply chain.

## Exemplo
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nova-cluster-audit
  namespace: platform-audit
spec:
  schedule: "0 6 * * 1"
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: nova-reader
          restartPolicy: Never
          containers:
            - name: nova
              image: us-docker.pkg.dev/fairwinds-ops/oss/nova:v3.12.0
              args: ["find", "--helm", "--containers", "--wide"]
```

## Limites e trade-offs
Manter referências legadas a `quay.io/fairwinds/nova:latest` em manifestos GitOps congela silenciosamente o scanner em uma versão antiga sem suporte.

## Como verificar
Audite todos os manifestos do cluster procurando por `quay.io/fairwinds/` e migre para `us-docker.pkg.dev/fairwinds-ops/oss/nova` com tag semântica completa ou digest SHA-256.

## Conexões
- [[nova-containers-errored-non-semver-timeout-diagnostico-registries]] — Veja também: Fairwinds Nova: Diagnóstico de Erros de Registry e Tags Não-SemVer (--show-errored-containers e --show-non-semver).
- [[nova-rbac-minimo-serviceaccount-leitura-helm-secrets-pods]] — Veja também: Fairwinds Nova: Configuração de RBAC de Mínimo Privilégio para Execução In-Cluster.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/quickstart/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/usage/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
