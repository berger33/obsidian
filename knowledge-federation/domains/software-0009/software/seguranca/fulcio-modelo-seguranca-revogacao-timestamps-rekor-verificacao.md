---
id: software.seguranca.tranche04.000392
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

# Sigstore Fulcio: Modelo de Segurança de Certificados de 10 Minutos — Por Que Não Há CRL/OCSP nem Re-Assinatura

## Em uma frase
O modelo de segurança do Fulcio substitui listas de revogação (CRL/OCSP) e re-assinaturas periódicas pela combinação de **certificados de 10 minutos** com o **carimbo de tempo imutável de inclusão no Rekor** (ou RFC 3161 TSA).

## Por que importa
Na PKI tradicional de código, se uma chave privada de 3 anos vaza hoje, todos os binários assinados no passado tornam-se suspeitos; no Fulcio, como a chave privada foi destruída segundos após o build e o certificado expirou 10 minutos depois, um atacante que roube uma conta OIDC hoje jamais poderá forjar uma assinatura com data retroativa.

## Como funciona
No momento da verificação (mesmo anos após o certificado de 10 minutos ter expirado), o verificador **não** compara a validade do certificado contra o relógio atual (`now()`), mas sim verifica matematicamente que o `IntegratedTime` do Rekor (ou o timestamp assinado RFC 3161) está contido dentro do intervalo `[NotBefore, NotAfter]` de 10 minutos do certificado X.509.

## Exemplo
```bash
# Extrair a janela de validade de 10 minutos de um certificado Fulcio para comparação com o IntegratedTime
openssl x509 -in fulcio-leaf.crt.pem -noout -dates -ext subjectAltName
```

## Limites e trade-offs
Se um verificador X.509 genérico (`openssl verify` sem `-attime`) for usado sobre um certificado Fulcio após 10 minutos, ele falhará com `certificate has expired`; a verificação Fulcio exige sempre validar no instante autenticado (`-attime <rekor_integrated_time>`).

## Como verificar
Extraia o `integratedTime` da entrada Rekor, execute `openssl verify -attime <epoch> -CAfile fulcio-chain.pem fulcio-leaf.crt.pem` e confirme `fulcio-leaf.crt.pem: OK`.

## Conexões
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Veja também: Sigstore Fulcio: Arquitetura da Autoridade Certificadora (CA) para *Keyless Code Signing* Baseada em OIDC.
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Veja também: Sigstore Fulcio: Especificação RFC 5280 dos Certificados Root, Intermediate (`pathlen:0`) e Leaf (Subject Vazio e SAN Crítico).
- [[rekor-sigstore-bundle-verificacao-offline-signed-timestamps]] — Referência cruzada direta com rekor-sigstore-bundle-verificacao-offline-signed-timestamps.
- [[fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison]] — Referência cruzada direta com fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
