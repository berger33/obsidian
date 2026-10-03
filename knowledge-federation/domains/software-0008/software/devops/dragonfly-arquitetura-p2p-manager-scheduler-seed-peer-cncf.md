---
id: software.devops.tranche13.001231
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md", "https://d7y.io/docs/next/", "https://github.com/dragonflyoss/dragonfly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Dragonfly: Arquitetura P2P CNCF Graduated (Manager, Scheduler, Seed Peer e Peer)

## Em uma frase
O **Dragonfly** (`dragonflyoss/dragonfly`, projeto **CNCF Graduated** desde outubro de 2025, auditado pela Trail of Bits) é um sistema de distribuição de arquivos e aceleração de imagens de containers e modelos de IA/ML baseado em tecnologia **Peer-to-Peer (P2P)** que aproveita a largura de banda ociosa entre nós do cluster.

## Por que importa
Quando centenas ou milhares de nós Kubernetes baixam simultaneamente imagens de containers pesadas ou pesos de modelos de IA de gigabytes a partir de um único registry ou bucket de objetos, a banda de saída da origem satura e os downloads falham por timeout.

## Como funciona
A arquitetura do Dragonfly divide-se em quatro componentes: **Manager** (opcional, gerencia configuração dinâmica, coleta de métricas e console web entre múltiplos clusters P2P), **Scheduler** (seleciona os melhores parents para cada Peer usando algoritmo de agendamento em dois estágios sensível à carga), **Seed Peer** (opcional, atua como peer raiz que baixa da origem sob comando do Scheduler) e **Peer** (daemon em cada nó que faz upload e download de peças em paralelo).

## Exemplo
```bash
helm repo add dragonfly https://dragonflyoss.github.io/helm-charts/
helm repo update
kubectl get pods -n dragonfly-system
```

## Limites e trade-offs
Desabilitar tanto o `Manager` quanto arquivos locais de configuração dinâmica atualizados sem planejar o modelo de implantação impede que os `Schedulers` e `Peers` descubram alterações de topologia da rede P2P.

## Como verificar
Implante o Dragonfly via Helm chart oficial no namespace `dragonfly-system` e verifique se `manager`, `scheduler`, `seed-peer` e o DaemonSet `dfdaemon` (`peer`) estão `Running`.

## Conexões
- [[dragonfly-fluxo-download-first-time-subsequent-pieces-streaming]] — Veja também: Dragonfly: Fluxo de Download P2P em Peças (First-Time Download via Seed Peer vs. Subsequent Downloads).

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://d7y.io/docs/next/) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
