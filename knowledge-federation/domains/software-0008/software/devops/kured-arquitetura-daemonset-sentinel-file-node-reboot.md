---
id: software.devops.tranche12.001181
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
fontes: ["https://raw.githubusercontent.com/kubereboot/kured/main/README.md", "https://kured.dev/docs/configuration/", "https://kured.dev/docs/operation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kured: Arquitetura do Kubernetes Reboot Daemon (DaemonSet e Arquivo Sentinela)

## Em uma frase
Kured (Kubernetes Reboot Daemon, projeto CNCF Sandbox) é um `DaemonSet` para Kubernetes que monitora a necessidade de reinicialização do sistema operacional em cada nó (indicada por gerenciadores de pacotes como `apt`/`unattended-upgrades` ou `yum`/`dnf`) e executa reboots automáticos seguros com cordon, drain e lock distribuído.

## Por que importa
Aplicar atualizações automáticas de pacotes de segurança e kernel Linux nos nós de um cluster Kubernetes sem reiniciá-los mantém o kernel vulnerável em execução na memória, enquanto reiniciar todos os nós simultaneamente derruba o cluster.

## Como funciona
Cada Pod do `DaemonSet` `kured` verifica periodicamente (padrão `--period=1h0m0s`, com offset aleatório na inicialização para evitar contenção simultânea) a presença do arquivo sentinela `/var/run/reboot-required` (configurável via `--reboot-sentinel`). Quando detectado, o pod adquire um lock na API do Kubernetes, aplica `cordon` e `drain` no nó, aciona a reinicialização do host e faz `uncordon` quando o nó retorna saudável.

## Exemplo
```bash
kubectl get daemonset kured -n kube-system
kubectl get pods -n kube-system -l name=kured -o wide
kubectl logs -n kube-system -l name=kured --tail=30
```

## Limites e trade-offs
Implantar o Kured em clusters onde cargas críticas de múltiplas réplicas não possuem `PodDisruptionBudget` (`PDB`) configurado pode fazer com que o `drain` desaloje réplicas sem respeitar o quórum mínimo da aplicação.

## Como verificar
Configure `PodDisruptionBudgets` adequados para os serviços de produção antes de ativar o Kured e verifique os logs do DaemonSet em `kube-system`.

## Conexões
- [[kured-lock-distribuido-annotations-concurrency-ttl-release-delay]] — Veja também: Kured: Controle de Concorrência e Lock Distribuído na Anotação do DaemonSet.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/configuration/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://kured.dev/docs/operation/) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
