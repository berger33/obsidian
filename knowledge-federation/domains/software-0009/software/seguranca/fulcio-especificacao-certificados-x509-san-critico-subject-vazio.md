---
id: software.seguranca.tranche04.000393
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

# Sigstore Fulcio: Especificação RFC 5280 dos Certificados Root, Intermediate (`pathlen:0`) e Leaf (Subject Vazio e SAN Crítico)

## Em uma frase
A especificação de certificados do Fulcio (`docs/certificate-specification.md`) impõe regras estritas compatíveis com a RFC 5280 para toda a cadeia (Root CA, Intermediate CA e Issued Leaf Certificate).

## Por que importa
Evita ambiguidades de parsing X.509 e ataques de escalação de CA: um certificado folha emitido para um desenvolvedor ou CI jamais pode assinar outros certificados nem carregar múltiplos SANs conflitantes.

## Como funciona
O certificado folha emitido pelo Fulcio **DEVE** ter o campo `Subject` completamente vazio (`Subject: `), exatamente **um** `Subject Alternative Name` (SAN, preenchido com um e-mail ou uma URI) marcado como extensão **crítica** (`X509v3 Subject Alternative Name: critical`), `Key Usage: Digital Signature`, `Extended Key Usage: Code Signing` e o OID do emissor OIDC (`1.3.6.1.4.1.57264.1.1`). Já a CA Intermediária possui `CA:TRUE, pathlen:0` e `EKU: Code Signing`.

## Exemplo
```bash
# Auditar a conformidade de um certificado folha Fulcio (Subject vazio, SAN crítico e EKU Code Signing)
openssl x509 -in fulcio-leaf.crt.pem -noout -subject -purpose -ext subjectAltName,keyUsage,extendedKeyUsage
```

## Limites e trade-offs
Qualquer biblioteca cliente que tente extrair a identidade do signatário lendo o `Common Name (CN)` do campo `Subject` encontrará uma string vazia; os verificadores devem ler obrigatoriamente a extensão crítica `Subject Alternative Name` e o OID `1.3.6.1.4.1.57264.1.1`.

## Como verificar
Execute o comando `openssl x509` acima e confirme `subject=` vazio e `X509v3 Subject Alternative Name: critical` seguido de `email:...` ou `URI:...`.

## Conexões
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Veja também: Sigstore Fulcio: Modelo de Segurança de Certificados de 10 Minutos — Por Que Não Há CRL/OCSP nem Re-Assinatura.
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Veja também: Sigstore Fulcio: Árvore de OIDs X.509 (`1.3.6.1.4.1.57264.1.*`) para GitHub Actions, GitLab CI e Buildkite.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison]] — Referência cruzada direta com fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
