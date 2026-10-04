---
id: software.devops.tranche02.000102
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

# Arquitetura dual de backend extensível e frontend declarativo configurável

## Em uma frase
A abertura do README explica que o Crossplane combina duas metades complementares: um backend altamente extensível que permite construir um control plane capaz de orquestrar aplicações e infraestrutura independentemente de onde rodem, e um frontend altamente configurável que coloca a equipe no controle do esquema da API declarativa oferecida.

## Por que importa
Separar o provedor que fala com a API externa (backend) do contrato consumido pelos times de produto (frontend) evita acoplamento direto entre aplicações e recursos específicos de um único provedor de nuvem.

## Como funciona
Configure provedores e funções no backend do Crossplane para interagir com APIs externas e defina no frontend os esquemas declarativos enxutos que os times de desenvolvimento podem instanciar com `kubectl` ou via GitOps.

## Exemplo
A equipe de plataforma expõe uma API declarativa interna para provisionar armazenamento de objetos enquanto o backend do Crossplane conversa com a nuvem pública ou infraestrutura local.

## Limites e trade-offs
Expor diretamente todos os parâmetros brutos do provedor de nuvem no frontend elimina o benefício de abstração do plano de controle.

## Como verificar
Conferi o primeiro parágrafo do README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-cloud-native-control-plane-framework]] — Veja também: Definição do Crossplane como framework de control planes sem escrever código.
- [[crossplane-get-started-and-composition-docs]] — Veja também: Ponto de partida oficial e guia de início com Composition.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane Documentation — Get Started with Composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition) — Documentação oficial de introdução ao Crossplane, instalação e quickstarts de recursos e composição referenciada no README.; consultado em 2026-10-03.
