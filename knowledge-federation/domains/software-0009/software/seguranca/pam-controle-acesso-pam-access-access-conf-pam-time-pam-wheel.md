---
id: software.seguranca.tranche13.001285
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

# Controle de Acesso Granular por Origem e Horário no PAM: **`pam_access.so` (`/etc/security/access.conf`)**, **`pam_time.so`** e Restrição de `su` com **`pam_wheel.so`**

## Em uma frase
Mesmo que um usuário possua credenciais válidas, como impor diretamente na camada de autenticação do sistema operacional regras de **Controle de Acesso Contextual**: por exemplo, permitir que contas de administração façam login **exclusivamente a partir da sub-rede da VPN de gerência (`10.10.10.0/24`) ou do console físico local (`LOCAL`)**, bloquear qualquer login interativo de contas de serviço e restringir o comando **`su`** apenas a membros do grupo `wheel`/`sudo`?

## Por que importa
O Linux-PAM resolve isso através de três módulos nativos de controle de conta e autorização: **(1) `pam_access.so`**, que lê a tabela de controle de acesso **`/etc/security/access.conf`** no formato `permissão : usuários/grupos : origens (IPs, sub-redes CIDR, TTYs, LOCAL, ALL)`; **(2) `pam_time.so`**, que lê **`/etc/security/time.conf`** para restringir logins a janelas de dias da semana e horários permitidos (ex.: `Wk0800-1900`); e **(3) `pam_wheel.so`** em **`/etc/pam.d/su`**!

## Como funciona
Em `/etc/pam.d/su`, descomentar a linha **`auth required pam_wheel.so use_uid`** garante que **apenas usuários cujo UID real pertença ao grupo `wheel` (ou `group=sudo`) possam sequer tentar executar o comando `su` para virar `root`** — bloqueando tentativas de movimentação lateral de contas de aplicação comprometidas!

## Exemplo
```text
# Exemplo de /etc/security/access.conf: permite admins apenas da VPN de gerencia (10.10.10.0/24) ou console local e nega todo o resto (Fail-Closed)
+ : root (admins) : 10.10.10.0/24 LOCAL
+ : deploy-ci : 10.20.30.50/32
- : ALL : ALL
```

## Limites e trade-offs
Veja a última linha do `/etc/security/access.conf` acima (**`- : ALL : ALL`**): como o `pam_access.so` avalia a tabela de cima para baixo e aplica a **primeira regra que casar (*First Match*)**, terminar o arquivo com `- : ALL : ALL` implementa uma política **Allowlist Estrita (Zero Trust)** no nível do PAM — qualquer usuário ou IP de origem não listado explicitamente nas linhas `+` anteriores é negado na fase `account`!

## Como verificar
Em `/etc/pam.d/su`, use sempre a opção **`use_uid`** junto com `pam_wheel.so` para que o módulo verifique o UID real do processo chamador (e não apenas o nome de login da sessão).

## Conexões
- [[pam-qualidade-senhas-pam-pwquality-entropia-dicionario-historico]] — Veja também: Políticas de Complexidade de Senhas (`pam_pwquality.so` / `/etc/security/pwquality.conf`) e Histórico Anti-Reuso (`pam_pwhistory.so`) no Linux-PAM.
- [[pam-limites-recursos-sessao-pam-limits-limits-conf-fork-bomb-core]] — Veja também: Blindagem de Sessão com **`pam_limits.so` (`/etc/security/limits.conf`)** e **`pam_umask.so`**: Prevenindo **Fork Bombs (`nproc`)**, Core Dumps (`core 0`) e Permissões Frouxas.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[pam-flags-controle-required-requisite-sufficient-optional-substack]] — Referência cruzada direta com pam-flags-controle-required-requisite-sufficient-optional-substack.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
