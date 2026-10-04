---
id: software.devops.tranche02.000196
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

# Arquitetura 100% client-side sem componentes instalados nem manutenção no cluster

## Em uma frase
Na seção `Features`, sob **Lightweight**, o README enfatiza duas características arquiteturais do Skaffold: **client-side only** — o Skaffold não possui nenhum componente do lado do cluster (`no cluster-side component`), portanto não há overhead de recursos nem carga de manutenção no cluster — e **minimal pipeline** — fornece um pipeline enxuto e opinativo para manter a operação simples.

## Por que importa
Ferramentas de desenvolvimento que exigem instalar agentes privilegiados, daemons de build ou operadores proprietários dentro do cluster compartilhado frequentemente esbarram em políticas de segurança corporativa e consomem recursos dos nós; por ser puramente client-side, o Skaffold precisa apenas das permissões normais do usuário no `kubeconfig` e no registro de imagens.

## Como funciona
Adote o Skaffold em ambientes corporativos onde desenvolvedores possuem namespaces restritos por RBAC no Kubernetes e não têm permissão para instalar operadores globais no cluster.

## Exemplo
Um desenvolvedor conecta seu cliente local `skaffold` ao seu namespace de desenvolvimento no cluster remoto usando seu próprio `kubeconfig`, sem instalar nenhum controlador adicional no cluster.

## Limites e trade-offs
Como o Skaffold roda no lado do cliente (estação do desenvolvedor ou runner de CI), garanta que as ferramentas invocadas por ele no pipeline (como `kubectl`, `helm`, `kustomize` ou `docker`) estejam presentes na máquina cliente.

## Como verificar
Conferi a subseção Lightweight na seção Features do README oficial de `GoogleContainerTools/skaffold`.

## Conexões
- [[skaffold-init-multi-component-and-pluggable-tools]] — Veja também: Descoberta com skaffold init, aplicações multi-componente e arquitetura plugável de build/deploy.
- [[skaffold-cloud-code-ide-integrations-vscode-jetbrains]] — Veja também: Integração gerenciada com IDEs via extensões Google Cloud Code para VS Code e JetBrains.

## Fontes
- [Skaffold — GitHub README](https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md) — Visão geral do Skaffold (desenvolvimento contínuo para Kubernetes e blocos de CI/CD), features (source-to-deploy, skaffold render, skaffold init, client-side only), Cloud Code e Deprecation Policy.; consultado em 2026-10-03.
- [Skaffold Documentation — Install & Deprecation Policy](https://skaffold.dev/docs/install/) — Documentação oficial de instalação, fases do pipeline e política de depreciação do Skaffold.; consultado em 2026-10-03.
