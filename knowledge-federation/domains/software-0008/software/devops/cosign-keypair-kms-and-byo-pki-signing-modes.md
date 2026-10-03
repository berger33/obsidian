---
id: software.devops.tranche04.000324
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

# Assinatura e verificação com par de chaves cosign.key/cosign.pub, KMS, hardware tokens e PKI própria

## Em uma frase
Além do fluxo keyless padrão, o Cosign suporta assinatura com par de chaves privada/pública criptografado gerado pelo próprio Cosign (`cosign.key` e `cosign.pub`), assinatura apoiada em provedores de **KMS (Key Management Service) e tokens de hardware**, e integração com infraestrutura de chaves públicas própria (**Bring-your-own PKI**). Na verificação por chave pública com `cosign verify --key cosign.pub $IMAGE_URI`, o comando retorna `0` se ao menos uma assinatura formatada pelo Cosign para a imagem corresponder à chave pública especificada, imprimindo os payloads validados em JSON no `stdout`.

## Por que importa
Organizações que operam em ambientes desconectados da internet, submetidos a requisitos regulatórios de HSM/KMS corporativo ou sem provedor OIDC compatível com a instância pública do Sigstore dependem de assinatura baseada em chaves KMS ou PKI interna.

## Como funciona
Em ambientes com KMS corporativo (AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault), referencie a URI da chave KMS em `cosign sign --key <kms-uri>` e distribua a chave pública correspondente para os verificadores (`cosign verify --key cosign.pub`).

## Exemplo
Uma instituição financeira armazena a chave privada de release em um KMS gerenciado com controle de acesso IAM estrito, assina os artefatos no pipeline com `cosign sign --key` e valida os payloads JSON na admissão do cluster com a chave pública correspondente.

## Limites e trade-offs
Ao usar chaves locais (`cosign.key`), nunca versione a chave privada no repositório Git nem deixe a senha da chave vazia; prefira chaves residentes em KMS ou HSM sempre que possível.

## Como verificar
Execute `cosign verify --key cosign.pub $IMAGE | jq .` e confirme que o retorno do processo é `0` e que a seção `Critical.Image.Docker-manifest-digest` lista o digest correto.

## Conexões
- [[cosign-verify-certificate-identity-and-oidc-issuer]] — Veja também: Verificação keyless com --certificate-identity e --certificate-oidc-issuer no Cosign.
- [[cosign-air-gapped-offline-verification-and-tuf-trusted-root]] — Veja também: Verificação offline e air-gapped no Cosign com cosign initialize, cosign save e trusted_root.json.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
