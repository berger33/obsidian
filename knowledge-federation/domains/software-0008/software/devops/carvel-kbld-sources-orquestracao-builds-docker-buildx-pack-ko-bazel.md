---
id: software.devops.tranche16.001524
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

# Carvel kbld: orquestração declarativa de builds de imagem a partir do código-fonte (`sources`)

## Em uma frase
A seção `sources` da configuração do `kbld` conecta referências lógicas de imagem nos manifestos Kubernetes diretamente ao diretório de código-fonte local e ao builder desejado (`docker`, `buildx`, `pack`, `kubectlBuildkit`, `ko` ou `bazel`).

## Por que importa
Em vez de manter scripts imperativos separados que constroem cada imagem, geram tags temporárias e usam `sed` para injetar a tag no YAML antes do deploy, o desenvolvedor declara a relação entre imagem e diretório de código em `kbld-config.yml` e executa um único pipeline `ytt | kbld | kapp`.

## Como funciona
Quando o `kbld` encontra no manifesto uma imagem que casa com uma entrada em `sources` (por exemplo `image: payments-service`), ele invoca o backend configurado (como Cloud Native Buildpacks via `pack` ou `docker buildx`) passando o diretório `path`, captura o digest imutável da imagem recém-construída e substitui a referência no manifesto emitido.

## Exemplo
```yaml
apiVersion: kbld.k14s.io/v1alpha1
kind: Config
sources:
  - image: payments-service
    path: ./services/payments
    docker:
      buildx:
        pull: true
        file: Dockerfile.prod
```

## Limites e trade-offs
Quando a construção é feita contra o daemon Docker local para desenvolvimento (sem uma entrada correspondente em `destinations` para fazer push a um registry remoto), o digest gerado é o ID da imagem local, utilizável apenas por nós que compartilhem aquele mesmo daemon Docker.

## Como verificar
Execute `kbld -f deployment.yml -f kbld-build.yml` e observe nos logs do `kbld` a invocação do `docker buildx`, seguida da emissão do manifesto com o digest resolvido e os metadados Git da árvore local.

## Conexões
- [[carvel-kbld-update-strategy-yaml-json-embutidos-configmap]] — Veja também: Carvel kbld: `updateStrategy` para resolver imagens dentro de strings YAML ou JSON embutidas em `ConfigMap`.
- [[carvel-kbld-destinations-publicacao-registries-remotos]] — Veja também: Carvel kbld: publicação automática de imagens construídas em registries OCI via `destinations`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
