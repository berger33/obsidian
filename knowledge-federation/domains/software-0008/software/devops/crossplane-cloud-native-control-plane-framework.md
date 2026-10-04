---
id: software.devops.tranche02.000101
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
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://docs.crossplane.io/latest/get-started/get-started-with-composition"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Definição do Crossplane como framework de control planes sem escrever código

## Em uma frase
O README oficial no repositório `crossplane/crossplane` define o Crossplane como um framework para construir control planes cloud-native sem precisar escrever código, sendo um projeto da Cloud Native Computing Foundation (CNCF) licenciado sob Apache 2.0.

## Por que importa
Em engenharia de plataforma, equipes frequentemente precisam expor APIs internas padronizadas para provisionar bancos de dados, filas, redes e clusters sem obrigar cada desenvolvedor a conhecer detalhes de provedores de nuvem ou escrever operadores customizados em Go do zero.

## Como funciona
Instale o Crossplane no cluster de controle Kubernetes (disponível inclusive via Helm Chart no Artifact Hub sob `packages/helm/crossplane/crossplane`) para transformar o API Server do Kubernetes em um plano de controle universal de infraestrutura e aplicações.

## Exemplo
Uma equipe de plataforma adota o Crossplane como camada de controle sobre Kubernetes e reconcilia os manifestos declarativos via Argo CD ou Flux.

## Limites e trade-offs
Construir um control plane sem escrever código de reconciliação exige ainda desenhar bons esquemas declarativos e políticas de RBAC no Kubernetes.

## Como verificar
Conferi a abertura e a seção License no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-extensible-backend-and-declarative-frontend]] — Veja também: Arquitetura dual de backend extensível e frontend declarativo configurável.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane Documentation — Get Started with Composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition) — Documentação oficial de introdução ao Crossplane, instalação e quickstarts de recursos e composição referenciada no README.; consultado em 2026-10-03.
