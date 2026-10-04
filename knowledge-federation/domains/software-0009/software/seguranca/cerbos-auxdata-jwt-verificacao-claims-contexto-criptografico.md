---
id: software.seguranca.tranche01.000088
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos `auxData` e Verificação Nativa de JWT: uso de claims autenticadas do token diretamente nas expressões de política

## Em uma frase
O bloco **`auxData`** do Cerbos permite passar um token **JWT** assinado (ou dados auxiliares estruturados) junto com a requisição `CheckResources`/`PlanResources`, de modo que o próprio Cerbos PDP valide a assinatura criptográfica do JWT contra um conjunto de chaves **JWKS** configurado no servidor e exponha as claims verificadas em **`request.auxData.jwt`**!

## Por que importa
Em arquiteturas Zero-Trust, confiar apenas nos atributos `principal.attr` montados por um gateway intermediário pode ser insuficiente se você quiser que o próprio PDP valide criptograficamente o token JWT emitido pelo IdP (ex.: nível de autenticação MFA `acr`, `amr`, `aud`, `iss` ou escopos OAuth2).

## Como funciona
Configurando `auxData.jwt.keySets` no `.cerbos.yaml` do servidor PDP (apontando para a URL JWKS remota do Keycloak/Auth0/Okta ou chave pública local), as políticas podem exigir condições como ` "mfa" in request.auxData.jwt.amr ` antes de autorizar uma ação sensível.

## Exemplo
```yaml
# Trecho do arquivo de configuração do servidor .cerbos.yaml habilitando verificação JWKS:
auxData:
  jwt:
    keySets:
      - id: corp-idp
        remote:
          url: https://idp.internal.corp/realms/main/protocol/openid-connect/certs
          refreshInterval: 1h
```

## Limites e trade-offs
Se o token JWT enviado em `auxData.jwt.token` estiver expirado ou com assinatura inválida, o Cerbos rejeita a requisição imediatamente antes mesmo de avaliar as regras.

## Como verificar
Teste expressões que leem `request.auxData.jwt` simulando `auxData` nos seus arquivos de teste do `cerbos compile`.

## Conexões
- [[cerbos-compilacao-testes-unitarios-cerbos-compile-schemas-json]] — Veja também: Cerbos `cerbos compile` e Validação de Schemas: testes unitários de políticas e checagem de tipos de atributos (`schemas`).
- [[cerbos-audit-logs-decision-logs-outputs-mascaramento-campos-sensiveis]] — Veja também: Cerbos Decision Audit Logs e Policy Outputs: trilha de auditoria de decisões e retorno de obrigações/máscaras para a aplicação.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
