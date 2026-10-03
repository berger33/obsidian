---
id: software.devops.tranche11.001067
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://pluto.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md", "https://pluto.docs.fairwinds.com/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Métodos de instalação do Pluto: plugin asdf, Homebrew Tap, binários de release e Scoop

## Em uma frase
O Pluto pode ser instalado localmente e em agentes de CI por meio do plugin oficial para **asdf** (`FairwindsOps/asdf-pluto`), do **Homebrew Tap** (`FairwindsOps/tap/pluto`), de binários pré-compilados nas releases do GitHub ou via **Scoop** no Windows.

## Por que importa
Como o catálogo interno de `apiVersions` depreciadas e removidas do Kubernetes evolui a cada novo lançamento do Kubernetes (`1.29`, `1.30`, `1.31`, `1.32`...), gerenciar a versão do binário `pluto` via gerenciadores de versão como `asdf` (ou `mise`) garante que toda a equipe de engenharia utilize uma versão atualizada do catálogo de depreciações.

## Como funciona
Conforme detalha o guia oficial *Installation* (`pluto.docs.fairwinds.com/installation/`): (1) via **asdf**, executa-se `asdf plugin-add pluto`, `asdf list-all pluto`, `asdf install pluto <version>` e `asdf local pluto <version>`; (2) no macOS/Linux via **Homebrew**, executa-se `brew install FairwindsOps/tap/pluto`; (3) no Windows via **Scoop** (mantido pela comunidade), executa-se `scoop install pluto`; ou (4) baixa-se o binário diretamente da página de releases do GitHub (`FairwindsOps/pluto/releases`).

## Exemplo
```bash
# Instalar e fixar a versão do Pluto em um repositório de infraestrutura usando asdf ou Homebrew
asdf plugin-add pluto
asdf install pluto latest
asdf local pluto latest

# Ou via Homebrew Tap oficial da Fairwinds:
brew install FairwindsOps/tap/pluto
```

## Limites e trade-offs
Uma versão antiga do binário `pluto` conhece apenas as depreciações anunciadas pelo Kubernetes até a data em que aquela versão do Pluto foi compilada; portanto, atualize sempre o binário do Pluto antes de auditar a prontidão de um cluster para uma versão recente do Kubernetes.

## Como verificar
Execute `pluto version` no terminal para verificar a versão instalada do binário e a versão padrão das APIs do Kubernetes embutida na ferramenta.

## Conexões
- [[pluto-integracao-github-action-ci-cd-detect-files]] — Veja também: Automação do Pluto no GitHub Actions (FairwindsOps/pluto/github-action) para validação de Pull Requests.
- [[pluto-migracao-registro-verificacao-cosign-checksums-v5-24]] — Veja também: Cadeia de suprimentos do Pluto (v5.24.0+): migração para Artifact Registry, tags imutáveis e verificação com Cosign.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.
- [[mise-gerenciador-ferramentas-variaveis-ambiente-tarefas]] — Referência cruzada direta com mise-gerenciador-ferramentas-variaveis-ambiente-tarefas.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/installation/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/quickstart/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
