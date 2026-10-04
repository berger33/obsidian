---
id: software.devops.tranche19.001899
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
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md", "https://github.com/buildpacks-community/kpack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack `Build` CRD e Execução em Pod: fases do CNB Lifecycle (`prepare`, `detect`, `analyze`, `restore`, `build`, `export`, `completion`)

## Em uma frase
Cada vez que uma `Image` precisa ser construída ou atualizada, o controlador cria um objeto imutável **`Build`** (`<image-name>-build-<number>`) que agenda um Pod Kubernetes onde cada fase do **Cloud Native Buildpacks Lifecycle** executa sequencialmente através de **Init Containers** compartilhando volumes em comum.

## Por que importa
Entender a sequência de *Init Containers* de um Pod de `Build` do kpack permite identificar rapidamente em qual etapa um build falhou (se foi no clone Git em `prepare`, na detecção de linguagem em `detect`, na compilação em `build` ou no push para o registry em `export`).

## Como funciona
Um Pod de `Build` padrão executa a cadeia de containers: 1) **`prepare`** (clona o código-fonte Git/Blob/Registry e prepara credenciais); 2) **`detect`** (testa os grupos de buildpacks de `spec.order`); 3) **`analyze`** (verifica metadados da imagem anterior no registry); 4) **`restore`** (restaura camadas do cache); 5) **`build`** (executa os buildpacks selecionados para compilar a app); 6) **`export`** (monta e faz push das camadas OCI e do cache); e 7) **`completion`** (opcionalmente assina com Cosign e reporta o digest final no `status.latestImage`).

## Exemplo
```bash
# Listando os builds de uma Image e inspecionando os initContainers do Pod correspondente:
kubectl get builds -n builds -l image.kpack.io/image=payment-service-img
kubectl get pod payment-service-img-build-1-build-pod -n builds \
  -o jsonpath='{.spec.initContainers[*].name}'
```

## Limites e trade-offs
Quando a razão do build é apenas `STACK` (atualização compatível da `runImage` na `ClusterStack`), o kpack cria um Pod de `Build` enxuto que executa apenas a operação rápida de **`rebase`**, pulando `detect`, `restore` e `build`.

## Como verificar
Verifique a coluna `REASON` (`CONFIG`, `COMMIT`, `BUILDPACK`, `STACK`) na saída de `kubectl get builds -n builds`.

## Conexões
- [[kpack-secrets-serviceaccount-git-ssh-docker-registry-cosign]] — Veja também: kpack Gerenciamento de Credenciais: vinculação de `Secrets` (Registry, Git SSH/Basic Auth e Cosign) à `ServiceAccount`.
- [[kpack-cli-kp-utilitario-logs-operacao-comparacao-pack]] — Veja também: kpack CLI (`kp`) e Utilitário `logs`: operação de `Images`/`Builders`, streaming de logs de build e comparação `kpack` vs `pack`.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
