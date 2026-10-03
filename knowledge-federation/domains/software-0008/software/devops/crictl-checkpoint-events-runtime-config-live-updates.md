---
id: software.devops.tranche14.001397
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Checkpoint de Containers (checkpoint), Stream de Eventos (events) e Runtime Config

## Em uma frase
Versões modernas do `crictl` incluem subcomandos avançados para forense e operação de runtime: `crictl checkpoint` (para criar um checkpoint CRIU de um container em execução sem perder seu estado em memória), `crictl events` (para assistir em tempo real ao stream de eventos de ciclo de vida dos containers no CRI) e `crictl runtime-config` / `update-runtime-config`.

## Por que importa
Quando um container apresenta comportamento suspeito de segurança ou vazamento complexo de memória em produção, matá-lo destrói toda a memória volátil que seria necessária para uma análise forense.

## Como funciona
Com suporte a CRIU habilitado no runtime (`containerd` ou `CRI-O`), `crictl checkpoint --export=/tmp/checkpoint.tar <container-id>` congela e exporta o estado completo da memória e processos do container para análise em um ambiente isolado, enquanto `crictl events` monitora criações, partidas e paradas em tempo real.

## Exemplo
```bash
crictl runtime-config
crictl checkpoint --export=/tmp/forensic-checkpoint.tar "$CONTAINER_ID"
```

## Limites e trade-offs
Arquivos de checkpoint gerados por `crictl checkpoint` contêm todo o conteúdo da memória RAM do processo (incluindo chaves privadas, tokens de sessão e variáveis de ambiente em texto claro).

## Como verificar
Proteja os arquivos `.tar` gerados por `crictl checkpoint` com permissões restritas (`0600`) e criptografia durante o transporte para análise forense.

## Conexões
- [[crictl-stats-statsp-metricsp-metricdescs-substituicao-cadvisor]] — Veja também: crictl: Métricas e Estatísticas de Recursos CRI (stats, statsp, metricsp e metricdescs).
- [[crictl-update-limites-cgroup-cpu-memory-containers-vivos]] — Veja também: crictl: Atualização Dinâmica de Limites de Cgroup (crictl update) e Tracing OpenTelemetry.

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
