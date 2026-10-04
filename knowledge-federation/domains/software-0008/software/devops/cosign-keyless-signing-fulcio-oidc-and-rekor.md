---
id: software.devops.tranche04.000321
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

# Assinatura keyless de contêineres OCI no Cosign com OIDC, Fulcio e Rekor

## Em uma frase
O Cosign, desenvolvido como parte do projeto Sigstore (`sigstore.dev`), tem como objetivo tornar assinaturas criptográficas uma infraestrutura invisível para contêineres OCI e outros artefatos. No modo padrão de **assinatura sem chaves de longa duração ("keyless signing")** com `cosign sign $IMAGE`, o Cosign gera um par de chaves efêmero, autentica o signatário via OpenID Connect (OIDC), solicita um certificado de assinatura de código de curta duração à autoridade certificadora **Fulcio** (cujo Subject reflete a identidade autenticada), registra a assinatura e o certificado no log público de transparência **Rekor** (`tlog entry created with index`) e envia a assinatura para o registro OCI ao lado da imagem assinada.

## Por que importa
Gerenciar, rotacionar e proteger chaves privadas de longa duração em pipelines de CI/CD é um dos maiores gargalos na adoção de assinatura de artefatos. O fluxo keyless vincula a assinatura diretamente à identidade OIDC verificável do workflow de CI ou do desenvolvedor e grava prova imutável no Rekor.

## Como funciona
Integre `cosign sign` aos pipelines de release autenticados via OIDC (como GitHub Actions ou GitLab CI) para assinar automaticamente cada imagem publicada sem armazenar chaves privadas em secrets do repositório.

## Exemplo
Ao concluir o build de produção no GitHub Actions, o job executa `cosign sign` autenticando-se com o token OIDC do workflow; o Fulcio emite o certificado efêmero, o Rekor grava a entrada no log de transparência e a assinatura é publicada no registro OCI junto à imagem.

## Limites e trade-offs
Observe o aviso oficial do Cosign: informações associadas à conta OIDC autenticada (como endereço de e-mail em fluxos interativos) são gravadas permanentemente no log público de transparência Rekor e não podem ser removidas posteriormente.

## Como verificar
Execute `cosign sign` em uma imagem de teste por digest e confirme na saída a verificação do SCT (`Successfully verified SCT`), o índice criado no Rekor (`tlog entry created with index`) e o push da assinatura ao registro.

## Conexões
- [[cosign-always-sign-by-digest-not-mutable-tag]] — Veja também: Obrigatoriedade de assinar imagens pelo digest SHA-256 em vez de tags mutáveis no Cosign.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
