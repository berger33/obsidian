---
id: software.devops.tranche16.001528
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/", "https://carvel.dev/imgpkg/docs/v0.43.x/resources/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: empacotamento e importação de imagens em tarball único (`pkg` / `unpkg`) mantendo digests

## Em uma frase
O `kbld` oferece funcionalidades para empacotar um conjunto de imagens referenciadas em um único arquivo tarball e importá-las em outro registry preservando exatamente os mesmos digests SHA-256.

## Por que importa
Em fluxos tradicionais que usam `docker save` e `docker load` seguidos de `docker push`, diferenças de metadados do daemon ou de compressão podem alterar o digest do manifesto no registry de destino, quebrando manifestos Kubernetes que travaram o `@sha256` original.

## Como funciona
O `kbld` transporta os manifestos e blobs OCI brutos exatamente como foram assinados na origem, garantindo que, após a importação no registry privado de destino, apenas o host/repositório mude enquanto o sufixo `@sha256:<digest>` permaneça 100% idêntico ao da origem.

## Exemplo
```bash
kbld -f deployment.yml --lock-output kbld.lock.yml
cat kbld.lock.yml
```

## Limites e trade-offs
Para cenários modernos de bundles completos (arquivos YAML + imagens dependentes + bundles aninhados), a suíte Carvel recomenda combinar `kbld --imgpkg-lock-output .imgpkg/images.yml` com `imgpkg copy --to-tar` e `imgpkg copy --tar`, que estendem esse modelo com cache de localização no registry.

## Como verificar
Confirme após a relocação das imagens que o digest SHA-256 no registry interno coincide caractere por caractere com o digest registrado no arquivo de lock original.

## Conexões
- [[carvel-kbld-lock-output-imgpkg-imageslock-geracao]] — Veja também: Carvel kbld: geração de arquivos de lock (`--lock-output` e `--imgpkg-lock-output`) para reprodutibilidade.
- [[carvel-kbld-anotacoes-rastreabilidade-git-build-auditoria]] — Veja também: Carvel kbld: auditoria de supply chain no cluster via anotação `kbld.k14s.io/images`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://carvel.dev/imgpkg/docs/v0.43.x/resources/) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
