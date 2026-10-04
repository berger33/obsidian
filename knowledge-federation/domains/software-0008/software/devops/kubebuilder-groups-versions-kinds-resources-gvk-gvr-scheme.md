---
id: software.devops.tranche18.001742
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md", "https://book.kubebuilder.io/architecture.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubebuilder: modelagem de `Groups`, `Versions`, `Kinds`, `Resources` (`GVK`/`GVR`) e registro no `runtime.Scheme`

## Em uma frase
Na arquitetura do Kubebuilder, cada tipo raiz em Go (`struct`) corresponde a um **GroupVersionKind (GVK)** servido em um endpoint REST **GroupVersionResource (GVR)** e registrado em um objeto `runtime.Scheme` para serialização e desserialização automática entre Go e a API do Kubernetes.

## Por que importa
Confundir `Kind` (o tipo em UpperCamelCase usado em manifestos YAML, como `CronJob`) com `Resource` (o nome plural em minúsculas na URL da API REST, como `cronjobs`) ou esquecer de registrar o tipo no `Scheme` causa falhas de lookup em tempo de execução no controlador.

## Como funciona
Um *API Group* (ex.: `batch.tutorial.kubebuilder.io`) agrupa funcionalidades relacionadas e possui uma ou mais *Versions* (`v1alpha1`, `v1beta1`, `v1`), permitindo evoluir o formato sem perder dados. O `Scheme` (`k8s.io/apimachinery/pkg/runtime`) mapeia bidirecionalmente a struct Go `&CronJob{}` ao GVK `batch.tutorial.kubebuilder.io/v1, Kind=CronJob`.

## Exemplo
```go
// api/v1/guestbook_types.go
// +kubebuilder:object:root=true
// +kubebuilder:subresource:status

type Guestbook struct {
    metav1.TypeMeta   `json:",inline"`
    metav1.ObjectMeta `json:"metadata,omitempty"`

    Spec   GuestbookSpec   `json:"spec,omitempty"`
    Status GuestbookStatus `json:"status,omitempty"`
}
```

## Limites e trade-offs
Seguindo o princípio de responsabilidade única destacado na documentação do Kubebuilder, evite criar um único CRD monolítico gigante para "App + Banco de Dados": crie um CRD `App` e um CRD `DB` separados, cada um com seu controlador coeso.

## Como verificar
Verifique em `cmd/main.go` que o pacote da sua nova API foi adicionado à função `init()` via `utilruntime.Must(webappv1.AddToScheme(scheme))`.

## Conexões
- [[kubebuilder-arquitetura-sdk-go-controller-runtime-controller-tools]] — Veja também: Kubebuilder: arquitetura do framework oficial SIG-API-Machinery para criação de APIs e Operators Kubernetes em Go.
- [[kubebuilder-markers-controller-gen-validacao-openapi-crd-rbac]] — Veja também: Kubebuilder: geração declarativa de CRDs OpenAPI v3, `DeepCopy` e RBAC via marcadores `// +kubebuilder:` e `controller-gen`.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://book.kubebuilder.io/architecture.html) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
