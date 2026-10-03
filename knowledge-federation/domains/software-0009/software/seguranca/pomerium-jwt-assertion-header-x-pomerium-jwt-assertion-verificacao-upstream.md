---
id: software.seguranca.tranche03.000243
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

# Pomerium Identity Propagation (`X-Pomerium-Jwt-Assertion`): assinatura criptográfica da identidade do usuário para a aplicação backend

## Em uma frase
Quando o Pomerium autoriza e encaminha uma requisição para o serviço protegido (`to:`), ele pode injetar o cabeçalho HTTP **`X-Pomerium-Jwt-Assertion`** contendo um **JSON Web Token (JWT) assinado criptograficamente pelo Pomerium** (com chave privada ES256 definida em `signing_key`) que atesta o `sub`, `email`, `name`, `groups` e `sid` do usuário autenticado!

## Por que importa
Confiar em cabeçalhos em texto puro como `X-Forwarded-User: admin@corp.com` sem assinatura criptográfica é perigoso: se qualquer outro serviço dentro do cluster conseguir conectar-se diretamente à porta HTTP da aplicação backend pulando o proxy, ele poderá forjar `X-Forwarded-User` para personificar qualquer usuário!

## Como funciona
Ao validar a assinatura do JWT contido em **`X-Pomerium-Jwt-Assertion`** contra o endpoint público JWKS do Pomerium (`https://authenticate.internal.corp/.well-known/pomerium/jwks.json`), a aplicação backend tem prova criptográfica Fim-a-Fim de que aquela requisição passou pelo Pomerium e pertence àquele usuário.

## Exemplo
```bash
# Inspecionando a chave pública de verificação do cabeçalho X-Pomerium-Jwt-Assertion exposta pelo Pomerium:
curl -sS https://authenticate.internal.corp/.well-known/pomerium/jwks.json | jq .
```

## Limites e trade-offs
Configure **`pass_identity_headers: true`** na rota (ou globalmente) e liste as claims desejadas em **`jwt_claims_headers`** para que o Pomerium assine e propague o `X-Pomerium-Jwt-Assertion` para o serviço upstream.

## Como verificar
Decodifique e valide o JWT recebido no cabeçalho `X-Pomerium-Jwt-Assertion` no seu serviço backend usando a chave pública do `jwks.json`.

## Conexões
- [[pomerium-policy-language-ppl-operadores-allow-deny-and-or-not-nor]] — Veja também: Pomerium Policy Language (`PPL`): autorização declarativa com operadores lógicos (`allow`/`deny`, `and`, `or`, `not`, `nor`) e critérios de contexto.
- [[pomerium-mtls-downstream-upstream-client-certificates-device-identity]] — Veja também: Pomerium `mTLS` Downstream (Certificados de Cliente/Dispositivo) e Upstream (Criptografia Mútua Proxy -> Backend).

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
