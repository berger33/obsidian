---
id: software.devops.tranche19.001897
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
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://github.com/buildpacks-community/kpack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack Configuração Avançada de Build (`spec.build` e `spec.cosign`): variáveis `BP_*`, limites de CPU/RAM, `project.toml` e assinatura Cosign

## Em uma frase
Na especificação do recurso `Image` (`docs/image.md`), o bloco **`spec.build`** controla as variáveis de ambiente passadas aos buildpacks (como `BP_JVM_VERSION`), os `resources` (`requests`/`limits` de CPU e memória do Pod de build), `tolerations`, `nodeSelector`, `affinity`, `buildTimeout` e `creationTime`, enquanto **`spec.cosign`** e **`spec.projectDescriptorPath`** configuram assinatura criptográfica e o arquivo `project.toml`.

## Por que importa
Diferentes linguagens exigem quantidades muito distintas de memória durante a compilação (um build GraalVM Native Image exige 6–8 GiB de RAM, enquanto um build Go precisa de 512 MiB), e cadeias de suprimentos seguras exigem assinar a imagem OCI gerada com **Cosign**.

## Como funciona
Além das variáveis declaradas em `spec.build.env`, o kpack procura automaticamente por um arquivo **`project.toml`** na raiz do código-fonte (ou em `subPath`, customizável via `projectDescriptorPath`). Definindo `creationTime: "now"`, a imagem gerada recebe o timestamp Unix atual em vez do timestamp fixo zero padrão dos buildpacks.

## Exemplo
```yaml
spec:
  projectDescriptorPath: project.toml
  defaultProcess: web
  build:
    buildTimeout: 1800
    creationTime: "now"
    env:
      - name: BP_JVM_VERSION
        value: "21"
    resources:
      requests:
        cpu: "500m"
        memory: "1Gi"
      limits:
        cpu: "2"
        memory: "4Gi"
```

## Limites e trade-offs
Se um build pesado falhar com código de saída `137` (`OOMKilled`), aumente `spec.build.resources.limits.memory` no recurso `Image` para que os containers do Pod de `Build` recebam mais memória.

## Como verificar
Verifique os recursos e variáveis injetados no último Pod de build executando `kubectl get builds -n builds` e `kubectl describe pod <build-pod> -n builds`.

## Conexões
- [[kpack-clusterstore-buildpack-clusterbuildpack-empacotamento-cnb]] — Veja também: kpack `ClusterStore`, `Buildpack` e `ClusterBuildpack`: catálogo e resolução de versões de Cloud Native Buildpacks.
- [[kpack-secrets-serviceaccount-git-ssh-docker-registry-cosign]] — Veja também: kpack Gerenciamento de Credenciais: vinculação de `Secrets` (Registry, Git SSH/Basic Auth e Cosign) à `ServiceAccount`.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
