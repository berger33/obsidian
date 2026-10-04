---
id: software.seguranca.tranche13.001286
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/linux-pam/linux-pam/master/README", "https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Blindagem de Sessão com **`pam_limits.so` (`/etc/security/limits.conf`)** e **`pam_umask.so`**: Prevenindo **Fork Bombs (`nproc`)**, Core Dumps (`core 0`) e Permissões Frouxas

## Em uma frase
O que acontece logo após um usuário ser autenticado com sucesso nas fases `auth` e `account` do PAM? A `libpam` executa a pilha **`session`** — que é o momento perfeito para aplicar limites de recursos do kernel e permissões padrão de arquivos a todos os processos daquela sessão!

## Por que importa
Dois módulos na pilha `session` são obrigatórios no hardening de servidores Linux (CIS Benchmark): **(1) `pam_limits.so`**, que lê **`/etc/security/limits.conf`** e **`/etc/security/limits.d/*.conf`** para impor limites `soft` e `hard` de sistema (`setrlimit(2)`) sobre cada sessão; e **(2) `pam_umask.so`**, que define a máscara padrão de criação de arquivos (**`umask=0027`** ou **`0077`**) para que nenhum arquivo criado pelo usuário nasça legível por `others` (`o-rwx`)!

## Como funciona
Em **`/etc/security/limits.conf`**, duas regras protegem a estabilidade e a confidencialidade do servidor: **`* hard core 0`** (proíbe a geração de arquivos de *Core Dump* em disco quando um programa falha — evitando que segredos, chaves privadas ou senhas presentes na memória RAM vazem para um arquivo de dump!) e **`* hard nproc 2048`** (limita o número máximo de processos por usuário, impedindo que uma **Fork Bomb** trave o servidor)!

## Exemplo
```text
# Regras de hardening em /etc/security/limits.d/99-security-hardening.conf: desabilitar core dumps e limitar processos por usuario
*    soft    core     0
*    hard    core     0
*    soft    nproc    1024
*    hard    nproc    2048
*    soft    nofile   4096
*    hard    nofile   65536
```

## Limites e trade-offs
Lembre-se de que para desabilitar completamente *Core Dumps* também em binários SUID e serviços gerenciados pelo `systemd`, você deve combinar `* hard core 0` no `limits.conf` com **`fs.suid_dumpable = 0`** no `/etc/sysctl.d/` e **`DefaultLimitCORE=0`** em `/etc/systemd/system.conf`!

## Como verificar
Verifique os limites aplicados à sua sessão atual executando **`ulimit -a`** (limites `soft`) e **`ulimit -Ha`** (limites `hard`).

## Conexões
- [[pam-controle-acesso-pam-access-access-conf-pam-time-pam-wheel]] — Veja também: Controle de Acesso Granular por Origem e Horário no PAM: **`pam_access.so` (`/etc/security/access.conf`)**, **`pam_time.so`** e Restrição de `su` com **`pam_wheel.so`**.
- [[pam-auditoria-rastreabilidade-pam-loginuid-auditd-pam-tty-audit]] — Veja também: Rastreabilidade Imutável de Identidade no Linux: Como o **`pam_loginuid.so`** Preserva o **`auid` (*Audit UID*)** Original Mesmo Após `sudo su -`!.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[firejail-integracao-apparmor-cgroups-rlimits-controle-recursos]] — Referência cruzada direta com firejail-integracao-apparmor-cgroups-rlimits-controle-recursos.
- [[keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866]] — Referência cruzada direta com keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
