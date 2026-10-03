---
id: software.devops.tranche17.001620
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/clusternet/clusternet/main/README.md", "https://clusternet.io/docs/introduction/", "https://github.com/clusternet/clusternet"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clusternet: integração programática com `client-go` wrapper e operação via plugin `kubectl-clusternet`

## Em uma frase
O Clusternet disponibiliza um wrapper mínimo sobre o `k8s.io/client-go` oficial e o plugin `kubectl clusternet` (instalável via Krew) para que aplicações Go e pipelines de CI passem de single-cluster para multi-cluster alterando apenas uma linha de inicialização.

## Por que importa
Reescrever plataformas internas de PaaS ou scripts de automação para usar SDKs proprietários de multi-cluster exige meses de refatoração. Ao interceptar a camada de transporte REST do `client-go`, todo o código existente que manipula `Clientset.AppsV1().Deployments()` continua funcionando sem alterações.

## Como funciona
Em Go, basta envolver a função `kubeClient.Transport` (ou o cliente REST) com o wrapper do Clusternet para redirecionar as chamadas `Create`, `Update`, `Watch` e `Delete` às Shadow APIs do `clusternet-hub` ou a um cluster filho específico via socket proxy. Na CLI, `kubectl clusternet get/apply/delete/edit` oferece exatamente a mesma experiência do `kubectl` nativo.

## Exemplo
```go
package main

import (
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"github.com/clusternet/clusternet/pkg/wrappers/clientgo"
)

func newMultiClusterClient(kubeconfigPath string) (*kubernetes.Clientset, error) {
	cfg, err := clientcmd.BuildConfigFromFlags("", kubeconfigPath)
	if err != nil {
		return nil, err
	}
	cfg.WrapTransport = clientgo.NewClusternetTransport
	return kubernetes.NewForConfig(cfg)
}
```

## Limites e trade-offs
O módulo de tipos e esquemas de CRDs do Clusternet é publicado separadamente em `github.com/clusternet/apis` para evitar arrastar dependências pesadas do servidor para clientes Go.

## Como verificar
Compile um cliente Go com `clientgo.NewClusternetTransport` (ou execute `kubectl clusternet get deploy`) e confirme que a requisição é atendida pelo `clusternet-hub` via Shadow API.

## Conexões
- [[clusternet-tolerancia-version-skew-multi-arquitetura-mcs-api]] — Veja também: Clusternet: compatibilidade com *Kubernetes Version Skew* amplo e descoberta de serviços via `mcs-api`.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
