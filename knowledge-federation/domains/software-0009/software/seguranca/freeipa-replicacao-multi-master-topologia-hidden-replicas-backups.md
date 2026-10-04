---
id: software.seguranca.tranche14.001389
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

# Alta Disponibilidade (**Multi-Master Topology**), **`Hidden Replicas`** e Backup/Restore (`ipa-backup` / `ipa-restore`) no FreeIPA

## Em uma frase
O que acontece se você tiver apenas um único servidor **FreeIPA** na sua infraestrutura e o hardware dele falhar? Como o Kerberos KDC, o LDAP, o DNS e a PKI rodam nele, novas autenticações, emissões de certificados e alterações de política ficariam indisponíveis!

## Por que importa
Para garantir **Alta Disponibilidade (HA) sem ponto único de falha**, o FreeIPA opera com **Replicação Multi-Master em Nível de Domínio 1 (`Domain Level 1` Topologia Gerenciada)**: você promove novos servidores como réplicas completas (**`ipa-replica-install --setup-ca --setup-dns`**) e gerencia os segmentos de replicação do 389-ds e da Dogtag CA (`domain` e `ca` suffixes) usando **`ipa topologysegment-find`**!

## Como funciona
Além disso, o FreeIPA suporta o conceito genial de **`Hidden Replicas` (`ipa-replica-install --hidden-replica`)**: uma réplica oculta recebe 100% da replicação LDAP/PKI em tempo real, mas **não publica seus registros SRV no DNS** para os clientes normais — ideal para usar como servidor dedicado de **Backup, Integração pesada de Keycloak/Vaultwarden/Ansible ou Disaster Recovery** sem receber tráfego de login de produção!

## Exemplo
```bash
# Verificar os segmentos da topologia de replicacao Multi-Master do FreeIPA, checar a saude com ipa-healthcheck e executar um backup completo
ipa topologysegment-find domain
ipa topologysegment-find ca
ipa-healthcheck --failures-only
ipa-backup
```

## Limites e trade-offs
Veja as duas ferramentas indispensáveis de operação e resiliência no exemplo acima: **(1) `ipa-healthcheck --failures-only`** (audita automaticamente dezenas de verificações críticas do cluster: expiração de certificados internos da Dogtag/Apache/LDAP, status de replicação CSN, permissões de arquivos, DNSSEC, Kerberos e SSSD, podendo exportar em `--output-type json` para o Prometheus/Zabbix!); e **(2) `ipa-backup`**!

## Como verificar
O utilitário **`ipa-backup`** (que salva os backups em `/var/lib/ipa/backup/`) possui dois modos: **Full Backup (`ipa-backup`)** — para brevemente os serviços (`ipactl stop`) para capturar um snapshot atômico de todos os bancos LDAP, Dogtag, Kerberos e configurações — e **Online Data-Only Backup (`ipa-backup --data --online`)**, que exporta os bancos LDIF do 389-ds a quente sem parar nenhum serviço (excelente para rodar em uma *Hidden Replica*!).

## Conexões
- [[freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba]] — Veja também: Integração Corporativa **FreeIPA + Microsoft Active Directory (`Cross-Forest Kerberos Trust`)**: Identidade Unificada Windows e Linux sem Duplicar Contas!.
- [[freeipa-rbac-delegacao-privilegios-selinux-usermap-subids-containers]] — Veja também: Delegação Administrativa (**RBAC: `role`, `privilege`, `permission`**), **SELinux User Mapping (`selinuxusermap`)** e **Subordinate IDs (`subid`)** no FreeIPA.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[vaultwarden-backups-consistentes-sqlite3-online-backup-rsa-keys-anexos]] — Referência cruzada direta com vaultwarden-backups-consistentes-sqlite3-online-backup-rsa-keys-anexos.
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Referência cruzada direta com kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
