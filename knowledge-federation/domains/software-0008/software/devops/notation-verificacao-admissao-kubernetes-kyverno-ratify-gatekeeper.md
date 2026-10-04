---
id: software.devops.tranche13.001298
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
fontes: ["https://raw.githubusercontent.com/notaryproject/notation/main/README.md", "https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/", "https://notaryproject.dev/docs/user-guides/installation/cli/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notary Project Notation: Verificação de Assinaturas na Admissão do Kubernetes com Kyverno e Ratify

## Em uma frase
No cluster Kubernetes, as assinaturas geradas pelo Notation são verificadas automaticamente na admissão de cada Pod (`ValidatingWebhookConfiguration`) por motores de política como o **Kyverno** (`verifyImages` com tipo `Notary`) ou o **Ratify** integrado ao **OPA Gatekeeper**.

## Por que importa
Assinar imagens no pipeline de CI com `notation sign` sem impor a verificação criptográfica no `kube-apiserver` não impede que alguém com permissão de deploy implante uma imagem não assinada ou adulterada diretamente no cluster.

## Como funciona
Na regra `verifyImages` do Kyverno (ou no `Verifier` Notary do Ratify), configura-se o certificado da CA corporativa (ou a `trustpolicy.json` e `TrustStore`) e habilita-se `mutateDigest: true`, de modo que o webhook verifica a assinatura `application/vnd.cncf.notary.v2.signature` no registry e fixa o digest `@sha256:...` verificado no Pod antes de admiti-lo.

## Exemplo
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: check-notation-signatures
spec:
  validationFailureAction: Enforce
  webhookTimeoutSeconds: 30
  rules:
    - name: verify-notary-v2
      match:
        any:
          - resources:
              kinds: ["Pod"]
      verifyImages:
        - imageReferences: ["ghcr.io/org/*"]
          type: Notary
          attestors:
            - count: 1
              entries:
                - certificates:
                    cert: |-
                      -----BEGIN CERTIFICATE-----
                      ...
                      -----END CERTIFICATE-----
```

## Limites e trade-offs
Definir um `webhookTimeoutSeconds` muito baixo (como 3 segundos) em uma política `verifyImages` que precisa consultar o registry OCI e validar cadeias de certificados e revogação pode causar falhas de admissão por timeout durante picos de criação de Pods.

## Como verificar
Configure `webhookTimeoutSeconds` adequado (15 a 30 segundos), habilite cache de resultados de verificação no controlador de admissão e use um mirror OCI local como o Zot.

## Conexões
- [[notation-inspect-assinaturas-cadeia-certificados-timestamps]] — Veja também: Notary Project Notation: Inspeção Detalhada de Assinaturas e Cadeias X.509 com notation inspect.
- [[notation-assinatura-sbom-artefatos-oras-grafo-supply-chain]] — Veja também: Notary Project Notation: Assinatura de SBOMs e Artefatos Anexados via ORAS no Grafo OCI.

## Fontes
- [Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)](https://raw.githubusercontent.com/notaryproject/notation/main/README.md) — Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect; consultado em 2026-10-03.
- [Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)](https://notaryproject.dev/docs/quickstart-guides/quickstart-sign-image-artifact/) — README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS; consultado em 2026-10-03.
- [Notary Project — Official CLI Installation & Configuration Reference](https://notaryproject.dev/docs/user-guides/installation/cli/) — Referência oficial de instalação e estrutura de diretórios do Notation; consultado em 2026-10-03.
