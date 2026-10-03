---
id: software.devops.tranche12.001185
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
fontes: ["https://kured.dev/docs/configuration/", "https://raw.githubusercontent.com/kubereboot/kured/main/README.md", "https://kured.dev/docs/operation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kured: Bloqueio Preventivo de Reboots via Alertas Prometheus e Seletores de Pods

## Em uma frase
O Kured pode adiar automaticamente qualquer reinicialização de nó quando há alertas ativos no Prometheus (`--prometheus-url`, `--alert-filter-regexp`, `--alert-firing-only`) ou quando determinados Pods sensíveis estão agendados naquele nó (`--blocking-pod-selector`).

## Por que importa
Reiniciar nós automaticamente enquanto o cluster já enfrenta um incidente ativo, degradação de armazenamento distribuído (Ceph/Longhorn rebuilding) ou execução de um Job crítico de fechamento contábil agrava a falha existente.

## Como funciona
Quando `--prometheus-url=http://prometheus.monitoring.svc.cluster.local` é definido, o Kured consulta a API do Prometheus antes de adquirir o lock; usando `--alert-firing-only=true` e `--alert-filter-regexp=^(Watchdog|RebootRequired)$`, ignora alertas benignos e bloqueia o reboot se qualquer alerta real estiver disparando. Além disso, `--blocking-pod-selector=batch-critical=true` impede o reboot de um nó específico enquanto aquele Pod existir nele.

## Exemplo
```bash
# Flags de protecao baseadas em Prometheus e Pods bloqueantes:
# --prometheus-url=http://prometheus-operated.monitoring.svc:9090
# --alert-firing-only=true
# --alert-filter-regexp=^(Watchdog|InfoInhibitor|RebootRequired)$
# --blocking-pod-selector=kured.io/block-reboot=true
kubectl logs -n kube-system -l name=kured | grep -i "alert"
```

## Limites e trade-offs
Configurar `--prometheus-url` sem ignorar o alerta permanente `Watchdog` (presente por padrão no `kube-prometheus-stack`) com `--alert-filter-regexp` bloqueia 100% dos reboots do Kured permanentemente.

## Como verificar
Filtre sempre alertas permanentes de heartbeat como `Watchdog` em `--alert-filter-regexp` e habilite `--alert-firing-only=true`.

## Conexões
- [[kured-janelas-manutencao-reboot-days-start-time-end-time-timezone]] — Veja também: Kured: Agendamento de Janelas de Reinicialização (--reboot-days, --start-time, --end-time e --time-zone).
- [[kured-drain-timeout-grace-period-prefer-no-schedule-taint]] — Veja também: Kured: Parametrização de Drain (--drain-timeout, --drain-grace-period) e Taint PreferNoSchedule.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://kured.dev/docs/operation/) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
