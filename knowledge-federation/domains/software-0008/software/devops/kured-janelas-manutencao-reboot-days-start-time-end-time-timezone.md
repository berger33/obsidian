---
id: software.devops.tranche12.001184
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

# Kured: Agendamento de Janelas de Reinicialização (--reboot-days, --start-time, --end-time e --time-zone)

## Em uma frase
O Kured permite restringir a execução de reboots automáticos a dias da semana e faixas de horário previsíveis por meio das flags `--reboot-days`, `--start-time`, `--end-time` e `--time-zone` (suportando qualquer fuso da base tz do Linux, como `America/Sao_Paulo` ou `UTC`).

## Por que importa
Por padrão, o Kured reinicia nós a qualquer hora em que detecta o arquivo sentinela; em sistemas críticos de varejo ou pagamentos, realizar `drain` e movimentação de Pods no meio do horário de pico comercial aumenta o risco de latência de cauda.

## Como funciona
Ao configurar `--reboot-days=mon,tue,wed,thu`, `--start-time=02:00`, `--end-time=05:00` e `--time-zone=America/Sao_Paulo`, o Kured aguarda silenciosamente até que o relógio local entre na janela permitida antes de disputar o lock e drenar os nós. Em janelas curtas, recomenda-se reduzir `--period` (por exemplo, para `15m`) para aproveitar melhor a janela.

## Exemplo
```bash
# Exemplo de flags no container do DaemonSet kured:
# --reboot-days=mon,tue,wed,thu
# --start-time=02:00
# --end-time=05:00
# --time-zone=America/Sao_Paulo
# --period=15m
kubectl -n kube-system get ds kured -o yaml | grep -A 15 "args:"
```

## Limites e trade-offs
Configurar uma janela de manutenção de apenas 30 minutos (`--start-time=03:00 --end-time=03:30`) mantendo `--period=1h0m0s` pode fazer o ciclo de verificação pular inteiramente a janela de reboot naquele dia.

## Como verificar
Garanta que `--period` seja significativamente menor que a duração da janela entre `--start-time` e `--end-time`.

## Conexões
- [[kured-reboot-sentinel-command-rhel-centos-fedora-custom]] — Veja também: Kured: Detecção de Reboot por Comando Sentinela (--reboot-sentinel-command) em RHEL e Derivados.
- [[kured-bloqueio-reboots-prometheus-alerts-blocking-pod-selector]] — Veja também: Kured: Bloqueio Preventivo de Reboots via Alertas Prometheus e Seletores de Pods.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://kured.dev/docs/operation/) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
