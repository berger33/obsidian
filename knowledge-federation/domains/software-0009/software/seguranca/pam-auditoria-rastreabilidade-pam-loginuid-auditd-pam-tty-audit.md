---
id: software.seguranca.tranche13.001287
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

# Rastreabilidade Imutável de Identidade no Linux: Como o **`pam_loginuid.so`** Preserva o **`auid` (*Audit UID*)** Original Mesmo Após `sudo su -`!

## Em uma frase
Já se perguntou como o **Linux Auditd (`/var/log/audit/audit.log`)**, o **Falco** e o **Tetragon** sabem exatamente **qual pessoa real (`auid=1001`, ex.: `carlos`)** executou um comando destrutivo como `root` (`uid=0`, `euid=0`), mesmo depois que esse administrador fez login via SSH com sua conta nominal e rodou `sudo su -` ou `sudo -i` virando `root`?

## Por que importa
O responsável por essa mágica forense é o módulo **`session required pam_loginuid.so`** executado na abertura da sessão inicial (em `/etc/pam.d/sshd`, `/etc/pam.d/login` e `/etc/pam.d/gdm`)!

## Como funciona
No momento em que o usuário faz seu login inicial no sistema (ex.: `carlos`, UID `1001`), o **`pam_loginuid.so`** grava o UID `1001` no atributo especial do processo no Kernel Linux **`/proc/self/loginuid`** (que corresponde ao campo **`auid=...` — *Audit User ID*** nos logs do `auditd`). A propriedade de segurança fundamental do `loginuid` no Kernel Linux é que ele é **herdado por todos os processos filhos (`fork`/`execve`) e permanece IMUTÁVEL mesmo quando o processo muda seu `uid`/`euid` para `0` (`root`) via `sudo` ou `su`**!

## Exemplo
```bash
# Verificar no /proc/self/loginuid que o Audit UID (auid) original do usuario humano permanece preservado mesmo dentro de um shell root (sudo)
cat /proc/self/loginuid; echo ""
id
```

## Limites e trade-offs
Além do `pam_loginuid.so`, para servidores críticos de alta segurança (como Bastion Hosts ou servidores PCI-DSS), o Linux-PAM oferece o módulo **`pam_tty_audit.so`** (`session required pam_tty_audit.so disable=* enable=root,admins log_passwd=no`), que instrui o kernel a registrar no subsistema `auditd` (`type=TTY`) todos os comandos digitados no terminal pelas contas auditadas!

## Como verificar
Atenção: o `pam_loginuid.so` deve estar presente apenas nos pontos de **entrada inicial de sessão** (`sshd`, `login`, `crond`, `gdm`) e **NUNCA** dentro de `/etc/pam.d/sudo` ou `/etc/pam.d/su` (pois o objetivo é justamente preservar o `loginuid` gravado no login inicial!).

## Conexões
- [[pam-limites-recursos-sessao-pam-limits-limits-conf-fork-bomb-core]] — Veja também: Blindagem de Sessão com **`pam_limits.so` (`/etc/security/limits.conf`)** e **`pam_umask.so`**: Prevenindo **Fork Bombs (`nproc`)**, Core Dumps (`core 0`) e Permissões Frouxas.
- [[pam-autenticacao-multifator-mfa-pam-u2f-fido2-google-authenticator-sshd]] — Veja também: Autenticação Multifator (**MFA**) no Linux-PAM para **`sshd`** e **`sudo`**: Integrando Chaves de Hardware **FIDO2 (`pam_u2f.so`)** e **TOTP (`pam_google_authenticator.so`)**.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[plaso-forense-linux-macos-containers-syslog-auditd-plist-unified-logs]] — Referência cruzada direta com plaso-forense-linux-macos-containers-syslog-auditd-plist-unified-logs.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
