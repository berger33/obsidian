---
id: software.devops.tranche16.001527
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
fontes: ["https://carvel.dev/imgpkg/docs/v0.43.x/resources/", "https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: geração de arquivos de lock (`--lock-output` e `--imgpkg-lock-output`) para reprodutibilidade

## Em uma frase
O `kbld` pode exportar o resultado da resolução de imagens para um arquivo de lock dedicado (`--lock-output` ou `--imgpkg-lock-output .imgpkg/images.yml`) e consumi-lo posteriormente (`-f lock.yml`) para reproduzir exatamente os mesmos digests sem consultar o registry novamente.

## Por que importa
Ao empacotar uma release de software ou construir um bundle OCI com o `imgpkg`, é fundamental congelar em um artefato versionado a lista exata de digests SHA-256 de todas as imagens referenciadas por aquela versão da aplicação.

## Como funciona
Na fase de release, o pipeline executa `kbld -f config/ --imgpkg-lock-output .imgpkg/images.yml`. O arquivo gerado (`apiVersion: imgpkg.carvel.dev/v1alpha1`, `kind: ImagesLock`) armazena cada digest resolvido junto com a anotação `kbld.carvel.dev/id` que identifica a referência original (por exemplo `"my-app:v1"`). Na fase de deploy no cliente, `kbld -f config/ -f .imgpkg/images.yml` aplica os digests gravados no lock.

## Exemplo
```bash
kbld -f config/ --imgpkg-lock-output .imgpkg/images.yml
cat .imgpkg/images.yml
kbld -f config/ -f .imgpkg/images.yml > final-manifests.yml
```

## Limites e trade-offs
O arquivo `ImagesLock` gerado para o `imgpkg` exige que todas as entradas possuam referências por digest (`@sha256:...`); referências apenas por tag não são permitidas na especificação `ImagesLock`.

## Como verificar
Verifique que o arquivo `.imgpkg/images.yml` contém `kind: ImagesLock` e que `kbld -f config/ -f .imgpkg/images.yml` resolve todas as imagens sem realizar requisições HTTP aos registries originais.

## Conexões
- [[carvel-kbld-overrides-redirecionamento-repositorios-preresolved]] — Veja também: Carvel kbld: redirecionamento de imagens e pré-resolução offline via `overrides`.
- [[carvel-kbld-empacotamento-tarball-pkg-unpkg-transporte-imagens]] — Veja também: Carvel kbld: empacotamento e importação de imagens em tarball único (`pkg` / `unpkg`) mantendo digests.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://carvel.dev/kbld/docs/v0.44.x/config/) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
