---
id: software.devops.tranche18.001749
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
fontes: ["https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md", "https://book.kubebuilder.io/architecture.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubebuilder: proteção do endpoint `/metrics` com `WithAuthenticationAndAuthorization` em substituição ao `kube-rbac-proxy`

## Em uma frase
O Kubebuilder e o Operator-SDK descontinuaram o uso do container sidecar `gcr.io/kubebuilder/kube-rbac-proxy` e adotaram nativamente o filtro **`metrics.WithAuthenticationAndAuthorization`** do `controller-runtime` para proteger o endpoint HTTPS `/metrics` diretamente dentro do processo `manager`.

## Por que importa
Projetos antigos que ainda dependem da imagem `gcr.io/kubebuilder/kube-rbac-proxy` correm risco de falha de `ImagePullBackOff` com o desligamento do Google Container Registry legado (`gcr.io`), além de gastarem memória extra mantendo um segundo container sidecar em cada Pod de operador.

## Como funciona
Com o filtro `WithAuthenticationAndAuthorization` habilitado nas opções do `MetricsServer` em `cmd/main.go`, o próprio binário Go do operador delega a autenticação (`TokenReview`) e a autorização (`SubjectAccessReview`) das chamadas ao `/metrics` diretamente para o `kube-apiserver`, usando TLS e RBAC nativos.

## Exemplo
```go
// cmd/main.go nos projetos Kubebuilder modernos:
metricsServerOptions := metricsserver.Options{
    BindAddress:   metricsAddr,
    SecureServing: secureMetrics,
    FilterProvider: filters.WithAuthenticationAndAuthorization,
}
```

## Limites e trade-offs
Se um operador antigo ainda referenciar `gcr.io/kubebuilder/kube-rbac-proxy` em `config/default/`, migre imediatamente para `filters.WithAuthenticationAndAuthorization` conforme o aviso oficial do Kubebuilder e do Operator-SDK.

## Como verificar
Verifique `config/default/kustomization.yaml` e `cmd/main.go` para garantir que não há referências residuais a `gcr.io/kubebuilder/kube-rbac-proxy`.

## Conexões
- [[kubebuilder-arquitetura-plugins-extensibilidade-biblioteca-go]] — Veja também: Kubebuilder: arquitetura de Plugins (`go/v4`, `kustomize/v2`, `grafana/v1-alpha`) e uso do Kubebuilder como biblioteca Go.
- [[kubebuilder-empacotamento-kustomize-config-dist-install-yaml-dockerfile]] — Veja também: Kubebuilder: organização de manifestos em `config/` via Kustomize e geração de `dist/install.yaml`.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://book.kubebuilder.io/architecture.html) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
