---
id: software.devops.tranche13.001300
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

# Notary Project Notation: Adoção Gradual com Níveis de Verificação (strict, permissive, audit e skip)

## Em uma frase
A especificação de Trust Policy do Notation define quatro níveis de verificação (`signatureVerification.level`) — **`strict`**, **`permissive`**, **`audit`** e **`skip`** — que permitem adotar a verificação de assinaturas gradualmente na organização e lidar com imagens base de terceiros.

## Por que importa
Impor `"level": "strict"` de imediato para todos os repositórios quando parte dos serviços legados ainda possui certificados expirados ou sem revogação OCSP/CRL acessível trava os pipelines de deploy.

## Como funciona
No arquivo `trustpolicy.json`, cada escopo de repositório pode ter seu próprio nível: `"audit"` apenas registra nos logs se a verificação de assinatura falhar (ideal para a fase inicial de rollout); `"permissive"` exige uma assinatura matemática e identidade válidas, mas apenas emite aviso em falhas de expiração/revogação; `"strict"` bloqueia qualquer falha em todas as validações; e `"skip"` isenta explicitamente repositórios públicos não assinados.

## Exemplo
```json
{
  "version": "1.0",
  "trustPolicies": [
    {
      "name": "internal-prod-strict",
      "registryScopes": ["ghcr.io/org/prod-services"],
      "signatureVerification": { "level": "strict" },
      "trustStores": ["ca:corp-ca"],
      "trustedIdentities": ["x509.subject: C=BR, O=AcmeCorp, CN=prod-signer"]
    },
    {
      "name": "legacy-migration-audit",
      "registryScopes": ["ghcr.io/org/legacy-services"],
      "signatureVerification": { "level": "audit" },
      "trustStores": ["ca:corp-ca"],
      "trustedIdentities": ["*"]
    }
  ]
}
```

## Limites e trade-offs
Deixar repositórios críticos de produção em `"level": "audit"` ou `"permissive"` permanentemente após concluir a migração faz com que o `notation verify` retorne código de saída `0` mesmo diante de certificados revogados.

## Como verificar
Promova todos os escopos internos de produção para `"level": "strict"` assim que o pipeline de assinatura estiver estável e monitore o `trustpolicy.json` via controle de versão.

## Conexões
- [[notation-assinatura-sbom-artefatos-oras-grafo-supply-chain]] — Veja também: Notary Project Notation: Assinatura de SBOMs e Artefatos Anexados via ORAS no Grafo OCI.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
