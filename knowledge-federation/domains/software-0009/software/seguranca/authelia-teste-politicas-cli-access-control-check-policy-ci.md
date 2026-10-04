---
id: software.seguranca.tranche02.000144
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

# Authelia `authelia access-control check-policy`: validação determinística de regras de autorização na linha de comando e CI/CD

## Em uma frase
O subcomando **`authelia access-control check-policy`** permite testar a matriz de regras de `access_control` do arquivo `configuration.yml` diretamente na CLI sem subir o servidor, simulando `--url`, `--method`, `--ip`, `--username` e `--groups` e exibindo qual regra casou (ou *potential match*) e qual política final (`deny`, `bypass`, `one_factor`, `two_factor`) foi aplicada.

## Por que importa
Editar expressões regulares em `resources` ou `domain_regex` em um arquivo YAML de 300 linhas sem testar casos de borda pode abrir acidentalmente um endpoint administrativo para `bypass` ou `one_factor`.

## Como funciona
Adicionando a flag `--verbose`, a CLI imprime uma tabela mostrando regra por regra (`#1`, `#2`, `#3`...) se cada critério (`Domain`, `Resource`, `Method`, `Network`, `Subject`) resultou em `hit`, `miss` ou `may`, facilitando depurar exatamente por que uma regra casou ou não.

## Exemplo
```bash
# Testando na CLI qual política será aplicada para uma requisição específica:
authelia access-control check-policy \
  --config /etc/authelia/configuration.yml \
  --url "https://admin.example.com/settings" \
  --method "GET" \
  --username "ana" \
  --groups "platform-admins" \
  --ip "203.0.113.10" \
  --verbose
```

## Limites e trade-offs
Inclua um script no seu pipeline de CI/CD executando `authelia validate-config` e uma bateria de asserções com `authelia access-control check-policy` antes de aplicar mudanças via GitOps.

## Como verificar
Execute o comando acima e verifique a linha final `Applied policy: two_factor`.

## Conexões
- [[authelia-criterios-regras-domain-regex-resources-subject-methods-query]] — Veja também: Authelia Critérios Granulares de Regra: `domain`, `domain_regex`, `resources`, `subject` (`AND`/`OR`), `methods` e `query`.
- [[authelia-backends-autenticacao-ldap-active-directory-file-argon2id]] — Veja também: Authelia Backends de Autenticação (`authentication_backend`): integração com `LDAP` (Active Directory / OpenLDAP / FreeIPA) e `file` (`Argon2id`).

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://www.authelia.com/configuration/security/access-control/) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
