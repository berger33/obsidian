---
id: software.devops.tranche18.001745
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

# Kubebuilder: criação de Admission Webhooks (`Defaulter`, `Validator`) e Webhooks de Conversão Multi-Versão (`Hub`/`Spoke`)

## Em uma frase
Com o comando `kubebuilder create webhook`, o Kubebuilder gera a estrutura completa de **Mutating Admission Webhooks** (`CustomDefaulter`), **Validating Admission Webhooks** (`CustomValidator`) e **Conversion Webhooks** (modelo `Hub` e `Spoke` para migração sem perda entre `v1alpha1` e `v1`).

## Por que importa
Validações que exigem comparar múltiplos campos entre si, rejeitar transições inválidas entre o objeto antigo e o novo (`ValidateUpdate(ctx, oldObj, newObj)`) ou converter schemas estruturalmente diferentes entre versões de API vão além do que regras estáticas OpenAPI conseguem expressar.

## Como funciona
Para conversão multi-versão, uma versão da API (ex.: `v1`) é marcada como o **Hub** (`// +kubebuilder:storageversion` implementando `Hub()`) e todas as demais versões (`v1alpha1`, `v1beta1`) atuam como **Spokes** implementando `ConvertTo(dst Hub)` e `ConvertFrom(src Hub)`.

## Exemplo
```bash
kubebuilder create webhook \
  --group webapp --version v1 --kind Guestbook \
  --defaulting --programmatic-validation
```

## Limites e trade-offs
Em clusters reais, os webhooks HTTPS exigem certificados TLS válidos injetados nas configurações de webhook e no `CustomResourceDefinition` (o Kubebuilder gera os manifestos Kustomize em `config/certmanager` e `config/webhook` prontos para integração com o `cert-manager`).

## Como verificar
Execute `make manifests` após criar o webhook e verifique os arquivos gerados em `config/webhook/manifests.yaml`.

## Conexões
- [[kubebuilder-reconcile-loop-manager-client-cache-watches-owns]] — Veja também: Kubebuilder: implementação do loop `Reconcile`, `Manager`, cache de leitura e watches (`For`, `Owns`, `Watches`).
- [[kubebuilder-testes-integracao-envtest-setup-envtest-ginkgo]] — Veja também: Kubebuilder: testes de integração rápidos com `envtest` (`setup-envtest`) usando `kube-apiserver` e `etcd` reais.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://book.kubebuilder.io/architecture.html) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
