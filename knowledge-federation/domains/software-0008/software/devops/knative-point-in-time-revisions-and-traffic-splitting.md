---
id: software.devops.tranche05.000462
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

# Snapshots imutáveis (Revisions) e divisão percentual de tráfego no Knative Serving

## Em uma frase
Uma das quatro capacidades fundamentais destacadas no README oficial do Knative Serving é a criação automática de **snapshots point-in-time do código implantado e das configurações**. A cada alteração na especificação de template de um Knative `Service` (como uma nova imagem OCI, variável de ambiente ou limite de recursos), o controlador cria uma **`Revision`** imutável correspondente àquele instante. A camada de **roteamento e programação de rede** do Knative permite então dividir o tráfego HTTP/gRPC em porcentagens exatas entre múltiplas Revisions (por exemplo, 90% na revisão estável e 10% na nova revisão canário) ou fazer rollback instantâneo.

## Por que importa
Em um `Deployment` tradicional do Kubernetes, o histórico de revisões guarda apenas o template do `ReplicaSet` e o balanceamento entre duas versões depende da proporção bruta do número de pods. Com Revisions imutáveis e roteamento de camada 7 no Knative Serving, é possível enviar 1% do tráfego para uma nova revisão mesmo que ela tenha apenas 1 pod ativo.

## Como funciona
Ao realizar entregas canário ou testes blue/green no Knative Serving, fixe os nomes das Revisions no bloco `traffic` do Knative `Service` e aumente gradualmente o percentual de tráfego após validar as métricas de erro e latência.

## Exemplo
Durante o lançamento de uma nova versão de uma API crítica, o manifesto do Knative Service direciona `95%` do tráfego para `api-v1` e `5%` para `api-v2`; ao detectar um erro de negócio em `api-v2`, a equipe reverte `100%` do tráfego para `api-v1` em segundos sem precisar reconstruir imagens.

## Limites e trade-offs
Configure políticas de coleta de lixo (garbage collection) de Revisions antigas não referenciadas no ConfigMap `config-gc` do namespace `knative-serving` para evitar o acúmulo infinito de objetos `Revision` históricos no etcd.

## Como verificar
Liste as revisões criadas com `kubectl get revisions` e inspecione a distribuição percentual de tráfego ativa em `kubectl get routes`.

## Conexões
- [[knative-serverless-containers-and-middleware-primitives]] — Veja também: Knative Serving e as quatro primitivas para contêineres serverless no Kubernetes.
- [[knative-scale-to-zero-activator-and-autoscaler-architecture]] — Veja também: Arquitetura de escalonamento até zero (scale-to-zero) com os pods activator, autoscaler e autoscaler-hpa.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
