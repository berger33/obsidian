---
id: software.seguranca.tranche14.001390
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

# Delegação Administrativa (**RBAC: `role`, `privilege`, `permission`**), **SELinux User Mapping (`selinuxusermap`)** e **Subordinate IDs (`subid`)** no FreeIPA

## Em uma frase
Como o **FreeIPA** vai além de um simples servidor LDAP ao governar recursos avançados de segurança do Kernel Linux em toda a frota, como **Confinamento de Usuários SELinux (`selinuxusermap`)** e **Rootless Containers (Podman / Docker `subuid` e `subgid` centralizados)**, além de delegar administração sem entregar a senha do `admin`?

## Por que importa
Três recursos nativos do FreeIPA brilham em ambientes Linux de alta segurança: **(1) RBAC Administrativo (`Role -> Privilege -> Permission`)** — permite que a equipe de Helpdesk resete senhas ou que o CI/CD registre hosts sem ter acesso de `admin` do diretório!;

## Como funciona
No fluxo complementar de configuração e verificação técnica: **(2) `selinuxusermap`** — quando um usuário faz login via SSH em um servidor RHEL/Fedora com SELinux ativo, o SSSD consulta as regras `selinuxusermap` do FreeIPA (que podem inclusive reutilizar regras HBAC via `--hbacrule=`) e confina a sessão daquele usuário automaticamente em um contexto SELinux restrito (`staff_u`, `user_u`, `guest_u` ou `sysadm_u`)!; e **(3) Gerenciamento Centralizado de `subid` (`ipa subid-generate`)** para **Podman Rootless**!

## Exemplo
```bash
# Mapear um grupo de usuarios no FreeIPA para o usuario confinado SELinux 'staff_u:s0-s0:c0.c1023' e alocar faixas de subuid/subgid para Podman Rootless
ipa selinuxusermap-add confinar_sre_staff --selinuxuser="staff_u:s0-s0:c0.c1023"
ipa selinuxusermap-add-user confinar_sre_staff --groups=sre-admins
ipa selinuxusermap-add-host confinar_sre_staff --hostgroups=prod-db-servers
ipa config-mod --enable-sid --add-sids
ipa subid-generate --owner=ana.silva
```

## Limites e trade-offs
Por que o suporte a **Subordinate IDs (`subid`: `subuid` e `subgid` servidos via `subid: sss` no `/etc/nsswitch.conf`)** do FreeIPA é tão importante para segurança moderna de containers com **Podman Rootless**? Porque sem o FreeIPA, você teria que manter arquivos `/etc/subuid` e `/etc/subgid` sincronizados manualmente em todos os servidores Linux para evitar colisão de UIDs de containers entre usuários de rede; com o FreeIPA, cada usuário recebe no LDAP uma faixa única de 65.536 UIDs subordinados válida em toda a frota!

## Como verificar
Combine sempre o **`selinuxusermap`** (`staff_u` para administradores que usam `sudo` e `user_u` para usuários comuns que jamais devem executar `sudo`/`su`) com as suas regras **HBAC** para alcançar defesa em profundidade no nível do Kernel Linux.

## Conexões
- [[freeipa-replicacao-multi-master-topologia-hidden-replicas-backups]] — Veja também: Alta Disponibilidade (**Multi-Master Topology**), **`Hidden Replicas`** e Backup/Restore (`ipa-backup` / `ipa-restore`) no FreeIPA.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Referência cruzada direta com freeipa-controle-acesso-hbac-host-based-access-control-regras-pam.
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Referência cruzada direta com freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
