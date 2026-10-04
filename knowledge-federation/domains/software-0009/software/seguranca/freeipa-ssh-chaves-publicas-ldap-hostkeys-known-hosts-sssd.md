---
id: software.seguranca.tranche14.001386
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/freeipa/freeipa/master/README.md", "https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança de **SSH Centralizada** no FreeIPA: Chaves Públicas de Usuário no LDAP (`ipaSshPubKey`), Verificação Automática de **Host Keys (`known_hosts`)** e **Kerberos GSSAPI**

## Em uma frase
Quais são os três problemas clássicos de segurança no uso tradicional de SSH em frotas Linux e como o **FreeIPA + SSSD** elimina todos os três de uma só vez? **(Problema 1)** Chaves públicas espalhadas em arquivos `~/.ssh/authorized_keys` locais que continuam lá mesmo depois que o funcionário é demitido; **(Problema 2)** Alertas *"The authenticity of host can't be established (TOFU)"* onde usuários aceitam chaves de host falsas sem conferir; e **(Problema 3)** Digitar senhas repetidamente ao pular entre servidores!

## Por que importa
Veja como o FreeIPA resolve os três: **(1) Chaves SSH de Usuário no LDAP (`--sshpubkey`)** — o `sshd_config` usa `AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys`, que busca a chave pública do usuário em tempo real no FreeIPA (se o usuário for desativado com `ipa user-disable`, o acesso SSH cai em 100% dos servidores na mesma hora!);

## Como funciona
No fluxo complementar de configuração e verificação técnica: **(2) Chaves SSH de Host verificadas pelo SSSD (`ProxyCommand /usr/bin/sss_ssh_knownhostsproxy`)** — quando um servidor ingressa no FreeIPA, sua chave pública `/etc/ssh/ssh_host_*_key.pub` é gravada no LDAP (e opcionalmente em registros DNS **`SSHFP` assinados por DNSSEC**!), de modo que o cliente SSH valida criptograficamente a identidade de todos os servidores do domínio sem perguntar `yes/no`!; e **(3) Single Sign-On via Kerberos GSSAPI (`GSSAPIAuthentication yes`)**!

## Exemplo
```bash
# Cadastrar a chave publica SSH Ed25519 de um engenheiro diretamente no perfil dele no FreeIPA e testar a recuperacao via sss_ssh_authorizedkeys
ipa user-mod ana.silva --sshpubkey="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGx... ana@estacao"
/usr/bin/sss_ssh_authorizedkeys ana.silva
```

## Limites e trade-offs
Olhe o comando de diagnóstico **`/usr/bin/sss_ssh_authorizedkeys ana.silva`** acima: se um usuário reclamar que sua chave SSH não está autenticando em um servidor membro do FreeIPA, basta executar esse comando no servidor para verificar se o SSSD está trazendo a chave pública do LDAP corretamente!

## Como verificar
E com o **Kerberos GSSAPI** ativo, depois que o administrador se autentica na sua estação de trabalho (`kinit` com senha + 2FA/Passkey), ele pode executar `ssh servidor01.exemplo.br` sem precisar nem mesmo ter uma chave privada SSH salva no disco: o `ssh` negocia um Service Ticket Kerberos `host/servidor01.exemplo.br` de curta duração diretamente com o KDC do FreeIPA!

## Conexões
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Veja também: Autenticação Multifator (**2FA / MFA**) e **Passwordless** no FreeIPA: Tokens **TOTP/HOTP (`otptoken`)**, **Passkeys FIDO2**, **Smartcards (`PKINIT`)** e **RADIUS Proxy**.
- [[freeipa-automember-grupos-dinamicos-hosts-usuarios-escalabilidade]] — Veja também: Automação Zero-Touch em Escala com **`automember` (Regras de Auto-Associação)** no FreeIPA: Classificando Servidores e Usuários Automaticamente no Ingresso.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Referência cruzada direta com freeipa-controle-acesso-hbac-host-based-access-control-regras-pam.
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Referência cruzada direta com teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
