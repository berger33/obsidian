---
id: software.devops.tranche19.001817
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

# Fission Arquitetura Interna: interação entre `Router`, `Executor`, sidecar `Fetcher` e `StorageSvc`

## Em uma frase
Sob o capô, o plano de dados e controle do Fission opera através da colaboração entre o **`Router`** (stateless), o **`Executor`**, o **`StorageSvc`** e o container sidecar **`Fetcher`** presente em cada Pod de ambiente.

## Por que importa
Compreender o fluxo interno entre `Router` -> `Executor` -> `Fetcher` é essencial para diagnosticar problemas de latência na primeira chamada ou falhas de download de pacotes em clusters com `NetworkPolicies` restritas.

## Como funciona
Quando uma requisição chega ao `Router` e ainda não há um Pod ativo mapeado em seu cache para aquela `Function`, o `Router` solicita um endereço ao `Executor`. No modo `poolmgr`, o `Executor` escolhe um Pod genérico aquecido do `Environment` e chama o sidecar `Fetcher` daquele Pod; o `Fetcher` baixa o arquivo da função a partir do `StorageSvc`, instrui o container de runtime a carregar a função em memória (~100 ms) e o `Router` encaminha a requisição HTTP.

## Exemplo
```bash
kubectl get pods -n fission
kubectl logs -n fission -l application=fission-router --tail=20
kubectl logs -n fission -l application=fission-executor --tail=20
```

## Limites e trade-offs
Se você aplicar `NetworkPolicies` default-deny no namespace onde rodam os Pods de funções, libere a comunicação do `Router` e do `Executor` para os Pods de função e dos sidecars `Fetcher` para o `StorageSvc`.

## Como verificar
Inspecione os containers de um Pod de ambiente Fission com `kubectl get pod <pod> -o jsonpath='{.spec.containers[*].name}'` e confirme a presença do container `fetcher`.

## Conexões
- [[fission-specs-declarativos-fission-spec-init-apply-gitops]] — Veja também: Fission Declarative Specs (`fission spec`): gerenciamento GitOps idempotente de funções e arquivos em `specs/`.
- [[fission-injecao-configmaps-secrets-funcoes-acesso-filesystem]] — Veja também: Fission: injeção de `ConfigMaps` e `Secrets` do Kubernetes em funções (`--configmap` e `--secret`).

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
