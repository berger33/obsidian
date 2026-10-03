---
id: software.seguranca.tranche03.000242
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://www.pomerium.com/docs", "https://raw.githubusercontent.com/pomerium/pomerium/main/README.md", "https://github.com/pomerium/pomerium"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pomerium Policy Language (`PPL`): autorização declarativa com operadores lógicos (`allow`/`deny`, `and`, `or`, `not`, `nor`) e critérios de contexto

## Em uma frase
O motor de autorização do Pomerium utiliza a **Pomerium Policy Language (PPL)** — uma linguagem declarativa em YAML ou JSON estruturada em blocos **`allow`** e **`deny`** compostos pelos quatro operadores lógicos **`and`**, **`or`**, **`not`** e **`nor`**, avaliando critérios ricos como **`email`**, **`user`**, **`domain`**, **`claim`** (qualquer claim do IdP, como `claim/groups` ou `claim/department`), **`day_of_week`**, **`time_of_day`**, **`source_ip`** e **`device`**!

## Por que importa
Sistemas de proxy simples que só validam "usuário logado = permitido" não impedem que um prestador externo autenticado no mesmo tenant OIDC acesse um painel administrativo restrito à equipe de SRE.

## Como funciona
Na PPL, uma rota só é autorizada se pelo menos uma regra **`allow`** avaliar como verdadeira **E nenhuma regra `deny`** avaliar como verdadeira (*Deny overrides Allow*); além disso, cada critério suporta matchers de comparação como `is`, `contains`, `starts_with`, `ends_with` e `in`!

## Exemplo
```yaml
routes:
  - from: https://argocd.internal.corp
    to: https://argocd-server.argocd.svc.cluster.local:443
    policy:
      - allow:
          and:
            - domain:
                is: internal.corp
            - claim/groups:
                has: platform-sre
      - deny:
          or:
            - claim/employment_type:
                is: contractor
```

## Limites e trade-offs
Por padrão, o Pomerium opera em modo **Deny-by-Default**: se você criar uma rota `from` -> `to` sem declarar nenhuma cláusula `policy` (e sem `allow_public_unauthenticated_access: true`), todas as requisições serão negadas com `403 Forbidden`!

## Como verificar
Teste sua política PPL acessando a rota com diferentes usuários e inspecione os logs de decisão de auditoria (`authorize-log`) do Pomerium.

## Conexões
- [[pomerium-arquitetura-identity-aware-access-proxy-beyondcorp-zero-trust]] — Veja também: Pomerium: arquitetura do *Identity-Aware Access Proxy* baseado nos princípios Google BeyondCorp e NIST Zero Trust.
- [[pomerium-jwt-assertion-header-x-pomerium-jwt-assertion-verificacao-upstream]] — Veja também: Pomerium Identity Propagation (`X-Pomerium-Jwt-Assertion`): assinatura criptográfica da identidade do usuário para a aplicação backend.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
