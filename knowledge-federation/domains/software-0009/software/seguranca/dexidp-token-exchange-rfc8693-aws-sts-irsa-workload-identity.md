---
id: software.seguranca.tranche03.000240
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
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/connectors/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex como Emissor OIDC para `AWS STS` (`AssumeRoleWithWebIdentity`) e Federação de Identidades Multi-Serviço

## Em uma frase
Conforme destacado na seção *ID Tokens* do README oficial (*"Systems that can already consume OpenID Connect ID Tokens issued by dex include: Kubernetes, AWS STS"*), como os ID Tokens emitidos pelo Dex seguem estritamente o padrão OpenID Connect 1.0 e expõem o endpoint público de descoberta (`/.well-known/openid-configuration` e `/keys`), eles podem ser consumidos diretamente pelo **AWS Security Token Service (AWS STS)** e outros provedores de nuvem para troca por credenciais temporárias!

## Por que importa
Distribuir chaves estáticas de longo prazo (`AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`) para desenvolvedores ou serviços on-premises acessarem recursos na AWS cria risco permanente de vazamento.

## Como funciona
Ao cadastrar a URL do `issuer` do seu Dex como um **IAM OpenID Connect Identity Provider** na conta AWS, um desenvolvedor ou serviço autenticado no Dex chama `sts:AssumeRoleWithWebIdentity` passando o `id_token` do Dex e recebe credenciais temporárias da AWS STS restritas por condições sobre `sub`, `aud` ou `email`!

## Exemplo
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/dex.internal.corp/dex"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "dex.internal.corp/dex:aud": "aws-sts-cli"
        }
      }
    }
  ]
}
```

## Limites e trade-offs
Para que o AWS STS possa validar a assinatura dos tokens emitidos pelo Dex, os endpoints públicos `/.well-known/openid-configuration` e `/keys` do Dex precisam ser acessíveis via HTTPS com certificado emitido por uma CA pública confiável.

## Como verificar
Teste `aws sts assume-role-with-web-identity --role-arn <ARN> --role-session-name test --web-identity-token <DEX_ID_TOKEN>`.

## Conexões
- [[dexidp-grpc-api-mtls-gerenciamento-dinamico-clientes-revogacao]] — Veja também: Dex API Administrativa `gRPC` com `mTLS`: criação dinâmica de clientes OAuth2 e revogação de Refresh Tokens.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
