---
id: software.devops.tranche19.001812
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

# Fission Executors: escolha entre `poolmgr` (pools aquecidos ~100 ms), `newdeploy` (HPA e alta carga) e `container`

## Em uma frase
O Fission oferece três tipos de **Executors** (`--executortype`) para provisionar e escalar Pods de função: **`poolmgr`** (gerenciador de pool genérico aquecido), **`newdeploy`** (Deployment dedicado com Service e HPA) e **`container`** (execução direta de imagem OCI arbitrária).

## Por que importa
Uma função chamada esporadicamente (1 vez por hora) precisa de *cold start* instantâneo de 100 ms sem manter Pods dedicados parados (`poolmgr`), enquanto uma API de alto tráfego contínuo precisa de múltiplas réplicas escaladas por CPU/memória com `HorizontalPodAutoscaler` (`newdeploy`).

## Como funciona
No **`poolmgr`** (padrão), o Fission mantém um pequeno pool de Pods genéricos daquele `Environment`; quando a função é chamada, um Pod aquecido é especializado em ~100 ms carregando o código do `Package`. No **`newdeploy`**, o Fission cria um `Deployment`, `Service` e `HPA` dedicados para a função (suportando `--minscale` e `--maxscale`). No **`container`**, você executa uma imagem de container já pronta com scale-to-zero.

## Exemplo
```bash
# Criando uma função com executor newdeploy e auto-scaling entre 1 e 10 réplicas:
fission function create --name high-traffic-api \
  --env nodejs \
  --code api.js \
  --executortype newdeploy \
  --minscale 1 --maxscale 10 --targetcpu 70
```

## Limites e trade-offs
No `newdeploy`, se `--minscale 0` for configurado, a primeira chamada sofrerá o tempo de criação de um novo Pod Kubernetes; se precisar de 0 Pods dedicados com resposta em 100 ms na primeira chamada, use `poolmgr` (ou `newdeploy` com `--minscale 1`).

## Como verificar
Compare os Pods criados no cluster para uma função `poolmgr` versus uma função `newdeploy` usando `kubectl get pods -A -l functionName`.

## Conexões
- [[fission-arquitetura-serverless-kubernetes-100ms-cold-start-crds]] — Veja também: Fission: arquitetura serverless Kubernetes-native com *cold start* de ~100 ms e 4 CRDs fundamentais.
- [[fission-environments-runtime-image-builder-image-poolsize]] — Veja também: Fission `Environment`: configuração de imagens de Runtime, imagens de Builder e `poolsize`.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
