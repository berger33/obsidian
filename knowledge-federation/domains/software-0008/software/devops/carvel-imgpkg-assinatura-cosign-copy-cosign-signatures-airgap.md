---
id: software.devops.tranche16.001540
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://github.com/carvel-dev/imgpkg"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: preservação de assinaturas Cosign (`--cosign-signatures`) na cópia de bundles air-gapped

## Em uma frase
O comando `imgpkg copy` suporta a flag `--cosign-signatures`, permitindo descobrir e copiar automaticamente os artefatos de assinatura criptográfica gerados pelo Sigstore Cosign junto com o bundle e todas as suas imagens dependentes.

## Por que importa
Em ambientes de alta segurança que aplicam políticas de admissão (Kyverno ou Conftest/Gatekeeper) exigindo verificação de assinatura Cosign nos nós do cluster, copiar apenas as imagens OCI para um registry air-gapped sem levar as tags `.sig` correspondentes faria todos os deploys serem bloqueados no cluster isolado.

## Como funciona
Quando `--cosign-signatures` é passado para `imgpkg copy -b ... --to-tar` e na importação `--tar ... --to-repo`, o `imgpkg` consulta no registry de origem as tags de assinatura associadas ao digest de cada imagem do `ImagesLock` e do próprio bundle, inclui esses artefatos no transporte e os publica no repositório de destino.

## Exemplo
```bash
cosign sign --yes ghcr.io/org/payments-bundle@sha256:b12026c7a0a6a1756a82a2a74ac759e9a7036523faca0e33dbddebc214e097df
imgpkg copy -b ghcr.io/org/payments-bundle:1.0.0 \
  --cosign-signatures \
  --to-repo registry.airgap.internal/payments/bundle
cosign verify --key cosign.pub registry.airgap.internal/payments/bundle:1.0.0
```

## Limites e trade-offs
Ativar `--cosign-signatures` realiza consultas adicionais à API do registry para cada imagem do grafo do bundle a fim de localizar os artefatos `.sig`, o que aumenta o número de requisições HTTP durante a exportação.

## Como verificar
Execute `cosign verify` apontando para o endereço do bundle e das imagens dependentes no registry de destino após o `imgpkg copy --cosign-signatures` e confirme a validação criptográfica.

## Conexões
- [[carvel-imgpkg-compatibilidade-registries-docker-layer-media-type-tags]] — Veja também: Carvel imgpkg: compatibilidade universal de registries via Docker layer media type e gestão de tags (`tag ls`).

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
