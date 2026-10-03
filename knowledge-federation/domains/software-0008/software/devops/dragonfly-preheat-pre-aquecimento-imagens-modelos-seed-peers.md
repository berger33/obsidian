---
id: software.devops.tranche13.001238
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

# Dragonfly: Pré-Aquecimento (Preheat) de Imagens e Modelos nos Seed Peers Antes de Rollouts Massivos

## Em uma frase
Por meio da API de **Preheat** do `Manager` (ou jobs de pré-aquecimento), o Dragonfly permite baixar antecipadamente uma nova imagem de container ou modelo de IA para os `Seed Peers` (e opcionalmente para todos os `Peers`) antes que o `Deployment` Kubernetes seja atualizado.

## Por que importa
Se o pré-aquecimento for acionado alguns minutos antes de um rollout de 1.000 réplicas, até mesmo o primeiro Pod agendado encontra todas as peças já disponíveis na rede local dos `Seed Peers`, eliminando o tempo de download da origem durante o deploy.

## Como funciona
No pipeline de CI/CD, logo após o `docker push` da nova versão da imagem para o registry corporativo, um step dispara uma requisição de `preheat` ao `Manager` do Dragonfly informando a URL do manifesto da imagem; o `Scheduler` instrui os `Seed Peers` a puxarem e dividirem as camadas em peças antes do `kubectl rollout`.

## Exemplo
```bash
# Verificar jobs de preheat registrados no Dragonfly Manager:
kubectl -n dragonfly-system logs deployment/dragonfly-manager --tail=30 | grep -i "preheat"
```

## Limites e trade-offs
Disparar pré-aquecimento (`preheat`) simultâneo de dezenas de imagens gigantes para 100% dos nós do cluster de uma só vez consome banda e disco em nós que talvez nunca recebam Pods daquela aplicação.

## Como verificar
Use o pré-aquecimento direcionado aos `Seed Peers` (ou filtrado por grupos de nós específicos) para que os worker nodes puxem as peças sob demanda a partir dos Seed Peers já aquecidos.

## Conexões
- [[dragonfly-consistencia-dados-isolamento-excecoes-seguranca]] — Veja também: Dragonfly: Verificação de Consistência de Dados, Isolamento de Exceções e Segurança (Trail of Bits Audit).
- [[dragonfly-combinado-nydus-rafs-lazy-pulling-p2p-chunks]] — Veja também: Dragonfly: Combinação de Distribuição P2P Dragonfly com Lazy Pulling em Chunks do Nydus.

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://d7y.io/docs/next/) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
