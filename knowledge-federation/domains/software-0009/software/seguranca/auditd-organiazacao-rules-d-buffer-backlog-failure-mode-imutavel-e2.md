---
id: software.seguranca.tranche05.000462
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

# Linux Audit (`auditd`): Ordenação `10`–`99` em `/etc/audit/rules.d/`, Backlog (`-b`), Modo de Falha (`-f`) e Trava Imutável (`-e 2`)

## Em uma frase
A documentação oficial de regras do `audit-userspace` estrutura `/etc/audit/rules.d/` em faixas numéricas estritas processadas em ordem pelo `augenrules`: **`10`** (configuração de kernel/auditctl), **`20`** (exceções `never` que devem preceder regras gerais), **`30`** (regras principais STIG/PCI/CIS), **`40–70`** (regras opcionais e locais) e **`90–99`** (finalização e modo imutável).

## Por que importa
Como o motor de regras do kernel avalia as listas na ordem de inserção (*first-match wins* dentro de cada lista de filtro), colocar uma regra de exclusão de ruído depois da regra geral de captura em `30-*` faz com que a exclusão nunca seja atingida.

## Como funciona
Em `10-base-config.rules`, `-D` limpa regras anteriores, `-b 8192` (ou `16384` em servidores movimentados) dimensiona o buffer de *backlog* do kernel para evitar perda de eventos sob pico, e `-f 1` define o modo de falha (`0=silent`, `1=printk` no dmesg, `2=panic` derrubando o kernel para ambientes de segurança máxima). Em `99-finalize.rules`, **`-e 2`** trava a configuração em **modo imutável**: nem mesmo o `root` pode remover ou alterar regras de auditoria sem reiniciar fisicamente o servidor.

## Exemplo
```ini
# /etc/audit/rules.d/10-base-config.rules
-D
-b 16384
--backlog_wait_time 60000
-f 1

# /etc/audit/rules.d/99-finalize.rules
-e 2
```

## Limites e trade-offs
Uma vez que `-e 2` (*immutable mode*) é carregado no kernel, qualquer tentativa de `auditctl -D` ou `augenrules --load` retornará erro até o próximo reboot; valide todas as regras com `-e 1` antes de ativar `-e 2`.

## Como verificar
Verifique com `sudo auditctl -s` que `backlog_limit` reflete `16384` e que `enabled` passa para `2` após carregar `99-finalize.rules`.

## Conexões
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Veja também: Linux Audit (`auditd`): Arquitetura do Subsistema de Auditoria do Kernel, `auditctl`, `augenrules` e `RefuseManualStop`.
- [[auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w]] — Veja também: Linux Audit (`auditd`): Monitoramento de Integridade de Arquivos Críticos (`-w` / `-F path=`) — Identidade, `sudoers`, SSH e Cron.
- [[auditd-protecao-disco-particao-dedicada-space-left-action-halt]] — Referência cruzada direta com auditd-protecao-disco-particao-dedicada-space-left-action-halt.
- [[auditd-exclusao-ruido-never-exit-cron-containers-alta-performance]] — Referência cruzada direta com auditd-exclusao-ruido-never-exit-cron-containers-alta-performance.

## Fontes
- [Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/README.md) — documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop); consultado em 2026-10-03.
- [Linux Audit Official Rules — README-rules & augenrules Ordering](https://raw.githubusercontent.com/linux-audit/audit-userspace/master/rules/README-rules) — especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules; consultado em 2026-10-03.
- [Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules](https://github.com/linux-audit/audit-userspace/tree/master/rules) — catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS; consultado em 2026-10-03.
