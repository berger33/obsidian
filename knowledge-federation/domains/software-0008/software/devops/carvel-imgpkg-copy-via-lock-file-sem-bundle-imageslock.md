---
id: software.devops.tranche16.001538
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

# Carvel imgpkg: cópia de coleções de imagens via `--lock` (`ImagesLock`) sem criar um Bundle

## Em uma frase
Além de copiar Bundles completos (`-b`), o `imgpkg copy --lock images-lock.yml` permite transportar e relocar uma lista arbitrária de imagens OCI descrita em um arquivo `ImagesLock` diretamente entre registries ou via tarball.

## Por que importa
Em alguns cenários (como pré-popular o registry interno de um cluster com imagens base de CI, imagens de nós kind ou sidecars globais), a equipe quer apenas espelhar um conjunto exato de imagens travadas por digest sem precisar criar e manter uma imagem de Bundle contendo arquivos de manifesto.

## Como funciona
O operador gera ou mantém um arquivo `images-lock.yml` (`kind: ImagesLock`), executa `imgpkg copy --lock images-lock.yml --to-repo registry.interno.local/mirror/base-images --lock-output relocated-images.yml`, e recebe um novo arquivo `ImagesLock` com todas as referências atualizadas para o repositório interno.

## Exemplo
```bash
kbld -f base-images-manifest.yml --imgpkg-lock-output base-images.lock.yml
imgpkg copy --lock base-images.lock.yml \
  --to-repo registry.corp.internal/mirror/images \
  --lock-output mirrored-images.lock.yml
```

## Limites e trade-offs
Assim como nos bundles, todas as entradas do arquivo `ImagesLock` passado para `--lock` devem obrigatoriamente usar referências por digest (`@sha256:...`).

## Como verificar
Inspecione `mirrored-images.lock.yml` e valide que cada imagem listada responde a `crane manifest` ou `imgpkg pull -i` no registry interno.

## Conexões
- [[carvel-imgpkg-reescrita-automatica-imageslock-pull-kbld]] — Veja também: Carvel imgpkg: reescrita automática de `.imgpkg/images.yml` no `imgpkg pull` e integração com `kbld`.
- [[carvel-imgpkg-compatibilidade-registries-docker-layer-media-type-tags]] — Veja também: Carvel imgpkg: compatibilidade universal de registries via Docker layer media type e gestão de tags (`tag ls`).

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
