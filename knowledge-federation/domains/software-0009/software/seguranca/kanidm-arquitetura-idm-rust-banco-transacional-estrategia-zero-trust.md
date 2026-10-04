---
id: software.seguranca.tranche14.001311
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

# Arquitetura do **Kanidm (`kanidm/kanidm`)**: Plataforma Completa de Gerenciamento de Identidade (IDM) em **Rust** com Banco Transacional Próprio e Padrões Estritos

## Em uma frase
Por que o projeto **Kanidm** (escrito 100% em **Rust** por engenheiros veteranos do servidor de diretório corporativo *389 Directory Server* / Red Hat Directory Server) vem conquistando equipes de infraestrutura e segurança que buscam substituir combinações complexas de OpenLDAP + Keycloak + FreeIPA por um único sistema moderno e *memory-safe*?

## Por que importa
Diferente de soluções que exigem empilhar 4 ou 5 softwares distintos (um servidor LDAP + um banco PostgreSQL + um servidor OIDC + um portal self-service + um gerenciador de chaves SSH), o **Kanidm (`kanidmd`)** entrega **tudo integrado em um único daemon em Rust**: **(1) Provedor OAuth2 / OpenID Connect (OIDC)** completo;

## Como funciona
Na camada complementar de implementação e execução técnica: **(2) Autenticação nativa por Passkeys / WebAuthn (com Attestation FIDO MDS!)**; **(3) Gateway LDAPS Read-Only** para sistemas legados; **(4) Distribuição de chaves públicas SSH e autenticação PAM/NSS offline com TPM 2.0 (`kanidm_unixd`)**; **(5) RADIUS**; e **(6) Seu próprio motor de banco de dados transacional (`kanidm.db`) com cache ARC (*Adaptive Replacement Cache*) em memória e replicação multi-nó integrada**!

## Exemplo
```bash
# Verificar a versao do servidor kanidmd, validar a configuracao /etc/kanidm/server.toml e checar a saude da instancia via CLI
kanidmd version
kanidmd configtest -c /etc/kanidm/server.toml
kanidm system status -H https://idm.exemplo.br
```

## Limites e trade-offs
Em benchmarks de diretório com milhares de usuários e grupos, o motor de banco de dados transacional nativo do Kanidm (com índices em memória e *Copy-on-Write* otimizado para blocos de 4 KB ou 64 KB em ZFS) realiza buscas ~3x mais rápidas e modificações ~5x mais rápidas que pilhas tradicionais baseadas em LDAP/SQL externos!

## Como verificar
Além disso, o Kanidm segue a filosofia **"Strict Defaults by Design"**: TLS é obrigatório desde o boot (`tls_chain` e `tls_key` em `server.toml`), políticas de privilégio mínimo vêm ativas de fábrica e contas administrativas padrão (`admin` e `idm_admin`) vêm bloqueadas até serem explicitamente recuperadas via console local!

## Conexões
- [[kanidm-configuracao-server-toml-domain-origin-zfs-backups-online]] — Veja também: Configuração Segura do **`server.toml`** no Kanidm: Consistência Estrita **`domain` / `origin` (WebAuthn)**, `http_client_address_info` (`proxy-v2`) e `[online_backup]`.
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Referência cruzada direta com kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
