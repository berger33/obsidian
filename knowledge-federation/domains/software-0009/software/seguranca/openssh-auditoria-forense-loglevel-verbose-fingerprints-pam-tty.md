---
id: software.seguranca.tranche12.001199
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

# Auditoria e Forense de Acessos SSH: **`LogLevel VERBOSE`**, Rastreamento de **Fingerprints `SHA256` de Chaves e Certificados** e Timers de Inatividade (`ChannelTimeout`)

## Em uma frase
Imagine o seguinte cenário de resposta a incidentes: 15 engenheiros da sua equipe possuem suas chaves públicas listadas no arquivo `/home/ubuntu/.ssh/authorized_keys` da conta compartilhada `ubuntu`, um invasor faz login como `ubuntu` e apaga o banco de dados de produção. Quando você abre o `/var/log/auth.log` com o `LogLevel INFO` padrão de algumas distribuições antigas, você vê apenas `Accepted publickey for ubuntu from 10.x.x.x` — **sem saber qual das 15 chaves públicas foi usada**!

## Por que importa
Para garantir rastreabilidade forense individual, configure sempre **`LogLevel VERBOSE`** no `/etc/ssh/sshd_config`: com `VERBOSE`, o OpenSSH registra no `/var/log/auth.log` / `journalctl -u ssh` o **Fingerprint criptográfico exato (`SHA256:...`) da chave pública usada** e, quando **Certificados SSH** são utilizados, registra também o **ID nominal do certificado (`-I alice@corp.interno`), o número de série (`Serial`) e o fingerprint da CA emissora**!

## Como funciona
Além disso, para encerrar automaticamente sessões SSH esquecidas abertas em estações de trabalho, combine **`ClientAliveInterval 300`** + **`ClientAliveCountMax 2`** com a diretiva moderna **`ChannelTimeout session:*=15m`** (cujo funcionamento dentro de blocos `Match` foi aprimorado no **OpenSSH 10.5**) e **`UnusedConnectionTimeout`**!

## Exemplo
```bash
# Auditar nos logs do systemd/auth.log todos os logins SSH por chave publica mapeando o Fingerprint SHA256 ao comentario do authorized_keys
for fp in $(sudo journalctl -u ssh -u sshd --no-pager | grep -oE "SHA256:[a-zA-Z0-9+/=]+" | sort -u); do
  echo "=== Fingerprint usado em login: ${fp} ==="
  ssh-keygen -l -f ~/.ssh/authorized_keys 2>/dev/null | grep "${fp}" || true
done
```

## Limites e trade-offs
A diretiva **`ChannelTimeout session:shell=30m,session:exec=1h`** (introduzida no OpenSSH 9.2+) é muito superior ao antigo `TMOUT` do bash: enquanto qualquer usuário podia burlar o `TMOUT` do bash rodando `vim`, `top` ou `python3`, o `ChannelTimeout` é monitorado diretamente pelo próprio processo **`sshd-session`** medindo a inatividade real de tráfego no canal criptografado!

## Como verificar
Configure também **`RekeyLimit 1G 1h`** no `sshd_config` para forçar a renegociação automática das chaves simétricas da sessão a cada 1 GB de dados transferidos ou a cada 1 hora.

## Conexões
- [[openssh-restricoes-authorized-keys-restrict-command-sftp-chroot]] — Veja também: Confinamento Granular em **`authorized_keys` (`restrict`, `command=`, `from=`)** e **SFTP Chroot Jail (`internal-sftp` + `ChrootDirectory`)**.
- [[openssh-auditoria-automatizada-ssh-audit-testes-conformidade-cicd]] — Veja também: Auditoria Automatizada de Servidores e Clientes OpenSSH: Inspecionando Banners, Algoritmos KEX/Ciphers/MACs e Prevenindo Regressões.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.
- [[openssh-certificados-ssh-ca-user-host-certificates-principals-ttl]] — Referência cruzada direta com openssh-certificados-ssh-ca-user-host-certificates-principals-ttl.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
