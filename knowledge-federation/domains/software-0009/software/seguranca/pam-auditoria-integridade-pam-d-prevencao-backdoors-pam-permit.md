---
id: software.seguranca.tranche13.001290
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

# Caça a **Backdoors PAM** em Resposta a Incidentes (DFIR): Detectando `pam_permit.so`, `pam_exec.so` Malicioso e Modificações de Binários em `/lib/security/`

## Em uma frase
Quando um atacante pós-exploração conquista privilégio `root` em um servidor Linux e quer instalar uma **Backdoor de Persistência Furtiva** que permita entrar via SSH com **qualquer senha** (ou com uma "senha mágica" secreta) e ainda capturar em texto claro as senhas digitadas pelos administradores reais, qual é um dos alvos favoritos de grupos APT?

## Por que importa
Subverter o subsistema **Linux-PAM**! Existem **três técnicas clássicas de Backdoor PAM (`MITRE ATT&CK T1556.003 — Pluggable Authentication Modules`)**: **(1) Adulteração de Configuração em `/etc/pam.d/`** — inserir uma linha `auth sufficient pam_permit.so` no topo de `/etc/pam.d/sshd` ou `/etc/pam.d/common-auth` (que aprova qualquer senha para qualquer usuário!); **(2) Abuso de `pam_exec.so`** — adicionar `auth optional pam_exec.so expose_authtok /usr/local/bin/steal.sh` (que recebe a senha digitada pelo usuário via `stdin` e a exfiltra silenciosamente!); e **(3) Trojanização de Módulo `.so` (`/lib/x86_64-linux-gnu/security/pam_unix.so`)** — substituir o binário `pam_unix.so` por uma versão recompilada que aceita uma senha hardcoded secreta!

## Como funciona
Como um analista de **DFIR / Blue Team** detecta instantaneamente qualquer uma dessas 3 backdoors em um servidor Linux?

## Exemplo
```bash
# Auditar /etc/pam.d/ em busca de uso suspeito de pam_permit.so / pam_exec.so e verificar a integridade criptografica dos binarios .so do PAM
grep -rnE "pam_permit\.so|pam_exec\.so" /etc/pam.d/
dpkg -V libpam-modules libpam-runtime libpam0g 2>/dev/null || rpm -Va "pam*" 2>/dev/null || true
```

## Limites e trade-offs
Explicando os dois comandos de verificação acima: **(1)** No primeiro comando (`grep -rnE`), `pam_permit.so` **jamais** deve aparecer como `sufficient` na pilha `auth` de `sshd`/`login`/`sudo`, e qualquer ocorrência de `pam_exec.so` deve ser auditada imediatamente; **(2)** No segundo comando, **`dpkg -V libpam-modules`** (Debian/Ubuntu) ou **`rpm -Va "pam*"`** (RHEL/Rocky/Fedora) recalcula o hash criptográfico de todos os binários `/lib/*/security/pam_*.so` e configurações contra o banco de pacotes — denunciando com **`5` (MD5/SHA256 mismatch)** qualquer `pam_unix.so` trojanizado em menos de 1 segundo!

## Como verificar
Inclua sempre `/etc/pam.d/`, `/etc/security/` e `/usr/lib/*/security/` na regra `FIPSR` (Hash `SHA256` + `SHA512`) do seu banco de integridade do **AIDE**!

## Conexões
- [[pam-isolamento-namespaces-pam-namespace-polimorfico-tmp-var-tmp]] — Veja também: Diretórios Polimórficos por Usuário com **`pam_namespace.so` (`/etc/security/namespace.conf`)**: Isolando `/tmp` e `/var/tmp` em Servidores Multiusuário.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[pam-flags-controle-required-requisite-sufficient-optional-substack]] — Referência cruzada direta com pam-flags-controle-required-requisite-sufficient-optional-substack.
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Referência cruzada direta com aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
