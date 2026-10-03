---
id: software.devops.tranche19.001895
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md", "https://github.com/buildpacks-community/kpack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack `ClusterStack` e Operação de `Rebase`: atualização instantânea da camada de SO (`runImage`) sem recompilar o código

## Em uma frase
O recurso **`ClusterStack`** (`kpack.io/v1alpha2`) define o par de imagens base do sistema operacional exigido pelos Cloud Native Buildpacks: a **`buildImage`** (ambiente onde o build executa) e a **`runImage`** (imagem base final sobre a qual as camadas compiladas da aplicação rodam em produção).

## Por que importa
Quando sai um patch de segurança crítico para `openssl` ou `libc` na imagem base do Ubuntu, reconstruir do zero 300 microsserviços Java e Node.js levaria horas de CPU no cluster.

## Como funciona
Graças à separação estrutural de camadas do formato OCI/CNB, quando você atualiza a `runImage` no `ClusterStack` (por exemplo para um novo digest do `paketobuildpacks/run-noble-base`), o kpack detecta que apenas a base de execução mudou e executa uma operação de **Rebase**: ele apenas troca os ponteiros de manifesto das camadas da `runImage` no registry em poucos segundos, sem clonar o Git nem recompilar uma única linha de código!

## Exemplo
```yaml
apiVersion: kpack.io/v1alpha2
kind: ClusterStack
metadata:
  name: noble-base-stack
spec:
  id: "io.buildpacks.stacks.noble"
  buildImage:
    image: "paketobuildpacks/build-noble-base:latest"
  runImage:
    image: "paketobuildpacks/run-noble-base:latest"
```

## Limites e trade-offs
O kpack resolve as tags de `buildImage` e `runImage` para seus digests SHA-256 imutáveis no `status` do `ClusterStack`, garantindo reprodutibilidade exata em cada build e rebase.

## Como verificar
Execute `kubectl get clusterstacks -o wide` para inspecionar o `ID` da stack e os digests resolvidos de `buildImage` e `runImage`.

## Conexões
- [[kpack-builder-vs-clusterbuilder-order-detection-resolution]] — Veja também: kpack `Builder` e `ClusterBuilder`: definição da ordem de detecção (`spec.order`) e resolução de IDs de Buildpacks.
- [[kpack-clusterstore-buildpack-clusterbuildpack-empacotamento-cnb]] — Veja também: kpack `ClusterStore`, `Buildpack` e `ClusterBuildpack`: catálogo e resolução de versões de Cloud Native Buildpacks.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
