---
id: software.seguranca.tranche05.000467
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

# Linux Audit (`auditd`): Partição `/var/log/audit` Dedicada, `space_left_action`, `admin_space_left_action` e `disk_full_action`

## Em uma frase
Conforme destacado na documentação oficial do `audit-userspace`, o daemon `auditd` monitora continuamente o espaço livre na partição de logs através de `/etc/audit/auditd.conf` (`max_log_file`, `num_logs`, `space_left`, `space_left_action`, `admin_space_left` e `admin_space_left_action`).

## Por que importa
Se `/var/log/audit` compartilhar a mesma partição que `/var/log` ou `/tmp`, um usuário não-privilegiado pode encher o disco usando o comando `logger` ou arquivos temporários e acionar intencionalmente a ação `admin_space_left_action = HALT` ou `SINGLE`, causando negação de serviço ou silenciando a auditoria.

## Como funciona
A arquitetura recomendada exige montar `/var/log/audit` em uma **partição lógica LVM dedicada**, acessível exclusivamente pelo `root` (`0700`), configurando `space_left = 25%` com `space_left_action = SYSLOG` (ou `EMAIL`) para alertar o SOC com antecedência e `max_log_file_action = ROTATE` (ou `KEEP_LOGS` quando o arquivamento externo move os arquivos antigos).

## Exemplo
```ini
# /etc/audit/auditd.conf — Parametros de resiliencia de armazenamento e retencao
log_file = /var/log/audit/audit.log
log_format = ENRICHED
max_log_file = 50
num_logs = 20
max_log_file_action = ROTATE
space_left = 25%
space_left_action = SYSLOG
admin_space_left = 5%
admin_space_left_action = SUSPEND
disk_full_action = SUSPEND
```

## Limites e trade-offs
Usar `log_format = ENRICHED` em `/etc/audit/auditd.conf` faz o `auditd` resolver no momento da escrita os nomes de usuários (`UID -> username`), grupos e números de syscalls locais no próprio host antes de enviar para o SIEM central.

## Como verificar
Verifique com `df -h /var/log/audit` que o diretório reside em um volume dedicado e confirme `log_format = ENRICHED` em `/etc/audit/auditd.conf`.

## Conexões
- [[auditd-exclusao-ruido-never-exit-cron-containers-alta-performance]] — Veja também: Linux Audit (`auditd`): Supressão Cirúrgica de Ruído com Regras `never,exit` e `exclude` em `20-dont-audit.rules`.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Veja também: Linux Audit (`auditd`): Investigação Forense e Resposta a Incidentes com `ausearch` (`-i`, `-k`, `-ua`, `--session`) e `aureport`.
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.
- [[lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot]] — Referência cruzada direta com lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot.
- [[auditd-streaming-tempo-real-audisp-af-unix-remote-siem]] — Referência cruzada direta com auditd-streaming-tempo-real-audisp-af-unix-remote-siem.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
