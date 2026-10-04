---
id: software.devops.tranche17.001616
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/clusternet/clusternet/main/README.md", "https://clusternet.io/docs/introduction/", "https://github.com/clusternet/clusternet"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clusternet: distribuição nativa de Helm Charts e artefatos OCI via CRD `HelmChart` e `HelmRelease`

## Em uma frase
O Clusternet gerencia o ciclo de vida de pacotes Helm em múltiplos clusters nativamente através dos CRDs `HelmChart` e `HelmRelease` (`apps.clusternet.io/v1alpha1`), suportando tanto repositórios HTTP tradicionais de `index.yaml` quanto registries OCI (`oci://...`).

## Por que importa
Implantar charts Helm em 100 clusters usando pipelines de CI imperativos que rodam `helm upgrade` em loop não possui reconciliação contínua se um cluster estiver temporariamente offline no momento do pipeline.

## Como funciona
O usuário declara um objeto `HelmChart` (especificando `repo`, `chart`, `version` e `targetNamespace`) e o referencia dentro de `spec.feeds` de uma `Subscription`. O Clusternet resolve o chart, aplica quaisquer valores customizados via `Globalization`/`Localization` (`type: Helm`) e cria automaticamente objetos `HelmRelease` que o `clusternet-agent` reconcilia localmente em cada cluster filho.

## Exemplo
```yaml
apiVersion: apps.clusternet.io/v1alpha1
kind: HelmChart
metadata:
  name: redis-cluster-chart
  namespace: default
spec:
  repo: oci://registry-1.docker.io/bitnamicharts
  chart: redis
  version: 20.1.0
  targetNamespace: cache-system
  createNamespace: true
```

## Limites e trade-offs
Se o repositório OCI ou HTTPS do chart exigir autenticação privada, as credenciais devem ser fornecidas via `Secret` referenciado no objeto `HelmChart` para que tanto o plano de controle quanto os agentes possam validar e instalar o pacote.

## Como verificar
Consulte `kubectl get helmchart -A` e `kubectl get helmrelease -n clusternet-abcde` para verificar a fase de instalação (`Phase: Installed`) do release Helm em cada cluster filho.

## Conexões
- [[clusternet-globalization-localization-overrides-duas-etapas-canary]] — Veja também: Clusternet: overrides em dois estágios (`Globalization` e `Localization`) com prioridades e rollback.
- [[clusternet-resource-predictor-framework-agendamento-capacidade-dinamica]] — Veja também: Clusternet: *Cluster Resource Predictor Framework* para agendamento dinâmico baseado em capacidade.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
