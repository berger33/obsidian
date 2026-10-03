---
id: software.devops.tranche05.000469
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

# Diagnóstico de reconciliação de Services, Routes e Revisions através dos logs do Knative controller

## Em uma frase
O guia `DEVELOPMENT.md` fornece o comando canônico para inspecionar os logs do controlador principal do Knative Serving durante operações e depuração: **`kubectl -n knative-serving logs $(kubectl -n knative-serving get pods -l app=controller -o name) -c controller`**. O pod `controller` executa os reconciliadores que transformam cada objeto de alto nível `Service` em uma `Configuration` (que gera a `Revision` e seu `Deployment` subjacente) e uma `Route` (que programa o ingress/gateway e aponta para o `Service` ou `activator`).

## Por que importa
Quando um Knative `Service` permanece com `READY False` ou `Unknown`, inspecionar as condições (`Conditions`) do recurso junto com os logs estruturados do contêiner `controller` no namespace `knative-serving` revela exatamente qual sub-reconciliador (`service`, `configuration`, `revision`, `serverlessservice` ou `route`) encontrou erro.

## Como funciona
Ao investigar falhas de criação de revisão ou programação de rota no Knative Serving, verifique `kubectl describe ksvc <nome>` e consulte os logs do contêiner `controller` com o comando oficial documentado em `DEVELOPMENT.md`.

## Exemplo
Uma nova `Revision` fica em estado `RevisionFailed`; ao consultar os logs do `controller` em `knative-serving`, o operador identifica rapidamente que o registro privado recusou a resolução do digest da imagem (`Unable to fetch image`) por falta de `imagePullSecrets` na ServiceAccount.

## Limites e trade-offs
Além dos logs do `controller`, lembre-se de verificar os logs do `autoscaler` e do `activator` quando o problema envolver especificamente transição de escala `0 -> 1` ou estrangulamento de concorrência de requisições.

## Como verificar
Execute o comando de leitura de logs do `controller` em `knative-serving` e confirme que os eventos de reconciliação estão sendo processados sem erros recorrentes.

## Conexões
- [[knative-webhook-validation-and-defaulting-in-knative]] — Veja também: Papel do pod webhook na validação, atribuição de defaults e conversão de recursos no Knative Serving.
- [[knative-protobuf-code-generation-and-bash-v4-build-requirements]] — Veja também: Requisitos de compilação do Knative Serving: Go, Bash v4+, protoc e protoc-gen-gogofaster.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
