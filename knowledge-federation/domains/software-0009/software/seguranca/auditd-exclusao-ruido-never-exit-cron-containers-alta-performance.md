---
id: software.seguranca.tranche05.000466
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

# Linux Audit (`auditd`): Supressão Cirúrgica de Ruído com Regras `never,exit` e `exclude` em `20-dont-audit.rules`

## Em uma frase
Em servidores de produção com alta carga, certos processos repetitivos (como `cron` trocando credenciais a cada minuto, agentes de monitoramento lendo `/proc` ou mensagens `CRYPTO_KEY_USER` verbosas) podem gerar gigabytes de logs irrelevantes se não forem filtrados em **`20-dont-audit.rules`**.

## Por que importa
Sem supressão cirúrgica de ruído benigno, a partição `/var/log/audit` enche rapidamente, rotaciona os logs forenses importantes e consome ciclos de CPU na serialização Netlink.

## Como funciona
O filtro `-a never,exclude -F msgtype=<TIPO>` descarta tipos inteiros de mensagens na origem, enquanto `-a never,exit` colocado no arquivo de prefixo **`20-*`** (para ser avaliado antes das regras `always,exit` em `30-*`) ignora eventos específicos quando todos os campos (`-F exe=...`, `-F uid=...`, `-F subj_type=...`) coincidem.

## Exemplo
```ini
# /etc/audit/rules.d/20-dont-audit.rules
# Ignorar mensagens ruidosas de negociacao de chaves criptograficas internas
-a never,exclude -F msgtype=CRYPTO_KEY_USER

# Ignorar eventos de troca de credenciais de servicos agendados pelo proprio daemon cron em background
-a never,user -F subj_type=crond_t
-a never,exit -F arch=b64 -S adjtimex -F auid=unset -F uid=chrony
```

## Limites e trade-offs
Nunca escreva uma regra ampla `-a never,exit -F uid=0` ou `-F dir=/tmp` sem restringir estritamente o executável (`-F exe=/usr/sbin/chronyd`) e `auid=unset`, caso contrário você criará um ponto cego que qualquer invasor poderá explorar.

## Como verificar
Execute `sudo augenrules --load` e verifique com `sudo auditctl -l` que as regras `never` aparecem listadas **acima** das regras `always`.

## Conexões
- [[auditd-regras-modulos-kernel-mount-ptrace-time-change-mac]] — Veja também: Linux Audit (`auditd`): Monitoramento de Carregamento de Módulos do Kernel (`init_module`, `finit_module`), `ptrace`, Alteração de Hora e MAC.
- [[auditd-protecao-disco-particao-dedicada-space-left-action-halt]] — Veja também: Linux Audit (`auditd`): Partição `/var/log/audit` Dedicada, `space_left_action`, `admin_space_left_action` e `disk_full_action`.
- [[auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2]] — Referência cruzada direta com auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
