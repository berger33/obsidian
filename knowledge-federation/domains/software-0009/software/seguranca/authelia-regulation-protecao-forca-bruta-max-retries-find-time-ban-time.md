---
id: software.seguranca.tranche02.000148
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

# Authelia `regulation`: proteção integrada contra ataques de força bruta com `max_retries`, `find_time` e `ban_time`

## Em uma frase
O subsistema **`regulation`** do Authelia monitora todas as tentativas de autenticação malsucedidas registradas no banco de `storage` e bloqueia temporariamente contas (e/ou endereços IP conforme os modos configurados) que excederem **`max_retries`** dentro da janela **`find_time`**, mantendo o bloqueio pelo período **`ban_time`**.

## Por que importa
Sem limitação de taxa e banimento temporário no próprio motor de autenticação, um invasor distribuído pode testar milhares de senhas por minuto contra o backend LDAP ou esgotar a CPU de hashing Argon2id.

## Como funciona
Configurando `max_retries: 3`, `find_time: '2m'` e `ban_time: '5m'`, se três tentativas de senha falharem em menos de 2 minutos, o Authelia rejeita novas tentativas pelos próximos 5 minutos mesmo que a senha correta seja enviada durante o banimento.

## Exemplo
```yaml
regulation:
  max_retries: 3
  find_time: '2m'
  ban_time: '5m'
```

## Limites e trade-offs
Caso um colaborador legítimo bloqueie sua própria conta acidentalmente digitando a senha errada 3 vezes, o administrador pode listar e remover o banimento imediatamente via CLI com **`authelia storage bans user list`** e **`authelia storage bans user revoke`**!

## Como verificar
Execute `authelia storage bans user list --config configuration.yml` para auditar banimentos ativos.

## Conexões
- [[authelia-session-redis-sentinel-cluster-storage-postgres-encryption-key]] — Veja também: Authelia Sessões e Persistência de Produção: `session.redis` (HA Sentinel/Cluster) e `storage.postgres` com `encryption_key`.
- [[authelia-openid-connect-provider-clients-authorization-policies-pkce]] — Veja também: Authelia como Provedor OpenID Connect 1.0 (`identity_providers.oidc`): proteção de aplicações nativas OIDC (Grafana, Argo CD, GitLab).

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
