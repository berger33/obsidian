---
id: software.devops.tranche19.001898
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

# kpack Gerenciamento de Credenciais: vinculação de `Secrets` (Registry, Git SSH/Basic Auth e Cosign) à `ServiceAccount`

## Em uma frase
O kpack gerencia todas as credenciais de acesso a registries de container privados, repositórios Git privados (SSH ou Basic Auth) e chaves de assinatura Cosign vinculando **`Secrets`** do Kubernetes anotados ao recurso **`ServiceAccount`** referenciado em `spec.serviceAccountName` da `Image` ou `Builder`.

## Por que importa
Se qualquer usuário do namespace pudesse ler credenciais globais do controlador, uma `Image` maliciosa poderia sobrescrever tags de outras equipes no registry corporativo.

## Como funciona
No modelo do kpack: 1) credenciais de container registry (`kubernetes.io/dockerconfigjson`) são listadas em **`imagePullSecrets`** (e `secrets`) da `ServiceAccount`; 2) credenciais Git (`kubernetes.io/ssh-auth` ou `kubernetes.io/basic-auth`) recebem a anotação **`kpack.io/git: https://github.com`** (ou `git@github.com`) e são listadas em **`secrets`** da `ServiceAccount`; e 3) chaves Cosign (`cosign.key` / `cosign.password`) também são associadas à `ServiceAccount` para assinar automaticamente cada imagem exportada.

## Exemplo
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: github-ssh-creds
  namespace: builds
  annotations:
    kpack.io/git: git@github.com
type: kubernetes.io/ssh-auth
stringData:
  ssh-privatekey: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    ...
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kpack-registry-sa
  namespace: builds
secrets:
  - name: github-ssh-creds
imagePullSecrets:
  - name: ghcr-push-secret
```

## Limites e trade-offs
Lembre-se da distinção no `ServiceAccount`: segredos de registry devem constar em `imagePullSecrets` (ou `secrets`), enquanto segredos de Git e Cosign devem constar na lista `secrets` da `ServiceAccount`.

## Como verificar
Verifique os segredos vinculados à ServiceAccount de build com `kubectl describe sa kpack-registry-sa -n builds`.

## Conexões
- [[kpack-build-configuration-env-resources-project-toml-cosign]] — Veja também: kpack Configuração Avançada de Build (`spec.build` e `spec.cosign`): variáveis `BP_*`, limites de CPU/RAM, `project.toml` e assinatura Cosign.
- [[kpack-crd-build-fases-cnb-lifecycle-pods-init-containers]] — Veja também: kpack `Build` CRD e Execução em Pod: fases do CNB Lifecycle (`prepare`, `detect`, `analyze`, `restore`, `build`, `export`, `completion`).

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
