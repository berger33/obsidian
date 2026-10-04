---
id: software.seguranca.tranche13.001284
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

# Políticas de Complexidade de Senhas (`pam_pwquality.so` / `/etc/security/pwquality.conf`) e Histórico Anti-Reuso (`pam_pwhistory.so`) no Linux-PAM

## Em uma frase
Quando contas locais precisam ter senhas no Linux (como a senha de `sudo` de um administrador ou contas de console de emergência), como impedir que alguém defina uma senha fraca, baseada em dicionário, derivada do próprio nome de usuário ou reutilize as mesmas senhas antigas ao rotacionar?

## Por que importa
A pilha **`password`** do Linux-PAM utiliza dois módulos complementares: **(1) `pam_pwquality.so`** (configurado em **`/etc/security/pwquality.conf`**), que valida comprimento mínimo, classes de caracteres, palíndromos, sequências monótonas (`1234`, `abcd`), similaridade com a senha anterior e dicionários Cracklib; e **(2) `pam_pwhistory.so`** (configurado em **`/etc/security/pwhistory.conf`** com `remember = 24`), que armazena os hashes das últimas `N` senhas do usuário em `/etc/security/opasswd` e proíbe reutilizá-las!

## Como funciona
No **`/etc/security/pwquality.conf`**, configure: **`minlen = 15`** (mínimo de 15 caracteres), **`minclass = 3`** (ou créditos negativos `dcredit = -1`, `ucredit = -1`, `lcredit = -1`, `ocredit = -1`), **`difok = 8`** (pelo menos 8 caracteres diferentes da senha antiga!), **`maxrepeat = 3`** (proíbe `aaaa`), **`usercheck = 1`**, **`dictcheck = 1`** e **`enforce_for_root`**!

## Exemplo
```ini
# Politica forte de qualidade de senhas em /etc/security/pwquality.conf (aplicada inclusive ao root via enforce_for_root)
minlen = 15
dcredit = -1
ucredit = -1
lcredit = -1
ocredit = -1
minclass = 4
maxrepeat = 3
maxclassrepeat = 4
difok = 8
dictcheck = 1
usercheck = 1
enforce_for_root
```

## Limites e trade-offs
Por que a diretiva **`enforce_for_root`** no `pwquality.conf` e no `pwhistory.conf` é indispensável? Porque sem ela, quando o `root` altera uma senha, o PAM apenas exibe um *warning* informativo na tela mas aceita a senha fraca; com `enforce_for_root`, a política é obrigatória para 100% das contas!

## Como verificar
Certifique-se também de que o módulo `pam_unix.so` na pilha `password` esteja configurado com o algoritmo **`yescrypt`** (ou **`sha512`** com `rounds=65536`) em `/etc/login.defs` (`ENCRYPT_METHOD YESCRYPT`) para proteger os hashes em `/etc/shadow`.

## Conexões
- [[pam-protecao-forca-bruta-pam-faillock-faillock-conf-bloqueio-contas]] — Veja também: Bloqueio contra Força Bruta no Linux com **`pam_faillock.so`** e **`/etc/security/faillock.conf`**: `deny`, `fail_interval`, `unlock_time` e `even_deny_root`.
- [[pam-controle-acesso-pam-access-access-conf-pam-time-pam-wheel]] — Veja também: Controle de Acesso Granular por Origem e Horário no PAM: **`pam_access.so` (`/etc/security/access.conf`)**, **`pam_time.so`** e Restrição de `su` com **`pam_wheel.so`**.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[keepassxc-auditoria-saude-senhas-hibp-k-anonymity-relatorios]] — Referência cruzada direta com keepassxc-auditoria-saude-senhas-hibp-k-anonymity-relatorios.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
