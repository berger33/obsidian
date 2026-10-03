---
id: software.seguranca.tranche05.000468
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

# Linux Audit (`auditd`): Investigação Forense e Resposta a Incidentes com `ausearch` (`-i`, `-k`, `-ua`, `--session`) e `aureport`

## Em uma frase
As ferramentas de espaço de usuário **`ausearch`** e **`aureport`** reconstroem eventos multi-linha do `audit.log` (agrupando os registros `SYSCALL`, `EXECVE`, `CWD`, `PATH` e `PROCTITLE` que compartilham o mesmo `serial` de evento) e decodificam argumentos codificados em hexadecimal (`-i` / `--interpret`).

## Por que importa
No `audit.log`, argumentos de linha de comando que contêm espaços ou caracteres especiais são gravados em hexadecimal no campo `proctitle=62617368002D63...` para evitar injeção de log; usar `ausearch -i` traduz automaticamente o hexadecimal, os UIDs numéricos, os números de syscalls e os timestamps epoch.

## Como funciona
Durante um incidente, `ausearch -ua <UID> -ts today -i` reconstrói absolutamente tudo o que um usuário específico fez na máquina desde o login SSH (mesmo após ter virado `root`), enquanto `aureport --summary`, `aureport -au --failed` (falhas de autenticação), `aureport -x` (executáveis) e `aureport -m` (modificações de contas) geram relatórios executivos imediatos.

## Exemplo
```bash
# Reconstruir todas as execucoes privilegiadas de hoje interpretando hex/UIDs e gerar relatorio de anomalias
sudo ausearch -k priv_esc_exec -ts today -i
sudo aureport --failed --summary
sudo aureport -x --summary
```

## Limites e trade-offs
Nunca faça `grep` textual simples procurando por comandos com espaços diretamente em `/var/log/audit/audit.log`, pois o campo `PROCTITLE` está codificado em hexadecimal quando contém espaços; use sempre `ausearch -i` para decodificar antes de filtrar.

## Como verificar
Execute `sudo ausearch -m USER_LOGIN -ts today -i` e verifique a correlação entre endereço IP de origem (`addr=`), `auid`, `ses` (ID de sessão) e resultado (`res=success`).

## Conexões
- [[auditd-protecao-disco-particao-dedicada-space-left-action-halt]] — Veja também: Linux Audit (`auditd`): Partição `/var/log/audit` Dedicada, `space_left_action`, `admin_space_left_action` e `disk_full_action`.
- [[auditd-streaming-tempo-real-audisp-af-unix-remote-siem]] — Veja também: Linux Audit (`auditd`): Streaming em Tempo Real com Plugins `audisp` (`/etc/audit/plugins.d/`, `af_unix` e `audisp-remote` TLS/Kerberos).
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.
- [[auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid]] — Referência cruzada direta com auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
