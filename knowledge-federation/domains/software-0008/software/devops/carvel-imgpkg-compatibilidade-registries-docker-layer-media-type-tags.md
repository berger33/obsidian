---
id: software.devops.tranche16.001539
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://github.com/carvel-dev/imgpkg"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: compatibilidade universal de registries via Docker layer media type e gestão de tags (`tag ls`)

## Em uma frase
O `imgpkg` utiliza o media type padrão de camada Docker para armazenar os arquivos de Bundles e Imagens OCI, garantindo compatibilidade imediata com qualquer container registry existente (Docker Hub, Harbor, ECR, GAR, ACR, Artifactory, Zot) sem exigir suporte a extensões OCI experimentais.

## Por que importa
Algumas ferramentas que usam especificações recentes de OCI Artifacts com `mediaType` customizados falham ao fazer push para registries corporativos mais antigos ou proxies que validam tipos de camada restritos ao formato clássico de imagem Docker.

## Como funciona
Graças ao uso de tipos de camada padrão e à normalização determinística do tarball interno, qualquer registry que aceite `docker push` aceita `imgpkg push`. Adicionalmente, `imgpkg tag ls -i <repo>` lista as tags publicadas e seus respectivos digests diretamente via API Registry V2 sem depender de um daemon Docker instalado na máquina.

## Exemplo
```bash
imgpkg tag ls -i ghcr.io/org/payments-bundle
imgpkg describe -b ghcr.io/org/payments-bundle:1.0.0
```

## Limites e trade-offs
Por padrão, `imgpkg tag ls` oculta as tags internas geradas automaticamente pelo `imgpkg` (como tags `.imgpkg` de metadados de localização), a menos que a flag `--imgpkg-internal-tags` seja solicitada.

## Como verificar
Execute `imgpkg describe -b ghcr.io/org/payments-bundle:1.0.0` para visualizar a árvore completa de imagens e bundles aninhados contidos no artefato remoto sem precisar baixá-lo.

## Conexões
- [[carvel-imgpkg-copy-via-lock-file-sem-bundle-imageslock]] — Veja também: Carvel imgpkg: cópia de coleções de imagens via `--lock` (`ImagesLock`) sem criar um Bundle.
- [[carvel-imgpkg-assinatura-cosign-copy-cosign-signatures-airgap]] — Veja também: Carvel imgpkg: preservação de assinaturas Cosign (`--cosign-signatures`) na cópia de bundles air-gapped.

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://github.com/carvel-dev/imgpkg) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
