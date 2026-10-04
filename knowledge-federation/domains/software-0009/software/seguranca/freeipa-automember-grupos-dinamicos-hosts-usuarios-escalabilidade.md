---
id: software.seguranca.tranche14.001387
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

# Automação Zero-Touch em Escala com **`automember` (Regras de Auto-Associação)** no FreeIPA: Classificando Servidores e Usuários Automaticamente no Ingresso

## Em uma frase
Imagine que o seu pipeline de Terraform / Auto-Scaling provisiona um novo servidor Linux chamado `web-prod-08.exemplo.br` e roda `ipa-client-install`. Se um administrador humano precisar entrar manualmente no FreeIPA toda vez que uma VM nova subir para adicioná-la ao `hostgroup` `web-servers` (para que ela receba as regras de **HBAC** e **`sudo`** corretas!), a automação de nuvem quebra!

## Por que importa
Como fazer com que qualquer novo servidor ou usuário recém-criado no FreeIPA seja **incluído automaticamente nos `hostgroups` ou `groups` corretos no exato milissegundo em que é registrado no LDAP**?

## Como funciona
Usando o plugin nativo **`automember`** do FreeIPA (`ipa automember-add` + `ipa automember-add-condition`)! As regras de **Auto-Membership (`automember`)** são avaliadas diretamente dentro do **389 Directory Server** durante a operação LDAP `ADD` usando expressões regulares sobre qualquer atributo do objeto (como `fqdn` para hosts ou `mail` / `title` / `departmentnumber` para usuários): por exemplo, todo host cujo `fqdn` casar com a regex **`^web-prod-[0-9]+\.exemplo\.br$`** entra instantaneamente no `hostgroup` **`web-servers`** e já herda todas as políticas HBAC e Sudo daquele grupo!

## Exemplo
```bash
# Criar uma regra automember no FreeIPA que adiciona automaticamente todo novo servidor cujo FQDN comece com 'db-prod-' ao hostgroup 'prod-db-servers'
ipa automember-add --type=hostgroup prod-db-servers
ipa automember-add-condition --type=hostgroup prod-db-servers \
  --key=fqdn --inclusive-regex="^db-prod-[0-9]+\.exemplo\.br$"
ipa automember-rebuild --type=hostgroup
```

## Limites e trade-offs
E se você criar uma nova regra `automember` hoje e quiser que ela também classifique retroativamente os 500 servidores que já estavam cadastrados no FreeIPA antes da regra existir? Basta executar o comando **`ipa automember-rebuild --type=hostgroup`** mostrado na última linha do exemplo acima!

## Como verificar
Para que o auto-ingresso de máquinas novas em Auto-Scaling seja seguro sem expor credenciais administrativas de `admin`, crie no FreeIPA uma conta de serviço ou Role restrita com a permissão específica **`System: Enroll a Host`** ou gere um OTP de host (`ipa host-add --random`).

## Conexões
- [[freeipa-ssh-chaves-publicas-ldap-hostkeys-known-hosts-sssd]] — Veja também: Segurança de **SSH Centralizada** no FreeIPA: Chaves Públicas de Usuário no LDAP (`ipaSshPubKey`), Verificação Automática de **Host Keys (`known_hosts`)** e **Kerberos GSSAPI**.
- [[freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba]] — Veja também: Integração Corporativa **FreeIPA + Microsoft Active Directory (`Cross-Forest Kerberos Trust`)**: Identidade Unificada Windows e Linux sem Duplicar Contas!.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Referência cruzada direta com freeipa-controle-acesso-hbac-host-based-access-control-regras-pam.
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Referência cruzada direta com freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
