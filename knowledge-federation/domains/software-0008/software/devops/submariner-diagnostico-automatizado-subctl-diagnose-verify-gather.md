---
id: software.devops.tranche14.001319
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

# Submariner: Diagnóstico Automatizado, Testes E2E e Coleta de Logs (subctl diagnose, verify e gather)

## Em uma frase
O utilitário `subctl` inclui uma suíte completa de diagnóstico e validação em produção composta por `subctl diagnose` (verificação proativa de CNI, firewall, MTU e Kube-proxy), `subctl verify` (testes E2E reais de conectividade entre dois clusters) e `subctl gather` (coleta automatizada de logs e CRDs).

## Por que importa
Depurar falhas de conectividade multi-cluster envolve inspecionar túneis IPsec/WireGuard, tabelas de roteamento Linux, firewalls de nuvem, CoreDNS e CRDs em múltiplos clusters simultaneamente.

## Como funciona
O comando `subctl diagnose all` valida se o plugin CNI é suportado e se as portas de túnel (`4500/UDP`, `4800/UDP`) estão abertas; `subctl verify --context cluster-a --tocontext cluster-b` sobe Pods de teste temporários para comprovar conectividade real entre Pods e Services; e `subctl gather` empacota todos os estados e logs para análise.

## Exemplo
```bash
subctl diagnose all
subctl verify --context cluster-a --tocontext cluster-b --only connectivity,service-discovery
subctl gather
```

## Limites e trade-offs
Executar `subctl verify` em um cluster de produção com políticas rígidas de PodSecurity/NetworkPolicy no namespace padrão sem especificar um namespace permitido pode causar falsos negativos no teste E2E.

## Como verificar
Execute `subctl diagnose all` primeiro após o `join` e utilize `subctl gather` para capturar o estado completo de todos os clusters antes de reiniciar componentes.

## Conexões
- [[submariner-operator-implantacao-subctl-vs-helm-charts]] — Veja também: Submariner: Arquitetura Baseada em Operator e Implantação via subctl vs Helm Charts.
- [[submariner-nat-traversal-natt-discovery-firewalls-nuvem-hibrida]] — Veja também: Submariner: NAT Traversal (NAT-T), Descoberta de IP Público e Portas de Firewall em Nuvem Híbrida.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://submariner.io/getting-started/architecture/) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
