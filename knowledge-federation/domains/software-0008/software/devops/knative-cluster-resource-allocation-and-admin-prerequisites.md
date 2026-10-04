---
id: software.devops.tranche05.000465
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

# Dimensionamento de CPU/memória do cluster e pré-requisitos de cluster-admin para o Knative Serving

## Em uma frase
A seção *Starting Knative Serving* em `DEVELOPMENT.md` especifica os pré-requisitos de permissões e recursos de hardware para operar o Knative Serving com estabilidade: (1) o usuário instalador precisa ter permissões de **`cluster-admin`**, especificamente para criar objetos de escopo de cluster (`Namespace`, `CustomResourceDefinition`, `ClusterRole` e `ClusterRoleBinding`), além da versão mínima suportada do Kubernetes (`>= 1.20.0`); e (2) recomenda-se alocar **no mínimo 6 CPUs e 8 GB de memória RAM** para uma instalação Kubernetes de nó único (single-node), ou **pelo menos 4 CPUs e 8 GB de memória RAM para cada nó** em um cluster de 3 nós.

## Por que importa
Subir o Knative Serving (junto com camada de ingress, `cert-manager` e cargas de trabalho) em uma VM local subdimensionada com apenas 2 CPUs e 2 GB de RAM causa estrangulamento de CPU (CPU throttling), falhas de timeout nos webhooks de admissão e despejo (eviction) de pods por pressão de memória.

## Como funciona
Antes de instalar o Knative Serving em clusters locais de desenvolvimento ou ambientes de homologação, configure a máquina virtual ou os nós trabalhadores para atender ou superar a recomendação oficial de **6 CPUs / 8 GB RAM** (nó único) ou **4 CPUs / 8 GB RAM por nó** (3 nós).

## Exemplo
Ao preparar um ambiente de teste em estação de trabalho para desenvolver integrações com Knative Serving, o engenheiro reconfigura seu cluster local de 1 nó para 6 vCPUs e 8 GB de RAM conforme `DEVELOPMENT.md`, eliminando timeouts de webhook durante o deploy.

## Limites e trade-offs
Em ambientes corporativos onde engenheiros de aplicação não possuem `cluster-admin`, separe a instalação dos CRDs e `ClusterRoles` do Knative Serving (executada pela equipe de plataforma) do uso diário de recursos `Service` nos namespaces das equipes.

## Como verificar
Inspecione a capacidade alocável dos nós com `kubectl describe nodes` e confirme que a soma de CPU e memória atende aos patamares recomendados pelo guia oficial.

## Conexões
- [[knative-release-manifests-crds-core-hpa-and-nscert]] — Veja também: Manifestos oficiais de instalação do Knative Serving: serving-crds, serving-core, serving-hpa e serving-nscert.
- [[knative-ko-build-tool-and-local-registries-ko-local-kind-local]] — Veja também: Desenvolvimento e deploy de imagens Go no Knative com a ferramenta ko (ko.local, kind.local e --platform).

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
