---
id: software.seguranca.tranche13.001281
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

# Arquitetura do **Linux-PAM (`linux-pam/linux-pam`)**: Os 4 Grupos de Gerenciamento (**`auth`, `account`, `password`, `session`**) e Arquivos `/etc/pam.d/`

## Em uma frase
Por que quando você configura autenticação multifator (FIDO2/TOTP), bloqueio contra força bruta (`pam_faillock`), limites de recursos (`limits.conf`) ou integração com Active Directory/FreeIPA (`SSSD`) no Linux, programas totalmente diferentes como **`sshd`**, **`sudo`**, **`login`**, **`su`** e **`gdm`** passam a obedecer instantaneamente à nova política sem precisar recompilar nenhum deles?

## Por que importa
Graças à arquitetura do **Linux-PAM (*Pluggable Authentication Modules*)**! Criado originalmente a partir da RFC 86.0 do OSF e mantido em **`linux-pam/linux-pam`**, o PAM desacopla as aplicações privilegiadas dos mecanismos concretos de autenticação através da biblioteca compartilhada **`libpam.so`** e dos arquivos de política por serviço em **`/etc/pam.d/<servico>`** (com fallback seguro em `/etc/pam.d/other` usando `pam_deny.so` + `pam_warn.so`)!

## Como funciona
Toda pilha PAM é dividida em **4 Grupos de Gerenciamento (*Management Groups*) independentes**: **(1) `auth`** — verifica *quem* é o usuário (valida senha, token hardware FIDO2, código TOTP) e concede credenciais; **(2) `account`** — verifica se a conta *pode* acessar neste momento (conta expirada? bloqueada no `faillock`? horário ou IP permitido no `access.conf`?); **(3) `password`** — gerencia a atualização e qualidade de senhas (`pam_pwquality`, `pam_unix`); e **(4) `session`** — prepara e encerra o ambiente da sessão (monta `/home`, aplica `ulimits`, registra `utmp`/`wtmp`, notifica `systemd-logind` e grava auditoria `loginuid`)!

## Exemplo
```bash
# Inspecionar a pilha de autenticacao PAM do servico SSH (/etc/pam.d/sshd) e a politica de fallback seguro (/etc/pam.d/other)
cat /etc/pam.d/other
head -n 25 /etc/pam.d/sshd
```

## Limites e trade-offs
Por que o arquivo **`/etc/pam.d/other`** sempre deve conter `auth required pam_deny.so` e `account required pam_deny.so`? Porque se um serviço novo for instalado no servidor sem seu próprio arquivo em `/etc/pam.d/<servico>`, a `libpam` aplica a política de `/etc/pam.d/other` — garantindo um comportamento **Fail-Closed (Negar por Padrão)** e registrando um alerta no syslog via `pam_warn.so`!

## Como verificar
Regra de ouro de administração Linux: **nunca edite arquivos em `/etc/pam.d/` sem manter um segundo terminal SSH com `root` logado aberto ao lado**, testando a alteração em uma terceira janela antes de fechar sua sessão de emergência!

## Conexões
- [[pam-flags-controle-required-requisite-sufficient-optional-substack]] — Veja também: Semântica das **Control Flags** do Linux-PAM (**`required`, `requisite`, `sufficient`, `optional`**) e Sintaxe Avançada `[success=done default=ignore]`.
- [[pam-protecao-forca-bruta-pam-faillock-faillock-conf-bloqueio-contas]] — Referência cruzada direta com pam-protecao-forca-bruta-pam-faillock-faillock-conf-bloqueio-contas.
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Referência cruzada direta com aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
