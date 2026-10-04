---
id: software.devops.tranche16.001537
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
fontes: ["https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel imgpkg: reescrita automática de `.imgpkg/images.yml` no `imgpkg pull` e integração com `kbld`

## Em uma frase
Quando um bundle relocado para um novo registry é extraído com `imgpkg pull -b`, o `imgpkg` reescreve automaticamente os endereços das imagens dentro do arquivo extraído `.imgpkg/images.yml` para apontarem para o repositório de onde o bundle foi baixado.

## Por que importa
Os manifestos YAML originais dentro do bundle (por exemplo, `deployment.yml` ou templates `ytt`) continuam referenciando os nomes públicos originais (`docker.io/user1/my-app:v1`). Se o `images.yml` não fosse reescrito no momento do `pull` para o endereço do registry privado, o cluster air-gapped tentaria baixar as imagens da internet pública e falharia.

## Como funciona
Como o `kbld` gravou a anotação `kbld.carvel.dev/id: "my-app:v1"` em cada entrada do `.imgpkg/images.yml` durante a criação do bundle, e o `imgpkg pull` atualizou o campo `image:` daquela entrada para `registry.privado.local/repo@sha256:4246...`, basta executar `ytt -f /tmp/bundle/config | kbld -f - -f /tmp/bundle/.imgpkg/images.yml` para que todos os manifestos saiam com os endereços do registry privado.

## Exemplo
```bash
imgpkg pull -b registry.airgap.internal/payments/bundle:1.0.0 -o /tmp/app-bundle
ytt -f /tmp/app-bundle/config \
  | kbld -f - -f /tmp/app-bundle/.imgpkg/images.yml \
  | kapp deploy -a payments -f - --yes
```

## Limites e trade-offs
Essa resolução automática no `kbld` depende da presença das anotações `kbld.carvel.dev/id` geradas originalmente por `kbld --imgpkg-lock-output .imgpkg/images.yml`; criar o `images.yml` à mão sem essas anotações impede que o `kbld` correlacione uma tag `my-app:v1` ao digest relocado.

## Como verificar
Inspecione `/tmp/app-bundle/.imgpkg/images.yml` após o `pull` e confirme que todos os campos `image:` começam com `registry.airgap.internal/payments/bundle@sha256:`.

## Conexões
- [[carvel-imgpkg-locations-oci-image-cache-image-locations-yml]] — Veja também: Carvel imgpkg: cache de metadados de cópia via Locations OCI Image (`image-locations.yml`).
- [[carvel-imgpkg-copy-via-lock-file-sem-bundle-imageslock]] — Veja também: Carvel imgpkg: cópia de coleções de imagens via `--lock` (`ImagesLock`) sem criar um Bundle.

## Fontes
- [Carvel imgpkg GitHub — README.md (OCI Bundles, Thick Copy, Air-Gapped Relocation & Deterministic Layers)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/imgpkg apresentando o conceito de OCI Bundle, comandos push/pull/copy e suporte a ambientes air-gapped; consultado em 2026-10-03.
- [Carvel imgpkg Official Documentation — Resources v0.43.x (Bundle, .imgpkg Directory, ImagesLock, BundleLock, Nested Bundles & ImageLocations)](https://raw.githubusercontent.com/carvel-dev/imgpkg/develop/README.md) — Referência oficial de recursos do Carvel imgpkg especificando ImagesLock, BundleLock, Nested Bundles recursivos e Locations OCI Image; consultado em 2026-10-03.
- [Carvel imgpkg — Official GitHub Repository](https://carvel.dev/kbld/docs/v0.44.x/config/) — Repositório oficial Apache-2.0 do Carvel imgpkg; consultado em 2026-10-03.
