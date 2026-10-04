---
id: software.devops.tranche18.001759
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
fontes: ["https://sdk.operatorframework.io/docs/overview/", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK: auditoria de compatibilidade de versões com Kubernetes e `client-go` por tipo de projeto

## Em uma frase
Cada release do `operator-sdk` (e dos runtimes `ansible-operator` e `helm-operator`) é compilado e testado contra uma versão específica do Kubernetes e da biblioteca `client-go` (por exemplo Kubernetes `1.33.1` e `client-go v0.33.9`), determinando a compatibilidade com o cluster alvo.

## Por que importa
Atualizar o cluster Kubernetes de produção sem verificar a versão do `controller-runtime` e do `client-go` usada pelo operador (ou na imagem base `quay.io/operator-framework/ansible-operator:${IMAGE_VERSION}`) pode expor incompatibilidades com APIs removidas.

## Como funciona
A documentação oficial define a estratégia canônica de lookup para consultar na matriz de compatibilidade do `client-go`: 1) para os binários CLI, execute `operator-sdk version`, `ansible-operator version` ou `helm-operator version`; 2) para projetos **Go**, consulte a versão de `sigs.k8s.io/controller-runtime` e `k8s.io/client-go` em `go.mod`; 3) para projetos **Ansible** e **Helm**, execute `version` contra a imagem base definida no `Dockerfile`.

## Exemplo
```bash
operator-sdk version
grep -E "controller-runtime|k8s.io/client-go" go.mod
```

## Limites e trade-offs
Assim como no Kubebuilder, o Operator SDK descontinuou o uso de `gcr.io/kubebuilder/kube-rbac-proxy` em favor de `filters.WithAuthenticationAndAuthorization` do `controller-runtime`.

## Como verificar
Verifique as versões no `go.mod` ou na imagem base do `Dockerfile` antes de promover o operador para uma nova versão minor do Kubernetes.

## Conexões
- [[operator-sdk-scorecard-test-kuttl-validacao-boas-praticas-bundles]] — Veja também: Operator SDK `scorecard`: validação automatizada de bundles com suítes básicas, OLM e testes declarativos KUTTL.
- [[operator-sdk-spec-status-descriptors-crds-annotations-olm-ui]] — Veja também: Operator SDK: marcadores de `specDescriptors` e `statusDescriptors` (`+operator-sdk:csv:customresourcedefinitions`).

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
