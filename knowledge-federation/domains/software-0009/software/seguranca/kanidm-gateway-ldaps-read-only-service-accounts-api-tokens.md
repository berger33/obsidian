---
id: software.seguranca.tranche14.001317
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
fontes: ["https://raw.githubusercontent.com/kanidm/kanidm/master/README.md", "https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gateway **LDAPS Somente-Leitura (`:636`)** e **Service Accounts** no Kanidm: Integrando Sistemas Legados sem Expor o Diretório a Escritas LDAP

## Em uma frase
Muitas aplicações corporativas existentes (como servidores de e-mail Postfix/Dovecot, Jenkins antigo, switches de rede, firewalls ou VPNs como strongSwan/OpenVPN) ainda não suportam OIDC e precisam fazer consultas e `Bind` via protocolo **LDAP**. No entanto, expor um servidor LDAP tradicional de leitura/escrita aumenta enormemente a superfície de ataque de ACLs complexas.

## Por que importa
A solução arquitetural do Kanidm é elegante: ele embute um **Gateway LDAPS Estritamente Somente-Leitura (*Read-Only LDAPS Gateway*)** na porta `636` (`ldapbindaddress = "[::]:636"`)! Qualquer tentativa de modificação via protocolo LDAP (`LDAP Modify`, `Add`, `Delete`) é **rejeitada por design**, garantindo que 100% das mutações de identidade passem obrigatoriamente pela API validada e auditada do Kanidm!

## Como funciona
E para autenticar nos sistemas que exigem um `Bind DN` ou consumir a API do Kanidm em automações, você cria uma **Service Account (`kanidm service-account create`)** e gera um **API Token (`generate-api-token`)** ou senha de aplicação gerenciada!

## Exemplo
```bash
# Testar uma consulta segura via LDAPS (porta 636) no gateway somente-leitura do Kanidm usando um token de Service Account
ldapsearch -H ldaps://idm.exemplo.br:636 \
  -D "dn=token" -w "${KANIDM_LDAP_TOKEN}" \
  -b "dc=idm,dc=exemplo,dc=br" "(name=ana.silva)"
```

## Limites e trade-offs
Olhe que detalhe genial no comando `ldapsearch` acima (**`-D "dn=token" -w "${KANIDM_LDAP_TOKEN}"`**): no Kanidm, uma aplicação LDAP pode fazer `Bind` passando literalmente `dn=token` como Bind DN e um **Token de API de Service Account com data de expiração e escopo somente-leitura** como senha!

## Como verificar
Por padrão, buscas anônimas LDAP no Kanidm só enxergam atributos públicos mínimos; usar `dn=token` com uma Service Account dedicada permite auditar individualmente qual sistema legado está consultando o diretório e revogar o token em 1 segundo se necessário.

## Conexões
- [[kanidm-integracao-linux-pam-nss-kanidm-unixd-ssh-keys-tpm]] — Veja também: Autenticação Linux/Unix e Distribuição de Chaves SSH no Kanidm: Daemon **`kanidm_unixd`**, PAM/NSS, **Cache Offline Protegido por TPM 2.0** e **`kanidm_ssh_authorizedkeys`**.
- [[kanidm-ciclo-vida-identidades-valid-from-expire-recycle-bin-tombstones]] — Veja também: Governança de Ciclo de Vida de Contas no Kanidm: Janelas Temporais Automáticas (**`--valid-from` / `--expire`**), **Recycle Bin** e **Tombstones**.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[kanidm-configuracao-server-toml-domain-origin-zfs-backups-online]] — Referência cruzada direta com kanidm-configuracao-server-toml-domain-origin-zfs-backups-online.
- [[authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida]] — Referência cruzada direta com authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
