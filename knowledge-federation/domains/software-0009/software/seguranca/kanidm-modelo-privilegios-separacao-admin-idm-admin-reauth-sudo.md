---
id: software.seguranca.tranche14.001314
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

# Modelo de Privilégio Mínimo e **Reautenticação (`re-auth` Estilo `sudo`)** no Kanidm: Por que `admin` e `idm_admin` São Estritamente Separados?

## Em uma frase
Em quase todos os sistemas de diretório antigos, existe um único superusuário onipotente (`cn=Directory Manager` ou `admin`) que pode tanto alterar configurações internas do servidor quanto resetar a senha do CEO da empresa. Por que o Kanidm rejeita esse modelo e implementa **duas segregações de segurança fundamentais**?

## Por que importa
Primeira segregação: **Separação Estrita entre Infraestrutura (`admin` / `system_admins`) e Identidades (`idm_admin` / `idm_people_admins`)**. No Kanidm, a conta `admin` gerencia configurações de sistema, esquema e topologia de replicação, mas **não tem permissão para gerenciar contas de pessoas comuns**, enquanto `idm_admin` gerencia pessoas e grupos de negócio, mas **não pode alterar configurações críticas de infraestrutura do sistema**! Além disso, você não deve usar `admin` nem `idm_admin` no dia a dia: você adiciona a conta nominal do administrador aos grupos **`idm_people_admins`**, **`idm_group_admins`** ou **`idm_service_desk`**!

## Como funciona
Segunda segregação: **Elevação de Privilégio Just-in-Time (`Re-Authentication` similar ao `sudo`)**. Mesmo que um administrador pertença ao grupo `idm_people_admins`, seu token de sessão normal opera em **modo somente leitura (não-privilegiado)**; quando ele tenta executar um comando administrativo de escrita na CLI ou WebUI, o Kanidm exige um desafio imediato de **Reautenticação com sua Passkey/MFA** que dura apenas alguns minutos!

## Exemplo
```bash
# Adicionar a conta nominal de uma engenheira ao grupo de administracao de identidades e verificar que acoes de escrita exigem reautenticacao
kanidm group add-members idm_people_admins ana.silva -D idm_admin
kanidm group list-members idm_people_admins
```

## Limites e trade-offs
Por que esse mecanismo de **Sessão Somente-Leitura por Padrão + Reautenticação Sob Demanda (`sudo` para IDM)** é uma defesa extraordinária contra roubo de sessão/cookies? Porque mesmo que um malware na estação do administrador roube o token de sessão normal do navegador ou da CLI, esse token **não tem poder de escrita administrativa** sem um novo toque físico na chave WebAuthn/YubiKey!

## Como verificar
Após configurar seus primeiros administradores nominais nos grupos `idm_*_admins`, bloqueie novamente o uso direto das contas de recuperação `admin` e `idm_admin`.

## Conexões
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Veja também: Autenticação Criptográfica no Kanidm: **Passkeys (WebAuthn)**, **Attested Passkeys (Verificação de Fabricante FIDO)** e Políticas de Credenciais por Grupo.
- [[kanidm-provedor-oauth2-oidc-pkce-strict-scope-maps-claims-custom]] — Veja também: Provedor **OAuth2 / OpenID Connect (OIDC)** no Kanidm: Obrigatoriedade de **PKCE (`S256`)**, **Scope Maps** Baseados em Grupos e **Claim Maps**.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
