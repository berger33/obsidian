---
id: software.seguranca.tranche13.001289
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

# Diretórios Polimórficos por Usuário com **`pam_namespace.so` (`/etc/security/namespace.conf`)**: Isolando `/tmp` e `/var/tmp` em Servidores Multiusuário

## Em uma frase
Em servidores Linux multiusuário (como servidores de compilação, clusters acadêmicos/HPC, bastiões compartilhados ou servidores de aplicação com múltiplas contas de serviço), o diretório compartilhado **`/tmp`** e **`/var/tmp`** é historicamente palco de vulnerabilidades de **Symlink Race Conditions**, **TOCTOU (*Time-of-Check to Time-of-Use*)** e espionagem de arquivos temporários entre usuários diferentes.

## Por que importa
Como o Linux-PAM permite dar a **cada usuário logado no servidor o seu próprio `/tmp` e `/var/tmp` privado e invisível para todos os outros usuários** automaticamente no momento do login?

## Como funciona
Através do módulo nativo **`session required pam_namespace.so`** configurado em **`/etc/security/namespace.conf`**! Quando um usuário inicia uma sessão, o `pam_namespace.so` cria um **Mount Namespace** exclusivo para aquela sessão e monta um **Diretório Polimórfico (*Polyinstantiated Directory*)** sobre `/tmp` e `/var/tmp` (por exemplo, mapeando `/tmp` daquele usuário para `/tmp-inst/<uid>/` com permissão `0700` ou para um `tmpfs` exclusivo em memória RAM!). Para qualquer aplicação que o usuário rodar, o caminho continua sendo `/tmp`, mas na realidade cada UID enxerga um diretório completamente isolado!

## Exemplo
```text
# Exemplo de configuracao em /etc/security/namespace.conf: cria instancias privadas de /tmp e /var/tmp por usuario (exceto root e adm)
/tmp        /tmp/tmp-inst/          level      root,adm
/var/tmp    /var/tmp/tmp-inst/      level      root,adm
```

## Limites e trade-offs
Antes de ativar o `pam_namespace.so`, crie os diretórios base de instância (`/tmp/tmp-inst` e `/var/tmp/tmp-inst`) com permissão **`0000` (`chmod 000 /tmp/tmp-inst`)** e dono `root:root`, conforme exigido pela documentação oficial do módulo para evitar acesso direto por fora do namespace.

## Como verificar
Complemente sempre essa proteção ativando no Kernel Linux as proteções nativas de links em diretórios `sticky`: **`fs.protected_symlinks = 1`**, **`fs.protected_hardlinks = 1`**, **`fs.protected_fifos = 2`** e **`fs.protected_regular = 2`** no `/etc/sysctl.d/`!

## Conexões
- [[pam-autenticacao-multifator-mfa-pam-u2f-fido2-google-authenticator-sshd]] — Veja também: Autenticação Multifator (**MFA**) no Linux-PAM para **`sshd`** e **`sudo`**: Integrando Chaves de Hardware **FIDO2 (`pam_u2f.so`)** e **TOTP (`pam_google_authenticator.so`)**.
- [[pam-auditoria-integridade-pam-d-prevencao-backdoors-pam-permit]] — Veja também: Caça a **Backdoors PAM** em Resposta a Incidentes (DFIR): Detectando `pam_permit.so`, `pam_exec.so` Malicioso e Modificações de Binários em `/lib/security/`.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Referência cruzada direta com firejail-isolamento-filesystem-private-private-dev-private-etc-bin.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
