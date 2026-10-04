---
id: software.seguranca.tranche02.000142
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
fontes: ["https://www.authelia.com/configuration/security/access-control/", "https://raw.githubusercontent.com/authelia/authelia/master/README.md", "https://github.com/authelia/authelia"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Authelia `access_control`: políticas `deny`, `bypass`, `one_factor` e `two_factor` e avaliação sequencial *first-match*

## Em uma frase
Conforme documentado na página oficial *Access Control* (`authelia.com/configuration/security/access-control/`), o motor de autorização de proxy do Authelia avalia uma lista ordenada de **`rules`** (onde a **primeira regra que casar com todos os critérios vence**) e aplica uma das quatro políticas: **`deny`** (bloqueia o acesso), **`bypass`** (permite acesso sem autenticação), **`one_factor`** (exige usuário/senha) ou **`two_factor`** (exige usuário/senha + segundo fator WebAuthn/TOTP/Duo).

## Por que importa
Colocar uma regra ampla (`domain: "*.example.com"`, `policy: one_factor`) no topo da lista `rules:` faz com que regras mais específicas declaradas abaixo (como `domain: "admin.example.com"`, `policy: two_factor`) **nunca sejam alcançadas**, pois o Authelia avalia em ordem sequencial estrita!

## Como funciona
Por segurança, a documentação oficial recomenda fortemente definir sempre **`default_policy: 'deny'`** (aplicada quando nenhuma regra casa com a requisição) e ordenar as regras da mais específica (rotas `/api/webhook` ou subdomínios administrativos restritos a grupos) para a mais genérica.

## Exemplo
```yaml
access_control:
  default_policy: 'deny'
  networks:
    - name: 'internal_vpn'
      networks:
        - '10.10.0.0/16'
  rules:
    - domain: 'admin.example.com'
      policy: 'two_factor'
      subject:
        - 'group:platform-admins'
    - domain: 'grafana.example.com'
      policy: 'one_factor'
      networks:
        - 'internal_vpn'
    - domain: 'grafana.example.com'
      policy: 'two_factor'
```

## Limites e trade-offs
Observe no exemplo acima como o mesmo domínio `grafana.example.com` aparece em duas regras seguidas: quem acessa de dentro da VPN (`internal_vpn`) precisa apenas de `one_factor`, enquanto quem acessa da internet cai na regra seguinte exigindo `two_factor`!

## Como verificar
Verifique a ordem e o casamento das suas regras com a ferramenta CLI `authelia access-control check-policy`.

## Conexões
- [[authelia-arquitetura-portal-autenticacao-autorizacao-forwardauth-oidc]] — Veja também: Authelia: arquitetura do servidor open-source de autenticação, 2FA, controle de acesso (`ForwardAuth`) e provedor OpenID Connect 1.0.
- [[authelia-criterios-regras-domain-regex-resources-subject-methods-query]] — Veja também: Authelia Critérios Granulares de Regra: `domain`, `domain_regex`, `resources`, `subject` (`AND`/`OR`), `methods` e `query`.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://www.authelia.com/configuration/security/access-control/) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
