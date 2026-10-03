---
id: software.devops.tranche13.001294
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://raw.githubusercontent.com/notaryproject/notation/main/README.md", "https://notaryproject.dev/docs/user-guides/installation/cli/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Configuração de Trust Policy (trustpolicy.json), Escopos e Níveis de Verificação

## Em uma frase
Para verificar assinaturas com `notation verify`, o Notation exige uma **Trust Policy** (`trustpolicy.json`, importada via `notation policy import ./trustpolicy.json` e inspecionada com `notation policy show`) que declara `registryScopes`, `signatureVerification.level`, `trustStores` e `trustedIdentities`.

## Por que importa
Apenas saber que uma assinatura é matematicamente válida contra um certificado da CA não basta: é preciso garantir que o certificado pertence à identidade autorizada para publicar naquele repositório específico (`registryScopes` + `trustedIdentities`).

## Como funciona
No arquivo `trustpolicy.json`, cada política define: `registryScopes` (lista de repositórios como `"ghcr.io/org/prod-api"` ou `"*"`), `signatureVerification.level` (`"strict"`, `"permissive"`, `"audit"` ou `"skip"`), `trustStores` (como `["ca:corp-pki"]`) e `trustedIdentities` (Subject DN do certificado X.509, como `"x509.subject: C=BR, O=Acme, CN=ci-signer"`).

## Exemplo
```json
{
  "version": "1.0",
  "trustPolicies": [
    {
      "name": "production-images-policy",
      "registryScopes": ["ghcr.io/org/payment-service"],
      "signatureVerification": {
        "level": "strict"
      },
      "trustStores": ["ca:corp-production-ca"],
      "trustedIdentities": [
        "x509.subject: C=BR, ST=SP, O=AcmeCorp, CN=release-signer"
      ]
    }
  ]
}
```

## Limites e trade-offs
Deixar `"registryScopes": ["*"]` e `"trustedIdentities": ["*"]` (usados apenas no exemplo de quickstart local) na política de produção aceita qualquer certificado emitido pela mesma CA para qualquer repositório.

## Como verificar
Restrinja sempre `registryScopes` aos repositórios exatos e especifique o `x509.subject` (ou ARN do AWS Signer) em `trustedIdentities`, validando a política ativa com `notation policy show`.

## Conexões
- [[notation-trust-store-ca-signingauthority-tsa-x509-pki]] — Veja também: Notary Project Notation: Gerenciamento de Trust Store (ca, signingAuthority e tsa) e Certificados X.509.
- [[notation-plugins-kms-aws-signer-azure-key-vault-vault]] — Veja também: Notary Project Notation: Arquitetura de Plugins KMS (AWS Signer, Azure Key Vault e HashiCorp Vault).

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
