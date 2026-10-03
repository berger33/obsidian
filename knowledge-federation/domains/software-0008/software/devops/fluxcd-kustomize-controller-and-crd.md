---
id: software.devops.tranche01.000054
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/fluxcd/flux2/main/README.md", "https://github.com/fluxcd/flux2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kustomize Controller e o CRD `Kustomization` para reconciliação de manifestos e overlays

## Em uma frase
O segundo item da subseção Components no README oficial é o **Kustomize Controller** (`fluxcd.io/flux/components/kustomize/`), que expõe o CRD `Kustomization` (`fluxcd.io/flux/components/kustomize/kustomizations/`).

## Por que importa
Em repositórios GitOps estruturados por ambientes (staging, produção, regiões), o Kustomize Controller consome os artefatos produzidos pelo Source Controller, gera os manifestos (inclusive aplicando overlays Kustomize ou manifestos YAML planos) e reconcilia continuamente os objetos no cluster.

## Como funciona
Crie um recurso `Kustomization` do Flux apontando para uma fonte do Source Controller (como um `GitRepository` ou `OCIRepository`) e para o caminho do diretório desejado dentro daquela fonte.

## Exemplo
Mesmo quando um diretório no repositório contém arquivos YAML Kubernetes puros sem um `kustomization.yaml` manual, o CRD `Kustomization` do Flux orquestra a aplicação e a reconciliação periódica daqueles recursos no cluster.

## Limites e trade-offs
Não confunda o arquivo de configuração `kustomization.yaml` da ferramenta CLI Kustomize com o Custom Resource `kind: Kustomization` da API do Flux (`kustomize.toolkit.fluxcd.io`), que instrui o Kustomize Controller sobre qual fonte sincronizar.

## Como verificar
Conferi o item Kustomize Controller e Kustomization CRD na subseção Components do README oficial.

## Conexões
- [[fluxcd-source-controller-seven-crds]] — Veja também: Source Controller e seus sete CRDs de origem: de `GitRepository` e `OCIRepository` a `ArtifactGenerator`.
- [[fluxcd-helm-controller-and-helmrelease-crd]] — Veja também: Helm Controller e o CRD `HelmRelease` para gerenciamento declarativo de charts Helm.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Repositório oficial fluxcd/flux2](https://github.com/fluxcd/flux2) — Repositório oficial do Flux v2 no GitHub com código-fonte, diagramas de arquitetura, CONTRIBUTING.md e releases SLSA 3.; consultado em 2026-10-03.
