---
id: software.devops.tranche19.001830
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
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio `NuclioAPIGateway` e `NuclioProject`: roteamento canário com divisão percentual de tráfego e governança multi-projeto

## Em uma frase
Os Custom Resources **`NuclioProject`** e **`NuclioAPIGateway`** (`nuclio.io/v1beta1`) organizam funções por domínio de equipe e permitem expor endpoints HTTP externos com autenticação e **canary deployments** (dividindo o tráfego percentual entre uma função primária `upstreams[0]` e uma função canário `upstreams[1]`).

## Por que importa
Atualizar um modelo de detecção de fraude em produção de uma só vez é arriscado; o engenheiro de ML precisa enviar primeiro 10% do tráfego em tempo real para a versão `v2` da função e manter 90% na versão `v1` comparando métricas.

## Como funciona
No recurso `NuclioAPIGateway`, o operador declara o `host`, `path`, modo de autenticação (`none`, `basicAuth`, `accessKey`, `oauth2`) e até dois `upstreams` com `percentage` para rollout canário gerenciado pelo Ingress do cluster.

## Exemplo
```yaml
apiVersion: nuclio.io/v1beta1
kind: NuclioAPIGateway
metadata:
  name: fraud-api-gw
  namespace: nuclio
spec:
  host: fraud.corp.internal
  path: /predict
  authenticationMode: basicAuth
  upstreams:
    - kind: nucliofunction
      nucliofunction:
        name: fraud-detector-v1
      percentage: 90
    - kind: nucliofunction
      nucliofunction:
        name: fraud-detector-v2
      percentage: 10
```

## Limites e trade-offs
Toda função Nuclio pertence a um `NuclioProject` (padrão `default`), permitindo listar, filtrar e aplicar políticas de governança por projeto.

## Como verificar
Execute `kubectl get nuclioapigateways,nuclioprojects -n nuclio` para auditar os gateways e projetos ativos no cluster.

## Conexões
- [[nuclio-dlx-auto-scaling-scale-to-zero-min-max-replicas]] — Veja também: Nuclio Auto-Scaling e DLX (*Dead Letter / Scale-to-Zero*): escalonamento dinâmico de `0` a `N` réplicas.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
