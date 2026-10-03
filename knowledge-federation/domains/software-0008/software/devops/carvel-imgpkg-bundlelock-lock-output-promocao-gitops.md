---
id: software.devops.tranche16.001535
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

# Carvel imgpkg: rastreamento determinístico de releases com `BundleLock` (`--lock-output`)

## Em uma frase
A configuração `BundleLock` (`apiVersion: imgpkg.carvel.dev/v1alpha1`, `kind: BundleLock`), gerada pela flag `--lock-output` durante `imgpkg push` ou `imgpkg copy`, registra a referência imutável por digest de um bundle juntamente com a tag semântica associada.

## Por que importa
Em fluxos GitOps e pipelines de promoção entre ambientes (Dev -> Staging -> Prod), referenciar um bundle apenas pela tag `:v1.0` não garante imutabilidade caso a tag seja reescrita no registry.

## Como funciona
Ao executar `imgpkg push -b ghcr.io/org/app:v1.0 -f config/ --lock-output bundle.lock.yml`, o `imgpkg` grava em `bundle.lock.yml` o campo `bundle.image` com o `@sha256:...` exato e `bundle.tag: v1.0`. Comandos subsequentes como `imgpkg copy --lock bundle.lock.yml --to-repo ...` usam esse arquivo de lock como entrada e emitem um novo `BundleLock` apontando para o novo repositório de destino.

## Exemplo
```bash
imgpkg push -b ghcr.io/org/payments:v1.2.0 -f bundle-dir/ --lock-output release-bundle.lock.yml
cat release-bundle.lock.yml
imgpkg copy --lock release-bundle.lock.yml --to-repo registry.prod.internal/payments --lock-output prod-bundle.lock.yml
```

## Limites e trade-offs
Ao usar `--lock` no `imgpkg copy`, o novo arquivo gerado por `--lock-output` conterá o host/repositório de destino atualizado mantendo exatamente o mesmo digest `@sha256:...` do bundle original.

## Como verificar
Compare `release-bundle.lock.yml` e `prod-bundle.lock.yml` e confirme que ambos compartilham o mesmo hash `@sha256:` diferindo apenas no prefixo do registry.

## Conexões
- [[carvel-imgpkg-nested-bundles-composicao-recursiva-sem-limites]] — Veja também: Carvel imgpkg: composição recursiva de Nested Bundles e extração estruturada em disco.
- [[carvel-imgpkg-locations-oci-image-cache-image-locations-yml]] — Veja também: Carvel imgpkg: cache de metadados de cópia via Locations OCI Image (`image-locations.yml`).

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
