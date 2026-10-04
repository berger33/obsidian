---
id: software.seguranca.tranche05.000498
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
fontes: ["https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md", "https://github.com/SELinuxProject/selinux/wiki", "https://github.com/SELinuxProject/selinux/wiki/Tools"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SELinux: Confinamento RBAC de Usuários Humanos e Administradores SSH (`semanage login`, `user_u`, `staff_u`, `sysadm_u` e `sudo -r`)

## Em uma frase
Por padrão na política `targeted`, daemons de rede são confinados mas usuários humanos que fazem login via SSH entram no contexto **`unconfined_u:unconfined_r:unconfined_t:s0`**. O SELinux permite confinar também todas as contas de usuários e administradores mapeando logins Linux para usuários SELinux restritos via **`semanage login`**.

## Por que importa
Se a estação de um administrador for comprometida e sua sessão SSH rodar como `unconfined_t`, malwares executados na sessão não sofrem restrição de domínio; mapeá-lo para **`staff_u`** força a sessão inicial a rodar no domínio restrito `staff_t` e exige transição explícita de Role (`sudo -r sysadm_r`) para tarefas administrativas.

## Como funciona
Os principais usuários SELinux confinados são: **`guest_u`** (sem acesso à rede, sem `sudo`/`su` e sem execução em `/home` ou `/tmp`), **`xguest_u`** (quiosque gráfico básico), **`user_u`** (usuário comum sem permissão de usar `sudo` ou `su`), **`staff_u`** (administrador que entra sem privilégios e usa `sudo -r sysadm_r` para transitar para `sysadm_t`) e **`sysadm_u`** (administrador confinado pelo SELinux).

## Exemplo
```bash
# Mapear um usuario desenvolvedor para user_u (proibindo sudo/su) e um operador para staff_u
sudo semanage login -a -s user_u dev_contractor
sudo semanage login -a -s staff_u sre_operator
sudo semanage login -l
```

## Limites e trade-offs
Ao mapear o login padrão `__default__` para `user_u` (`sudo semanage login -m -s user_u -r s0 __default__`), certifique-se de mapear **antes** os administradores de sistema explicitamente para `staff_u` (e configurar `role=sysadm_r` na regra do `/etc/sudoers`), caso contrário ninguém mais conseguirá executar `sudo` no servidor.

## Como verificar
Faça login via SSH com a conta `dev_contractor`, execute `id -Z` e confirme que o contexto retornado é `user_u:user_r:user_t:s0`.

## Conexões
- [[selinux-compilacao-modulos-customizados-te-cil-udica-semodule]] — Veja também: SELinux: Desenvolvimento e Gerenciamento de Módulos de Política (`.te` / `.cil`), `checkmodule`, `semodule_package`, `secilc` e `semodule`.
- [[selinux-analise-politicas-setools-sesearch-seinfo-auditoria]] — Veja também: SELinux: Auditoria e Consulta Formal da Política Binária com `setools` (`sesearch`, `seinfo` e Desativação Temporária de `dontaudit`).
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.
- [[auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid]] — Referência cruzada direta com auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
