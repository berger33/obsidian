---
id: software.devops.tranche13.001240
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

# Dragonfly: Observabilidade da Malha P2P com Métricas Prometheus e Tracing Distribuído

## Em uma frase
Os componentes `Manager`, `Scheduler`, `Seed Peer` e `Peer` do Dragonfly expõem métricas Prometheus detalhadas sobre taxa de acerto de cache P2P, throughput de upload/download, latência de agendamento de peças e falhas de retorno à origem (`back-to-source`).

## Por que importa
Sem monitorar a proporção entre downloads servidos por Peers (`P2P hit ratio`) e downloads que caíram em `back-to-source` (direto da origem), uma falha silenciosa no `Scheduler` pode fazer todos os nós voltarem a sobrecarregar o registry central sem que ninguém perceba.

## Como funciona
Ao habilitar `metrics` no Helm chart do Dragonfly (`ServiceMonitor`), a equipe de SRE acompanha no Grafana o volume de tráfego economizado na origem, a distribuição de tarefas por tamanho de arquivo e a taxa de erro de Tasks P2P, alertando imediatamente se a taxa de falha de agendamento subir.

## Exemplo
```bash
# Verificar os endpoints de metricas dos componentes do Dragonfly:
kubectl -n dragonfly-system get svc -o wide
```

## Limites e trade-offs
Monitorar apenas se os Pods do `dragonfly-system` estão `Running` sem acompanhar a métrica de `back-to-source` não detecta problemas de firewall entre nós que impedem a transferência Peer-to-Peer.

## Como verificar
Crie alertas no Prometheus para quedas abruptas na taxa de tráfego servido via P2P e picos de falhas nas Tasks do `Scheduler`.

## Conexões
- [[dragonfly-combinado-nydus-rafs-lazy-pulling-p2p-chunks]] — Veja também: Dragonfly: Combinação de Distribuição P2P Dragonfly com Lazy Pulling em Chunks do Nydus.

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://d7y.io/docs/next/) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
