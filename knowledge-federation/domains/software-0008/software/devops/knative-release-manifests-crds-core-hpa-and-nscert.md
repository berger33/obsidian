---
id: software.devops.tranche05.000464
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/knative/serving/main/README.md", "https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md", "https://github.com/knative/serving"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Manifestos oficiais de instalação do Knative Serving: serving-crds, serving-core, serving-hpa e serving-nscert

## Em uma frase
O guia `DEVELOPMENT.md` documenta que a instalação completa de uma versão lançada do Knative Serving equivale à aplicação ordenada dos manifestos oficiais **`serving-crds.yaml`** (definições dos Custom Resource Definitions do Knative Serving), **`serving-core.yaml`** (controladores centrais, webhook, activator e autoscaler KPA), **`serving-hpa.yaml`** (controlador `autoscaler-hpa` para escalonamento baseado em Horizontal Pod Autoscaler do Kubernetes) e **`serving-nscert.yaml`** (gerenciamento de certificados por namespace, apoiado por `cert-manager`), além do job opcional de pós-instalação `default-domain.yaml` (que configura um domínio `sslip.io` quando o `LoadBalancer` possui endereço IPv4).

## Por que importa
Aplicar os controladores (`serving-core.yaml`) antes que os CRDs (`serving-crds.yaml`) estejam completamente estabelecidos (`Established`) no Kubernetes API Server faz com que os pods do controlador falhem na inicialização ao tentar registrar informers sobre tipos inexistentes.

## Como funciona
Ao instalar ou atualizar o Knative Serving, aplique primeiro `serving-crds.yaml`, aguarde `kubectl wait --for=condition=Established --all crd` e somente então aplique `serving-core.yaml` e as extensões opcionais (`serving-hpa.yaml`, camada de rede e `serving-nscert.yaml`).

## Exemplo
Em um script de bootstrap automatizado de cluster, a equipe aplica `serving-crds.yaml`, bloqueia em `kubectl wait --for=condition=Established --all crd`, aplica `serving-core.yaml` e `serving-hpa.yaml` e valida os Deployments em `knative-serving`.

## Limites e trade-offs
Observe a nota do guia oficial sobre o job opcional `default-domain.yaml` (`sslip.io`): ele só funciona automaticamente se o serviço `LoadBalancer` do cluster já possuir um endereço IPv4 atribuído (por exemplo via provedor cloud ou MetalLB).

## Como verificar
Verifique com `kubectl get crds | grep knative.dev` que todos os CRDs estão estabelecidos e que os pods em `knative-serving` subiram sem erros.

## Conexões
- [[knative-scale-to-zero-activator-and-autoscaler-architecture]] — Veja também: Arquitetura de escalonamento até zero (scale-to-zero) com os pods activator, autoscaler e autoscaler-hpa.
- [[knative-cluster-resource-allocation-and-admin-prerequisites]] — Veja também: Dimensionamento de CPU/memória do cluster e pré-requisitos de cluster-admin para o Knative Serving.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
