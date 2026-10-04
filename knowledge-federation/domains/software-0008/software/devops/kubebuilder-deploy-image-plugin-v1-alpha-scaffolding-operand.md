---
id: software.devops.tranche18.001747
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

# Kubebuilder: plugin `deploy-image/v1-alpha` para geração automática de APIs e Controllers que gerenciam um Operand

## Em uma frase
O Kubebuilder fornece o plugin oficial **`deploy-image/v1-alpha`**, que gera automaticamente uma API (CRD), um Controller completo com boas práticas de reconciliação, Conditions de status, eventos e testes `envtest` prontos para implantar e gerenciar uma imagem de container (*Operand*) no cluster.

## Por que importa
Muitos operadores começam com o caso de uso clássico de implantar um `Deployment` de uma imagem específica (ex.: `memcached` ou `busybox`), configurar variáveis de ambiente, portas, `SecurityContext` restritivo e reportar `status.conditions` (`Available`, `Progressing`, `Degraded`).

## Como funciona
Ao executar `kubebuilder create api --plugins="deploy-image/v1-alpha" --image=...`, o plugin preenche `api/v1alpha1/*_types.go` e `internal/controller/*_controller.go` com código idiomático que cria o `Deployment`, aplica `Finalizers`, registra eventos Kubernetes e atualiza as Conditions de status.

## Exemplo
```bash
kubebuilder create api \
  --group example.com --version v1alpha1 --kind Memcached \
  --image=memcached:1.6.26-alpine \
  --image-container-command="memcached,-m=64,-o,modern,-v" \
  --image-container-port="11211" \
  --run-as-user="1001" \
  --plugins="deploy-image/v1-alpha"
```

## Limites e trade-offs
O código gerado pelo plugin `deploy-image/v1-alpha` já inclui contextos de segurança compatíveis com o perfil *Restricted* do Kubernetes Pod Security Standards (`RunAsNonRoot: true`, `AllowPrivilegeEscalation: false`, `SeccompProfile: RuntimeDefault`).

## Como verificar
Gere uma API com `--plugins="deploy-image/v1-alpha"` e execute `make test` imediatamente para ver os testes gerados passando contra o `envtest`.

## Conexões
- [[kubebuilder-testes-integracao-envtest-setup-envtest-ginkgo]] — Veja também: Kubebuilder: testes de integração rápidos com `envtest` (`setup-envtest`) usando `kube-apiserver` e `etcd` reais.
- [[kubebuilder-arquitetura-plugins-extensibilidade-biblioteca-go]] — Veja também: Kubebuilder: arquitetura de Plugins (`go/v4`, `kustomize/v2`, `grafana/v1-alpha`) e uso do Kubebuilder como biblioteca Go.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://book.kubebuilder.io/architecture.html) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
