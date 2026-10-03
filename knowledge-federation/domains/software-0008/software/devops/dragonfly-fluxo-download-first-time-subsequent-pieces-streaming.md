---
id: software.devops.tranche13.001232
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

# Dragonfly: Fluxo de Download P2P em Peças (First-Time Download via Seed Peer vs. Subsequent Downloads)

## Em uma frase
No Dragonfly, toda transferência de imagem ou arquivo é registrada como uma **Task** no `Scheduler` e dividida em **pieces** (peças), diferenciando automaticamente o primeiro download no cluster P2P dos downloads subsequentes servidos entre múltiplos Peers em paralelo.

## Por que importa
Em sistemas de cache tradicionais por proxy, o cliente precisa esperar o proxy terminar de baixar o blob inteiro da origem antes de receber os bytes, enquanto o Dragonfly faz streaming peça-a-peça em tempo real.

## Como funciona
Quando um cliente solicita um blob ao `Peer` local (via proxy HTTP/HTTPS ou gRPC), se o Peer já possui as peças no cache local, ele monta e entrega o arquivo imediatamente sem contatar o `Scheduler`. Se for o **primeiro download** da Task no cluster, o `Scheduler` aciona o `Seed Peer` para baixar da origem e faz streaming peça-a-peça para o Peer solicitante; nos **downloads subsequentes**, o `Scheduler` designa múltiplos Peers que já possuem as peças como `Parents`, permitindo download paralelo.

## Exemplo
```bash
# Inspecionar logs de transferencia P2P no daemon do Peer (dfdaemon):
kubectl -n dragonfly-system logs daemonset/dragonfly-client --tail=50
```

## Limites e trade-offs
Dimensionar os `Seed Peers` com discos lentos ou limite de banda de rede muito baixo estrangula o primeiro download de novas imagens (`First-Time Download`), atrasando a semeadura inicial das peças para o restante do cluster.

## Como verificar
Aloque nós com alta vazão de rede e SSDs NVMe rápidos para os Pods de `Seed Peer` a fim de maximizar a velocidade da primeira ingestão da origem.

## Conexões
- [[dragonfly-arquitetura-p2p-manager-scheduler-seed-peer-cncf]] — Veja também: Dragonfly: Arquitetura P2P CNCF Graduated (Manager, Scheduler, Seed Peer e Peer).
- [[dragonfly-load-aware-scheduling-two-stage-parent-selection]] — Veja também: Dragonfly: Algoritmo de Agendamento em Dois Estágios Sensível à Carga (Load-Aware Scheduling).

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://d7y.io/docs/next/) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
