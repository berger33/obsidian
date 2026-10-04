---
id: software.devops.tranche13.001233
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
fontes: ["https://d7y.io/docs/next/", "https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md", "https://github.com/dragonflyoss/dragonfly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Dragonfly: Algoritmo de Agendamento em Dois Estágios Sensível à Carga (Load-Aware Scheduling)

## Em uma frase
O `Scheduler` do Dragonfly utiliza um algoritmo de agendamento em dois estágios sensível à carga em tempo real (`Load-Aware Scheduling Algorithm`), combinando o agendamento centralizado do `Scheduler` com reavaliação secundária no nível do nó (`Peer`) para escolher os `Parents` ótimos.

## Por que importa
Em uma árvore P2P estática, se um nó `Parent` ficar subitamente sobrecarregado de CPU, disco ou rede por causa de uma carga de aplicação local, todos os nós filhos que baixam peças dele sofrerão queda brusca de throughput.

## Como funciona
À medida que cada peça é baixada, o `Peer` reporta metadados de latência, taxa de transferência e sucesso de volta ao `Scheduler`. O `Scheduler` mantém um grafo dinâmico da saúde e carga de cada Peer e reatribui imediatamente outros `Parents` caso um nó apresente lentidão ou anomalia, isolando falhas em nível de Service, Peer e Task.

## Exemplo
```bash
# Verificar a saude e os logs de decisao do Scheduler do Dragonfly:
kubectl -n dragonfly-system get pods -l component=scheduler
kubectl -n dragonfly-system logs -l component=scheduler --tail=40
```

## Limites e trade-offs
Bloquear portas de comunicação direta (gRPC/TCP de transferência de peças) entre os worker nodes nas regras de `NetworkPolicy` ou Security Groups da nuvem impede que um `Peer` baixe peças de outros `Peers`, forçando fallback para a origem.

## Como verificar
Libere explicitamente nos Security Groups/NetworkPolicies do cluster as portas de controle e de transferência de dados entre todos os Pods `Peer` e `Seed Peer` do `dragonfly-system`.

## Conexões
- [[dragonfly-fluxo-download-first-time-subsequent-pieces-streaming]] — Veja também: Dragonfly: Fluxo de Download P2P em Peças (First-Time Download via Seed Peer vs. Subsequent Downloads).
- [[dragonfly-integracao-containerd-cri-o-docker-mirror-proxy]] — Veja também: Dragonfly: Integração Não-Intrusiva com containerd, CRI-O e Docker para Pull de Imagens OCI.

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://d7y.io/docs/next/) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
