---
id: software.seguranca.tranche02.000146
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

# Authelia Segundo Fator (`2FA`): configuração de `WebAuthn` (FIDO2 / YubiKey / Passkeys), `TOTP` e notificações `Duo Push`

## Em uma frase
O Authelia oferece três métodos nativos de segundo fator para satisfazer políticas `two_factor`: **WebAuthn (FIDO2)** (chaves de segurança de hardware resistentes a phishing, como YubiKey, e autenticadores de plataforma), **TOTP (`RFC 6238`)** (com configuração de `issuer`, `algorithm: SHA1/SHA256/SHA512`, `digits: 6/8` e `period: 30`) e **Duo Push** (notificações push via Duo Auth API).

## Por que importa
Ataques modernos de phishing com proxy reverso em tempo real (*Adversary-in-the-Middle — AitM*, como Evilginx) conseguem capturar códigos TOTP digitados pelo usuário, mas **são neutralizados pelo WebAuthn**, pois o navegador vincula criptograficamente a assinatura FIDO2 ao domínio real (`rp_id`).

## Como funciona
No `configuration.yml`, você pode habilitar `webauthn` e `totp` simultaneamente ou restringir dispositivos de alta segurança desativando métodos menos resistentes conforme a política da organização.

## Exemplo
```yaml
totp:
  disable: false
  issuer: 'AutheliaCorp'
  algorithm: 'SHA1'
  digits: 6
  period: 30
  skew: 1

webauthn:
  disable: false
  display_name: 'Authelia SSO'
  attestation_conveyance_preference: 'indirect'
  timeout: '60s'
```

## Limites e trade-offs
Ao configurar cookies de sessão e WebAuthn para múltiplos subdomínios (`app1.example.com`, `app2.example.com`), defina o `domain` da sessão como `example.com` para que o escopo do `rp_id` e do cookie cubra todos os subdomínios protegidos.

## Como verificar
Cadastre uma chave WebAuthn ou aplicativo TOTP no portal do Authelia e verifique o registro salvo no banco de storage.

## Conexões
- [[authelia-backends-autenticacao-ldap-active-directory-file-argon2id]] — Veja também: Authelia Backends de Autenticação (`authentication_backend`): integração com `LDAP` (Active Directory / OpenLDAP / FreeIPA) e `file` (`Argon2id`).
- [[authelia-session-redis-sentinel-cluster-storage-postgres-encryption-key]] — Veja também: Authelia Sessões e Persistência de Produção: `session.redis` (HA Sentinel/Cluster) e `storage.postgres` com `encryption_key`.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
