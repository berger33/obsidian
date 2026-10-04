---
id: software.devops.tranche16.001522
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
fontes: ["https://carvel.dev/kbld/docs/v0.44.x/config/", "https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://github.com/carvel-dev/kbld"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: configuração de `searchRules` com `keyMatcher` e `valueMatcher`

## Em uma frase
A seção `searchRules` do arquivo `kind: Config` (`apiVersion: kbld.k14s.io/v1alpha1`) define como o `kbld` descobre referências de imagens de container fora do campo padrão `image` dos manifestos Kubernetes.

## Por que importa
Muitos operadores, CRDs (como `Prometheus`, `Kafka`, `CertManager`) ou argumentos de linha de comando de containers (`--sidecar-image=ghcr.io/org/proxy:v1`) declaram imagens em chaves como `baseImage`, `helperImage` ou caminhos específicos de arrays que não se chamam simplesmente `image`.

## Como funciona
Por padrão, o `kbld` já procura por qualquer chave chamada `image`. Com `searchRules`, o engenheiro adiciona seletores `keyMatcher` (por `name: sidecarImage` ou por caminho `path: [spec, images, {allIndexes: true}]`) e/ou `valueMatcher` (por `image` exata ou prefixo de repositório `imageRepo: ghcr.io/org/app`). Quando ambos são declarados na mesma regra, suas condições são combinadas com `AND` lógico.

## Exemplo
```yaml
apiVersion: kbld.k14s.io/v1alpha1
kind: Config
minimumRequiredVersion: 0.31.0
searchRules:
  - keyMatcher:
      name: sidecarImage
  - keyMatcher:
      path: [spec, workerImages, {allIndexes: true}]
  - valueMatcher:
      imageRepo: ghcr.io/org/custom-agent
```

## Limites e trade-offs
Dentro de um `keyMatcher`, os campos `name` e `path` são mutuamente exclusivos (se ambos forem informados acidentalmente, `name` tem precedência sobre `path`).

## Como verificar
Execute `kbld -f crd-manifest.yml -f kbld-config.yml` e confirme que o campo `sidecarImage` e todos os elementos do array `spec.workerImages` foram convertidos para `@sha256:...`.

## Conexões
- [[carvel-kbld-resolucao-imutavel-digests-sha256-anotacoes-metadados]] — Veja também: Carvel kbld: resolução de referências de imagens para digests imutáveis SHA-256 e anotações de rastreabilidade.
- [[carvel-kbld-update-strategy-yaml-json-embutidos-configmap]] — Veja também: Carvel kbld: `updateStrategy` para resolver imagens dentro de strings YAML ou JSON embutidas em `ConfigMap`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
