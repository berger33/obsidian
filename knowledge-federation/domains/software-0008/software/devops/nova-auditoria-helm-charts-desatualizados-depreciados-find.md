---
id: software.devops.tranche12.001141
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

# Fairwinds Nova: Detecção de Helm Charts Desatualizados e Depreciados no Cluster (nova find)

## Em uma frase
Fairwinds Nova é uma ferramenta open-source de linha de comando e auditoria contínua que escaneia releases Helm instalados em um cluster Kubernetes e os compara contra repositórios Helm conhecidos e o ArtifactHub para identificar versões desatualizadas (`Old: true`) ou depreciadas (`Deprecated: true`).

## Por que importa
À medida que um cluster acumula dezenas de add-ons instalados via Helm (`cert-manager`, `metrics-server`, `ingress-nginx`, `external-dns`, `kube-prometheus-stack`), acompanhar manualmente novas releases e avisos de depreciação de charts torna-se inviável.

## Como funciona
Ao executar `nova find` (ou `nova find --wide`), o Nova consulta os Secrets/ConfigMaps de releases Helm no cluster, extrai o nome do chart, a versão instalada e a `appVersion`, e cruza esses dados com o ArtifactHub (por padrão com `--poll-artifacthub=true`) ou repositórios Helm informados via `--url`, gerando um relatório tabular ou JSON com `Installed`, `Latest`, `Old` e `Deprecated`.

## Exemplo
```bash
nova find --wide --format table
nova find --show-old --format json --output-file nova-helm-report.json
jq '.helm[] | select(.outdated == true or .deprecated == true)' nova-helm-report.json
```

## Limites e trade-offs
Confiar apenas na versão do binário da aplicação (`appVersion`) sem atualizar charts marcados como `Deprecated: true` mantém manifestos com APIs Kubernetes antigas e templates sem correções de segurança.

## Como verificar
Execute `nova find --wide --format table` regularmente em todos os clusters e priorize a migração imediata de qualquer release onde a coluna `Deprecated` seja `true`.

## Conexões
- [[nova-auditoria-imagens-containers-semver-minor-patch]] — Veja também: Fairwinds Nova: Auditoria de Imagens de Containers Desatualizadas com --containers.

## Fontes
- [Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)](https://raw.githubusercontent.com/FairwindsOps/nova/master/README.md) — README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova; consultado em 2026-10-03.
- [Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)](https://nova.docs.fairwinds.com/quickstart/) — Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON; consultado em 2026-10-03.
- [Fairwinds Nova — Official Documentation Portal](https://nova.docs.fairwinds.com/usage/) — Portal oficial de documentação do Fairwinds Nova; consultado em 2026-10-03.
