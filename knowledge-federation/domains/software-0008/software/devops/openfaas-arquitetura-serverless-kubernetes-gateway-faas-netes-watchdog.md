---
id: software.devops.tranche19.001801
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
fontes: ["https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS: arquitetura serverless para Kubernetes com Gateway, `faas-netes`, `of-watchdog` e NATS

## Em uma frase
O **OpenFaaS** (*Functions as a Service*) simplifica o empacotamento e a implantação de funções orientadas a eventos e microsserviços em imagens OCI sobre Kubernetes (por meio do provedor `faas-netes`) ou em hosts leves (`faasd`), fornecendo auto-scaling, métricas Prometheus e fila assíncrona integrada.

## Por que importa
Transformar um script Python, handler Node.js ou binário legado em um serviço HTTP escalável no Kubernetes normalmente exigiria escrever servidor web, Dockerfile, Deployment, Service, HPA e exporter de métricas manualmente.

## Como funciona
Na pilha do OpenFaaS sobre Kubernetes, os recursos de infraestrutura residem no namespace `openfaas` (**API Gateway**, **faas-netes** controller/operator, **queue-worker** com **NATS** e **Prometheus**), enquanto as funções implantadas rodam isoladas no namespace `openfaas-fn`. Cada container de função inclui o binário leve **`of-watchdog`** como PID 1, que atua como proxy reverso HTTP, expõe métricas e gerencia o arquivo `.lock` de readiness probe.

## Exemplo
```bash
faas-cli new --lang python3-http hello-openfaas
faas-cli up -f hello-openfaas.yml
```

## Limites e trade-offs
A edição comunitária (*OpenFaaS CE*) possui restrições de licença (uso pessoal/exploratório ou PoC comercial limitada a 60 dias), enquanto ambientes comerciais de produção utilizam *OpenFaaS Standard* ou *OpenFaaS for Enterprises*.

## Como verificar
Execute `kubectl get pods -n openfaas` e `kubectl get pods -n openfaas-fn` para verificar o plano de controle e os Pods de funções.

## Conexões
- [[openfaas-faas-cli-stack-yaml-template-store-build-push-deploy]] — Veja também: OpenFaaS `faas-cli` e `stack.yaml`: ciclo de vida de funções (`new`, `build`, `push`, `deploy`, `up`) e Template Store.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
