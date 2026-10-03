---
id: software.devops.tranche04.000379
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Observabilidade do CRI-O com métricas Prometheus, tracing distribuído e Evented PLEG

## Em uma frase
O README oficial referencia os guias dedicados de **Métricas** (`tutorials/metrics.md`), **Tracing** (`tutorials/tracing.md`) e **Debugging** (`tutorials/debugging.md`), além de destacar nos jobs periódicos de CI (GitHub Actions e OpenShift Prow) os testes contínuos de **Evented PLEG** (`periodic-ci-cri-o-cri-o-main-periodics-evented-pleg-periodic`). As métricas e spans exportados pelo CRI-O permitem medir a latência de cada operação CRI (`RunPodSandbox`, `CreateContainer`, `StartContainer`, `PullImage`), enquanto o Evented PLEG reduz o consumo de CPU do Kubelet substituindo polling constante por eventos de ciclo de vida emitidos pelo CRI-O.

## Por que importa
Sem métricas específicas do CRI-O no Prometheus, uma demora na inicialização de pods pode ser atribuída erroneamente ao agendador do Kubernetes quando na verdade a latência está concentrada em `PullImage` ou na criação do sandbox de rede CNI no nó.

## Como funciona
Habilite o exportador de métricas Prometheus do CRI-O na configuração do daemon, colete os indicadores de latência de operações CRI e habilite tracing OpenTelemetry quando precisar investigar gargalos entre o Kubelet e o runtime.

## Exemplo
Em um nó com centenas de pods ativos, a equipe monitora as métricas de latência de operações CRI do CRI-O no Grafana e valida em homologação o suporte ao Evented PLEG para reduzir o uso basal de CPU do Kubelet e do `crio`.

## Limites e trade-offs
Ao habilitar tracing detalhado no CRI-O em nós produtivos de alto tráfego, utilize uma taxa de amostragem (sampling rate) controlada para evitar sobrecarga de memória e rede no envio de spans.

## Como verificar
Consulte o endpoint de métricas do CRI-O nos nós do cluster e confirme a exposição dos contadores e histogramas de operações da Container Runtime Interface.

## Conexões
- [[crio-running-kubernetes-with-crio-socket-and-systemd]] — Veja também: Configuração do Kubelet com CRI-O via endpoint unix:///var/run/crio/crio.sock e systemd cgroup.
- [[crio-ci-prow-validation-and-packaging-ecosystem]] — Veja também: Validação contínua em GitHub Actions e OpenShift Prow e pacotes DEB/RPM do CRI-O.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
