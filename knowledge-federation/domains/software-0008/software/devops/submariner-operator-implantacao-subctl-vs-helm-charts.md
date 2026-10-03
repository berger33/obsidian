---
id: software.devops.tranche14.001318
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md", "https://submariner.io/getting-started/architecture/", "https://github.com/submariner-io/submariner"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Submariner: Arquitetura Baseada em Operator e Implantação via subctl vs Helm Charts

## Em uma frase
Toda implantação do Submariner é gerenciada em tempo de execução por um controlador customizado em Go chamado **submariner-operator**, que pode ser instalado e operado tanto pelo utilitário CLI **`subctl`** (método recomendado) quanto via **Helm charts**.

## Por que importa
Gerenciar manualmente o ciclo de vida, certificados, CRDs (`Submariner`, `ServiceDiscovery`, `Broker`) e DaemonSets em múltiplos clusters sem um Operator leva a desvios de versão entre o Gateway Engine e o Route Agent.

## Como funciona
Ao executar `subctl join` (ou instalar os charts `submariner-k8s-broker` e `submariner-operator`), o Operator é implantado no namespace `submariner-operator` e passa a reconciliar os recursos declarativos `Submariner` e `ServiceDiscovery`, instanciando automaticamente os Pods de Gateway, Route Agent e Lighthouse.

## Exemplo
```bash
kubectl -n submariner-operator get deployment submariner-operator
kubectl -n submariner-operator get submariner,servicediscovery
```

## Limites e trade-offs
Editar diretamente os DaemonSets gerados (`submariner-gateway` ou `submariner-routeagent`) com `kubectl edit` faz com que o `submariner-operator` reverta as alterações na próxima reconciliação.

## Como verificar
Aplique qualquer customização de imagem, cable driver ou NAT diretamente no recurso customizado `Submariner` (ou via flags do `subctl` / `values.yaml` do Helm chart).

## Conexões
- [[submariner-globalnet-controller-overlapping-cidrs-nat]] — Veja também: Submariner: Interconexão de Clusters com CIDRs Sobrepostos usando Globalnet Controller.
- [[submariner-diagnostico-automatizado-subctl-diagnose-verify-gather]] — Veja também: Submariner: Diagnóstico Automatizado, Testes E2E e Coleta de Logs (subctl diagnose, verify e gather).

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://submariner.io/getting-started/architecture/) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
