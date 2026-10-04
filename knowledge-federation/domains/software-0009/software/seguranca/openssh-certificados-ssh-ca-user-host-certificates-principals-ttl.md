---
id: software.seguranca.tranche12.001195
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

# Eliminando `authorized_keys` Estáticos e Alertas TOFU (`known_hosts`) com **Autoridade Certificadora SSH (`ssh-keygen -s` User & Host Certificates)**

## Em uma frase
Gerenciar arquivos `~/.ssh/authorized_keys` espalhados em 500 servidores Linux é um pesadelo operacional e de segurança: chaves antigas nunca são removidas, não têm data de expiração e, quando um servidor é recriado, os engenheiros recebem o temido alerta `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!` e acabam criando o hábito perigoso de apagar o `known_hosts` sem verificar!

## Por que importa
O OpenSSH possui um sistema nativo, leve e muito mais simples que o X.509 de **Certificados SSH (`ssh-ed25519-cert-v01@openssh.com`)** para **Host Certificates** e **User Certificates**!

## Como funciona
Na arquitetura de **SSH CA**: **(1) Para Host Certificates**, a sua CA de Hosts assina a chave pública de cada novo servidor (`ssh-keygen -s host_ca -I srv01 -h -n srv01.corp.interno -V +52w ssh_host_ed25519_key.pub`) e você coloca uma única linha **`@cert-authority *.corp.interno <PUBKEY_HOST_CA>`** no `~/.ssh/known_hosts` dos engenheiros — eliminando 100% dos alertas TOFU para qualquer servidor legítimo!; e **(2) Para User Certificates**, os servidores confiam na chave pública da User CA (**`TrustedUserCAKeys /etc/ssh/user_ca.pub`** no `sshd_config`, com zero chaves em `~/.ssh/authorized_keys`!), e o engenheiro recebe pela manhã (via Vault, Step-CA ou Teleport) um **certificado SSH efêmero válido por apenas 8 horas (`-V +8h`)** restrito aos seus `principals`!

## Exemplo
```bash
# Emitir um User Certificate SSH efemero com validade de apenas 8 horas (-V +8h) restrito ao principal 'sre-oncall' e inspeciona-lo
ssh-keygen -s ./ca_usuarios_ed25519 \
  -I "alice@corp.interno-turno-2026-10-03" \
  -n sre-oncall,deploy \
  -V +8h \
  -O clear -O permit-pty \
  ./id_ed25519_alice.pub

ssh-keygen -L -f ./id_ed25519_alice-cert.pub
```

## Limites e trade-offs
Observe as flags **`-O clear -O permit-pty`** na emissão do certificado acima: `-O clear` desabilita por padrão todas as permissões de encaminhamento (port forwarding, agent forwarding, X11, user-rc) dentro do próprio certificado criptográfico, habilitando exclusivamente a alocação de terminal interativo (`permit-pty`)!

## Como verificar
Mesmo com certificados de curta duração (`+8h`), configure sempre **`RevokedKeys /etc/ssh/revoked_keys`** (gerado em formato binário KRL — *Key Revocation List* — via `ssh-keygen -k`) no `sshd_config` para revogação emergencial imediata.

## Conexões
- [[openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch]] — Veja também: Autenticação Resistente a Phishing e Infostealers com **Chaves de Hardware FIDO2/U2F (`ed25519-sk` e `ecdsa-sk`)** no OpenSSH.
- [[openssh-seguranca-ssh-agent-destination-constraints-session-bind]] — Veja também: Segurança do **`ssh-agent`**: O Perigo do **`ForwardAgent yes`**, Restrições de Destino (**`ssh-add -h` + `session-bind@openssh.com`**) e Isolamento.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[wireguard-governanca-zero-trust-automacao-malha-headscale-tailscale]] — Referência cruzada direta com wireguard-governanca-zero-trust-automacao-malha-headscale-tailscale.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
