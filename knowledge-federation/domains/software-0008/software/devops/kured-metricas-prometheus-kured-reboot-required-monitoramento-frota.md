---
id: software.devops.tranche12.001190
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

# Kured: Métricas Prometheus ( Porta 8080 ) e Alerta de Nós com Reboot Pendente Estagnado

## Em uma frase
Cada Pod do `DaemonSet` `kured` expõe métricas no formato Prometheus na porta `8080` (`--metrics-host`, `--metrics-port=8080`), permitindo monitorar quantos nós do cluster estão com reinicialização pendente (`kured_reboot_required`) e alertar caso os reboots fiquem bloqueados por dias.

## Por que importa
Se um `PodDisruptionBudget` mal configurado ou um lock travado impedir o Kured de concluir os reboots, os nós acumularão atualizações de kernel pendentes silenciosamente se a métrica `kured_reboot_required` não for monitorada.

## Como funciona
Configurando um `ServiceMonitor` (ou scrape de pods na porta `8080`), o Prometheus coleta `kured_reboot_required` de cada nó. A equipe cria então um alerta PromQL que dispara apenas se um nó permanecer com `kured_reboot_required == 1` por mais de 48 horas, adicionando o nome desse alerta em `--alert-filter-regexp` para que o próprio alerta de atraso de reboot não bloqueie o Kured.

## Exemplo
```bash
# Testar o endpoint de metricas de um pod do Kured:
kubectl -n kube-system port-forward ds/kured 8080:8080 &
curl -s http://127.0.0.1:8080/metrics | grep kured
```

## Limites e trade-offs
Criar um alerta Prometheus como `RebootRequired` quando `kured_reboot_required > 0` e esquecer de adicioná-lo na regex de exclusão `--alert-filter-regexp` cria um deadlock onde o alerta de que um nó precisa reiniciar impede o Kured de reiniciar o nó.

## Como verificar
Inclua obrigatoriamente qualquer alerta derivado de `kured_reboot_required` na expressão `--alert-filter-regexp` quando `--prometheus-url` estiver ativo.

## Conexões
- [[kured-notificacoes-shoutrrr-notify-url-annotations-labels-auditoria]] — Veja também: Kured: Notificações de Eventos (--notify-url), Anotações de Nós e Rastreabilidade de Reboots.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/operation/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
