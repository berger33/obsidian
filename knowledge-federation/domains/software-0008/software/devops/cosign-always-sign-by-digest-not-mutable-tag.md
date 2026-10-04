---
id: software.devops.tranche04.000322
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

# Obrigatoriedade de assinar imagens pelo digest SHA-256 em vez de tags mutáveis no Cosign

## Em uma frase
O Quick Start oficial do Cosign enfatiza que imagens de contêiner devem **sempre ser assinadas com base em seu digest imutável (`@sha256:...`) em vez de uma tag mutável (como `:latest`)**, pois assinar uma tag pode fazer com que o operador assine uma imagem diferente da pretendida devido a condições de corrida (TOCTOU) ou reatribuição posterior da tag no registro. Os payloads assinados pelo Cosign incluem explicitamente o campo `Docker-manifest-digest` (`sha256:...`), garantindo que assinaturas destacadas (detached signatures) cubram exatamente aquele manifesto criptográfico.

## Por que importa
Tags em registros OCI são ponteiros mutáveis que podem ser sobrescritos a qualquer instante entre o término do build e a execução do comando de assinatura. Assinar diretamente `registry/app@sha256:...` garante vínculo criptográfico inequívoco entre o artefato construído e a assinatura emitida.

## Como funciona
Nos pipelines de CI/CD, capture o digest retornado pelo passo de push da imagem e passe a referência completa `IMAGE@sha256:DIGEST` para `cosign sign` e para os manifestos de deploy ou políticas de admissão (como Kyverno).

## Exemplo
Um pipeline de build publica a imagem no registro, extrai o digest `sha256:87ef60f5...` gerado no push e executa `cosign sign ghcr.io/org/app@sha256:87ef60f5...`, impedindo que qualquer alteração de tag afete o artefato assinado.

## Limites e trade-offs
Nunca passe `:latest` ou tags de branch mutáveis diretamente para `cosign sign` em automações de produção; trate o uso de tag em comandos de assinatura como falha de lint de pipeline.

## Como verificar
Verifique o JSON retornado por `cosign verify` e confirme que `Critical.Image.Docker-manifest-digest` corresponde exatamente ao digest `sha256` da imagem implantada.

## Conexões
- [[cosign-keyless-signing-fulcio-oidc-and-rekor]] — Veja também: Assinatura keyless de contêineres OCI no Cosign com OIDC, Fulcio e Rekor.
- [[cosign-verify-certificate-identity-and-oidc-issuer]] — Veja também: Verificação keyless com --certificate-identity e --certificate-oidc-issuer no Cosign.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
