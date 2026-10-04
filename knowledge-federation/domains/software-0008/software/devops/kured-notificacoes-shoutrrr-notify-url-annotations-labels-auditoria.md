---
id: software.devops.tranche12.001189
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

# Kured: Notificações de Eventos (--notify-url), Anotações de Nós e Rastreabilidade de Reboots

## Em uma frase
O Kured oferece visibilidade operacional sobre cada etapa do ciclo de vida de reinicialização por meio da flag `--notify-url` (integração com Slack, Teams, Discord e webhooks genéricos), `--annotate-nodes` e `--pre-reboot-node-labels` / `--post-reboot-node-labels`.

## Por que importa
Quando um nó é drenado e reiniciado automaticamente durante a madrugada, a equipe de SRE precisa saber no histórico do cluster e no canal de operações exatamente qual nó reiniciou e em qual timestamp ocorreu o último reboot.

## Como funciona
Quando `--annotate-nodes` está habilitado, o Kured grava no próprio objeto `Node` as anotações `weave.works/kured-reboot-in-progress` e `weave.works/kured-most-recent-reboot-needed`. Simultaneamente, `--notify-url` envia mensagens parametrizáveis por `--message-template-drain`, `--message-template-reboot` e `--message-template-uncordon`.

## Exemplo
```bash
# Consultar as anotacoes de auditoria de reboot nos nos do cluster:
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.annotations.weave\.works/kured-most-recent-reboot-needed}{"\n"}{end}'
```

## Limites e trade-offs
Continuar utilizando as flags depreciadas `--slack-hook-url` em conjunto com `--notify-url` causa erro de validação na inicialização do binário do Kured, pois ambas as flags são mutuamente exclusivas.

## Como verificar
Padronize todas as integrações de chat na flag `--notify-url` e habilite `--annotate-nodes` e `--log-format=json` para correlação no sistema de logs.

## Conexões
- [[kured-reboot-method-command-vs-signal-privilegios-container]] — Veja também: Kured: Métodos de Reinicialização (--reboot-method command vs signal) e Segurança de Container.
- [[kured-metricas-prometheus-kured-reboot-required-monitoramento-frota]] — Veja também: Kured: Métricas Prometheus ( Porta 8080 ) e Alerta de Nós com Reboot Pendente Estagnado.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/operation/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
