---
id: software.devops.tranche19.001814
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

# Fission `Package` e Build Pipeline: gerenciamento de `source` archives, `deployment` archives e `buildermgr`

## Em uma frase
O recurso **`Package`** do Fission armazena o código da aplicação como arquivos compactados (*archives* gerenciados pelo serviço `storagesvc` do Fission ou referenciados por URL com checksum) e vincula-os a um `Environment`, rastreando o status de compilação pelo componente `buildermgr`.

## Por que importa
Se dez funções diferentes compartilharem o mesmo pacote zipado de código e dependências (mudando apenas o `entrypoint` de cada função), compilar o mesmo arquivo dez vezes desperdiçaria CPU e armazenamento.

## Como funciona
Um `Package` distingue dois artefatos: o **source archive** (`--sourcearchive`, contendo o código-fonte bruto e manifesto de dependências como `requirements.txt` + `build.sh`) e o **deployment archive** (`--deployarchive`, contendo o artefato pronto para rodar). Quando um `source archive` é enviado a um `Environment` que possui builder, o `buildermgr` compila o código automaticamente e grava o `deployment archive` resultante no `Package`.

## Exemplo
```bash
zip -r source-pkg.zip main.py requirements.txt build.sh
fission package create --name data-proc-pkg \
  --sourcearchive source-pkg.zip \
  --env python-ml
fission package info --name data-proc-pkg
```

## Limites e trade-offs
Antes de invocar uma função associada a um `Package` com build em andamento, verifique com `fission package info --name <pkg>` se o status de build mudou de `running` para `succeeded`.

## Como verificar
Crie um `Package` e acompanhe os logs de compilação com `fission package info --name <pkg>`.

## Conexões
- [[fission-environments-runtime-image-builder-image-poolsize]] — Veja também: Fission `Environment`: configuração de imagens de Runtime, imagens de Builder e `poolsize`.
- [[fission-triggers-httptrigger-timetrigger-mqtrigger-kubewatch]] — Veja também: Fission `Triggers`: vinculação de eventos HTTP, Cron (`TimeTrigger`), Filas (`MessageQueueTrigger`/KEDA) e Kubernetes Watch.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
