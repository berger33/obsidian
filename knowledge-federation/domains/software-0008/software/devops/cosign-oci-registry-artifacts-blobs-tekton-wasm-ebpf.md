---
id: software.devops.tranche04.000327
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

# Publicação e assinatura de Blobs, Tekton Bundles, módulos WASM e programas eBPF em registros OCI

## Em uma frase
O README oficial do Cosign demonstra como aproveitar registros OCI como sistema universal de distribuição e assinatura de artefatos além de imagens de contêiner: `cosign upload blob -f artifact $BLOB_URI` publica arquivos arbitrários retornando a URI com digest SHA-256 para assinatura com `cosign sign`; **Tekton Bundles** publicados via `tkn bundle push` são assinados por digest no registro; módulos **WebAssembly (WASM)** são enviados com `cosign upload wasm -f hello.wasm <uri>` e assinados; e imagens de programas **eBPF** construídas com a ferramenta `bee` (`bee build` / `bee push`) são assinadas e verificadas com `cosign sign` e `cosign verify`.

## Por que importa
Centralizar imagens de contêiner, pipelines Tekton, filtros WASM (usados por exemplo no Envoy) e programas eBPF em registros OCI assinados pelo Cosign unifica o controle de cadeia de suprimentos e o armazenamento de artefatos sob o mesmo protocolo e política de verificação.

## Como funciona
Armazene artefatos auxiliares de plataforma (bundles Tekton, plugins WASM, objetos eBPF) no mesmo registro OCI corporativo e aplique o mesmo fluxo de assinatura por digest `@sha256:...` utilizado para imagens de contêiner.

## Exemplo
Uma plataforma que distribui pipelines Tekton compartilhados publica cada `Task` com `tkn bundle push`, captura o digest `sha256:...` retornado e assina o bundle com `cosign sign`, garantindo que apenas tarefas assinadas sejam executadas pelos clusters.

## Limites e trade-offs
Assim como em imagens de contêiner, nunca assine a tag mutável de um blob, módulo WASM ou Tekton bundle; utilize sempre a URI com digest `@sha256:...` retornada pelo comando de upload/push.

## Como verificar
Publique um artefato de teste ou inspecione o manifesto OCI assinado e confirme com `cosign verify` que o payload validado referencia exatamente o `docker-manifest-digest` do artefato.

## Conexões
- [[cosign-sign-blob-and-verify-blob-bundles]] — Veja também: Assinatura e verificação keyless de arquivos arbitrários com cosign sign-blob, verify-blob e bundles.
- [[cosign-in-toto-attestations-and-chainguard-container-image]] — Veja também: Suporte a atestações in-toto e uso da imagem oficial ghcr.io/sigstore/cosign/cosign.

## Fontes
- [Sigstore Cosign GitHub — README.md (Keyless Signing, Verification, Air-Gapped, Blobs, Attestations)](https://raw.githubusercontent.com/sigstore/cosign/main/README.md) — README oficial do Sigstore Cosign cobrindo assinatura keyless via OIDC, Fulcio e Rekor, assinatura por chave/KMS, verificação online e air-gapped com TUF trusted_root.json, sign-blob/verify-blob e suporte a artefatos OCI (Tekton, WASM, eBPF) e atestações in-toto.; consultado em 2026-10-03.
- [Sigstore Documentation — Cosign Signing Overview](https://docs.sigstore.dev/cosign/signing/overview/) — Documentação oficial do Sigstore sobre fluxos de assinatura e verificação de contêineres e artefatos com Cosign.; consultado em 2026-10-03.
- [Sigstore Cosign — Official GitHub Repository](https://github.com/sigstore/cosign) — Repositório oficial do Cosign no projeto Sigstore com evolução futura convergente para sigstore-go.; consultado em 2026-10-03.
