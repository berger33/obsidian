---
id: software.devops.tranche02.000197
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

# Integração gerenciada com IDEs via extensões Google Cloud Code para VS Code e JetBrains

## Em uma frase
A seção `IDE integrations` do README explica que, para uma experiência gerenciada do Skaffold diretamente no editor, o desenvolvedor pode instalar as extensões **Google Cloud Code** para **Visual Studio Code** (`cloud.google.com/code/docs/vscode/quickstart-k8s#installing`) e para **JetBrains IDEs** (`cloud.google.com/code/docs/intellij/quickstart-k8s#installing_the_plugin`), que mantêm o Skaffold atualizado, oferecem inicialização guiada, gerenciam dependências comuns e funcionam com qualquer cluster Kubernetes (`works with any kubernetes cluster`).

## Por que importa
Nem todo desenvolvedor de aplicação deseja operar flags de linha de comando e editar esquemas YAML manualmente; integrar o motor do Skaffold dentro do VS Code ou do IntelliJ/GoLand/PyCharm permite depurar contêineres em Kubernetes com breakpoints visuais mantendo o mesmo `skaffold.yaml` usado pelo CI.

## Como funciona
Indique as extensões `Cloud Code` para VS Code ou JetBrains às equipes de produto que preferem fluxo visual na IDE, mantendo na raiz do projeto o arquivo `skaffold.yaml` padrão para garantir paridade entre a IDE e o terminal/CI.

## Exemplo
Um desenvolvedor Java usa a extensão Cloud Code no IntelliJ IDEA para rodar e depurar seu serviço em um cluster Kubernetes local enquanto o colega de equipe executa o mesmo `skaffold.yaml` via CLI.

## Limites e trade-offs
Apesar do nome `Google Cloud Code`, o próprio README ressalta que a extensão funciona com **qualquer** cluster Kubernetes (local, on-premises ou de qualquer nuvem).

## Como verificar
Conferi a seção IDE integrations no README oficial de `GoogleContainerTools/skaffold`.

## Conexões
- [[skaffold-client-side-only-lightweight-architecture]] — Veja também: Arquitetura 100% client-side sem componentes instalados nem manutenção no cluster.
- [[skaffold-production-readiness-and-deprecation-policy]] — Veja também: Maturidade GA pronta para produção e política formal de depreciação.

## Fontes
- [Skaffold — GitHub README](https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md) — Visão geral do Skaffold (desenvolvimento contínuo para Kubernetes e blocos de CI/CD), features (source-to-deploy, skaffold render, skaffold init, client-side only), Cloud Code e Deprecation Policy.; consultado em 2026-10-03.
- [Skaffold Documentation — Install & Deprecation Policy](https://skaffold.dev/docs/install/) — Documentação oficial de instalação, fases do pipeline e política de depreciação do Skaffold.; consultado em 2026-10-03.
