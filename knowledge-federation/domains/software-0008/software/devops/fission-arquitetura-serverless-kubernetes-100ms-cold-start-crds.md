---
id: software.devops.tranche19.001811
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/fission/fission/main/README.md", "https://fission.io/docs/concepts/", "https://github.com/fission/fission"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fission: arquitetura serverless Kubernetes-native com *cold start* de ~100 ms e 4 CRDs fundamentais

## Em uma frase
O **Fission** (licenciado sob Apache 2.0) é um framework serverless nativo para Kubernetes que permite executar funções de curta duração sem construir imagens Docker manualmente para cada função, alcançando latências de *cold start* de aproximadamente **100 milissegundos** por meio de pools de containers aquecidos.

## Por que importa
Em frameworks onde cada função exige fazer pull de uma nova imagem OCI e iniciar um novo Pod do zero na primeira requisição, o *cold start* leva de 2 a 15 segundos, prejudicando APIs interativas.

## Como funciona
Todo o modelo mental do Fission baseia-se em **quatro objetos principais** respaldados por Custom Resource Definitions (CRDs) do Kubernetes: 1) **`Environment`** (o container específico da linguagem que compila e executa o código); 2) **`Package`** (o arquivo de código-fonte ou artefato compilado vinculado ao Environment); 3) **`Function`** (a configuração que une o código à forma de execução); e 4) **`Trigger`** (`HTTPTrigger`, `TimeTrigger`, `MessageQueueTrigger`, `KubernetesWatchTrigger`).

## Exemplo
```bash
fission env create --name nodejs --image ghcr.io/fission/node-env
fission function create --name hello --env nodejs \
  --code https://raw.githubusercontent.com/fission/examples/master/nodejs/hello.js
fission function test --name hello
```

## Limites e trade-offs
Como o Fission roda nativamente sobre o Kubernetes, toda a pilha de observabilidade, agregação de logs e políticas de rede que já opera no cluster aplica-se automaticamente aos Pods das funções Fission.

## Como verificar
Execute `kubectl get functions,environments,packages,httptriggers -A` para inspecionar os Custom Resources gerenciados pelo Fission.

## Conexões
- [[fission-executors-poolmgr-vs-newdeploy-vs-container-comparacao]] — Veja também: Fission Executors: escolha entre `poolmgr` (pools aquecidos ~100 ms), `newdeploy` (HPA e alta carga) e `container`.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://raw.githubusercontent.com/fission/fission/main/README.md) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://fission.io/docs/concepts/) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
