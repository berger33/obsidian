---
id: software.devops.tranche01.000023
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/helm/helm/main/README.md", "https://github.com/helm/helm"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ciclo de vida de versões: Helm v4 estável na branch `main` e calendário de fim de suporte do Helm v3

## Em uma frase
A seção Helm Development and Stable Versions (e a seção Roadmap) do README oficial documenta o estado atual das linhas de versão: o Helm v4 é a release estável atual, desenvolvida na branch `main` (com pacote Go `helm.sh/helm/v4` referenciado nos badges do topo), enquanto o Helm v3 encontra-se em modo de suporte na branch `dev-v3`, recebendo correções de bugs (bug fixes) até **8 de julho de 2026** e correções de segurança (security fixes) até **11 de novembro de 2026**.

## Por que importa
Equipes de plataforma que ainda fixam binários do Helm v3 em imagens de CI/CD ou operadores internos precisam planejar a migração para o Helm v4 dentro dessas datas formais, pois após 8 de julho de 2026 a linha v3 deixa de receber correções de bugs gerais e após 11 de novembro de 2026 encerra também as correções de segurança.

## Como funciona
Audite a versão do cliente Helm usada nos seus runners de CI/CD e ferramentas GitOps, planeje a atualização para o Helm v4 (ou importe `helm.sh/helm/v4` se consumir o SDK em Go) antes do encerramento das janelas de manutenção da linha `dev-v3`.

## Exemplo
Os badges de Go Report Card e GoDoc no topo do README já apontam para o caminho de módulo `helm.sh/helm/v4`.

## Limites e trade-offs
Se você for submeter um pull request de nova funcionalidade para o projeto, desenvolva sobre a branch `main` (Helm v4), já que a branch `dev-v3` aceita apenas correções de bugs e de segurança dentro do cronograma publicado.

## Como verificar
Conferi as seções Helm Development and Stable Versions e Roadmap no README oficial de `helm/helm`.

## Conexões
- [[helm-chart-structure-and-rendering-flow]] — Veja também: Anatomia mínima de um Chart (`Chart.yaml` e `templates/`) e o fluxo de renderização para a API Kubernetes.
- [[helm-installation-seven-package-managers]] — Veja também: Instalação oficial do cliente Helm: binários de release e os sete gerenciadores de pacotes suportados.

## Fontes
- [Helm — README oficial](https://raw.githubusercontent.com/helm/helm/main/README.md) — README oficial do Helm com definição de Charts, cinco casos de uso, Chart.yaml e templates/, suporte Helm v4 (main) vs Helm v3 (dev-v3 até jul/nov 2026), sete gerenciadores de pacotes, roadmap e canais da comunidade.; consultado em 2026-10-03.
- [Repositório oficial helm/helm](https://github.com/helm/helm) — Repositório oficial do Helm no GitHub com código-fonte v4, milestones, CONTRIBUTING.md, code-of-conduct.md e releases.; consultado em 2026-10-03.
