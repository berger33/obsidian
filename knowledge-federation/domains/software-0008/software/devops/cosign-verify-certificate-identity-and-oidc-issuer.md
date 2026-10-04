---
id: software.devops.tranche04.000323
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/sigstore/cosign/main/README.md", "https://docs.sigstore.dev/cosign/signing/overview/", "https://github.com/sigstore/cosign"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação keyless com --certificate-identity e --certificate-oidc-issuer no Cosign

## Em uma frase
Para verificar uma imagem assinada no modo keyless do Cosign, o consumidor deve informar explicitamente o sujeito esperado do certificado e o emissor OIDC esperado por meio das flags `--certificate-identity=$IDENTITY` e `--certificate-oidc-issuer=$OIDC_ISSUER` (ou suas variantes de expressão regular `--certificate-identity-regexp` e `--certificate-oidc-issuer-regexp`) no comando `cosign verify $IMAGE`.

## Por que importa
Como qualquer usuário ou repositório na internet pode obter um certificado efêmero válido da instância pública do Fulcio para sua própria identidade OIDC, verificar apenas a validade criptográfica da assinatura sem restringir `--certificate-identity` e `--certificate-oidc-issuer` aceitaria imagens assinadas por terceiros não autorizados.

## Como funciona
Exija sempre em políticas de CI e em controladores de admissão Kubernetes a combinação exata da identidade do workflow ou conta de serviço (`--certificate-identity`) e a URL do provedor OIDC confiável (`--certificate-oidc-issuer`, como `https://token.actions.githubusercontent.com`).

## Exemplo
Antes de promover uma imagem para produção, o pipeline executa `cosign verify $IMAGE --certificate-identity="https://github.com/org/repo/.github/workflows/release.yml@refs/heads/main" --certificate-oidc-issuer="https://token.actions.githubusercontent.com"`, rejeitando qualquer imagem assinada por outra conta ou workflow.

## Limites e trade-offs
Evite expressões regulares excessivamente permissivas em `--certificate-identity-regexp` (como `.*`), que anulam a validação de identidade do signatário e abrem brecha para ataques de substituição de imagem.

## Como verificar
Teste `cosign verify` passando uma identidade incorreta de propósito e confirme que o comando falha com código de saída diferente de zero, aprovando apenas quando identidade e emissor OIDC coincidem com o esperado.

## Conexões
- [[cosign-always-sign-by-digest-not-mutable-tag]] — Veja também: Obrigatoriedade de assinar imagens pelo digest SHA-256 em vez de tags mutáveis no Cosign.
- [[cosign-keypair-kms-and-byo-pki-signing-modes]] — Veja também: Assinatura e verificação com par de chaves cosign.key/cosign.pub, KMS, hardware tokens e PKI própria.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
