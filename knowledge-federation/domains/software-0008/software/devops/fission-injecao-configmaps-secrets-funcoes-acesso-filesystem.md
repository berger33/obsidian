---
id: software.devops.tranche19.001818
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

# Fission: injeção de `ConfigMaps` e `Secrets` do Kubernetes em funções (`--configmap` e `--secret`)

## Em uma frase
Ao criar ou atualizar uma `Function` no Fission, as flags `--configmap` e `--secret` permitem vincular objetos `ConfigMap` e `Secret` do Kubernetes à função, disponibilizando suas chaves como arquivos montados em `/configs/<namespace>/<name>/<key>` e `/secrets/<namespace>/<name>/<key>` dentro do Pod.

## Por que importa
Como os Pods do `poolmgr` nascem de forma genérica antes mesmo de saberem qual função vão executar, o mecanismo de montagem do Fission precisa entregar apenas os segredos e configurações pertencentes à função especializada naquele Pod.

## Como funciona
Durante a especialização da função (ou na criação do Deployment no `newdeploy`), o Fission verifica se o `Secret` e o `ConfigMap` existem no namespace indicado e disponibiliza os arquivos para leitura direta pelo código da função.

## Exemplo
```bash
kubectl create secret generic db-creds --from-literal=password=s3cr3t
fission function create --name query-db \
  --env python \
  --code query.py \
  --secret db-creds
```

## Limites e trade-offs
No código da função (por exemplo em Python), basta ler `/secrets/default/db-creds/password` como um arquivo texto comum.

## Como verificar
Crie uma função com `--secret` e `--configmap` e valide a leitura do conteúdo das chaves em `/secrets/` e `/configs/` durante a invocação.

## Conexões
- [[fission-arquitetura-interna-router-executor-fetcher-storagesvc]] — Veja também: Fission Arquitetura Interna: interação entre `Router`, `Executor`, sidecar `Fetcher` e `StorageSvc`.
- [[fission-container-executor-execucao-imagens-oci-customizadas-scale-zero]] — Veja também: Fission `container` Executor: execução de imagens OCI arbitrárias com scale-to-zero no Fission.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
