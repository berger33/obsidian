---
id: software.seguranca.tranche14.001388
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

# Integração Corporativa **FreeIPA + Microsoft Active Directory (`Cross-Forest Kerberos Trust`)**: Identidade Unificada Windows e Linux sem Duplicar Contas!

## Em uma frase
Em quase toda grande empresa, as estações de trabalho corporativas e o e-mail já vivem em uma floresta **Microsoft Active Directory (`corp.empresa.br`)**, enquanto a infraestrutura de datacenters, nuvem e containers roda em **Linux**. Como permitir que os usuários do Active Directory façam login nos servidores Linux usando suas credenciais do AD, mas mantendo a governança de **HBAC, Sudo, Chaves SSH, Automount e SELinux User Mapping** 100% controlada pela equipe de Linux dentro do **FreeIPA (`linux.empresa.br`)**?

## Por que importa
Estabelecendo um **Cross-Forest Trust (`ipa trust-add`) entre o FreeIPA e o Active Directory**!

## Como funciona
Após preparar o servidor FreeIPA com **`ipa-adtrust-install`** (que configura os módulos Samba/LSA RPC e Kerberos cross-realm), você cria uma relação de confiança entre a floresta do AD e o domínio DNS separado do FreeIPA: **(1)** Os usuários continuam existindo **apenas no Active Directory** (sem sincronizar nem copiar hashes de senha!); **(2)** Você mapeia grupos do AD para **Grupos Externos (`--external`)** encapsulados em grupos POSIX do FreeIPA; **(3)** O SSSD resolve automaticamente os SIDs do Windows para UIDs/GIDs Linux determinísticos (**ID Ranges**) ou aplica sobrescritas via **`ID Views`**; e **(4)** Todas as regras de **HBAC e Sudo do FreeIPA** funcionam transparentemente para os usuários do AD!

## Exemplo
```bash
# Instalar o suporte a AD Trust no FreeIPA, estabelecer a confianca com a floresta Active Directory e mapear um grupo do AD para um grupo POSIX
ipa-adtrust-install --add-sids
ipa trust-add corp.empresa.br --type=ad --admin=Administrator --password
ipa group-add sre-ad-externo --desc="Grupo externo mapeado do AD" --external
ipa group-add sre-linux --desc="Grupo POSIX interno do FreeIPA"
ipa group-add-member sre-ad-externo --external="CORP\\SRE-Admins"
ipa group-add-member sre-linux --groups=sre-ad-externo
```

## Limites e trade-offs
Preste muita atenção ao padrão arquitetural de **Duplo Grupo (`External Group` -> `POSIX Group`)** mostrado nas 4 últimas linhas acima: como objetos do Active Directory não residem na árvore LDAP do FreeIPA, as regras HBAC e Sudo exigem grupos POSIX nativos do FreeIPA; por isso, você coloca o grupo do AD (`CORP\SRE-Admins`) dentro de um grupo `--external` (`sre-ad-externo`) e torna esse grupo externo membro do grupo POSIX (`sre-linux`)!

## Como verificar
Requisito técnico fundamental do **Cross-Forest Trust**: o domínio DNS do FreeIPA (ex.: `linux.empresa.br`) e o domínio DNS do Active Directory (ex.: `corp.empresa.br`) **DEVEM ter nomes DNS e NetBIOS distintos** e encaminhamento DNS condicional (Conditional Forwarders) configurado entre ambos!

## Conexões
- [[freeipa-automember-grupos-dinamicos-hosts-usuarios-escalabilidade]] — Veja também: Automação Zero-Touch em Escala com **`automember` (Regras de Auto-Associação)** no FreeIPA: Classificando Servidores e Usuários Automaticamente no Ingresso.
- [[freeipa-replicacao-multi-master-topologia-hidden-replicas-backups]] — Veja também: Alta Disponibilidade (**Multi-Master Topology**), **`Hidden Replicas`** e Backup/Restore (`ipa-backup` / `ipa-restore`) no FreeIPA.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Referência cruzada direta com freeipa-controle-acesso-hbac-host-based-access-control-regras-pam.
- [[teleport-federacao-trusted-clusters-leaf-root-isolamento-multi-tenant]] — Referência cruzada direta com teleport-federacao-trusted-clusters-leaf-root-isolamento-multi-tenant.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
