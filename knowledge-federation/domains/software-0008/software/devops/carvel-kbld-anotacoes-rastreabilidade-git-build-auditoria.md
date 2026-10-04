---
id: software.devops.tranche16.001529
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md", "https://carvel.dev/kbld/docs/v0.44.x/config/", "https://github.com/carvel-dev/kbld"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kbld: auditoria de supply chain no cluster via anotação `kbld.k14s.io/images`

## Em uma frase
Além de reescrever a referência `image:` para `@sha256:...`, o `kbld` injeta nos recursos de workload a anotação `kbld.k14s.io/images`, registrando um histórico estruturado de cada imagem utilizada pelo recurso.

## Por que importa
Quando uma imagem em produção é referenciada apenas por `ghcr.io/org/api@sha256:9f86d08...`, um engenheiro de plantão que inspeciona o Pod no cluster não consegue saber imediatamente de qual tag semântica (`v1.4.2`), branch ou commit Git aquele digest foi originado.

## Como funciona
O `kbld` grava dentro de `metadata.annotations["kbld.k14s.io/images"]` uma lista YAML contendo o `url` final com digest e os metadados `origins` (como a tag original resolvida, a URL do repositório Git local, o SHA do commit `git.sha` e se havia arquivos não commitados `git.dirty` no momento do build).

## Exemplo
```bash
kubectl get deployment payments-api -o jsonpath='{.metadata.annotations.kbld\.k14s\.io/images}'
```

## Limites e trade-offs
Se o build for executado a partir de uma árvore Git local com alterações não commitadas, o `kbld` registrará `dirty: true` nos metadados da anotação; em pipelines de produção, deve-se exigir árvore Git limpa antes do build.

## Como verificar
Execute o comando `kubectl get deployment ... -o jsonpath` acima após implantar um manifesto processado pelo `kbld` e verifique a presença da tag original e dos metadados de origem.

## Conexões
- [[carvel-kbld-empacotamento-tarball-pkg-unpkg-transporte-imagens]] — Veja também: Carvel kbld: empacotamento e importação de imagens em tarball único (`pkg` / `unpkg`) mantendo digests.
- [[carvel-kbld-pipeline-composicao-ytt-kbld-kapp-unix-philosophy]] — Veja também: Carvel kbld: composição Unix em pipeline com `ytt`, `kbld` e `kapp` para entrega contínua.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
