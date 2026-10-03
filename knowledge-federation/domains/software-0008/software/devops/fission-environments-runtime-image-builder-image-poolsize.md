---
id: software.devops.tranche19.001813
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

# Fission `Environment`: configuração de imagens de Runtime, imagens de Builder e `poolsize`

## Em uma frase
Um **`Environment`** no Fission encapsula toda a parte específica de uma linguagem de programação (Node.js, Python, Go, Java, Ruby, PHP, .NET, binários Linux) em uma imagem de container de **runtime** (que inclui um carregador dinâmico HTTP) e, opcionalmente, uma imagem de **builder**.

## Por que importa
Para funções simples de um único arquivo `.py` ou `.js`, basta carregar o script diretamente no container de runtime; porém, quando a função possui dependências `requirements.txt`, `package.json` ou código compilado Go, é necessário um container *builder* separado para instalar pacotes e compilar o artefato antes da execução.

## Como funciona
Ao criar um `Environment` com `fission env create --name python --image ghcr.io/fission/python-env --builder ghcr.io/fission/python-builder --poolsize 3`, o Fission mantém um pool de 3 Pods de runtime prontos para especialização rápida e sobe um Pod do builder para compilar `Packages` de código-fonte.

## Exemplo
```bash
fission env create --name python-ml \
  --image ghcr.io/fission/python-env \
  --builder ghcr.io/fission/python-builder \
  --poolsize 2 \
  --version 3
fission env list
```

## Limites e trade-offs
Ajustar `--poolsize` em cada `Environment` permite controlar exatamente quantos Pods ociosos aquecidos o `poolmgr` mantém no cluster para aquela linguagem.

## Como verificar
Execute `fission env get --name python-ml` e `kubectl get pods -l environmentName=python-ml -A` para verificar o pool aquecido.

## Conexões
- [[fission-executors-poolmgr-vs-newdeploy-vs-container-comparacao]] — Veja também: Fission Executors: escolha entre `poolmgr` (pools aquecidos ~100 ms), `newdeploy` (HPA e alta carga) e `container`.
- [[fission-packages-source-archive-deployment-archive-buildermgr]] — Veja também: Fission `Package` e Build Pipeline: gerenciamento de `source` archives, `deployment` archives e `buildermgr`.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
