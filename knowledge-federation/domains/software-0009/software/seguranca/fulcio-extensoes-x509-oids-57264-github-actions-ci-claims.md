---
id: software.seguranca.tranche04.000394
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

# Sigstore Fulcio: Árvore de OIDs X.509 (`1.3.6.1.4.1.57264.1.*`) para GitHub Actions, GitLab CI e Buildkite

## Em uma frase
Sob o Private Enterprise Number (PEN `57264`) da Linux Foundation / Sigstore, o Fulcio grava os *claims* de execução do pipeline de CI/CD diretamente em extensões X.509 padronizadas (`1.3.6.1.4.1.57264.1.1` a `.1.22`) dentro do certificado emitido.

## Por que importa
Permite criar políticas de verificação granulares que exigem não apenas que uma imagem tenha sido assinada pelo repositório correto, mas que o build tenha ocorrido na branch `refs/heads/main`, no commit SHA esperado, em um runner `github-hosted` e a partir de um workflow específico.

## Como funciona
A primeira geração de extensões (`.1.1` a `.1.6`) codificava strings brutas para Issuer (`.1.1`) e GitHub Actions. A especificação atual (`.1.8` a `.1.22`, codificada em UTF8String ASN.1 DER) é agnóstica de plataforma de CI: `.1.8` (*Issuer V2*), `.1.9` (*Build Signer URI*, ex.: caminho do `.github/workflows/release.yml`), `.1.10` (*Build Signer Digest*), `.1.11` (*Runner Environment*, ex.: `github-hosted` vs `self-hosted`), `.1.12` (*Source Repository URI*), `.1.13` (*Source Repository Digest*), `.1.14` (*Source Repository Ref*) e `.1.18` (*Build Config URI*).

## Exemplo
```bash
# Inspecionar as extensões OID 1.3.6.1.4.1.57264.1.* em um certificado Fulcio emitido para GitHub Actions
openssl asn1parse -in fulcio-leaf.crt.pem \
  | grep -A 3 -E "1\.3\.6\.1\.4\.1\.57264\.1\."
```

## Limites e trade-offs
Políticas de admissão que validam apenas `--certificate-oidc-issuer=https://token.actions.githubusercontent.com` sem restringir o `--certificate-identity` (SAN / Source Repository URI) aceitarão imagens assinadas por **qualquer** repositório público de qualquer usuário do GitHub.

## Como verificar
Verifique com `openssl asn1parse` que o certificado emitido em CI contém o OID `1.3.6.1.4.1.57264.1.8` (Issuer) e `1.3.6.1.4.1.57264.1.12` (Source Repository URI).

## Conexões
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Veja também: Sigstore Fulcio: Especificação RFC 5280 dos Certificados Root, Intermediate (`pathlen:0`) e Leaf (Subject Vazio e SAN Crítico).
- [[fulcio-provedores-oidc-meta-issuers-kubernetes-spiffe-ci]] — Veja também: Sigstore Fulcio: Configuração de Provedores OIDC (`config.json`), Meta-Issuers (EKS/GKE/AKS) e SPIFFE/Workload Identity.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
