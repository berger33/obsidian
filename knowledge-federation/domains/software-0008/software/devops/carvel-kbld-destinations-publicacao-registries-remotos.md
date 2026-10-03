---
id: software.devops.tranche16.001525
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

# Carvel kbld: publicação automática de imagens construídas em registries OCI via `destinations`

## Em uma frase
A seção `destinations` do arquivo `kind: Config` instrui o `kbld` a publicar (`push`) automaticamente as imagens construídas na etapa `sources` para os repositórios de container registry de destino antes de gravar o digest final do manifesto no YAML.

## Por que importa
Um digest SHA-256 de manifesto OCI (`RepoDigest`) só é definitivo e acessível pelos worker nodes de um cluster Kubernetes remoto após a imagem ser enviada e registrada no container registry.

## Como funciona
Ao associar `image: payments-service` tanto em `sources` (apontando para `./services/payments`) quanto em `destinations` (definindo `newImage: ghcr.io/org/payments-service`), o `kbld` constrói a imagem, faz o push das camadas para `ghcr.io/org/payments-service`, obtém o digest assinado pelo registry e reescreve o Deployment para `ghcr.io/org/payments-service@sha256:...`.

## Exemplo
```yaml
apiVersion: kbld.k14s.io/v1alpha1
kind: Config
sources:
  - image: payments-service
    path: ./services/payments
destinations:
  - image: payments-service
    newImage: ghcr.io/org/payments-service
    tags: [v1.4.0, latest]
```

## Limites e trade-offs
Para que o push em `destinations` funcione sem prompt interativo em pipelines de CI, as credenciais do registry já devem estar autenticadas em `~/.docker/config.json` (ou passadas via variáveis de ambiente do `kbld`).

## Como verificar
Execute `kbld -f deployment.yml -f kbld-publish.yml` e confirme no registry remoto a criação das tags `v1.4.0` e `latest` apontando para o mesmo `@sha256:...` emitido no YAML.

## Conexões
- [[carvel-kbld-sources-orquestracao-builds-docker-buildx-pack-ko-bazel]] — Veja também: Carvel kbld: orquestração declarativa de builds de imagem a partir do código-fonte (`sources`).
- [[carvel-kbld-overrides-redirecionamento-repositorios-preresolved]] — Veja também: Carvel kbld: redirecionamento de imagens e pré-resolução offline via `overrides`.

## Fontes
- [Carvel kbld GitHub — README.md (Image Building Orchestration, Immutable Digest Resolution & Resource Metadata Annotations)](https://carvel.dev/kbld/docs/v0.44.x/config/) — README oficial do carvel-dev/kbld descrevendo orquestração de builds, resolução de imagens para digests SHA-256 e anotações de metadados; consultado em 2026-10-03.
- [Carvel kbld Official Documentation — Configuration v0.44.x (searchRules, keyMatcher, valueMatcher, updateStrategy, overrides, sources & destinations)](https://raw.githubusercontent.com/carvel-dev/kbld/develop/README.md) — Especificação oficial do objeto Config (kbld.k14s.io/v1alpha1) detalhando searchRules, parse recursivo de YAML/JSON em ConfigMaps, sources, destinations e overrides; consultado em 2026-10-03.
- [Carvel kbld — Official GitHub Repository](https://github.com/carvel-dev/kbld) — Repositório oficial Apache-2.0 do Carvel kbld; consultado em 2026-10-03.
