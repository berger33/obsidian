---
id: software.seguranca.tranche14.001383
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

# Governança Centralizada de **`sudo` (`sudorule`, `sudocmd`, `sudocmdgroup`)** no FreeIPA: Aposentando arquivos `/etc/sudoers` Locais Espalhados

## Em uma frase
Por que gerenciar permissões de `sudo` editando arquivos `/etc/sudoers` ou `/etc/sudoers.d/*` localmente em cada servidor Linux é um pesadelo de segurança e auditoria? Porque arquivos locais sofrem *Configuration Drift*, esquecem permissões temporárias concedidas meses atrás e impedem que um auditor veja em uma única tela quem tem permissão de root em qual servidor da empresa!

## Por que importa
No **FreeIPA**, toda a política de elevação de privilégios `sudo` da frota inteira reside centralizadamente no diretório LDAP e é servida em tempo real para o `sudo` de cada máquina pelo **SSSD (`sudoers: files sss` no `/etc/nsswitch.conf`)**!

## Como funciona
Você modela a política com três objetos no FreeIPA: **(1) `sudocmd`** (comandos exatos com caminho absoluto, ex.: `/usr/bin/systemctl restart nginx`), **(2) `sudocmdgroup`** (agrupamentos lógicos de comandos permitidos ou proibidos, ex.: `comandos-operacao-web`) e **(3) `sudorule`** (que vincula `User Group` + `Host Group` + `RunAsUser` + `Sudo Option` + `Allow/Deny Command Groups`)!

## Exemplo
```bash
# Criar comandos sudo permitidos, agrupa-los e aplica-los em uma sudorule restrita ao grupo 'devops-web' nos servidores 'web-servers' exigindo autenticacao (!authenticate negado)
ipa sudocmd-add "/usr/bin/systemctl restart nginx" --desc="Reiniciar Nginx"
ipa sudocmd-add "/usr/bin/journalctl -u nginx" --desc="Ler logs do Nginx"
ipa sudocmdgroup-add operacao-nginx --desc="Comandos de operacao do Nginx"
ipa sudocmdgroup-add-member operacao-nginx --sudocmds="/usr/bin/systemctl restart nginx" --sudocmds="/usr/bin/journalctl -u nginx"
ipa sudorule-add regra_sudo_devops_nginx
ipa sudorule-add-user regra_sudo_devops_nginx --groups=devops-web
ipa sudorule-add-host regra_sudo_devops_nginx --hostgroups=web-servers
ipa sudorule-add-allow-command regra_sudo_devops_nginx --sudocmdgroups=operacao-nginx
```

## Limites e trade-offs
Assim como os clientes configurados com `ipa-client-install` já vêm com o provedor `sss` habilitado para `sudoers` no `/etc/nsswitch.conf`, você pode testar imediatamente na máquina cliente quais regras `sudo` do FreeIPA estão ativas para o seu usuário rodando **`sudo -l`**!

## Como verificar
Evite adicionar a opção `!authenticate` (`NOPASSWD`) em regras `sudorule` humanas; ao manter a exigência de autenticação (integrada ao PAM/SSSD com suporte a 2FA/OTP ou Smartcard), você impede que um processo malicioso rodando na sessão do usuário eleve privilégios silenciosamente.

## Conexões
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Veja também: Controle de Acesso Baseado em Host (**HBAC — *Host-Based Access Control***) e **`hbactest`** no FreeIPA: Restringindo *Quem* Acessa *Qual Servidor* por *Qual Serviço PAM*.
- [[freeipa-pki-dogtag-certmonger-auto-renovacao-mtls-subca]] — Veja também: PKI Corporativa Integrada (**Dogtag CA & KRA**) e Renovação Automática de Certificados em Hosts Linux com **`certmonger` (`ipa-getcert`)** no FreeIPA.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Referência cruzada direta com freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
