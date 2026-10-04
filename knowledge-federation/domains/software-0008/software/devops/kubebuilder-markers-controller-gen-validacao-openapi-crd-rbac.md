---
id: software.devops.tranche18.001743
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md", "https://book.kubebuilder.io/architecture.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubebuilder: geração declarativa de CRDs OpenAPI v3, `DeepCopy` e RBAC via marcadores `// +kubebuilder:` e `controller-gen`

## Em uma frase
O Kubebuilder utiliza o gerador `controller-gen` (do projeto `controller-tools`) guiado por comentários especiais de código Go (`// +kubebuilder:...`, chamados *markers*) para gerar automaticamente os manifestos de CRD com schema OpenAPI v3, métodos `DeepCopyObject` e `ClusterRoles` de RBAC.

## Por que importa
Manter manualmente um arquivo YAML de CRD de 2.000 linhas sincronizado com os campos de uma struct Go e com as permissões RBAC que o controlador precisa em produção é trabalhoso e propenso a divergências.

## Como funciona
No arquivo `*_types.go`, marcadores como `// +kubebuilder:validation:Minimum=1`, `// +kubebuilder:validation:Enum= Gold;Silver;Bronze`, `// +kubebuilder:default="Silver"`, `// +kubebuilder:printcolumn:...` e `// +kubebuilder:subresource:status` instruem `make manifests` a gerar o CRD em `config/crd/bases/`; já no `*_controller.go`, marcadores `// +kubebuilder:rbac:groups=...,resources=...,verbs=...` geram `config/rbac/role.yaml`.

## Exemplo
```go
type GuestbookSpec struct {
    // +kubebuilder:validation:Minimum=1
    // +kubebuilder:validation:Maximum=10
    // +kubebuilder:default=2
    Replicas int32 `json:"replicas,omitempty"`

    // +kubebuilder:validation:MinLength=3
    Image string `json:"image"`
}
```

## Limites e trade-offs
Sempre que alterar structs em `api/<version>/*_types.go` ou marcadores RBAC nos controllers, execute `make generate manifests` antes de rodar os testes ou construir a imagem.

## Como verificar
Execute `make generate manifests` e inspecione o YAML gerado em `config/crd/bases/` e `config/rbac/role.yaml`.

## Conexões
- [[kubebuilder-groups-versions-kinds-resources-gvk-gvr-scheme]] — Veja também: Kubebuilder: modelagem de `Groups`, `Versions`, `Kinds`, `Resources` (`GVK`/`GVR`) e registro no `runtime.Scheme`.
- [[kubebuilder-reconcile-loop-manager-client-cache-watches-owns]] — Veja também: Kubebuilder: implementação do loop `Reconcile`, `Manager`, cache de leitura e watches (`For`, `Owns`, `Watches`).

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://book.kubebuilder.io/architecture.html) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
