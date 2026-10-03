---
id: software.devops.tranche05.000463
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

# Arquitetura de escalonamento até zero (scale-to-zero) com os pods activator, autoscaler e autoscaler-hpa

## Em uma frase
A listagem oficial de pods no namespace `knative-serving` documentada em `DEVELOPMENT.md` revela os cinco componentes fundamentais do plano de controle e dados do Knative Serving: **`activator`**, **`autoscaler`**, **`autoscaler-hpa`**, **`controller`** e **`webhook`**. Enquanto o `controller` e o `webhook` gerenciam a validação, mutação e reconciliação dos CRDs, o **`autoscaler`** (Knative Pod Autoscaler — KPA, orientado a concorrência de requisições em tempo real) e o **`autoscaler-hpa`** (integração com o HPA de CPU/memória do Kubernetes) decidem a contagem de réplicas, e o **`activator`** atua no caminho de dados segurando (buffering) requisições que chegam para uma Revision escalada em zero (`0` pods) enquanto solicita ao `autoscaler` o provisionamento imediato do primeiro pod.

## Por que importa
Sem o componente `activator` segurando a conexão HTTP enquanto o primeiro pod sobe do zero, qualquer requisição recebida durante o estado `0` réplicas receberia erro imediato `502/503 Connection Refused`. A cooperação entre `activator` e `autoscaler` torna o scale-to-zero transparente para o cliente.

## Como funciona
Monitore a saúde e a latência das réplicas dos Deployments `activator`, `autoscaler`, `autoscaler-hpa`, `controller` e `webhook` em `kubectl -n knative-serving get pods`, mantendo múltiplas réplicas do `activator` em produção para alta disponibilidade no caminho de dados.

## Exemplo
Quando uma Revision ociosa está com `0` pods e recebe uma requisição HTTP, a camada de rede encaminha o pacote ao pod `activator`, que aciona o `autoscaler`, aguarda o novo pod da aplicação passar no readiness probe e encaminha a requisição sem erro para o usuário.

## Limites e trade-offs
Se uma carga de trabalho não puder tolerar nenhuma latência de partida a frio (cold start) na primeira requisição após um período ocioso, configure a anotação de escala mínima (`autoscaling.knative.dev/min-scale: "1"`) naquela Revision específica.

## Como verificar
Execute `kubectl -n knative-serving get pods` e confirme que `activator`, `autoscaler`, `autoscaler-hpa`, `controller` e `webhook` estão todos com status `Running` e `1/1 READY`.

## Conexões
- [[knative-point-in-time-revisions-and-traffic-splitting]] — Veja também: Snapshots imutáveis (Revisions) e divisão percentual de tráfego no Knative Serving.
- [[knative-release-manifests-crds-core-hpa-and-nscert]] — Veja também: Manifestos oficiais de instalação do Knative Serving: serving-crds, serving-core, serving-hpa e serving-nscert.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
