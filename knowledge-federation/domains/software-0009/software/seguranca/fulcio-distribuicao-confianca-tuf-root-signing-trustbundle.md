---
id: software.seguranca.tranche04.000398
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

# Sigstore Fulcio: Raiz de Confiança com The Update Framework (TUF `sigstore/root-signing`) e `trusted_root.json`

## Em uma frase
A distribuição das chaves raiz e intermediárias do Fulcio, das chaves públicas do CT Log (`ctfe`) e dos shards do Rekor para todos os clientes é protegida pelo **The Update Framework (TUF)** mantido através de cerimônias distribuídas com chaves de hardware no repositório `sigstore/root-signing`.

## Por que importa
Permite rotacionar certificados intermediários do Fulcio, chaves anuais do CT Log ou shards do Rekor de forma transparente e resistente a comprometimento de espelhos CDN (`tuf-repo-cdn.sigstore.dev`).

## Como funciona
Em vez de embutir certificados estáticos eternos no binário do cliente, ferramentas como `cosign` e `go-tuf` inicializam a confiança a partir do metadado raiz TUF assinado por um quórum ($M$ de $N$) de detentores de chaves comunitárias, baixam os alvos verificados (`fulcio_v1.crt.pem`, `fulcio_intermediate_v1.crt.pem`, `ctfe.pub`, `rekor.pub` unificados em `trusted_root.json`) e validam assinaturas e datas de expiração dos metadados TUF.

## Exemplo
```bash
# Inicializar cliente TUF com a raiz do Sigstore e obter o certificado raiz autenticado do Fulcio
curl -sSfLo sigstore-root.json \
  https://raw.githubusercontent.com/sigstore/root-signing/main/metadata/root_history/5.root.json

tuf-client init https://tuf-repo-cdn.sigstore.dev sigstore-root.json
tuf-client get https://tuf-repo-cdn.sigstore.dev fulcio_v1.crt.pem > fulcio_v1.crt.pem
openssl x509 -in fulcio_v1.crt.pem -noout -subject -issuer -dates
```

## Limites e trade-offs
Baixar a cadeia de certificados diretamente de `/api/v2/trustBundle` sem validá-la contra a raiz TUF confia apenas no TLS da conexão com o servidor Fulcio; em produção, inicialize sempre os verificadores via TUF (`trusted_root.json`).

## Como verificar
Execute os comandos `tuf-client` acima e confirme que o certificado `fulcio_v1.crt.pem` possui `Subject: O = sigstore.dev, CN = sigstore` e `CA:TRUE`.

## Conexões
- [[fulcio-fluxo-protocolo-create-signing-certificate-proof-possession]] — Veja também: Sigstore Fulcio: Fluxo Criptográfico da API v2 (`CreateSigningCertificate`) e Prova de Posse da Chave.
- [[fulcio-implantacao-privada-certificate-maker-kms-pkcs11-tuf]] — Veja também: Sigstore Fulcio: Implantação Corporativa Privada com `certificate-maker`, Cloud KMS e HSM PKCS#11.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[rekor-sigstore-bundle-verificacao-offline-signed-timestamps]] — Referência cruzada direta com rekor-sigstore-bundle-verificacao-offline-signed-timestamps.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
