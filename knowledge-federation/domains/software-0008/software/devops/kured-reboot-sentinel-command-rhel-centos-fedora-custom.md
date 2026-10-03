---
id: software.devops.tranche12.001183
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

# Kured: Detecção de Reboot por Comando Sentinela (--reboot-sentinel-command) em RHEL e Derivados

## Em uma frase
Em distribuições Linux baseadas em RHEL, CentOS, Rocky Linux, AlmaLinux ou Fedora — que não criam o arquivo Debian/Ubuntu `/var/run/reboot-required` por padrão —, o Kured suporta a flag `--reboot-sentinel-command`, acionando o fluxo de reboot sempre que o comando configurado retornar código de saída `0`.

## Por que importa
Instalar o Kured com a configuração padrão (`--reboot-sentinel=/var/run/reboot-required`) em nós RHEL ou Amazon Linux faz com que o daemon nunca detecte atualizações de kernel, pois essas distribuições verificam pendências via `needs-restarting -r` ou `--reboothint`.

## Como funciona
Quando `--reboot-sentinel-command` é especificado, a verificação de arquivo sentinela é ignorada. Como o utilitário `needs-restarting --reboothint` do RHEL retorna `1` quando o reboot é necessário e `0` quando não é, a documentação oficial recomenda envolvê-lo em `sh -c "! needs-restarting --reboothint"` para inverter o código de saída para `0` quando houver necessidade de reinicialização.

## Exemplo
```yaml
# No values.yaml do Helm chart do Kured para nos RHEL/Rocky/AlmaLinux:
configuration:
  rebootSentinelCommand: 'sh -c "! needs-restarting --reboothint"'
  period: 30m
```

## Limites e trade-offs
Passar `needs-restarting --reboothint` diretamente em `--reboot-sentinel-command` sem inverter o código de retorno (`!`) faz o Kured reiniciar continuamente todos os nós que **não** precisam de reboot.

## Como verificar
Teste o comando sentinela manualmente no nó verificando `echo $?` (deve ser `0` apenas quando o reboot for necessário) antes de implantar no DaemonSet.

## Conexões
- [[kured-lock-distribuido-annotations-concurrency-ttl-release-delay]] — Veja também: Kured: Controle de Concorrência e Lock Distribuído na Anotação do DaemonSet.
- [[kured-janelas-manutencao-reboot-days-start-time-end-time-timezone]] — Veja também: Kured: Agendamento de Janelas de Reinicialização (--reboot-days, --start-time, --end-time e --time-zone).

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://kured.dev/docs/operation/) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
