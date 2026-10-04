---
id: software.seguranca.tranche04.000391
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

# Sigstore Fulcio: Arquitetura da Autoridade Certificadora (CA) para *Keyless Code Signing* Baseada em OIDC

## Em uma frase
**Fulcio** (projeto Sigstore / Linux Foundation sob Apache-2.0) é uma Autoridade Certificadora (CA) gratuita e open-source que emite certificados X.509 de assinatura de código de curtíssima duração (**10 minutos**) vinculando uma chave pública efêmera a uma identidade OpenID Connect (OIDC).

## Por que importa
Elimina o maior ponto de falha da assinatura de software tradicional: a necessidade de armazenar, proteger por anos e rotacionar chaves privadas de longa duração que podem ser vazadas ou roubadas.

## Como funciona
O cliente (`cosign`, `gitsign`, `sigstore-go`) gera um par de chaves efêmero **apenas na memória RAM**, obtém um ID Token OIDC de curta duração de um provedor confiável (GitHub Actions, GitLab CI, Google, Microsoft, Kubernetes ServiceAccount), assina o claim `sub`/e-mail como prova de posse da chave privada e envia ao Fulcio (`/api/v2/signingCert`). O Fulcio valida o token OIDC, registra o certificado no Certificate Transparency Log (`ctfe`) e devolve o certificado X.509 válido por 10 minutos; após assinar o artefato e registrá-lo no Rekor, o cliente descarta a chave privada da memória para sempre.

## Exemplo
```bash
# Obter a cadeia de certificados atual da instância pública do Fulcio via API v2 TrustBundle
curl -sS https://fulcio.sigstore.dev/api/v2/trustBundle | jq .
```

## Limites e trade-offs
Chamar o fluxo Fulcio de *"keyless signing"* não significa ausência de criptografia de chave pública: chaves ECDSA/Ed25519 continuam existindo, mas são **efêmeras** (vivem segundos na memória) e substituem a posse de chaves estáticas pela autenticação OIDC.

## Como verificar
Inspecione um certificado emitido pelo Fulcio com `openssl x509 -noout -text` e confirme que a janela entre `Not Before` e `Not After` é de exatamente 10 minutos.

## Conexões
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Veja também: Sigstore Fulcio: Modelo de Segurança de Certificados de 10 Minutos — Por Que Não Há CRL/OCSP nem Re-Assinatura.
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Referência cruzada direta com fulcio-especificacao-certificados-x509-san-critico-subject-vazio.
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Referência cruzada direta com fulcio-extensoes-x509-oids-57264-github-actions-ci-claims.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
