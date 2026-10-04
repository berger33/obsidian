---
id: software.seguranca.tranche02.000143
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

# Authelia Critérios Granulares de Regra: `domain`, `domain_regex`, `resources`, `subject` (`AND`/`OR`), `methods` e `query`

## Em uma frase
Cada regra em `access_control.rules` do Authelia pode combinar até sete critérios de filtragem da requisição: **`domain`**, **`domain_regex`**, **`resources`** (expressões regulares sobre o caminho da URL), **`subject`** (usuários `user:alice` ou grupos `group:devs`), **`networks`**, **`methods`** (verbos HTTP como `GET`, `POST`, `DELETE`) e **`query`** (operadores `present`, `absent`, `pattern`, `not pattern` sobre query strings).

## Por que importa
No critério `subject`, entender a diferença entre lista simples e lista aninhada de listas evita falhas lógicas: múltiplos itens em listas externas operam como **`OR`**, enquanto múltiplos itens dentro da mesma sub-lista interna operam como **`AND`**!

## Como funciona
Por exemplo, `subject: [['group:devs', 'group:oncall'], ['group:secops']]` exige que o usuário pertença simultaneamente a `devs` **E** `oncall`, **OU** pertença ao grupo `secops`.

## Exemplo
```yaml
access_control:
  default_policy: 'deny'
  rules:
    - domain: 'api.example.com'
      policy: 'two_factor'
      methods:
        - 'DELETE'
        - 'PUT'
      resources:
        - '^/v1/production(/.*)?$'
      subject:
        - ['group:sre', 'group:oncall']
```

## Limites e trade-offs
Conforme nota importante na documentação oficial de *Access Control*, os antigos wildcards `{user}.` e `{group}.` em `domain` estão depreciados em favor de **`domain_regex`** com grupos nomeados (`^(?P<User>[a-z0-9-]+)\.dev\.example\.com$`), e nunca devem ser combinados com a política `bypass`.

## Como verificar
Simule requisições com método, caminho e usuário via `authelia access-control check-policy --config configuration.yml --url https://api.example.com/v1/production/db --method DELETE --username alice --groups sre,oncall`.

## Conexões
- [[authelia-access-control-policies-deny-bypass-one-factor-two-factor]] — Veja também: Authelia `access_control`: políticas `deny`, `bypass`, `one_factor` e `two_factor` e avaliação sequencial *first-match*.
- [[authelia-teste-politicas-cli-access-control-check-policy-ci]] — Veja também: Authelia `authelia access-control check-policy`: validação determinística de regras de autorização na linha de comando e CI/CD.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://www.authelia.com/configuration/security/access-control/) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
