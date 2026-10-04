---
id: software.seguranca.tranche12.001197
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

# Arquitetura de **Bastion Host (Jump Host)** com **`ProxyJump` (`-J`)** e Blindagem do Bastion com `AllowTcpForwarding local`, `PermitOpen` e `ForceCommand`

## Em uma frase
Como projetar um servidor **SSH Bastion (Jump Host)** moderno onde os engenheiros o utilizam apenas como salto criptografado (`ssh -J user@bastion.corp.interno user@srv-interno`) para alcançar servidores em sub-redes privadas, **sem que ninguém consiga abrir um shell interativo no próprio Bastion nem criar túneis reversos (`-R`) ou proxies SOCKS arbitrários**?

## Por que importa
No cliente (`~/.ssh/config`), a diretiva **`ProxyJump bastion.corp.interno`** (ou flag `-J`) instrui o cliente SSH local a abrir uma conexão SSH com o bastion, solicitar apenas um canal `direct-tcpip` (`stdio forwarding -W %h:%p`) até a porta `22` do servidor interno e, por dentro desse canal TCP, estabelecer **um segundo túnel SSH criptografado de ponta a ponta** entre o seu notebook e o servidor interno!

## Como funciona
No servidor Bastion (`/etc/ssh/sshd_config`), você tranca completamente a superfície das contas de salto usando um bloco **`Match Group jump-users`**: desativa a alocação de terminal (**`PermitTTY no`**), força **`ForceCommand /bin/false`** (impedindo execução de qualquer comando ou shell no bastion!), permite apenas encaminhamento TCP de saída (**`AllowTcpForwarding local`**) e restringe os destinos e portas permitidos com **`PermitOpen *:22`**!

## Exemplo
```ini
# Configuracao de um Bastion Host puro (apenas salto ProxyJump para a porta 22 interna, sem shell local) em /etc/ssh/sshd_config
Match Group jump-users
    PermitTTY no
    X11Forwarding no
    AllowAgentForwarding no
    PermitTunnel no
    GatewayPorts no
    AllowTcpForwarding local
    PermitOpen 10.20.0.0/16:22
    ForceCommand /bin/false
```

## Limites e trade-offs
Com esse bloco **`Match Group jump-users`** ativo no Bastion, se um usuário tentar rodar `ssh user@bastion.corp.interno` para abrir um shell no bastion, a conexão é encerrada imediatamente pelo `ForceCommand /bin/false`; se tentar fazer um túnel para a porta `5432` do banco de dados (`ssh -L 5432:db:5432`), o `PermitOpen 10.20.0.0/16:22` bloqueia; mas quando ele executa **`ssh -J user@bastion.corp.interno user@10.20.1.50`**, o salto para a porta `22` funciona com perfeição e transparência!

## Como verificar
No **OpenSSH 10.5**, um bug em que a keyword `restrict` do `authorized_keys` não se aplicava ao `tunnel forwarding` (`PermitTunnel`) também foi corrigido, reforçando o isolamento de túneis.

## Conexões
- [[openssh-seguranca-ssh-agent-destination-constraints-session-bind]] — Veja também: Segurança do **`ssh-agent`**: O Perigo do **`ForwardAgent yes`**, Restrições de Destino (**`ssh-add -h` + `session-bind@openssh.com`**) e Isolamento.
- [[openssh-restricoes-authorized-keys-restrict-command-sftp-chroot]] — Veja também: Confinamento Granular em **`authorized_keys` (`restrict`, `command=`, `from=`)** e **SFTP Chroot Jail (`internal-sftp` + `ChrootDirectory`)**.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
