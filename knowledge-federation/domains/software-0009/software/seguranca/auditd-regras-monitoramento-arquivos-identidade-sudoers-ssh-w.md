---
id: software.seguranca.tranche05.000463
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

# Linux Audit (`auditd`): Monitoramento de Integridade de Arquivos Críticos (`-w` / `-F path=`) — Identidade, `sudoers`, SSH e Cron

## Em uma frase
O `auditd` monitora acessos e modificações em arquivos e diretórios sensíveis através de regras de *File System Watch* (`-w <caminho> -p <permissoes> -k <chave>` ou a forma equivalente de syscall `-a always,exit -F path=<caminho> -F perm=wa -F key=<chave>`).

## Por que importa
Qualquer tentativa de persistência de um invasor em Linux envolve modificar bancos de dados de identidade (`/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow`, `/etc/security/opasswd`), escalação de privilégio (`/etc/sudoers`, `/etc/sudoers.d/`), chaves/configuração SSH (`/etc/ssh/sshd_config`) ou tarefas agendadas (`/etc/crontab`, `/etc/cron.*`, `/var/spool/cron`).

## Como funciona
Os filtros de permissão `-p` combinam quatro operações do VFS: **`r`** (*read*), **`w`** (*write*), **`x`** (*execute*) e **`a`** (*attribute change* — `chmod`/`chown`/`setxattr`). Para arquivos de configuração, `-p wa` registra exclusivamente gravações e mudanças de permissão/proprietário sem inundar o log com leituras normais do sistema.

## Exemplo
```ini
# /etc/audit/rules.d/30-identity-and-privilege-files.rules
-w /etc/passwd -p wa -k identity_tamper
-w /etc/shadow -p wa -k identity_tamper
-w /etc/group -p wa -k identity_tamper
-w /etc/gshadow -p wa -k identity_tamper
-w /etc/sudoers -p wa -k sudoers_changes
-w /etc/sudoers.d -p wa -k sudoers_changes
-w /etc/ssh/sshd_config -p wa -k sshd_config_changes
-w /etc/ssh/sshd_config.d -p wa -k sshd_config_changes
```

## Limites e trade-offs
Regras `-w` resolvem o *inode* do arquivo ou diretório no momento em que a regra é carregada; se o arquivo ainda não existir quando o `auditd` iniciar, a regra falhará — monitore sempre o diretório pai (ex.: `-w /etc/sudoers.d -p wa`) quando arquivos internos puderem ser criados dinamicamente.

## Como verificar
Carregue as regras, execute `sudo touch /etc/sudoers` e verifique o registro imediato com `sudo ausearch -k sudoers_changes -i`.

## Conexões
- [[auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2]] — Veja também: Linux Audit (`auditd`): Ordenação `10`–`99` em `/etc/audit/rules.d/`, Backlog (`-b`), Modo de Falha (`-f`) e Trava Imutável (`-e 2`).
- [[auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid]] — Veja também: Linux Audit (`auditd`): Auditoria de Syscalls por Arquitetura (`b64`/`b32`), Execução Privilegiada (`auid!=unset`, `uid!=euid`) e Binários SUID.
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
