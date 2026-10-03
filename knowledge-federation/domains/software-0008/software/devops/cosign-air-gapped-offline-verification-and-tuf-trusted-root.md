---
id: software.devops.tranche04.000325
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

# Verificação offline e air-gapped no Cosign com cosign initialize, cosign save e trusted_root.json

## Em uma frase
O Cosign suporta verificação completamente offline em ambientes isolados (air-gapped) validando o bundle anexado por padrão como anotação no manifesto da imagem durante `cosign sign`. Para preparar a verificação em um ambiente conectado, executa-se `cosign initialize` (para baixar a raiz TUF atualizada) e `cosign save $IMAGE_NAME --dir ./path/to/dir` para salvar localmente a imagem e suas assinaturas. No ambiente air-gapped, a validação é executada com `cosign verify --offline=true --local-image ./path/to/dir` apontando para `--trusted-root ~/.sigstore/root/tuf-repo-cdn.sigstore.dev/targets/trusted_root.json` (ou `--key cosign.pub --offline --local-image ./path/to/dir` quando assinado por chave).

## Por que importa
Clusters industriais, militares ou de data centers críticos isolados da internet não podem consultar online os servidores do Rekor ou o repositório TUF da Sigstore no momento do deploy, exigindo validação criptográfica 100% local a partir do bundle e da raiz de confiança sincronizada.

## Como funciona
Sincronize periodicamente o arquivo `trusted_root.json` do repositório TUF de produção através de um processo seguro de transferência para a rede isolada e utilize `cosign save` / `--local-image` com `--offline=true` nos pipelines internos.

## Exemplo
Uma equipe de infraestrutura de defesa exporta semanalmente as imagens homologadas com `cosign save`, transfere o diretório e o `trusted_root.json` atualizado para o ambiente air-gapped e executa `cosign verify --offline=true --local-image` antes de carregar as imagens no registro interno.

## Limites e trade-offs
Conforme adverte a documentação oficial, o conteúdo de `trusted_root.json` pode mudar sem aviso prévio; se o ambiente não usa atualização TUF automática, é obrigatório manter um mecanismo próprio para atualizar regularmente a cópia air-gapped desse arquivo.

## Como verificar
Em um ambiente de teste com rede desabilitada, execute `cosign verify --offline=true --local-image ./saved-image` e confirme que a verificação conclui com sucesso sem realizar chamadas de rede externas.

## Conexões
- [[cosign-keypair-kms-and-byo-pki-signing-modes]] — Veja também: Assinatura e verificação com par de chaves cosign.key/cosign.pub, KMS, hardware tokens e PKI própria.
- [[cosign-sign-blob-and-verify-blob-bundles]] — Veja também: Assinatura e verificação keyless de arquivos arbitrários com cosign sign-blob, verify-blob e bundles.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
