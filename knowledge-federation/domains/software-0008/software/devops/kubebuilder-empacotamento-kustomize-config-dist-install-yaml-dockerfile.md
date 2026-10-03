---
id: software.devops.tranche18.001750
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

# Kubebuilder: organização de manifestos em `config/` via Kustomize e geração de `dist/install.yaml`

## Em uma frase
O Kubebuilder organiza todos os manifestos de infraestrutura do operador no diretório `config/` em pacotes modulares do **Kustomize** (`config/crd`, `config/rbac`, `config/manager`, `config/webhook`, `config/certmanager`, `config/prometheus`, `config/default`) e oferece o alvo `make build-installer` para consolidar um único `dist/install.yaml`.

## Por que importa
Durante o desenvolvimento o engenheiro quer aplicar apenas os CRDs (`make install`) e rodar o controlador localmente na máquina (`make run`), mas na release final precisa tanto publicar a imagem containerizada (`make docker-build docker-push`) quanto distribuir um bundle YAML único de instalação.

## Como funciona
O `Makefile` gerado orquestra todo o fluxo: `make install` aplica `config/crd` no cluster; `make deploy IMG=<registry>/op:v1.0.0` ajusta a imagem via `kustomize edit set image` em `config/manager` e aplica `config/default`; e `make build-installer IMG=<registry>/op:v1.0.0` renderiza o Kustomize completo em `dist/install.yaml`.

## Exemplo
```bash
make build-installer IMG=ghcr.io/org/webapp-operator:v1.0.0
ls -lh dist/install.yaml
```

## Limites e trade-offs
O `Dockerfile` gerado pelo Kubebuilder usa multi-stage build (`golang` -> `gcr.io/distroless/static:nonroot`) compilando um binário Go estático sem shell e rodando como usuário não-root (`65532:65532`).

## Como verificar
Execute `make build-installer IMG=example.com/op:v0.1.0` e valide o arquivo `dist/install.yaml` gerado com `kubectl apply --dry-run=client -f dist/install.yaml`.

## Conexões
- [[kubebuilder-protecao-metricas-withauthenticationandauthorization-sem-kube-rbac-proxy]] — Veja também: Kubebuilder: proteção do endpoint `/metrics` com `WithAuthenticationAndAuthorization` em substituição ao `kube-rbac-proxy`.

## Fontes
- [Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/README.md) — README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões; consultado em 2026-10-03.
- [The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)](https://book.kubebuilder.io/architecture.html) — Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs; consultado em 2026-10-03.
- [The Kubebuilder Book — Architecture](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/book/src/cronjob-tutorial/gvks.md) — Visão geral oficial da arquitetura de projetos Kubebuilder; consultado em 2026-10-03.
