---
id: software.seguranca.tranche13.001283
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

# Bloqueio contra Força Bruta no Linux com **`pam_faillock.so`** e **`/etc/security/faillock.conf`**: `deny`, `fail_interval`, `unlock_time` e `even_deny_root`

## Em uma frase
No Linux moderno (RHEL 8/9, Debian 12+, Ubuntu 22.04/24.04+, Fedora, SUSE), os antigos módulos `pam_tally` e `pam_tally2` foram depreciados e removidos em favor do módulo oficial **`pam_faillock.so`**, configurado centralizadamente no arquivo **`/etc/security/faillock.conf`**!

## Por que importa
Como o **`pam_faillock`** protege contra ataques de força bruta de senha em SSH, console e telas de login? Ele mantém arquivos de contagem de falhas por usuário no diretório `/var/run/faillock/<usuario>` e é chamado em três pontos da pilha PAM: **`preauth`** (no topo de `auth` como `requisite`: antes mesmo de verificar a senha, checa se a conta já está bloqueada!), **`authfail`** (após `pam_unix.so`: incrementa o contador se a senha falhou!) e **`account`**!

## Como funciona
Em **`/etc/security/faillock.conf`**, os parâmetros recomendados por baselines **CIS Benchmark / DISA STIG** são: **`deny = 5`** (bloqueia após 5 falhas), **`fail_interval = 900`** (janela de 15 minutos), **`unlock_time = 900`** (tempo de bloqueio de 15 minutos; use `0` apenas se quiser bloqueio permanente até desbloqueio manual!), **`audit`** (registra o nome do usuário no Linux Auditd!), **`silent`** (não informa ao atacante que a conta entrou em lockout!) e **`even_deny_root`** com **`root_unlock_time = 60`**!

## Exemplo
```ini
# Configuracao recomendada em /etc/security/faillock.conf para protecao contra forca bruta local e remota
dir = /var/run/faillock
audit
silent
deny = 5
fail_interval = 900
unlock_time = 900
even_deny_root
root_unlock_time = 60
```

## Limites e trade-offs
E como um administrador consulta ou desbloqueia no terminal uma conta que atingiu o limite de falhas do `pam_faillock`? Usando o comando utilitário **`faillock`**: **`faillock --user <usuario>`** (exibe todas as tentativas falhas com timestamp e IP/TTY de origem!) e **`faillock --user <usuario> --reset`** (zera imediatamente o contador e desbloqueia a conta)!

## Como verificar
Por padrão, `/var/run/faillock` reside em `tmpfs` (para evitar que um ataque de força bruta encha o disco raiz); se o seu requisito de conformidade exigir persistência do bloqueio mesmo após um reboot físico do servidor, altere `dir = /var/log/faillock` em `faillock.conf`.

## Conexões
- [[pam-flags-controle-required-requisite-sufficient-optional-substack]] — Veja também: Semântica das **Control Flags** do Linux-PAM (**`required`, `requisite`, `sufficient`, `optional`**) e Sintaxe Avançada `[success=done default=ignore]`.
- [[pam-qualidade-senhas-pam-pwquality-entropia-dicionario-historico]] — Veja também: Políticas de Complexidade de Senhas (`pam_pwquality.so` / `/etc/security/pwquality.conf`) e Histórico Anti-Reuso (`pam_pwhistory.so`) no Linux-PAM.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
