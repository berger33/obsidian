---
id: software.devops.tranche19.001816
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

# Fission Declarative Specs (`fission spec`): gerenciamento GitOps idempotente de funções e arquivos em `specs/`

## Em uma frase
Além de comandos imperativos (`fission function create`), o Fission possui um fluxo totalmente declarativo baseado no diretório **`specs/`** (`fission spec init`, `fission spec apply`, `fission spec destroy`), ideal para controle de versão no Git e pipelines de CI/CD.

## Por que importa
Rodar scripts bash cheios de `fission function create` em pipelines de CI falha na segunda execução porque o recurso já existe; já os arquivos YAML em `specs/` permitem criar, atualizar e empacotar o código-fonte de forma idempotente.

## Como funciona
Ao executar `fission spec init`, a CLI cria a pasta `specs/` com `fission-deployment-config.yaml`. Passar a flag `--spec` em qualquer comando (`fission env create --spec ...`, `fission fn create --spec ...`) grava os manifestos YAML e definições `ArchiveUploadSpec` em `specs/` em vez de tocar no cluster. Depois, `fission spec apply` empacota os diretórios locais, faz upload para o `storagesvc` e reconcilia todos os CRDs no cluster.

## Exemplo
```bash
fission spec init
fission env create --name nodejs --image ghcr.io/fission/node-env --spec
fission fn create --name hello --env nodejs --code hello.js --spec
fission spec apply
```

## Limites e trade-offs
O comando `fission spec apply --delete` remove automaticamente do cluster quaisquer recursos que faziam parte daquele `uid` de deployment em `specs/` e que foram deletados dos arquivos YAML no Git.

## Como verificar
Execute `fission spec validate` seguido de `fission spec apply` em seu repositório para validar e aplicar os manifestos declarativos.

## Conexões
- [[fission-triggers-httptrigger-timetrigger-mqtrigger-kubewatch]] — Veja também: Fission `Triggers`: vinculação de eventos HTTP, Cron (`TimeTrigger`), Filas (`MessageQueueTrigger`/KEDA) e Kubernetes Watch.
- [[fission-arquitetura-interna-router-executor-fetcher-storagesvc]] — Veja também: Fission Arquitetura Interna: interação entre `Router`, `Executor`, sidecar `Fetcher` e `StorageSvc`.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
