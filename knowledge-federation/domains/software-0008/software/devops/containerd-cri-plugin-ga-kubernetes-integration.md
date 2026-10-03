---
id: software.devops.tranche01.000077
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://pkg.go.dev/github.com/containerd/containerd/v2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# O plugin nativo `cri` (GA): integração direta com a Container Runtime Interface do Kubernetes

## Em uma frase
A seção CRI do README oficial explica que `cri` é a implementação em forma de plugin nativo do containerd para a Kubernetes Container Runtime Interface (`cri-api`): desde o containerd 1.1, o plugin `cri` já vem compilado dentro dos binários de release e **habilitado por padrão**, tendo atingido status **GA** (feature complete, compatível com Kubernetes 1.10+ e aprovado em todos os testes de validação CRI, node e2e tests e e2e tests).

## Por que importa
Incorporar o plugin `cri` nativamente dentro do próprio binário do containerd (habilitado por padrão) eliminou a necessidade de shims intermediários legados entre o `kubelet` e o containerd, reduzindo consumo de memória/CPU por nó e simplificando a pilha de execução do Kubernetes.

## Como funciona
Em nós de clusters Kubernetes, utilize o plugin `cri` nativo já habilitado nos binários oficiais do containerd e ajuste seus parâmetros específicos seguindo `./docs/cri/config.md` e a manpage `docs/man/containerd-config.8.md`.

## Exemplo
O README mostra que a saúde contínua da integração entre o Kubernetes (`main` e branches de release) e o containerd é monitorada publicamente nos painéis do TestGrid em `https://testgrid.k8s.io/containerd` e `https://testgrid.k8s.io/containerd-periodic`.

## Limites e trade-offs
Se uma distribuição Linux customizada desabilitar plugins no arquivo `config.toml` do containerd, verifique a configuração conforme `./docs/cri/config.md` para garantir que o plugin `cri` esteja ativo antes de iniciar o `kubelet`.

## Como verificar
Conferi as seções Kubernetes (k8s) CI Dashboard Group e CRI / CRI Status no README oficial de `containerd/containerd`.

## Conexões
- [[containerd-releases-stability-and-ctr-autocompletion]] — Veja também: Estabilidade de API (`RELEASES.md`, `FEATURES.MD`) e autocompletar de shell para o cliente `ctr`.
- [[containerd-cri-validation-critest-and-crictl-debugging]] — Veja também: Validação e depuração de setups CRI com `cri-tools`: `critest` e `crictl`.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Pacote containerd v2 no pkg.go.dev](https://pkg.go.dev/github.com/containerd/containerd/v2) — Referência oficial da biblioteca Go github.com/containerd/containerd/v2 no pkg.go.dev.; consultado em 2026-10-03.
