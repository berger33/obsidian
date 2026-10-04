---
id: software.seguranca.tranche12.001192
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

# Criptografia **Pós-Quântica Híbrida** no OpenSSH: Key Exchange **`mlkem768x25519-sha256`** e **`sntrup761x25519-sha512`**, Cifras AEAD e MACs `etm`

## Em uma frase
Adversários estatais já praticam hoje o ataque ***"Harvest Now, Decrypt Later"*** (*Coletar Agora, Descriptografar Depois*): eles gravam passivamente conexões SSH criptografadas na internet esperando o dia em que computadores quânticos consigam quebrar a troca de chaves clássica ECDH (`curve25519-sha256` ou `ecdh-sha2-nistp256`). Como o **OpenSSH** protege suas sessões contra esse risco hoje?

## Por que importa
O OpenSSH implementou e ativou **por padrão** algoritmos de **Troca de Chaves Híbrida Pós-Quântica (*Post-Quantum Hybrid Key Exchange*)**, que combinam a segurança clássica comprovada do **X25519 (`Curve25519`)** com algoritmos reticulados resistentes a computadores quânticos: **`mlkem768x25519-sha256`** (baseado no padrão **NIST FIPS 203 ML-KEM / Kyber-768**) e **`sntrup761x25519-sha512`** (*Streamlined NTRU Prime* + X25519)!

## Como funciona
Como a construção é **híbrida**, a chave de sessão derivada é no mínimo tão forte quanto o `X25519` clássico e simultaneamente resistente a ataques quânticos! Combinada com cifras AEAD (**`chacha20-poly1305@openssh.com`**, **`aes256-gcm@openssh.com`**) e MACs **Encrypt-then-MAC (`hmac-sha2-512-etm@openssh.com`)**, a camada de transporte fica blindada contra ataques de downgrade, quânticos e de padding (como o *Terrapin Attack* `CVE-2023-48795`, mitigado pelo *strict KEX* do OpenSSH 9.6+)!

## Exemplo
```ini
# Configuracao criptografica de estado-da-arte e Pos-Quantica em /etc/ssh/sshd_config.d/10-crypto-hardening.conf
KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512,curve25519-sha256,curve25519-sha256@libssh.org
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com
HostKeyAlgorithms ssh-ed25519-cert-v01@openssh.com,ssh-ed25519,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-512
```

## Limites e trade-offs
Você pode verificar na prática se a sua conexão SSH está negociando criptografia pós-quântica conectando com **`ssh -v usuario@servidor`** e procurando na linha `debug1: kex: algorithm:` por **`mlkem768x25519-sha256`** ou **`sntrup761x25519-sha512`**!

## Como verificar
Remova do `/etc/ssh/` chaves de host legadas `ssh_host_dsa_key` e `ssh_host_ecdsa_key` se sua política padronizar apenas **`ssh_host_ed25519_key`** e **`ssh_host_rsa_key` (4096 bits com `rsa-sha2-512`)**.

## Conexões
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Veja também: Arquitetura de Segurança do **OpenSSH (`openssh-portable`)**: Separação de Processos (`sshd`, `sshd-session`, `sshd-auth`) e Sandbox `seccomp` no Kernel.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Veja também: Hardening Completo do **`/etc/ssh/sshd_config`**: Desabilitando Senhas, `PermitRootLogin no`, `AuthenticationMethods`, `MaxAuthTries` e `LoginGraceTime`.
- [[wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico]] — Referência cruzada direta com wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
