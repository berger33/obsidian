---
id: software.seguranca.tranche04.000399
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

# Sigstore Fulcio: Implantação Corporativa Privada com `certificate-maker`, Cloud KMS e HSM PKCS#11

## Em uma frase
O Fulcio inclui a ferramenta oficial **`certificate-maker`** para criar cadeias de certificados conformes à especificação Fulcio (de 2 níveis `root -> leaf` ou 3 níveis `root -> intermediate -> leaf`) usando chaves residentes em AWS KMS, GCP KMS, Azure Key Vault ou HashiCorp Vault, além de suporte a HSMs via PKCS#11 no servidor.

## Por que importa
Permite que organizações operem sua própria CA Fulcio interna sem jamais expor a chave privada da Root CA ou da Intermediate CA no sistema de arquivos dos servidores.

## Como funciona
O comando `certificate-maker` conecta-se ao KMS/Vault configurado, aplica os templates X.509 obrigatórios (`root-template.json` e `intermediate-template.json` com `pathlen:0` e `EKU: Code Signing`) e emite os certificados PEM. Em seguida, o `fulcio-server` é iniciado com `--ca=kms` (ou `--ca=pkcs11ca` / `--ca=googleca`), `--kms-resource` e `--ct-log-url` apontando para o `ctfe` interno.

## Exemplo
```bash
# Gerar cadeia Root + Intermediate CA conformes ao Fulcio usando chaves gerenciadas em KMS
certificate-maker create \
  --kms-type=awskms \
  --root-kms-key-id="arn:aws:kms:us-east-1:111122223333:key/root-ca-key" \
  --root-cert-path=fulcio-root.pem \
  --intermediate-kms-key-id="arn:aws:kms:us-east-1:111122223333:key/interm-ca-key" \
  --intermediate-cert-path=fulcio-intermediate.pem \
  --common-name="corp-sigstore.internal" \
  --org-name="Corp Internal Engineering"
```

## Limites e trade-offs
Nunca utilize `--ca=ephemeralca` em ambientes de produção ou homologação persistente, pois essa opção gera uma CA em memória que desaparece quando o container reinicia.

## Como verificar
Verifique a cadeia gerada com `openssl verify -CAfile fulcio-root.pem fulcio-intermediate.pem` e confirme o retorno `fulcio-intermediate.pem: OK`.

## Conexões
- [[fulcio-distribuicao-confianca-tuf-root-signing-trustbundle]] — Veja também: Sigstore Fulcio: Raiz de Confiança com The Update Framework (TUF `sigstore/root-signing`) e `trusted_root.json`.
- [[fulcio-integracao-ecossistema-cosign-gitsign-policy-controller]] — Veja também: Sigstore Fulcio: Integração Ponta a Ponta com `cosign`, `gitsign` e Kubernetes `policy-controller` / Kyverno.
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Referência cruzada direta com fulcio-especificacao-certificados-x509-san-critico-subject-vazio.
- [[rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles]] — Referência cruzada direta com rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
