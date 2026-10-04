---
id: software.seguranca.tranche12.001193
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/openssh/openssh-portable/master/README", "https://www.openssh.com/releasenotes.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Hardening Completo do **`/etc/ssh/sshd_config`**: Desabilitando Senhas, `PermitRootLogin no`, `AuthenticationMethods`, `MaxAuthTries` e `LoginGraceTime`

## Em uma frase
Quais são as diretivas obrigatórias no **`/etc/ssh/sshd_config`** (ou em `/etc/ssh/sshd_config.d/00-hardening.conf`) para transformar uma instalação padrão do OpenSSH em um serviço compatível com **CIS Benchmark Level 2** e resistente a força bruta, enumeração e exaustão de conexões pré-autenticação?

## Por que importa
Na camada de autenticação: defina **`PermitRootLogin no`** (proibindo login direto como `root`), **`PasswordAuthentication no`** e **`KbdInteractiveAuthentication no`** (eliminando 100% da superfície de força bruta de senhas), **`PermitEmptyPasswords no`**, **`PubkeyAuthentication yes`** e restrinja explicitamente quem pode fazer login com **`AllowGroups ssh-admins`**!

## Como funciona
Na camada de proteção contra abuso de conexões pré-autenticação (mitigando ataques de esgotamento de slots e *race conditions* na fase pré-auth): reduza **`LoginGraceTime 20s`** (padrão é 120s!), reduza **`MaxAuthTries 3`**, ajuste **`MaxStartups 10:30:100`**, configure **`PerSourceMaxStartups 3`** (que impede que um único endereço IP de atacante consuma todos os slots de pré-autenticação dos demais usuários!) e ative **`PerSourcePenalties yes`**!

## Exemplo
```ini
# Hardening defensivo de producao em /etc/ssh/sshd_config.d/20-access-hardening.conf
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitEmptyPasswords no
LoginGraceTime 20
MaxAuthTries 3
MaxSessions 4
PerSourceMaxStartups 3
PerSourcePenalties yes
X11Forwarding no
AllowAgentForwarding no
AllowTcpForwarding no
AllowGroups ssh-admins
```

## Limites e trade-offs
A diretiva **`PerSourcePenalties yes`** (introduzida no OpenSSH 9.8+) é um mecanismo nativo de autodefesa do próprio `sshd`: se um endereço IP causar um crash em um processo filho, falhar repetidamente na autenticação ou exceder o `LoginGraceTime`, o próprio `sshd` bloqueia temporariamente aquele IP em memória sem nem precisar do Fail2ban!

## Como verificar
Sempre valide qualquer alteração com **`sudo sshd -t`** (que retorna código `0` se não houver erros de sintaxe) antes de executar `sudo systemctl reload ssh`.

## Conexões
- [[openssh-criptografia-pos-quantica-kex-mlkem768-sntrup761-chacha20]] — Veja também: Criptografia **Pós-Quântica Híbrida** no OpenSSH: Key Exchange **`mlkem768x25519-sha256`** e **`sntrup761x25519-sha512`**, Cifras AEAD e MACs `etm`.
- [[openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch]] — Veja também: Autenticação Resistente a Phishing e Infostealers com **Chaves de Hardware FIDO2/U2F (`ed25519-sk` e `ecdsa-sk`)** no OpenSSH.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh]] — Referência cruzada direta com nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
