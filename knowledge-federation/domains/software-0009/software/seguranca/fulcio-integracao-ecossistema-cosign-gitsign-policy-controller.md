---
id: software.seguranca.tranche04.000400
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/sigstore/fulcio/main/README.md", "https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md", "https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Fulcio: Integração Ponta a Ponta com `cosign`, `gitsign` e Kubernetes `policy-controller` / Kyverno

## Em uma frase
No fluxo completo de segurança da cadeia de suprimentos Sigstore, o Fulcio emite o certificado de identidade OIDC para que o **`cosign`** assine imagens OCI/SBOMs e o **`gitsign`** assine commits Git, enquanto o **`policy-controller`** (ou Kyverno) valida essas identidades na admissão do cluster Kubernetes.

## Por que importa
Conecta a identidade do desenvolvedor (commits Git assinados via `gitsign` com OIDC) e a identidade do pipeline de CI (imagens assinadas via `cosign` com OIDC) a políticas declarativas de runtime no Kubernetes sem gerenciar uma única chave privada estática.

## Como funciona
No GitHub Actions, o workflow solicita `permissions: id-token: write`, executa `cosign sign --yes registry.corp/app@sha256:...`, obtendo um certificado Fulcio com os OIDs `.1.8` a `.1.22` do workflow e gravando a entrada no Rekor. No cluster Kubernetes, uma `ClusterImagePolicy` exige que a imagem possua certificado emitido pela CA Fulcio cujo `issuer` e `subject` (Expressão Regular da URI do workflow) correspondam ao pipeline oficial de release.

## Exemplo
```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: require-fulcio-github-release-workflow
spec:
  images:
    - glob: "ghcr.io/org-corp/**"
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subjectRegExp: "^https://github\\.com/org-corp/[a-z0-9-]+/\\.github/workflows/release\\.yml@refs/tags/v.*"
      ctlog:
        url: https://rekor.sigstore.dev
```

## Limites e trade-offs
Usar uma regex em `subjectRegExp` que não ancore a branch/tag final (`@refs/heads/main` ou `@refs/tags/v.*`) permitirá que qualquer desenvolvedor que abra uma branch de *feature* ou *pull request* no repositório assine imagens aceitas pelo cluster de produção.

## Como verificar
Aplique a `ClusterImagePolicy` no cluster de homologação e tente implantar uma imagem assinada a partir de uma branch `refs/heads/feature-test`, confirmando o bloqueio imediato pelo webhook de admissão.

## Conexões
- [[fulcio-implantacao-privada-certificate-maker-kms-pkcs11-tuf]] — Veja também: Sigstore Fulcio: Implantação Corporativa Privada com `certificate-maker`, Cloud KMS e HSM PKCS#11.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Referência cruzada direta com fulcio-extensoes-x509-oids-57264-github-actions-ci-claims.
- [[rekor-sigstore-bundle-verificacao-offline-signed-timestamps]] — Referência cruzada direta com rekor-sigstore-bundle-verificacao-offline-signed-timestamps.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
