---
id: software.devops.tranche18.001744
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
fontes: ["https://book.kubebuilder.io/architecture.html", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubebuilder: implementação do loop `Reconcile`, `Manager`, cache de leitura e watches (`For`, `Owns`, `Watches`)

## Em uma frase
Em projetos Kubebuilder, um processo `Manager` (`ctrl.NewManager`) coordena o cache compartilhado de Informers, o cliente de API, a eleição de líder e múltiplos `Reconcilers`, onde cada `Reconciler` implementa `Reconcile(ctx, ctrl.Request) (ctrl.Result, error)` de forma idempotente e baseada em nível (*level-triggered*).

## Por que importa
Reagir apenas a eventos isolados de borda ("criou", "atualizou") perde mudanças se o controlador estiver reiniciando ou se múltiplos eventos ocorrerem em sequência; por isso, `ctrl.Request` entrega apenas `NamespacedName` para que o `Reconcile` leia o estado atual do cache e calcule a diferença até o estado desejado.

## Como funciona
No método `SetupWithManager`, o controlador registra a qual recurso primário ele reage (`For(&v1.Guestbook{})`) e quais recursos filhos secundários ele possui (`Owns(&appsv1.Deployment{})`), usando `ctrl.SetControllerReference` na criação dos filhos para que alterações ou exclusões no Deployment filho re-enfileirem automaticamente o `Guestbook` pai e acionem o Garbage Collector do Kubernetes.

## Exemplo
```go
func (r *GuestbookReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&webappv1.Guestbook{}).
        Owns(&appsv1.Deployment{}).
        Complete(r)
}
```

## Limites e trade-offs
Sempre habilite o sub-recurso de status (`// +kubebuilder:subresource:status`) e atualize o status via `r.Status().Update(ctx, obj)` (e nunca `r.Update(ctx, obj)`) para não sobrescrever `spec` nem disparar loops infinitos de geração (`metadata.generation`).

## Como verificar
Execute `make run` contra um cluster de desenvolvimento, aplique um CR de exemplo de `config/samples/` e verifique a reconciliação nos logs.

## Conexões
- [[kubebuilder-markers-controller-gen-validacao-openapi-crd-rbac]] — Veja também: Kubebuilder: geração declarativa de CRDs OpenAPI v3, `DeepCopy` e RBAC via marcadores `// +kubebuilder:` e `controller-gen`.
- [[kubebuilder-admission-webhooks-defaulter-validator-conversion]] — Veja também: Kubebuilder: criação de Admission Webhooks (`Defaulter`, `Validator`) e Webhooks de Conversão Multi-Versão (`Hub`/`Spoke`).

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://book.kubebuilder.io/architecture.html) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
