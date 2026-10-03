---
id: software.devops.tranche01.000028
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
fontes: ["https://raw.githubusercontent.com/helm/helm/main/README.md", "https://github.com/helm/helm"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Rastreamento de roadmap por GitHub Milestones e automação de releases

## Em uma frase
A seção Roadmap e o badge de Build Status no topo do README oficial mostram que o progresso do projeto Helm é acompanhado publicamente por meio de GitHub Milestones (`https://github.com/helm/helm/milestones`) e que o pipeline de release é automatizado via GitHub Actions (`actions?workflow=release`).

## Por que importa
Quando uma equipe aguarda um recurso novo do Helm v4 ou uma correção planejada para a próxima versão menor, consultar diretamente os GitHub Milestones do repositório mostra o escopo fechado e o andamento de cada marco sem depender de roadmaps estáticos desatualizados.

## Como funciona
Acompanhe os marcos de desenvolvimento em `https://github.com/helm/helm/milestones` para verificar em qual versão uma issue ou pull request foi alocada.

## Exemplo
A mesma seção Roadmap reforça a separação de branches: o desenvolvimento do Helm v4 ocorre na branch `main`, enquanto o Helm v3 permanece em modo de manutenção na branch `dev-v3` apenas para correções de bugs e segurança.

## Limites e trade-offs
Antes de abrir um pull request visando uma milestone específica, o README destaca em negrito a leitura obrigatória do guia `CONTRIBUTING.md`.

## Como verificar
Conferi a seção Roadmap e a subseção Contribution no README oficial de `helm/helm`.

## Conexões
- [[helm-reproducible-builds-and-release-lifecycle]] — Veja também: Builds reproduzíveis e gerenciamento do ciclo de vida de releases Kubernetes.
- [[helm-openssf-scorecard-cii-and-lfx-health]] — Veja também: Postura de segurança e saúde do projeto: CII Best Practices, OpenSSF Scorecard e LFX Health Score.

## Fontes
- [Helm — README oficial](https://raw.githubusercontent.com/helm/helm/main/README.md) — README oficial do Helm com definição de Charts, cinco casos de uso, Chart.yaml e templates/, suporte Helm v4 (main) vs Helm v3 (dev-v3 até jul/nov 2026), sete gerenciadores de pacotes, roadmap e canais da comunidade.; consultado em 2026-10-03.
- [Repositório oficial helm/helm](https://github.com/helm/helm) — Repositório oficial do Helm no GitHub com código-fonte v4, milestones, CONTRIBUTING.md, code-of-conduct.md e releases.; consultado em 2026-10-03.
