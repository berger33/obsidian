---
id: software.seguranca.tranche04.000397
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

# Sigstore Fulcio: Fluxo Criptográfico da API v2 (`CreateSigningCertificate`) e Prova de Posse da Chave

## Em uma frase
O endpoint `POST /api/v2/signingCert` (ou RPC gRPC `CA.CreateSigningCertificate`) do Fulcio exige que o cliente apresente simultaneamente o token OIDC no cabeçalho `Authorization: Bearer <jwt>` e uma prova criptográfica de posse da chave privada correspondente à chave pública submetida.

## Por que importa
Impede que um atacante intercepte ou reutilize a chave pública de terceiro: a CA valida que o mesmo agente que detém o token OIDC detém também a chave privada efêmera.

## Como funciona
O cliente suporta duas modalidades no `CreateSigningCertificateRequest`: enviar uma `publicKeyRequest` (contendo a chave pública PEM/DER e `proofOfPossession`, que é a assinatura do claim `sub` ou `email` do JWT OIDC feita pela chave privada efêmera) ou enviar um `certificateSigningRequest` (CSR PKCS#10 assinado pela chave privada efêmera). O Fulcio verifica que a chave tem força mínima exigida (ECDSA P-256/P-384/P-521, Ed25519 ou RSA $\ge$ 2048 sem primos fracos) antes de emitir o certificado.

## Exemplo
```bash
# Testar conectividade e inspecionar os emissores OIDC aceitos pela API v2 do Fulcio
curl -sS https://fulcio.sigstore.dev/api/v2/configuration | jq .
```

## Limites e trade-offs
O Fulcio rejeita chaves RSA menores que 2048 bits, chaves RSA com expoente diferente de `65537` ou esquemas de chave pública mais fortes que o certificado pai da CA Intermediária.

## Como verificar
Verifique o código de resposta da API v2 ao submeter uma chave de teste e valide que chaves ECDSA P-256 e Ed25519 são aceitas conforme a especificação.

## Conexões
- [[fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison]] — Veja também: Sigstore Fulcio: Certificate Transparency Log (`ctfe`), Precertificates (`OID 1.3.6.1.4.1.11129.2.4.3`) e SCT (`OID 1.3.6.1.4.1.11129.2.4.2`).
- [[fulcio-distribuicao-confianca-tuf-root-signing-trustbundle]] — Veja também: Sigstore Fulcio: Raiz de Confiança com The Update Framework (TUF `sigstore/root-signing`) e `trusted_root.json`.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Referência cruzada direta com fulcio-especificacao-certificados-x509-san-critico-subject-vazio.
- [[fulcio-provedores-oidc-meta-issuers-kubernetes-spiffe-ci]] — Referência cruzada direta com fulcio-provedores-oidc-meta-issuers-kubernetes-spiffe-ci.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
