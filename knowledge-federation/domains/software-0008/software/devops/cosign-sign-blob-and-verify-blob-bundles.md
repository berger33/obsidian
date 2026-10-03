---
id: software.devops.tranche04.000326
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

# Assinatura e verificação keyless de arquivos arbitrários com cosign sign-blob, verify-blob e bundles

## Em uma frase
Para artefatos que não são imagens de contêiner (como binários compilados, pacotes `.tar.gz`, scripts ou manifestos YAML), o Cosign oferece `cosign sign-blob` e `cosign verify-blob` usando bundles Sigstore autocontidos (`--bundle artifact.sigstore.json`). O comando `cosign sign-blob artifact --bundle artifact.sigstore.json --yes` gera a assinatura keyless e empacota certificado e prova de transparência no arquivo de bundle, permitindo que o usuário final verifique o arquivo com `cosign verify-blob artifact --bundle artifact.sigstore.json --certificate-identity "..." --certificate-oidc-issuer "https://token.actions.githubusercontent.com"`.

## Por que importa
Distribuir binários de CLI ou pacotes em GitHub Releases apenas com arquivos `SHA256SUMS` não comprova quem gerou aquele hash se a conta ou espelho de download for comprometido. O bundle `.sigstore.json` assinado com `sign-blob` autentica criptograficamente a origem do binário.

## Como funciona
Ao publicar binários em releases de projetos open-source ou internos, gere e anexe um arquivo `<binario>.sigstore.json` com `cosign sign-blob` e documente o comando exato de `cosign verify-blob` nas instruções de download.

## Exemplo
No workflow de release em `.github/workflows/release.yml@refs/heads/main`, cada arquivo tar.gz compilado recebe um bundle via `cosign sign-blob`, e os scripts de instalação dos clientes executam `cosign verify-blob` antes de extrair o executável em `/usr/local/bin`.

## Limites e trade-offs
Nunca distribua a assinatura de um blob sem o certificado e a prova do log quando operar em modo keyless: utilize sempre a flag `--bundle artifact.sigstore.json`, que consolida todos os materiais criptográficos em um único arquivo.

## Como verificar
Assine um arquivo local de teste com `cosign sign-blob` gerando um bundle, altere um único byte do arquivo para confirmar que `cosign verify-blob` rejeita a adulteração e restaure o arquivo original confirmando a aprovação.

## Conexões
- [[cosign-air-gapped-offline-verification-and-tuf-trusted-root]] — Veja também: Verificação offline e air-gapped no Cosign com cosign initialize, cosign save e trusted_root.json.
- [[cosign-oci-registry-artifacts-blobs-tekton-wasm-ebpf]] — Veja também: Publicação e assinatura de Blobs, Tekton Bundles, módulos WASM e programas eBPF em registros OCI.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
