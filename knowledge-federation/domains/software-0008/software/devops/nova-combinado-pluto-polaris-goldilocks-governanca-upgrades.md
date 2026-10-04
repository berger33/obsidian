---
id: software.devops.tranche12.001148
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md", "https://nova.docs.fairwinds.com/usage/", "https://nova.docs.fairwinds.com/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Nova: Uso Combinado com Pluto, Polaris e Goldilocks no Planejamento de Upgrades de Cluster

## Em uma frase
Combinar o Fairwinds Nova (versões de charts Helm e imagens) com o Fairwinds Pluto (APIs Kubernetes depreciadas), Polaris (boas práticas de segurança/configuração) e Goldilocks (dimensionamento de recursos) forma um pipeline completo de prontidão antes de atualizar a versão do control plane Kubernetes.

## Por que importa
Quando uma equipe descobre via Pluto que um `Ingress` ou `PodDisruptionBudget` instalado por um chart Helm de terceiro usa uma API removida na próxima versão do Kubernetes, a correção correta não é editar o recurso manualmente no cluster, mas descobrir com o Nova qual versão mais nova daquele chart Helm já atualizou os manifestos.

## Como funciona
No roteiro de upgrade de cluster, executa-se primeiro `pluto detect-helm` para listar releases com APIs depreciadas e, em seguida, `nova find --wide --show-old` para verificar a versão mais recente (`Latest`) disponível de cada chart afetado, planejando o `helm upgrade` antes de atualizar os nós do Kubernetes.

## Exemplo
```bash
pluto detect-helm -o wide
nova find --helm --containers --wide --show-old --format table
```

## Limites e trade-offs
Atualizar o control plane do Kubernetes sem antes cruzar os alertas de API depreciada do Pluto com as versões de charts disponíveis no Nova deixa add-ons críticos impossibilitados de reconciliar após o upgrade.

## Como verificar
Integre `nova find` e `pluto detect-helm` no mesmo relatório semanal de saúde da plataforma para manter os charts base atualizados continuamente.

## Conexões
- [[nova-rbac-minimo-serviceaccount-leitura-helm-secrets-pods]] — Veja também: Fairwinds Nova: Configuração de RBAC de Mínimo Privilégio para Execução In-Cluster.
- [[nova-filtragem-namespace-context-include-all-relatorios-json]] — Veja também: Fairwinds Nova: Escopo por Namespace (--namespace), Multi-Contexto (--context) e Exportação JSON.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/usage/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/quickstart/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
