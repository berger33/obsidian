---
id: software.devops.tranche18.001751
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://sdk.operatorframework.io/docs/overview/", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK: arquitetura do kit CNCF Incubating para criação de Operators em Go, Ansible e Helm

## Em uma frase
O **Operator SDK** (componente central do *Operator Framework*, projeto CNCF Incubating licenciado sob Apache 2.0) é um toolkit de desenvolvimento que utiliza a biblioteca `controller-runtime` e a arquitetura de plugins do Kubebuilder para construir operadores Kubernetes em **Go**, **Ansible** ou **Helm**.

## Por que importa
Nem toda equipe de operações ou infraestrutura domina programação avançada em Go com `controller-runtime`; muitas equipes já possuem *Helm charts* maduros ou *Ansible playbooks/roles* testados e desejam transformá-los em Operators Kubernetes nativos sem escrever código Go.

## Como funciona
O Operator SDK oferece três fluxos de projeto de primeira classe por meio da CLI `operator-sdk init --plugins=<go|ansible|helm>`: 1) **Go Operators** (máxima flexibilidade em Go sobre `controller-runtime`); 2) **Ansible Operators** (reconciliação declarativa usando playbooks e roles Ansible via imagem base `ansible-operator`); e 3) **Helm Operators** (reconciliação de CRs mapeados diretamente para `values.yaml` de um Helm chart via imagem base `helm-operator`).

## Exemplo
```bash
operator-sdk version
# Inicializando um Go Operator:
operator-sdk init --domain=example.com --repo=github.com/example/memcached-operator
```

## Limites e trade-offs
Os binários oficiais (`operator-sdk`, `ansible-operator`, `helm-operator`) são distribuídos para `linux/amd64`, `linux/arm64`, `linux/ppc64le`, `linux/s390x`, `darwin/amd64` e `darwin/arm64`.

## Como verificar
Execute `operator-sdk version` para verificar a versão do SDK, a versão do Kubernetes e a versão do `client-go` embutidas no binário.

## Conexões
- [[operator-sdk-modelo-maturidade-5-capability-levels-go-ansible-helm]] — Veja também: Operator SDK: modelo de maturidade de 5 níveis (*Operator Capability Levels*) e comparação entre Go, Ansible e Helm.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://sdk.operatorframework.io/docs/overview/) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
