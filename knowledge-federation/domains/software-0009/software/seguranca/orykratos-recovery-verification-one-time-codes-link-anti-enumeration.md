---
id: software.seguranca.tranche02.000137
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
fontes: ["https://raw.githubusercontent.com/ory/kratos/master/README.md", "https://www.ory.com/docs/kratos/manage-identities/overview", "https://github.com/ory/kratos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Kratos Fluxos de `Recovery` e `Verification`: códigos OTP (`code`) vs `link`, `courier` SMTP/HTTP e prevenção de enumeração de contas

## Em uma frase
Para recuperação de conta e verificação de endereço de e-mail/telefone, o Ory Kratos suporta duas estratégias (`use: code` ou `use: link`), despachando as mensagens de forma assíncrona pelo subsistema **`courier`** (`kratos courier watch`, via SMTP ou HTTP canalizado para provedores de e-mail/SMS).

## Por que importa
Dois problemas frequentes quebram fluxos de recuperação baseados em links mágicos (`use: link`): 1) scanners corporativos de antivírus de e-mail (como Microsoft Defender Safe Links) fazem `GET` automático no link e consomem o token antes do usuário clicar; e 2) o usuário abre o e-mail no celular mas estava tentando fazer login no navegador do desktop.

## Como funciona
Por isso, o Kratos recomenda a estratégia **`use: code`** (código numérico de uso único com TTL curto e limite estrito de tentativas): ela é imune a *prefetching* de scanners de e-mail e permite que o usuário leia o código no celular e digite no computador, além de nunca revelar na resposta da API se um e-mail existe ou não na base (*Account Enumeration Protection*)!

## Exemplo
```yaml
selfservice:
  flows:
    recovery:
      enabled: true
      use: code
      lifespan: 15m
    verification:
      enabled: true
      use: code
      lifespan: 15m
courier:
  smtp:
    connection_uri: smtps://smtp-user:secret@mail.internal:465/
```

## Limites e trade-offs
Em produção, execute pelo menos uma instância do worker `kratos courier watch` (ou habilite o courier em background) para processar a fila de e-mails/SMS gravada no banco pelo Kratos.

## Como verificar
Teste solicitar recuperação para um e-mail cadastrado e para um e-mail inexistente e verifique que a resposta HTTP e a mensagem de UI são idênticas.

## Conexões
- [[orykratos-seguranca-senhas-argon2id-haveibeenpwned-k-anonymity]] — Veja também: Ory Kratos Segurança de Credenciais `password`: hashing `Argon2id` (ou `bcrypt`), política de similaridade e checagem *Have I Been Pwned* (`k-Anonymity`).
- [[orykratos-webhooks-actions-before-after-hooks-jsonnet-sincronizacao]] — Veja também: Ory Kratos Actions & Webhooks (`before` / `after` hooks): interceptação e enriquecimento de fluxos com templates `Jsonnet`.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
