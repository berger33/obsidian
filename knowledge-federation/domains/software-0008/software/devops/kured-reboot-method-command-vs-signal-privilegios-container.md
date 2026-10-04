---
id: software.devops.tranche12.001188
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

# Kured: Métodos de Reinicialização (--reboot-method command vs signal) e Segurança de Container

## Em uma frase
O Kured suporta dois métodos para acionar a reinicialização do nó host após concluir o `drain`: `--reboot-method=command` (padrão, invocando `/bin/systemctl reboot` no namespace do host) e `--reboot-method=signal` (enviando o sinal `SIGRTMIN+5` / `39` para o processo PID 1 do systemd no host).

## Por que importa
Invocar `/bin/systemctl reboot` dentro do container exige montar binários/sockets do host ou entrar no namespace de mount do host, enquanto o método por sinal (`signal`) requer apenas compartilhar `hostPID: true` e a capability `CAP_KILL` para sinalizar o PID 1.

## Como funciona
Com `--reboot-method=signal` e `--reboot-signal=39`, o Kured envia o sinal padrão de reinicialização do `systemd` diretamente ao processo `init` (PID 1), reduzindo a superfície de montagem de diretórios do sistema operacional hospedeiro dentro do Pod do DaemonSet.

## Exemplo
```bash
# Inspecionar o metodo de reboot e o securityContext do DaemonSet kured:
kubectl -n kube-system get ds kured -o jsonpath='{.spec.template.spec.hostPID}{"\n"}'
kubectl -n kube-system get ds kured -o jsonpath='{.spec.template.spec.containers[0].securityContext}{"\n"}'
```

## Limites e trade-offs
Configurar `--reboot-method=signal` em um sistema operacional de nó que não utiliza `systemd` como PID 1 (ou onde `SIGRTMIN+5` não está mapeado para `reboot.target`) faz o sinal ser ignorado e o nó permanecer em estado `SchedulingDisabled` (`cordoned`).

## Como verificar
Teste o método de reboot escolhido em um nó de homologação (criando `/var/run/reboot-required`) e confirme que o host reinicia e volta para `Ready`.

## Conexões
- [[kured-operacao-manual-lock-unlock-teste-reboot-required]] — Veja também: Kured: Operação Manual de Pausa (Lock Manual), Desbloqueio (Unlock) e Teste de Sentinela.
- [[kured-notificacoes-shoutrrr-notify-url-annotations-labels-auditoria]] — Veja também: Kured: Notificações de Eventos (--notify-url), Anotações de Nós e Rastreabilidade de Reboots.

## Fontes
- [Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)](https://kured.dev/docs/configuration/) — Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods; consultado em 2026-10-03.
- [Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)](https://kured.dev/docs/operation/) — Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay; consultado em 2026-10-03.
- [Kured — Official GitHub Repository](https://raw.githubusercontent.com/kubereboot/kured/main/README.md) — Repositório oficial CNCF Sandbox do Kured; consultado em 2026-10-03.
