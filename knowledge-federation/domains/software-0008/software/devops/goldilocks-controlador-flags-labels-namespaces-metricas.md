---
id: software.devops.tranche11.001043
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://goldilocks.docs.fairwinds.com/advanced/", "https://goldilocks.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Controlador do Goldilocks: precedência de labels sobre flags de CLI, --on-by-default, --ignore-controller-kind e métricas Prometheus

## Em uma frase
O comando `goldilocks controller` gerencia dinamicamente os objetos VPA no cluster seguindo flags como `--on-by-default`, `--include-namespaces`, `--exclude-namespaces` e `--ignore-controller-kind` (com labels de namespace tendo sempre precedência sobre flags de CLI) e expõe métricas Prometheus e `/healthz` na porta `--metrics-port` (padrão `8080`).

## Por que importa
Em clusters com dezenas de namespaces de equipes, rotular manualmente cada novo namespace pode ser substituído por `--on-by-default` combinado com `--exclude-namespaces=kube-system,monitoring` e `--ignore-controller-kind=Job,CronJob`, evitando criar VPAs inúteis para jobs efêmeros.

## Como funciona
Conforme a documentação *Advanced Usage* (`goldilocks.docs.fairwinds.com/advanced/`): (1) quando especificadas, **labels nos recursos têm sempre precedência sobre as flags de linha de comando**; (2) **`--on-by-default`** cria VPAs em todos os namespaces do cluster, exceto os listados em **`--exclude-namespaces`** ou rotulados com `goldilocks.fairwinds.com/enabled=false`; (3) **`--include-namespaces`** adiciona namespaces específicos além dos rotulados; (4) **`--ignore-controller-kind`** recebe uma lista separada por vírgulas de tipos de controladores a ignorar na criação automática de VPAs (ex.: `--ignore-controller-kind=Job,CronJob`); e (5) na porta `--metrics-port` (padrão `8080`), o controlador serve `/healthz` e `/metrics` com as métricas **`goldilocks_controller_events_processed_total{resource, event_type}`** e **`goldilocks_controller_process_errors_total{resource}`**.

## Exemplo
```yaml
# Argumentos do controlador Goldilocks habilitando todos os namespaces por padrão, exceto sistema, e ignorando Jobs/CronJobs
args:
  - controller
  - --on-by-default
  - --exclude-namespaces=kube-system,kube-public,kube-node-lease,goldilocks
  - --ignore-controller-kind=Job,CronJob
  - --metrics-port=8080
```

## Limites e trade-offs
Mesmo que um namespace esteja listado em `--exclude-namespaces`, se alguém adicionar a label explícita `goldilocks.fairwinds.com/enabled=true` naquele namespace, o Goldilocks criará os VPAs nele porque as labels têm precedência sobre as flags de CLI.

## Como verificar
Consulte `curl -s http://localhost:8080/metrics | grep goldilocks_controller_` no pod do controlador para monitorar o total de eventos processados (`pod` / `namespace`) e verificar que `goldilocks_controller_process_errors_total` permanece em `0`.

## Conexões
- [[goldilocks-requisitos-vpa-recommender-metrics-server-gke]] — Veja também: Requisitos de infraestrutura do Goldilocks: VPA Recommender isolado (sem webhook), metrics-server, Prometheus e GKE.
- [[goldilocks-modos-atualizacao-vpa-update-mode-resource-policy]] — Veja também: Configuração avançada de VPA no Goldilocks: vpa-update-mode e vpa-resource-policy por namespace ou workload.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.
- [[goldilocks-cli-dashboard-summary-exclusao-containers-sidecars]] — Referência cruzada direta com goldilocks-cli-dashboard-summary-exclusao-containers-sidecars.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
