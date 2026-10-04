---
id: software.devops.tranche16.001523
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

# Carvel kbld: `updateStrategy` para resolver imagens dentro de strings YAML ou JSON embutidas em `ConfigMap`

## Em uma frase
A propriedade `updateStrategy` das `searchRules` do `kbld` permite fazer o parse recursivo de strings multi-linha YAML ou JSON armazenadas dentro de um `ConfigMap` (ou anotação), localizar referências de imagens lá dentro e reescrever a string serializada com os digests resolvidos.

## Por que importa
Controladores que lançam Jobs ou Pods dinamicamente (como runners de CI, operadores de workflow ou plugins de backup) frequentemente leem a imagem do container worker a partir de um arquivo `config.yml` ou `settings.json` embutido em `data` de um `ConfigMap`. Sem parse recursivo, essas imagens escapariam da trava de digest e da relocação air-gapped.

## Como funciona
Ao declarar `keyMatcher: {name: data.yml}` com `updateStrategy: {yaml: {searchRules: [{keyMatcher: {name: image}}]}}`, o `kbld` decodifica a string `data.yml` do `ConfigMap` como um documento YAML independente, aplica as `searchRules` internas para resolver `image` para `@sha256:...` e re-serializa a string atualizada dentro do `ConfigMap`.

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: runner-config
data:
  runner.yml: |
    executor: kubernetes
    helperImage: alpine:3.20
---
apiVersion: kbld.k14s.io/v1alpha1
kind: Config
searchRules:
  - keyMatcher:
      name: runner.yml
    updateStrategy:
      yaml:
        searchRules:
          - keyMatcher:
              name: helperImage
```

## Limites e trade-offs
Caso uma chave chamada `image` em algum documento represente outro conceito (como o ID de uma AMI de máquina virtual e não uma imagem OCI), deve-se usar `updateStrategy: {none: {}}` para excluí-la do processamento do `kbld`.

## Como verificar
Execute `kbld -f configmap-embutido.yml` e verifique que o texto interno de `data.runner.yml` passou a conter `helperImage: index.docker.io/library/alpine@sha256:...`.

## Conexões
- [[carvel-kbld-config-search-rules-keymatcher-valuematcher]] — Veja também: Carvel kbld: configuração de `searchRules` com `keyMatcher` e `valueMatcher`.
- [[carvel-kbld-sources-orquestracao-builds-docker-buildx-pack-ko-bazel]] — Veja também: Carvel kbld: orquestração declarativa de builds de imagem a partir do código-fonte (`sources`).

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
