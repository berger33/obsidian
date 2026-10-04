---
id: software.seguranca.tranche12.001194
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

# Autenticação Resistente a Phishing e Infostealers com **Chaves de Hardware FIDO2/U2F (`ed25519-sk` e `ecdsa-sk`)** no OpenSSH

## Em uma frase
Qual é o maior risco de chaves privadas SSH tradicionais (`~/.ssh/id_ed25519` ou `~/.ssh/id_rsa`) gravadas no SSD do notebook de um engenheiro? Se o notebook sofrer infecção por um malware *infostealer* (ou se um atacante roubar o backup do disco e capturar a passphrase via keylogger), o invasor copia o arquivo `~/.ssh/id_ed25519` para a máquina dele e passa a ter acesso permanente aos servidores!

## Por que importa
A partir do OpenSSH 8.2+ (com melhorias contínuas até o OpenSSH 10.5!), o OpenSSH suporta nativamente **chaves SSH baseadas em tokens de hardware FIDO2/U2F (YubiKey, SoloKey, Nitrokey)**: os tipos **`sk-ssh-ed25519@openssh.com` (`-t ed25519-sk`)** e **`sk-ecdsa-sha2-nistp256@openssh.com` (`-t ecdsa-sk`)**!

## Como funciona
Em uma chave `ed25519-sk`, **o material criptográfico da chave privada NUNCA existe no disco do computador**: o arquivo `~/.ssh/id_ed25519_sk` contém apenas um *Key Handle* opaco que só o chip seguro da sua YubiKey física consegue usar para assinar o desafio do servidor mediante **toque físico capacitivo humano (`touch-required`)** e/ou **PIN do hardware (`-O verify-required`)**! Mesmo que um invasor roube o arquivo `id_ed25519_sk` do seu notebook, o arquivo é 100% inútil sem o token físico na porta USB!

## Exemplo
```bash
# Gerar uma chave SSH FIDO2/U2F em hardware (YubiKey) exigindo toque fisico e verificacao de PIN do token (-O verify-required)
ssh-keygen -t ed25519-sk -O resident -O verify-required -O application=ssh:producao -f ~/.ssh/id_ed25519_sk_prod

# No OpenSSH 10.5+, inspecionar a ordem exata em que o cliente ssh tentara as chaves para um host (preferindo menor friccao primeiro)
ssh -Z deploy@srv-prod-01.corp.interno
```

## Limites e trade-offs
No **OpenSSH 10.5**, duas novidades excelentes aprimoraram o uso de chaves FIDO2: **(1)** O `ssh-keygen -p` agora permite definir ou limpar as flags `touch-required` e `verify-required` ao redefinir a passphrase de uma chave FIDO; e **(2)** O cliente `ssh` ganhou a flag **`ssh -Z user@host`**, que imprime a ordem exata em que as chaves serão testadas (priorizando chaves de menor fricção antes das chaves FIDO que exigem PIN/biometria)!

## Como verificar
No servidor (`/etc/ssh/sshd_config` ou `authorized_keys`), você pode exigir que o hardware FIDO tenha verificado a presença física (`no-touch-required` desabilitado por padrão) e o PIN do usuário (`verify-required`) antes de aceitar a assinatura.

## Conexões
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Veja também: Hardening Completo do **`/etc/ssh/sshd_config`**: Desabilitando Senhas, `PermitRootLogin no`, `AuthenticationMethods`, `MaxAuthTries` e `LoginGraceTime`.
- [[openssh-certificados-ssh-ca-user-host-certificates-principals-ttl]] — Veja também: Eliminando `authorized_keys` Estáticos e Alertas TOFU (`known_hosts`) com **Autoridade Certificadora SSH (`ssh-keygen -s` User & Host Certificates)**.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[openssh-seguranca-ssh-agent-destination-constraints-session-bind]] — Referência cruzada direta com openssh-seguranca-ssh-agent-destination-constraints-session-bind.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
