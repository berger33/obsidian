---
id: software.seguranca.tranche14.001381
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

# Arquitetura do **FreeIPA (`freeipa/freeipa` / Red Hat Identity Management)**: Identidade, Política e Auditoria Integrada para Linux (**389-ds LDAP, MIT Kerberos KDC, Dogtag PKI e BIND DNS**)

## Em uma frase
Se o **Active Directory** é o domínio integrado clássico para estações e servidores Windows, qual é a plataforma open-source padrão mundial de **Gerenciamento Centralizado de Identidade, Política e Auditoria (`IPA`) para Frotas Linux e UNIX** (e base direta do **Red Hat Identity Management — IdM** no RHEL, Fedora, AlmaLinux, Rocky Linux, Debian e Ubuntu)?

## Por que importa
É o **FreeIPA (`freeipa/freeipa`)**!

## Como funciona
Em vez de obrigar o administrador a configurar e integrar manualmente meia dúzia de daemons separados, o comando **`ipa-server-install`** orquestra uma arquitetura coesa composta por **5 pilares de código aberto**: **(1) `389 Directory Server` (`389-ds`)** — o diretório LDAPv3 multi-master de altíssima performance que armazena usuários, hosts, grupos e políticas; **(2) `MIT Kerberos KDC`** — autenticação Single Sign-On criptográfica baseada em tickets (`krb5`) integrada ao esquema LDAP; **(3) `Dogtag PKI`** — Autoridade Certificadora (CA e KRA) X.509 corporativa integrada; **(4) `BIND DNS` com `bind-dyndb-ldap`** — DNS dinâmico armazenado no LDAP com suporte a DNSSEC; e **(5) Framework de Gerenciamento `ipa` (CLI JSON-RPC/XML-RPC e Web UI)**!

## Exemplo
```bash
# Autenticar via Kerberos como administrador do dominio FreeIPA, verificar o status de todos os servicos integrados e consultar os servidores
kinit admin
ipactl status
ipa env
ipa server-find
```

## Limites e trade-offs
Veja no comando acima como toda a administração do FreeIPA é protegida por **Tickets Kerberos (`kinit admin`)**: você não passa senhas em linha de comando nem edita arquivos LDIF complexos na mão; a CLI **`ipa`** envia chamadas autenticadas por **GSSAPI/Kerberos sobre HTTPS** para o Apache (`mod_wsgi` + `mod_auth_gssapi`) do servidor FreeIPA!

## Como verificar
No cliente Linux (RHEL, Fedora, Ubuntu, Debian), basta executar um único comando (**`ipa-client-install --mkhomedir`**) para ingressar a máquina no domínio FreeIPA: ele configura automaticamente o **SSSD**, o `/etc/krb5.conf`, o `/etc/nsswitch.conf`, o PAM, o SSH (chaves públicas de host e usuário no LDAP!) e o certificado X.509 da máquina!

## Conexões
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Veja também: Controle de Acesso Baseado em Host (**HBAC — *Host-Based Access Control***) e **`hbactest`** no FreeIPA: Restringindo *Quem* Acessa *Qual Servidor* por *Qual Serviço PAM*.
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Referência cruzada direta com freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
