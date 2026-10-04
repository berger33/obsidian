---
id: software.devops.tranche19.001802
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
fontes: ["https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://github.com/openfaas/faas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS `faas-cli` e `stack.yaml`: ciclo de vida de funções (`new`, `build`, `push`, `deploy`, `up`) e Template Store

## Em uma frase
A ferramenta de linha de comando **`faas-cli`** gerencia todo o ciclo de desenvolvimento de funções OpenFaaS a partir de um arquivo declarativo YAML (`stack.yaml`), baixando templates de linguagens da **Template Store** oficial (`faas-cli template store pull`) e executando `build`, `push` e `deploy` (ou o atalho unificado `faas-cli up`).

## Por que importa
Padronizar a estrutura de dezenas de funções em Node.js (`node20`), Python (`python3-http`), Go (`golang-middleware`) ou C# sem espalhar Dockerfiles divergentes entre repositórios requer um sistema central de templates.

## Como funciona
No arquivo `stack.yaml`, o desenvolvedor declara o endereço do `gateway`, o mapa `functions` (especificando `lang`, pasta `handler`, `image`, `environment`, `labels`, `annotations`, `secrets` e `limits`/`requests`). O comando `faas-cli build` combina a pasta `handler/` com o template selecionado em `./build/` e gera a imagem OCI.

## Exemplo
```yaml
version: 1.0
provider:
  name: openfaas
  gateway: http://127.0.0.1:8080
functions:
  stripe-webhooks:
    lang: node20
    handler: ./stripe-webhooks
    image: ghcr.io/org/stripe-webhooks:0.1.0
    environment:
      write_debug: true
```

## Limites e trade-offs
Ao desenvolver localmente com Minikube ou k3d compartilhando o daemon Docker, configurar `image_pull_policy: IfNotPresent` permite usar `faas-cli build` + `faas-cli deploy` sem precisar de `faas-cli push` para um registry remoto.

## Como verificar
Execute `faas-cli template store list` para inspecionar os templates oficiais disponíveis e `faas-cli build -f stack.yaml` para validar o empacotamento.

## Conexões
- [[openfaas-arquitetura-serverless-kubernetes-gateway-faas-netes-watchdog]] — Veja também: OpenFaaS: arquitetura serverless para Kubernetes com Gateway, `faas-netes`, `of-watchdog` e NATS.
- [[openfaas-faas-netes-modos-operacao-controller-vs-operator-function-crd]] — Veja também: OpenFaaS `faas-netes`: comparação entre o modo Controller e o modo Operator com o CRD `Function` (`openfaas.com/v1`).

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
