---
id: software.seguranca.tranche05.000461
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

# Linux Audit (`auditd`): Arquitetura do Subsistema de Auditoria do Kernel, `auditctl`, `augenrules` e `RefuseManualStop`

## Em uma frase
O **Linux Audit System** (`linux-audit/audit-userspace`, GPLv2) é o subsistema nativo do kernel Linux e espaço de usuário projetado para atender requisitos de Common Criteria (FAU_GEN), PCI-DSS, DISA STIG e CIS Benchmarks interceptando chamadas de sistema (*syscalls*) e eventos de aplicações privilegiadas (PAM, `sudo`, `sshd`, SELinux/AppArmor).

## Por que importa
Diferente do `syslog` comum, o subsistema de auditoria do kernel vincula cada evento ao **`auid`** (*Audit Login UID* imutável, preservado mesmo após `sudo su -` ou troca de UID efetivo `uid=0`), garantindo atribuição forense irrefutável de quem iniciou a sessão.

## Como funciona
O kernel gera os eventos e os envia via socket Netlink para o daemon **`auditd`**, que grava em `/var/log/audit/audit.log` e distribui em tempo real para plugins `audisp`. As regras modulares ficam em `/etc/audit/rules.d/*.rules` (organizadas numericamente de `10-base-config.rules` até `99-finalize.rules`) e são compiladas e carregadas por **`augenrules --load`** (que invoca `auditctl -R`).

## Exemplo
```bash
# Compilar e carregar todas as regras de /etc/audit/rules.d/ e verificar o status do subsistema no kernel
sudo augenrules --check
sudo augenrules --load
sudo auditctl -s
```

## Limites e trade-offs
O arquivo `auditd.service` inclui intencionalmente `RefuseManualStop=yes` porque parar o daemon via `systemctl` usa o D-Bus e perderia o `loginuid` de quem enviou o sinal (registrando `auid=-1`); para reiniciar ou parar em conformidade com Common Criteria, use `sudo service auditd restart` (ou `auditctl --signal`).

## Como verificar
Execute `sudo auditctl -s` e confirme `enabled 1` (ou `2` se imutável), `lost 0` e o PID ativo do `auditd`.

## Conexões
- [[auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2]] — Veja também: Linux Audit (`auditd`): Ordenação `10`–`99` em `/etc/audit/rules.d/`, Backlog (`-b`), Modo de Falha (`-f`) e Trava Imutável (`-e 2`).
- [[auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w]] — Referência cruzada direta com auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
