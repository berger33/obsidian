---
id: software.seguranca.tranche15.001439
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Correlação de Bloqueios do fapolicyd com **`auditd` (`FANOTIFY`)** e Customização do **`syslog_format`** para Detecção Imediata no SIEM

## Em uma frase
Quando uma regra do `fapolicyd` com decisão **`deny_audit`** bloqueia uma tentativa de execução maliciosa em um servidor de produção, onde esse alerta é gravado e como correlacioná-lo no **Linux Audit (`auditd` / `ausearch`)** e no **SIEM (Wazuh / OpenSearch)**?

## Por que importa
Quando a decisão na regra é **`deny_audit`**, o próprio Kernel Linux (subsistema `fanotify` integrado ao `kauditd`) gera automaticamente um registro de auditoria completo do tipo **`SYSCALL` + `FANOTIFY`** no `/var/log/audit/audit.log`!

## Como funciona
Ao mesmo tempo, se você usar `deny_syslog` (ou rodar com log ativo), o `fapolicyd` formata o evento seguindo a diretiva **`syslog_format = rule,dec,perm,auid,pid,exe,:,path,ftype,trust`** do `/etc/fapolicyd/fapolicyd.conf`! Assim, o seu SOC recebe em tempo real: qual regra bloqueou (`rule`), qual usuário humano original iniciou a sessão SSH (`auid`), qual processo tentou executar (`exe`), qual arquivo exato foi bloqueado (`path`) e o status de confiança (`trust=0`)!

## Exemplo
```bash
# Pesquisar no Linux Audit (ausearch) todos os bloqueios de execucao acionados pelo fapolicyd (regras deny_audit / eventos FANOTIFY) hoje
ausearch -m FANOTIFY -ts today -i || ausearch -sc execve --success no -ts today -i
```

## Limites e trade-offs
Por que todo alerta de **`deny_audit` (`FANOTIFY`)** do `fapolicyd` em um servidor de produção deve ser tratado como um **Alerta de Alta Fidelidade (Zero Ruído)** pelo seu SOC? Porque em um servidor de produção devidamente homologado, nenhum processo legítimo tenta executar binários fora do banco de confiança (`trust=0`); portanto, um evento `deny_audit` significa que **alguém (ou um exploit automatizado) acabou de tentar rodar código não autorizado na máquina e foi travado na hora pelo Kernel**!

## Como verificar
Configure no Wazuh / SIEM uma regra de correlação imediata para eventos `type=FANOTIFY` ou mensagens `fapolicyd: rule=... dec=deny_audit` acionando resposta a incidentes.

## Conexões
- [[fapolicyd-tuning-performance-watch-fs-q-size-caches-containers]] — Veja também: Tuning de Performance do **`/etc/fapolicyd/fapolicyd.conf`**: Sistemas de Arquivos Monitorados (`watch_fs`), `ignore_mounts`, Tamanho de Fila `q_size` e Cache Hit Ratio.
- [[fapolicyd-automacao-ansible-systemd-hardening-ciclo-vida-pacotes]] — Veja também: Operação em Escala do fapolicyd com **Ansible (`rhel-system-roles.fapolicyd`)**, Integração **`dnf` / `rpm`** e Proteção do Daemon contra Parada Indevida.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.
- [[fapolicyd-sintaxe-regras-decision-perm-subject-object-customizacao]] — Referência cruzada direta com fapolicyd-sintaxe-regras-decision-perm-subject-object-customizacao.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
