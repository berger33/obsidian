---
id: software.devops.tranche16.001536
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

# Carvel imgpkg: cache de metadados de cópia via Locations OCI Image (`image-locations.yml`)

## Em uma frase
Durante a cópia de Bundles e imagens dependentes, o `imgpkg` cria e publica no repositório de destino uma imagem OCI auxiliar (*Locations OCI Image*) contendo um único arquivo `image-locations.yml` (`kind: ImageLocations`) que funciona como cache de descoberta.

## Por que importa
Um bundle pode referenciar dezenas de imagens e bundles aninhados que originalmente residiam em múltiplos repositórios e registries distintos. Sem um índice de localização no repositório de destino, um `imgpkg pull` ou uma segunda cópia precisaria inspecionar cada imagem individualmente para descobrir onde os blobs foram colocalizados e quais deles são bundles.

## Como funciona
A Locations OCI Image armazena em uma única camada o documento `apiVersion: imgpkg.carvel.dev/v1alpha1`, `kind: ImageLocations`, mapeando cada digest de imagem (`some.image.io/test@sha256:...`) e o booleano `isBundle: true/false`, acelerando drasticamente operações subsequentes de `pull` e `copy`.

## Exemplo
```yaml
apiVersion: imgpkg.carvel.dev/v1alpha1
kind: ImageLocations
images:
  - image: ghcr.io/org/sub-bundle@sha256:4c8b96d4fffdfae29258d94a22ae4ad1fe36139d47288b8960d9958d1e63a9d0
    isBundle: true
  - image: docker.io/library/postgres@sha256:6ecba6f14373a449f8d54fa4286f57fb8ef37c4ffa637969551f2fda52672206
    isBundle: false
```

## Limites e trade-offs
Esse artefato `ImageLocations` é gerenciado automaticamente pelo próprio `imgpkg` no repositório de destino (associado por tag derivada do digest do bundle raiz) e não deve ser editado manualmente pelo operador.

## Como verificar
Execute `imgpkg tag ls -i registry.airgap.internal/payments/bundle` após um `imgpkg copy` para observar as tags gerenciadas no repositório.

## Conexões
- [[carvel-imgpkg-bundlelock-lock-output-promocao-gitops]] — Veja também: Carvel imgpkg: rastreamento determinístico de releases com `BundleLock` (`--lock-output`).
- [[carvel-imgpkg-reescrita-automatica-imageslock-pull-kbld]] — Veja também: Carvel imgpkg: reescrita automática de `.imgpkg/images.yml` no `imgpkg pull` e integração com `kbld`.

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
