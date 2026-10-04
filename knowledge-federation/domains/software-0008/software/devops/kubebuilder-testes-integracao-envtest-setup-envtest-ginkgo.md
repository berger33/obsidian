---
id: software.devops.tranche18.001746
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md", "https://book.kubebuilder.io/architecture.html", "https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubebuilder: testes de integração rápidos com `envtest` (`setup-envtest`) usando `kube-apiserver` e `etcd` reais

## Em uma frase
Todo projeto inicializado pelo Kubebuilder inclui uma suíte de testes de integração baseada no pacote `sigs.k8s.io/controller-runtime/pkg/envtest` e na ferramenta `setup-envtest` (configurada automaticamente no `Makefile`), que sobe binários reais do `kube-apiserver` e do `etcd` localmente sem precisar de cluster Docker/VM.

## Por que importa
Usar clientes falsos (*fake clients*) em testes unitários não valida schemas OpenAPI de CRDs, sub-recursos `/status`, otimismo de `resourceVersion` nem webhooks; por outro lado, subir um cluster `kind` inteiro a cada `go test` torna o ciclo de TDD lento.

## Como funciona
Quando `make test` é executado, o `setup-envtest` baixa os binários do `kube-apiserver` e do `etcd` para a versão exata configurada, inicia o control plane local em milissegundos, instala os CRDs de `config/crd/bases` e permite testar o `Reconciler` contra uma API Kubernetes real.

## Exemplo
```bash
make test
```

## Limites e trade-offs
O `envtest` inicia apenas `etcd` e `kube-apiserver` (não há `kubelet`, `kube-scheduler` nem `kube-controller-manager` rodando): portanto, um `Deployment` criado pelo seu controller durante o teste não criará `ReplicaSets`/`Pods` sozinho nem será deletado por Garbage Collection a menos que o próprio teste simule essa transição.

## Como verificar
Execute `make test` e inspecione `internal/controller/suite_test.go` para ver a inicialização do `envtest.Environment`.

## Conexões
- [[kubebuilder-admission-webhooks-defaulter-validator-conversion]] — Veja também: Kubebuilder: criação de Admission Webhooks (`Defaulter`, `Validator`) e Webhooks de Conversão Multi-Versão (`Hub`/`Spoke`).
- [[kubebuilder-deploy-image-plugin-v1-alpha-scaffolding-operand]] — Veja também: Kubebuilder: plugin `deploy-image/v1-alpha` para geração automática de APIs e Controllers que gerenciam um Operand.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://book.kubebuilder.io/architecture.html) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
