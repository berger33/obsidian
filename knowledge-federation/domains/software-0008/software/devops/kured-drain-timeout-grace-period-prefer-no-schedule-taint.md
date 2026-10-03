---
id: software.devops.tranche12.001186
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://kured.dev/docs/configuration/", "https://kured.dev/docs/operation/", "https://raw.githubusercontent.com/kubereboot/kured/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kured: Parametrização de Drain (--drain-timeout, --drain-grace-period) e Taint PreferNoSchedule

## Em uma frase
Durante o processo de evacuação de um nó, o Kured controla o comportamento do `drain` por meio de `--drain-delay`, `--drain-grace-period`, `--drain-timeout`, `--skip-wait-for-delete-timeout`, `--force-reboot` e da aplicação preventiva de taint `--prefer-no-schedule-taint`.

## Por que importa
Quando um nó está aguardando sua vez de reiniciar na fila do lock, sem uma taint `PreferNoSchedule`, os Pods recém-desalojados do nó que está reiniciando agora podem ser agendados justamente no próximo nó que também será reiniciado em minutos, causando duplo despejo.

## Como funciona
Habilitar `--prefer-no-schedule-taint=weave.works/kured-node-reboot` faz o Kured aplicar uma taint `PreferNoSchedule` assim que detecta o arquivo sentinela no nó, desencorajando o scheduler de colocar novos Pods ali antes do reboot. Já `--drain-timeout` evita que um `PodDisruptionBudget` bloqueado trave o drain para sempre.

## Exemplo
```bash
# Verificar taints e anotacoes aplicadas pelo Kured nos nos:
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints,SCHEDULABLE:.spec.unschedulable
```

## Limites e trade-offs
Habilitar `--force-reboot=true` em combinação com um `--drain-timeout` curto força o desligamento abrupto do sistema operacional mesmo quando Pods stateful (como bancos de dados ou brokers Kafka) não puderam ser drenados com segurança.

## Como verificar
Mantenha `--force-reboot=false` em nós que hospedam workloads stateful e investigue falhas de drain via alertas em vez de forçar o desligamento do host.

## Conexões
- [[kured-bloqueio-reboots-prometheus-alerts-blocking-pod-selector]] — Veja também: Kured: Bloqueio Preventivo de Reboots via Alertas Prometheus e Seletores de Pods.
- [[kured-operacao-manual-lock-unlock-teste-reboot-required]] — Veja também: Kured: Operação Manual de Pausa (Lock Manual), Desbloqueio (Unlock) e Teste de Sentinela.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/operation/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
