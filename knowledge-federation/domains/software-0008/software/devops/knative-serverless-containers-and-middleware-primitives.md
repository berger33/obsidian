---
id: software.devops.tranche05.000461
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

# Knative Serving e as quatro primitivas para contêineres serverless no Kubernetes

## Em uma frase
O Knative Serving (`knative.dev/docs/serving/`), licenciado sob Apache-2.0, constrói sobre o Kubernetes para suportar a implantação e o atendimento de aplicações e funções como **contêineres serverless**. Conforme define o README oficial, o projeto fornece primitivas de middleware que habilitam quatro capacidades centrais: (1) **implantação rápida** de contêineres serverless; (2) **escalonamento automático para cima e até zero (automatic scaling up and down to zero)**; (3) **roteamento e programação de rede**; e (4) **snapshots point-in-time** do código implantado e de suas configurações.

## Por que importa
No Kubernetes padrão, expor um microsserviço exige gerenciar separadamente `Deployment`, `Service`, `Ingress`/`HTTPRoute` e `HorizontalPodAutoscaler` (que além disso não escala até zero nativamente por tráfego HTTP). O Knative Serving unifica todo esse ciclo em um único modelo declarativo `Service` (`serving.knative.dev/v1`).

## Como funciona
Adote o Knative Serving quando precisar executar microsserviços HTTP/gRPC, funções serverless ou endpoints de inferência de IA que devem escalar rapidamente durante picos de requisições e recolher para zero réplicas quando ociosos.

## Exemplo
Uma equipe de dados implanta múltiplos serviços de inferência leve como Knative Services; fora do horário comercial, os serviços sem tráfego escalam para `0` pods liberando recursos do cluster, e ao receber uma nova chamada HTTP são ativados automaticamente.

## Limites e trade-offs
Certifique-se de que as aplicações implantadas no Knative Serving sejam stateless e iniciem rapidamente (fast cold start), pois contêineres que levam vários minutos para subir degradam a experiência quando escalam a partir de zero.

## Como verificar
Aplique um manifesto `Service` do Knative Serving (`apiVersion: serving.knative.dev/v1`) e verifique com `kubectl get ksvc` a criação da URL de rota e o estado `READY True`.

## Conexões
- [[knative-point-in-time-revisions-and-traffic-splitting]] — Veja também: Snapshots imutáveis (Revisions) e divisão percentual de tráfego no Knative Serving.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
