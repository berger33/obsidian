---
id: software.devops.tranche05.000481
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
fontes: ["https://raw.githubusercontent.com/dapr/dapr/master/README.md", "https://docs.dapr.io/getting-started/", "https://github.com/dapr/dapr"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura sidecar leve do Dapr (~58MB binário, ~4MB RAM) e as 12 APIs de blocos de construção

## Em uma frase
O Dapr (*Distributed Application Runtime*), projeto **graduado na CNCF** sob licença Apache-2.0, é um runtime de código aberto para construir aplicações distribuídas, workflows duráveis e agentes de IA que roda em qualquer lugar — Kubernetes, AWS/Azure/GCP, VMs, bare-metal, ambientes de borda/IoT, laptops ou redes air-gapped. Conforme detalha o README oficial, o Dapr executa como um **sidecar** (contêiner ou processo `daprd` extremamente leve: um binário de **~58 MB que consome ~4 MB de memória RAM**) ao lado da aplicação, expondo **12 APIs de blocos de construção** sobre **HTTP e gRPC** padrão: **Workflows, Service Invocation, State Management, Pub/Sub, Actors, Conversation, Bindings, Secrets, Configuration, Distributed Lock, Cryptography e Jobs**.

## Por que importa
Sem o Dapr, cada equipe de desenvolvimento precisa importar dezenas de bibliotecas específicas de fornecedores (SDKs de Redis, Kafka, AWS SQS, DynamoDB, Vault) em cada linguagem de programação e reimplementar retentativas, mTLS e tracing. Com o sidecar `daprd`, qualquer linguagem consome APIs HTTP/gRPC locais uniformes e pode adotar o Dapr incrementalmente, uma API por vez, sem lock-in de runtime.

## Como funciona
Implante o Dapr no cluster Kubernetes (ou localmente via Dapr CLI) e consuma apenas os blocos de construção necessários para cada serviço via chamadas HTTP/gRPC para `localhost` ou usando os SDKs nativos oficiais.

## Exemplo
Um serviço escrito em Python chama a API local de `State Management` e `Pub/Sub` do sidecar `daprd` via gRPC sem importar nenhum driver de banco ou mensageria; o time de plataforma troca o componente subjacente de Redis em desenvolvimento para AWS/GCP gerenciado em produção sem alterar uma única linha do código Python.

## Limites e trade-offs
Ao adotar o Dapr em clusters Kubernetes, habilite a injeção do sidecar `daprd` apenas nos Deployments/Pods que efetivamente utilizam as APIs do Dapr por meio das anotações `dapr.io/enabled: "true"` e `dapr.io/app-id`.

## Como verificar
Inspecione o pod com sidecar injetado (`2/2 Running`) e consulte o endpoint local de saúde do `daprd` confirmando o baixo consumo de memória (~4 MB) e o carregamento dos componentes.

## Conexões
- [[dapr-durable-execution-with-dapr-workflows]] — Veja também: Execução durável e retomada automática de etapas com Dapr Workflows.

## Fontes
- [Dapr GitHub — README.md (Durable Execution, AI Agents, Zero-Trust mTLS, 12 Building Block APIs & Sidecar Architecture)](https://raw.githubusercontent.com/dapr/dapr/master/README.md) — README oficial do Dapr (projeto graduado na CNCF sob Apache-2.0) detalhando execução durável com Dapr Workflows, primitivas para agentes de IA e Conversation API, segurança por padrão com mTLS e Configuration accessControl, execução verificável, tabela das 12 APIs de blocos de construção sobre HTTP/gRPC (binário de ~58MB usando ~4MB de RAM) e repositórios de SDKs e components-contrib.; consultado em 2026-10-03.
- [Dapr Official Documentation — Getting Started & Concepts](https://docs.dapr.io/getting-started/) — Documentação oficial do Dapr cobrindo inicialização com Dapr CLI local e em Kubernetes, sidecar daprd, componentes plugáveis e observabilidade.; consultado em 2026-10-03.
- [Dapr — Official GitHub Repository](https://github.com/dapr/dapr) — Repositório principal Apache-2.0 do Dapr na CNCF.; consultado em 2026-10-03.
