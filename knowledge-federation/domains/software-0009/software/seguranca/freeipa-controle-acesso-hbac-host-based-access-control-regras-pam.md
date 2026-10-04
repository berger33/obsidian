---
id: software.seguranca.tranche14.001382
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

# Controle de Acesso Baseado em Host (**HBAC — *Host-Based Access Control***) e **`hbactest`** no FreeIPA: Restringindo *Quem* Acessa *Qual Servidor* por *Qual Serviço PAM*

## Em uma frase
O que acontece por padrão após você instalar um domínio **FreeIPA** se não desativar a regra inicial de boas-vindas? O FreeIPA vem com uma regra HBAC inicial chamada **`allow_all`** habilitada para facilitar os primeiros testes — que permite que qualquer usuário autenticado no domínio faça login em qualquer máquina via qualquer serviço PAM!

## Por que importa
Em produção, o primeiro passo de **Hardening Zero-Trust no FreeIPA** é: **(1) Criar regras granulares de `HBAC` (*Host-Based Access Control*)** que cruzam **Grupo de Usuários (`User Group`) + Grupo de Servidores (`Host Group`) + Serviço PAM (`Service`: `sshd`, `sudo`, `cockpit`, `login`, `su`)**,

## Como funciona
No fluxo complementar de configuração e verificação técnica: **(2) Simular e validar todas as regras com o simulador integrado `ipa hbactest`** e **(3) Desabilitar imediatamente a regra `allow_all` (`ipa hbacrule-disable allow_all`)**!

## Exemplo
```bash
# Criar uma regra HBAC permitindo que apenas o grupo 'sre-admins' acesse o grupo de servidores 'prod-db-servers' via 'sshd' e 'sudo', testar com hbactest e desativar allow_all
ipa hbacrule-add permitir_sre_prod_db --desc="Acesso SSH e Sudo para SRE nos bancos de producao"
ipa hbacrule-add-user permitir_sre_prod_db --groups=sre-admins
ipa hbacrule-add-host permitir_sre_prod_db --hostgroups=prod-db-servers
ipa hbacrule-add-service permitir_sre_prod_db --hbacsvcs=sshd --hbacsvcs=sudo
ipa hbactest --user=ana.silva --host=db01.exemplo.br --service=sshd
ipa hbacrule-disable allow_all
```

## Limites e trade-offs
Nunca desative a regra `allow_all` no escuro sem antes rodar **`ipa hbactest --user=<admin> --host=<servidor> --service=sshd`**! O comando `ipa hbactest` avalia exatamente a mesma lógica que o demônio **SSSD (`pam_sss`)** executará no servidor de destino e mostra na tela **`Access granted: True/False`** junto com a lista exata de regras (`Matched rules` / `Not matched rules`)!

## Como verificar
Como as regras HBAC são baixadas e avaliadas pelo **SSSD** em cada servidor Linux a partir do diretório LDAP (com suporte a cache seguro), o controle de acesso funciona de forma instantânea e consistente em milhares de máquinas sem precisar editar `/etc/security/access.conf` ou `AllowGroups` no `sshd_config` local!

## Conexões
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Veja também: Arquitetura do **FreeIPA (`freeipa/freeipa` / Red Hat Identity Management)**: Identidade, Política e Auditoria Integrada para Linux (**389-ds LDAP, MIT Kerberos KDC, Dogtag PKI e BIND DNS**).
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Veja também: Governança Centralizada de **`sudo` (`sudorule`, `sudocmd`, `sudocmdgroup`)** no FreeIPA: Aposentando arquivos `/etc/sudoers` Locais Espalhados.
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Referência cruzada direta com teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
