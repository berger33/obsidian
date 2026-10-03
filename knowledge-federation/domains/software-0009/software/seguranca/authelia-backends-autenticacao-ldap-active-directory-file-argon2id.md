---
id: software.seguranca.tranche02.000145
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/authelia/authelia/master/README.md", "https://www.authelia.com/configuration/security/access-control/", "https://github.com/authelia/authelia"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Authelia Backends de Autenticação (`authentication_backend`): integração com `LDAP` (Active Directory / OpenLDAP / FreeIPA) e `file` (`Argon2id`)

## Em uma frase
O Authelia suporta dois provedores de diretório de usuários em `authentication_backend`: **`ldap`** (integrando-se a Microsoft Active Directory, OpenLDAP, FreeIPA ou LLDAP com pooling TLS, filtros de busca de usuários/grupos e redefinição de senha via Bind) e **`file`** (banco de dados em arquivo YAML local com senhas hasheadas em **Argon2id** ou **SHA512**).

## Por que importa
Para homelabs, ambientes de borda isolados ou equipes pequenas que não desejam manter um cluster LDAP, o backend `file` entrega autenticação completa com grupos e e-mails em um único arquivo YAML auditável.

## Como funciona
Para gerar hashes de senha seguros compatíveis com o backend `file`, utilize o comando embutido **`authelia crypto hash generate argon2`** (calibrando memória, iterações e paralelismo).

## Exemplo
```bash
# Gerando um hash Argon2id seguro para uso no arquivo users_database.yml do Authelia:
authelia crypto hash generate argon2 --password 'MinhaSenhaForteDeTeste!2026'
```

## Limites e trade-offs
Se você habilitar `watch: true` no bloco `authentication_backend.file`, o Authelia recarrega automaticamente o arquivo `users_database.yml` sempre que novos usuários ou grupos são adicionados, sem precisar reiniciar o processo.

## Como verificar
Valide o hash gerado com `authelia crypto hash validate` ou testando login no portal.

## Conexões
- [[authelia-teste-politicas-cli-access-control-check-policy-ci]] — Veja também: Authelia `authelia access-control check-policy`: validação determinística de regras de autorização na linha de comando e CI/CD.
- [[authelia-mfa-webauthn-passkeys-totp-duo-push-configuracao]] — Veja também: Authelia Segundo Fator (`2FA`): configuração de `WebAuthn` (FIDO2 / YubiKey / Passkeys), `TOTP` e notificações `Duo Push`.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
