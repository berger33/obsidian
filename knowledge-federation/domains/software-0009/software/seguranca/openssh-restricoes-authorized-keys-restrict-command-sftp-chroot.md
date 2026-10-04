---
id: software.seguranca.tranche12.001198
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

# Confinamento Granular em **`authorized_keys` (`restrict`, `command=`, `from=`)** e **SFTP Chroot Jail (`internal-sftp` + `ChrootDirectory`)**

## Em uma frase
Quando uma pipeline de CI/CD, um servidor de backup (`rsync`/`borgbackup`) ou um parceiro externo precisa se conectar via SSH a um servidor seu para executar **um único comando específico** ou **transferir arquivos via SFTP em uma única pasta**, dar a essa chave SSH acesso a um shell `/bin/bash` completo viola frontalmente o Princípio do Menor Privilégio!

## Por que importa
O OpenSSH oferece dois mecanismos nativos de confinamento cirúrgico: **(1) Opções de restrição no `~/.ssh/authorized_keys`** — iniciando a linha da chave pública com a palavra-chave **`restrict`** (que desativa de uma só vez port forwarding, agent forwarding, X11, PTY e user-rc!), seguida de **`from="10.10.50.12/32"`** (restringindo o IP de origem da chave) e **`command="/usr/local/bin/backup-wrapper.sh"`** (que ignora qualquer comando enviado pelo cliente e executa exclusivamente aquele script!); e **(2) Jaula SFTP (`ChrootDirectory` + `ForceCommand internal-sftp`)** no `sshd_config`!

## Como funciona
Com **`ForceCommand internal-sftp`** e **`ChrootDirectory /sftp/%u`**, o processo do usuário é confinado via syscall `chroot(2)` dentro do seu diretório antes mesmo de ler qualquer arquivo, utilizando o servidor SFTP embutido no próprio código do `sshd-session` (sem precisar copiar `/bin/sh` ou bibliotecas `/lib` para dentro da jaula)!

## Exemplo
```ini
# 1) Exemplo de linha blindada em ~/.ssh/authorized_keys usando 'restrict', filtro de IP 'from=' e comando fixo 'command='
# restrict,from="10.50.10.20/32",command="/usr/local/bin/roda-backup-apenas.sh" ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... svc-backup

# 2) Exemplo de SFTP Chroot Jail seguro em /etc/ssh/sshd_config para usuarios do grupo 'sftp-parceiros'
Match Group sftp-parceiros
    ChrootDirectory /srv/sftp/%u
    ForceCommand internal-sftp -u 0077 -l INFO
    AllowTcpForwarding no
    X11Forwarding no
    PermitTunnel no
```

## Limites e trade-offs
Atenção ao requisito obrigatório de segurança do OpenSSH para **`ChrootDirectory /srv/sftp/%u`**: o diretório raiz do chroot (`/srv/sftp/parceiro1`) e todos os seus diretórios pais **DEVEM pertencer a `root:root` e não podem ter permissão de escrita para grupo ou outros (`chmod 755`)**; crie um subdiretorio interno (ex.: `/srv/sftp/parceiro1/upload` pertencente a `parceiro1`) onde o usuário possa gravar seus arquivos!

## Como verificar
Ao escrever um script acionado por `command="..."` no `authorized_keys`, se você precisar inspecionar qual argumento o cliente solicitou originalmente (`SSH_ORIGINAL_COMMAND`), valide-o contra uma *allowlist* estrita sem jamais passá-lo para `eval` ou `sh -c`!

## Conexões
- [[openssh-tunelamento-seguro-proxyjump-bastion-restricao-forwarding]] — Veja também: Arquitetura de **Bastion Host (Jump Host)** com **`ProxyJump` (`-J`)** e Blindagem do Bastion com `AllowTcpForwarding local`, `PermitOpen` e `ForceCommand`.
- [[openssh-auditoria-forense-loglevel-verbose-fingerprints-pam-tty]] — Veja também: Auditoria e Forense de Acessos SSH: **`LogLevel VERBOSE`**, Rastreamento de **Fingerprints `SHA256` de Chaves e Certificados** e Timers de Inatividade (`ChannelTimeout`).
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
