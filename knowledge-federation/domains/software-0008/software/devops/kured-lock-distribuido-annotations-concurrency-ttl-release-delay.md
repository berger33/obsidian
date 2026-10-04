---
id: software.devops.tranche12.001182
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

# Kured: Controle de Concorrência e Lock Distribuído na Anotação do DaemonSet

## Em uma frase
Para garantir que apenas um nó (ou o número definido em `--concurrency`, padrão `1`) reinicie por vez no cluster, o Kured utiliza uma anotação de lock atômica no próprio objeto `DaemonSet` (`weave.works/kured-node-lock`), suportando expiração automática (`--lock-ttl`) e atraso de liberação (`--lock-release-delay`).

## Por que importa
Se dois ou mais nós que receberam atualização de kernel tentassem executar `drain` e reiniciar ao mesmo tempo sem coordenação central, o cluster perderia capacidade abruptamente e violaria a disponibilidade de serviços distribuídos.

## Como funciona
Antes de iniciar o `cordon` e `drain`, o pod do Kured grava seu `nodeID` na anotação configurada por `--lock-annotation` (padrão `weave.works/kured-node-lock` no DaemonSet `kured` em `kube-system`). Caso um nó seja destruído pelo `cluster-autoscaler` enquanto detém o lock, `--lock-ttl=30m` garante a liberação automática após o tempo limite; já `--lock-release-delay=30m` retém o lock após o retorno do nó para espaçar os reboots na frota.

## Exemplo
```bash
# Inspecionar a anotacao de lock atual no DaemonSet do Kured:
kubectl -n kube-system get ds kured -o jsonpath='{.metadata.annotations.weave\.works/kured-node-lock}{"\n"}'
```

## Limites e trade-offs
Deixar `--lock-ttl` desabilitado (`0`, padrão) em clusters com `cluster-autoscaler` ou instâncias Spot faz com que a remoção de um nó que estava reiniciando trave a anotação `weave.works/kured-node-lock` indefinidamente para o restante do cluster.

## Como verificar
Defina sempre `--lock-ttl` (por exemplo, `30m` ou `45m`) e `--lock-release-delay` (por exemplo, `10m`) em clusters de produção com auto-scaling ativo.

## Conexões
- [[kured-arquitetura-daemonset-sentinel-file-node-reboot]] — Veja também: Kured: Arquitetura do Kubernetes Reboot Daemon (DaemonSet e Arquivo Sentinela).
- [[kured-reboot-sentinel-command-rhel-centos-fedora-custom]] — Veja também: Kured: Detecção de Reboot por Comando Sentinela (--reboot-sentinel-command) em RHEL e Derivados.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/operation/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
