---
id: software.seguranca.tranche05.000465
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md", "https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules", "https://github.com/linux-audit/audit-userspace/tree/master/rules"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Linux Audit (`auditd`): Monitoramento de Carregamento de Módulos do Kernel (`init_module`, `finit_module`), `ptrace`, Alteração de Hora e MAC

## Em uma frase
Padrões como DISA STIG, PCI-DSS e CIS exigem que o `auditd` monitore eventos capazes de subverter o próprio kernel, adulterar carimbos de tempo forenses ou injetar código em outros processos.

## Por que importa
Um rootkit de kernel é carregado via `init_module` / `finit_module` (ou descarregado via `delete_module`, ou injetado via `kexec_load`); um invasor que deseja falsificar a linha do tempo de um ataque altera o relógio do sistema (`adjtimex`, `settimeofday`, `clock_settime`); e o roubo de credenciais em memória usa `ptrace`.

## Como funciona
As regras STIG (`30-stig.rules`) interceptam essas syscalls específicas em `arch=b64` (e `b32` em sistemas x86_64 com suporte 32-bit), além de monitorar alterações nas políticas de Mandatory Access Control (`/etc/apparmor/`, `/etc/apparmor.d/`, `/etc/selinux/`).

## Exemplo
```ini
# /etc/audit/rules.d/30-kernel-and-integrity.rules
-a always,exit -F arch=b64 -S init_module,finit_module,delete_module,kexec_load -k kernel_modules
-a always,exit -F arch=b64 -S ptrace -F a0=0x4 -k code_injection_ptrace_poketext
-a always,exit -F arch=b64 -S ptrace -F a0=0x5 -k code_injection_ptrace_pokedata
-a always,exit -F arch=b64 -S adjtimex,settimeofday,clock_settime -k time_change
-w /etc/localtime -p wa -k time_change
-w /etc/apparmor.d/ -p wa -k mac_policy_changes
-w /etc/selinux/ -p wa -k mac_policy_changes
```

## Limites e trade-offs
Daemons legítimos de sincronização de tempo (como `chronyd` ou `systemd-timesyncd`) invocam `adjtimex` / `clock_adjtime` periodicamente; adicione uma regra de exclusão anterior (`20-dont-audit.rules`) filtrando pelo UID específico do usuário `chrony` se necessário.

## Como verificar
Liste as regras carregadas com `sudo auditctl -l | grep kernel_modules` e confirme que as syscalls estão ativas no kernel.

## Conexões
- [[auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid]] — Veja também: Linux Audit (`auditd`): Auditoria de Syscalls por Arquitetura (`b64`/`b32`), Execução Privilegiada (`auid!=unset`, `uid!=euid`) e Binários SUID.
- [[auditd-exclusao-ruido-never-exit-cron-containers-alta-performance]] — Veja também: Linux Audit (`auditd`): Supressão Cirúrgica de Ruído com Regras `never,exit` e `exclude` em `20-dont-audit.rules`.
- [[auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2]] — Referência cruzada direta com auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
