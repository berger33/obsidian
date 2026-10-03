---
id: software.devops.tranche19.001819
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
fontes: ["https://fission.io/docs/concepts/", "https://raw.githubusercontent.com/fission/fission/main/README.md", "https://github.com/fission/fission"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fission `container` Executor: execução de imagens OCI arbitrárias com scale-to-zero no Fission

## Em uma frase
O executor do tipo **`container`** (`--executortype container`) permite registrar qualquer imagem OCI/Docker já construída (escrita em qualquer linguagem ou framework HTTP que escute na porta configurada) diretamente como uma `Function` do Fission sem precisar de `Environment` nem `Package`.

## Por que importa
Às vezes uma equipe já possui um container de microsserviço existente (por exemplo um servidor FastAPI, Gin ou Rust Axum) e quer apenas aproveitar os `Triggers` (HTTP, Cron, Kafka/KEDA) e o *scale-to-zero* do Fission sem adaptar o código ao formato de handler de um `Environment`.

## Como funciona
Com `fission function create --name my-container-fn --image ghcr.io/org/app:v1 --port 8080 --executortype container`, o Fission gerencia o `Deployment`, `Service` e `HPA` da imagem informada, escalando de `0` para `N` réplicas quando acionado por um `Trigger`.

## Exemplo
```bash
fission function create --name custom-rust-service \
  --executortype container \
  --image ghcr.io/org/rust-http:v1.0.0 \
  --port 8080 \
  --minscale 0 --maxscale 5
fission route create --function custom-rust-service --url /rust-api --method POST
```

## Limites e trade-offs
Para que uma imagem funcione com `--executortype container`, o servidor HTTP dentro do container deve escutar exatamente na porta declarada em `--port` em todas as interfaces (`0.0.0.0`).

## Como verificar
Invoque a rota criada para a função `container` quando estiver em `0` réplicas e verifique a subida automática do Pod e o retorno da resposta.

## Conexões
- [[fission-injecao-configmaps-secrets-funcoes-acesso-filesystem]] — Veja também: Fission: injeção de `ConfigMaps` e `Secrets` do Kubernetes em funções (`--configmap` e `--secret`).
- [[fission-comparacao-arquitetural-knative-openfaas-quando-escolher]] — Veja também: Fission vs Knative e OpenFaaS: critérios arquiteturais de *cold start*, peso operacional e experiência de código.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
