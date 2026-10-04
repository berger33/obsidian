---
id: software.seguranca.tranche12.001200
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

# Auditoria Automatizada de Servidores e Clientes OpenSSH: Inspecionando Banners, Algoritmos KEX/Ciphers/MACs e Prevenindo Regressões

## Em uma frase
Depois de aplicar o hardening completo do OpenSSH (criptografia pós-quântica `mlkem768x25519-sha256` / `sntrup761x25519-sha512`, certificados SSH, chaves FIDO2 `ed25519-sk`, `PerSourcePenalties` e `seccomp`), como auditar continuamente toda a sua frota de servidores Linux para garantir que nenhum servidor novo subiu com algoritmos legados fracos (`diffie-hellman-group14-sha1`, `ssh-rsa` SHA-1, cifras `cbc`) ou `PasswordAuthentication yes`?

## Por que importa
Você combina duas verificações automatizadas: **(1) Auditoria local de configuração (`sshd -T`)** executada via Ansible/OSQuery/CI sobre o arquivo de configuração antes e depois do deploy; e **(2) Auditoria de protocolo na rede** usando o próprio cliente OpenSSH (`ssh -Q`, `ssh -G`, `ssh -vvv -o BatchMode=yes`) ou ferramentas de auditoria de handshake SSH (como `ssh-audit` ou templates `nuclei` para SSH)!

## Como funciona
Como o handshake de negociação de algoritmos do protocolo SSH (`SSH_MSG_KEXINIT`) ocorre em texto claro logo após a troca de banners (`SSH-2.0-OpenSSH_...`), você pode inspecionar remotamente a lista exata de `KexAlgorithms`, `ServerHostKeyAlgorithms`, `Ciphers` e `MACs` oferecidos por qualquer servidor sem precisar de credenciais de login!

## Exemplo
```bash
# Auditar localmente os algoritmos suportados pela instalacao do OpenSSH (ssh -Q) e verificar a configuracao efetiva compilada do sshd (-T)
ssh -Q kex | grep -E "(mlkem|sntrup|curve25519)"
ssh -Q key-sig | grep -E "(sk-|cert-v01|ed25519)"
sudo sshd -T | grep -E "^(kexalgorithms|ciphers|macs|hostkeyalgorithms|passwordauthentication|permitrootlogin|loglevel)"
```

## Limites e trade-offs
Adicione um step no seu playbook **Ansible** (ou imagem Packer/Golden AMI) que executa `sudo sshd -t` e valida com `sudo sshd -T` que `passwordauthentication no`, `permitrootlogin no` e `kexalgorithms` pós-quânticos estão presentes antes de liberar o servidor para produção!

## Como verificar
Monitore também com o **AIDE** os arquivos `/etc/ssh/sshd_config`, `/etc/ssh/sshd_config.d/*`, `/etc/ssh/user_ca.pub` e `/usr/sbin/sshd` para detectar qualquer tentativa de enfraquecimento da configuração (*configuration drift*) pós-deploy.

## Conexões
- [[openssh-auditoria-forense-loglevel-verbose-fingerprints-pam-tty]] — Veja também: Auditoria e Forense de Acessos SSH: **`LogLevel VERBOSE`**, Rastreamento de **Fingerprints `SHA256` de Chaves e Certificados** e Timers de Inatividade (`ChannelTimeout`).
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[openssh-criptografia-pos-quantica-kex-mlkem768-sntrup761-chacha20]] — Referência cruzada direta com openssh-criptografia-pos-quantica-kex-mlkem768-sntrup761-chacha20.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
