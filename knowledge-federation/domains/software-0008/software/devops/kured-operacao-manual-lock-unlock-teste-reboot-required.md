---
id: software.devops.tranche12.001187
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
fontes: ["https://kured.dev/docs/operation/", "https://kured.dev/docs/configuration/", "https://raw.githubusercontent.com/kubereboot/kured/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kured: Operação Manual de Pausa (Lock Manual), Desbloqueio (Unlock) e Teste de Sentinela

## Em uma frase
Em operações de emergência ou janelas de congelamento (code freeze / Black Friday), os operadores podem pausar globalmente todos os reboots do Kured adquirindo manualmente a anotação `weave.works/kured-node-lock` no `DaemonSet` e liberá-la posteriormente removendo a anotação com o sufixo `-`.

## Por que importa
Editar e reimplantar o manifesto do `DaemonSet` apenas para pausar temporariamente os reboots durante um incidente é lento e pode gerar deriva com o estado gerenciado pelo GitOps.

## Como funciona
Para bloquear manualmente qualquer novo reboot no cluster, executa-se `kubectl -n kube-system annotate ds kured weave.works/kured-node-lock='{"nodeID":"manual"}'`. Para destravar um lock manual ou liberar um lock órfão deixado por um nó que falhou permanentemente durante o reboot, remove-se a anotação com `kubectl -n kube-system annotate ds kured weave.works/kured-node-lock-`.

## Exemplo
```bash
# Pausar temporariamente todos os reboots do Kured:
kubectl -n kube-system annotate ds kured weave.works/kured-node-lock='{"nodeID":"manual"}'

# Liberar o lock no DaemonSet (note o hifen no final):
kubectl -n kube-system annotate ds kured weave.works/kured-node-lock-
```

## Limites e trade-offs
Adquirir o lock manual (`{"nodeID":"manual"}`) durante uma manutenção e esquecer de removê-lo depois desativa silenciosamente todas as reinicializações de segurança do cluster por meses.

## Como verificar
Monitore a idade do lock via métricas Prometheus do Kured e confirme a remoção da anotação com `kubectl -n kube-system get ds kured -o yaml` após encerrar a janela de bloqueio.

## Conexões
- [[kured-drain-timeout-grace-period-prefer-no-schedule-taint]] — Veja também: Kured: Parametrização de Drain (--drain-timeout, --drain-grace-period) e Taint PreferNoSchedule.
- [[kured-reboot-method-command-vs-signal-privilegios-container]] — Veja também: Kured: Métodos de Reinicialização (--reboot-method command vs signal) e Segurança de Container.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/operation/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/configuration/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
