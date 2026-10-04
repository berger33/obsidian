---
id: software.devops.tranche20.001937
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/smallstep/cli/master/README.md", "https://raw.githubusercontent.com/smallstep/certificates/master/README.md", "https://github.com/smallstep/cli"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Smallstep `step crypto` e `step oauth`: toolkit de linha de comando para JWT, JWK, JWS, JWE, NaCl, TOTP e fluxos OAuth/OIDC

## Em uma frase
Além de X.509 e SSH, a CLI `step` fornece os subcomandos **`step crypto`** e **`step oauth`**, um toolkit criptográfico completo para criar chaves **JWK** (`step crypto jwk create`), assinar/verificar/inspecionar **JWTs** (RFC 7519), **JWS** e **JWE**, gerar tokens **TOTP**, derivar senhas (`scrypt`, `bcrypt`, `argon2`) e obter tokens OAuth2/OIDC diretamente no terminal.

## Por que importa
Depurar problemas de autenticação OIDC ou assinar tokens JWT de serviço em pipelines de CI usando scripts Python improvisados ou colando tokens sensíveis de produção em sites públicos na internet representa um grave risco de segurança.

## Como funciona
Com `step oauth --oidc --provider https://... | step crypto jwt inspect --insecure`, você autentica no provedor OIDC e decodifica o payload JSON do token localmente no seu terminal, ou valida criptograficamente a assinatura contra o JWKS do provedor com `step crypto jwt verify`.

## Exemplo
```bash
# Gerando um par de chaves JWK (EC P-256) e assinando um token JWT local:
step crypto jwk create pub.jwk priv.jwk --kty EC --crv P-256 --no-password --insecure
step crypto jwt sign \
  --key priv.jwk \
  --iss "ci-runner" \
  --aud "https://api.corp.internal" \
  --sub "deploy-bot" \
  --exp $(($(date +%s) + 300))
```

## Limites e trade-offs
Ao inspecionar um JWT com `step crypto jwt inspect --insecure`, a flag `--insecure` apenas informa que você está visualizando os claims sem verificar a assinatura; para autenticar o token em scripts, use sempre `step crypto jwt verify --jwks ...`.

## Como verificar
Crie um par JWK de teste, assine um JWT e verifique-o com `step crypto jwt verify --key pub.jwk --iss ci-runner --aud https://api.corp.internal`.

## Conexões
- [[stepca-renovacao-automatica-step-ca-renew-daemon-systemd-autocert]] — Veja também: Smallstep Renovação Automática e Revogação Passiva: `step ca renew --daemon`, timers systemd e Kubernetes `autocert`.
- [[stepca-hierarquia-two-tier-pki-offline-root-online-intermediate]] — Veja também: Smallstep Two-Tier PKI: operação do `step-ca` como CA Intermediária Online subordinada a uma Root CA Offline.

## Fontes
- [Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)](https://raw.githubusercontent.com/smallstep/cli/master/README.md) — README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH; consultado em 2026-10-03.
- [Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)](https://raw.githubusercontent.com/smallstep/certificates/master/README.md) — README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH; consultado em 2026-10-03.
- [Smallstep Certificates — Official GitHub Repository](https://github.com/smallstep/cli) — Repositório oficial Apache-2.0 do Smallstep step-ca; consultado em 2026-10-03.
