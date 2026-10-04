---
id: software.devops.tranche02.000194
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md", "https://skaffold.dev/docs/install/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Blocos de construção de CI/CD e geração de manifestos hidratados com skaffold render para GitOps

## Em uma frase
Ainda em **Project portability**, o item **CI/CD building blocks** do README explica que você pode usar `skaffold run` de ponta a ponta ou invocar fases individuais do Skaffold para compor seu pipeline de CI/CD, destacando especificamente que o comando `skaffold render` produz manifestos Kubernetes hidratados (`hydrated Kubernetes manifests`) que podem ser usados diretamente em fluxos de trabalho GitOps.

## Por que importa
Em arquiteturas GitOps modernas com Argo CD ou Flux (vistas na Tranche 1), o pipeline de CI não deve dar `kubectl apply` direto no cluster de produção: ele constrói a imagem, injeta o digest imutável nos manifestos (hidratando Helm ou Kustomize) via `skaffold render` e grava o YAML resultante no repositório Git monitorado pelo controlador GitOps.

## Como funciona
Utilize as fases modulares do Skaffold no seu pipeline de CI (por exemplo, em Tekton Pipelines ou GitHub Actions) e execute `skaffold render` para gerar os manifestos finais com as tags/digests exatos das imagens recém-construídas para o repositório GitOps.

## Exemplo
Uma Task do Tekton compila as imagens da aplicação com o Skaffold e roda `skaffold render` para atualizar o manifesto hidratado que o Argo CD sincronizará no cluster de produção.

## Limites e trade-offs
Versionar manifestos hidratados por `skaffold render` no repositório GitOps exige garantir que dados sensíveis não sejam renderizados em texto claro nos objetos `Secret`.

## Como verificar
Conferi o item CI/CD building blocks na seção Features do README oficial de `GoogleContainerTools/skaffold`.

## Conexões
- [[skaffold-project-portability-and-profiles]] — Veja também: Portabilidade de projeto (`git clone` e `skaffold run`) e perfis sensíveis ao contexto.
- [[skaffold-init-multi-component-and-pluggable-tools]] — Veja também: Descoberta com skaffold init, aplicações multi-componente e arquitetura plugável de build/deploy.

## Fontes
- [Skaffold — GitHub README](https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md) — Visão geral do Skaffold (desenvolvimento contínuo para Kubernetes e blocos de CI/CD), features (source-to-deploy, skaffold render, skaffold init, client-side only), Cloud Code e Deprecation Policy.; consultado em 2026-10-03.
- [Skaffold Documentation — Install & Deprecation Policy](https://skaffold.dev/docs/install/) — Documentação oficial de instalação, fases do pipeline e política de depreciação do Skaffold.; consultado em 2026-10-03.
